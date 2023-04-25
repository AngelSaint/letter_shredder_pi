import serial
import sys
import mysql.connector

# Define MySQL database connection details
mydb = mysql.connector.connect(
  host="localhost",
  user="angelos4",
  password="12345678",
  database="letter_shredder"
)

MAX_TIMEOUT = 10  # Maximum time we should wait for a response from the arduino.


def capture():
    # Capture image and then use the OCR library to conver the image to text
    data = "Angelo Santos\n123 Main Street Apt 1\nChampaign, IL 61820\n"
    return data


def parse(data):
    output = {"Name": "", "Address": "", "Local": ""}
    entries = data.split("\n")
    output["Name"] = entries[0]
    output["Address"] = entries[1]
    output["Local"] = entries[2]
    return output


def db_search(query_data):
    if (query_data["Local"] == "Champaign, IL 61820"):
        Name = query_data["Name"]
        Address = query_data["Address"]
        cursor = mydb.cursor()
        cursor.execute(f"SELECT `Box #` FROM Residents WHERE Name='{Name}' AND Address = '{Address}'")
        # cursor.execute("SELECT * FROM BlackList")
        return cursor.fetchall()
    else:
        return 4


def parse_mail(signal):
    if "Mail: " not in signal:
        return -1
    strings = signal.split(" ")
    return int(strings[1])


def test_db():
    data = capture()
    output = parse(data)
    box = db_search(output)
    print(box)
    assert box == 1


ser = serial.Serial('/dev/serial0', 9600, timeout=1)
ser.reset_input_buffer()
signal = "Wait"
connected = False
mode = sys.argv[1]
if mode == 1:
    mode = "Stop on Fail"
else:
    mode = "Continuous"

test_db()

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
    while signal != "Ready":
        signal = ser.readline().decode('utf-8').rstrip()
        print(signal)

    # Process the Image within the mail capsule
    # data = capture()
    # query_data = parse(data)
    # box = db_search(query_data)
    box = 1

    # Send box signal
    send = bytes(f"Box: {box}\n", 'utf-8')
    ser.write(send)

    # Wait for the arduino to notify us that the mail has reached it's destination
    signal = "Wait\n"
    while signal == "Wait\n":
        signal = ser.readline().decode('utf-8').rstrip()
        if ("Invalid" in signal):
            print(signal)
            ser.write(send)
            signal = "Wait\n"


    print(signal)
    if parse_mail(signal) != box and mode == "Stop on Fail":
        signal = "Finish"
    else:
        signal = "Wait"
