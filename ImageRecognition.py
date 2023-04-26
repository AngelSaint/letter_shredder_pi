import serial
import sys
import mysql.connector
import cv2
import numpy as np
import pytesseract
import threading

# Define MySQL database connection details
mydb = mysql.connector.connect(
  host="localhost",
  user="angelos4",
  password="12345678",
  database="letter_shredder"
)

MAX_TIMEOUT = 10  # Maximum time we should wait for a response from the arduino.
CAM_0_IDX = 0
CAM_1_IDX = 4


def read_camera(camera_num, result):
    cap = cv2.VideoCapture(camera_num)
    ret,img = cap.read()
    if(ret):
        text = process_image(img)
        result.append(text)
    cap.release()

# Puts images through the image pipeline, and returns the text if found. None otherwise
# images are numpy arrays taken straight from the camera.
def process_image(img):
    img = np.array(img)

    # grayscale
    img_proc = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # crop
    img_proc = img_proc[150:350,150:450]
    # threshold
    ret, img_proc = cv2.threshold(img_proc,100,255,cv2.THRESH_BINARY)
    # skew correct
    # angle = deskew.determine_skew(img_proc)
    # if(angle and abs(angle) > 1 and abs(angle) < 15):
    #   img_proc = rotate_image(img_proc, angle)
    # rotate
    img_proc_rot = cv2.rotate(img_proc, cv2.ROTATE_180)

    # two OCR calls to cover both orientations
    text = pytesseract.image_to_string(img_proc)
    text_rot = pytesseract.image_to_string(img_proc_rot)

    # return the better result
    if len(text) == 0 and len(text_rot) == 0:
        return None
    elif len(text) > len(text_rot) or text_rot.startswith('0'):
        return text
    else:
        return text_rot

# Capture image and then use the OCR library to conver the image to text
def capture():
    camera1_ret = []
    camera2_ret = []
    camera1_thread = threading.Thread(target=read_camera, args=(CAM_0_IDX, camera1_ret))
    camera2_thread = threading.Thread(target=read_camera, args=(CAM_1_IDX, camera2_ret))
    camera1_thread.start()
    camera2_thread.start()
    camera1_thread.join()
    camera2_thread.join()

    if len(camera1_ret[0]) > len(camera2_ret[0]):
        return camera1_ret[0]
    else:
        return camera2_ret[0]


def parse(data):
    output = {}
    entries_all = data.split("\n")

    # remove all empty lines
    entries = []
    for e in entries_all:
        if len(e) > 0:
            entries.append(e)
    try:
        output["from"] = ' '.join(entries[0].split()[1:])
        output["to"] = ' '.join(entries[1].split()[1:])
        output["address"] = entries[2]
        output["apartment"] = int(entries[3].split()[1])
        output["local"] = entries[4]
    except:
        return -1
    return output


def db_search(query_data):
    From_Name = query_data["from"]
    To_Name = query_data["to"]
    Address = query_data["address"]
    Apartment = query_data["apartment"]

    blacklist_cursor = mydb.cursor()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT `Box#` FROM Residents WHERE Name='{To_Name}' AND Address = '{Address}'")

    try:
        box = cursor.fetchall()[0][0]
        print("Query box:", box)
        blacklist_cursor.execute(f"SELECT 'Box{str(box)}' FROM BlackList WHERE Name='{From_Name}'")
        try:
            print("Blacklist value: ", cursor.fetchall()[0][0])
            if (cursor.fetchall()[0][0] == 'N'):
                return 4
            else:
                return box
        except:
            print("blacklist query is empty")
            return box
    except:
        print("Blacklist query failed or box is empty")
        return 4



def parse_mail(signal):
    if "Mail: " not in signal:
        return -1
    strings = signal.split(" ")
    return int(strings[1])


# def test_db():
#     data = capture()
#     output = parse(data)
#     box = db_search(output)
#     print(box)
#     # assert box == 1


ser = serial.Serial('/dev/serial0', 9600, timeout=1)
ser.reset_input_buffer()
signal = "Wait"
connected = False
mode = sys.argv[1]
if mode == 1:
    mode = "Stop on Fail"
else:
    mode = "Continuous"

# test_db()

# Send arduino begin signal indicating that we are ready
while not connected:
    timeout = 0
    print("Made it here")
    send = bytes(f"Begin\n", 'utf-8')
    ser.write(send)

    # Check for Estab signal from arduino. Timeout if it takes too long
    while signal != "Estab" and timeout < MAX_TIMEOUT:
        print(f"Waiting for response, attempt : {timeout}")
        signal = ser.readline().decode('utf-8').rstrip()
        timeout += 1
    if timeout >= MAX_TIMEOUT:
        print("Arduino not responding")
        # Send Reset Signal to Arduino
        continue
    if signal == "Estab":
        break

print("Connection Established")

while signal != "Finish":
    # Check for Ready signal from arduino, indicating mail is ready to be captured.
    print("Waiting for Ready Signal")
    while signal != "Ready":
        signal = ser.readline().decode('utf-8').rstrip()
        if (signal == "Ready"):
            print("Signal: ", signal)

    # Process the Image within the mail capsule
    data = capture()
    print(data)
    query_data = parse(data)
    print(query_data)
    if query_data == -1:
        box = 4
    else:
        box = db_search(query_data)
    print("Box:", box)

    # Send box signal
    send = bytes(f"Box: {box}\n", 'utf-8')
    ser.write(send)

    print("Box Number Sent, waiting for response.")
    # Wait for the arduino to notify us that the mail has reached it's destination
    signal = "Wait\n"
    while signal == "Wait\n":
        signal = ser.readline().decode('utf-8').rstrip()
        if ("Invalid" in signal):
            print("Signal: ", signal)
            print("Box Number Sent again, waiting for response.")
            ser.write(send)
            signal = "Wait\n"
        if len(signal) == 0:
            signal = "Wait\n"

    print("Signal: ", signal)
    if parse_mail(signal) != box and mode == "Stop on Fail":
        signal = "Finish"
    else:
        signal = "Wait"
