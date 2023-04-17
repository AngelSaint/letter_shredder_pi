import multiprocessing as mp
import Webserver
import ImageRecognition
import serial
import sys


MAX_TIMEOUT = 10  # Maximum time we should wait for a response from the arduino.


def ImageRecognitionPipeline(mode):
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    signal = "Wait"
    connected = False

    # Send arduino begin signal indicating that we are ready
    while not connected:
        timeout = 0
        send = bytes(f"Begin", 'utf-8')
        ser.write(send)

        # Check for Estab signal from arduino. Timeout if it takes too long
        while signal != "Estab" and timeout < MAX_TIMEOUT:
            print(f"Waiting for response, attempt : {timeout}")
            timeout += 1
        if timeout >= MAX_TIMEOUT:
            print("Arduino not responding")
            break

    print("Connection Established")

    while signal != "Finish":
        # Check for Ready signal from arduino, indicating mail is ready to be captured.
        while signal != "Ready":
            signal = ser.readline().decode('utf-8').rstrip()

        # Process the Image within the mail capsule
        data = ImageRecognition.capture()
        # name = ImageRecognition.parse(data)
        name = "Angelo Santos"
        box = Webserver.db_search(name)

        # Send box signal
        send = bytes(f"Box: {box}\n", 'utf-8')
        ser.write(send)

        # Wait for the arduino to notify us that the mail has reached it's destination
        signal = "Wait"
        while signal == "Wait":
            signal = ser.readline().decode('utf-8').rstrip()

        if int(signal) != box and mode == "Stop on Fail":
            signal = "Finish"
        else:
            signal = "Wait"
    return


def WebserverPipeline(webserver_mode):
    # Webserver.run()
    if webserver_mode == 1:
        Webserver.run()
    else:
        print("Webserver would be running right now\n")
        return


# These can be seperated into two files for sure.
if __name__ == '__main__':
    webserver_mode = sys.argv[1]
    OCR_mode = sys.argv[2]
    if OCR_mode == 1:
        OCR_mode = "Stop on Fail"
    else:
        OCR_mode = "Continuous"

    p1 = mp.Process(target=ImageRecognitionPipeline, args=(OCR_mode,))
    p2 = mp.Process(target=WebserverPipeline, args=(webserver_mode,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

