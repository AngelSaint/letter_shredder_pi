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
    data = "Sahas Munamala\n1001 Main St. Apt 100\nChampaign, IL 61820\n"
    return data


def parse(data):
    output = {"Name" : "", "Address": "", "Local": ""}
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
        return cursor.fetchall()
    else:
        return 4


ser = serial.Serial('/dev/serial0', 9600, timeout=1)
ser.reset_input_buffer()
signal = "Wait"
connected = False
mode = sys.argv[1]
if mode == 1:
    mode = "Stop on Fail"
else:
    mode = "Continuous"


# Send arduino begin signal indicating that we are ready
while not connected:
    timeout = 0
    send = bytes(f"Begin\n", 'utf-8')
    ser.write(send)

    # Check for Estab signal from arduino. Timeout if it takes too long
    while signal != "Estab\n" and timeout < MAX_TIMEOUT:
        print(f"Waiting for response, attempt : {timeout}")
        signal = ser.readline().decode('utf-8').rstrip()
        timeout += 1
    if timeout >= MAX_TIMEOUT:
        print("Arduino not responding")
        break

print("Connection Established")

while signal != "Finish\n":
    # Check for Ready signal from arduino, indicating mail is ready to be captured.
    while signal != "Ready\n":
        signal = ser.readline().decode('utf-8').rstrip()

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

    if int(signal) != box and mode == "Stop on Fail":
        signal = "Finish\n"
    else:
        signal = "Wait\n"
