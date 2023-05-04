NOTEBOOK : I was in charge of the Mail Sorting subsystem

# Week 2 (1/23):

Wrote up project idea for self udjusting heated jacket on the Web Board:
My thoughts included having a sensor that would measure body temperature and adjust the temperature accordingly. It would auto-adjust itself when the ideal temperature is reached and gradually lower itself as to not overheat the person wearing it. There can even be buttons the wearer can press to manually adjust the temperature for further comfort.

Didn't get project approved by TA.

Found groupmates: Sahas Munamala (sahasrm2) and Angelo Santos (angelos4)

# Week 3 (1/30):

Worked on different project for a automatic Mail shredder and sorter that would read the address on mail and sort to mail box using OCR we found (https://tesseract-ocr.github.io/).

_TEAM MEMBERS:
Angelo Santos (angelos4)
Sahas Munamala (sahasrm2)
Lisa Pachikara (lisamp2)_


_PROBLEM:
It is common for many residents to encounter mail that does not belong to them from prior tenants. The documents may contain personal information about that tenant that could risk security threats and negative legal implications. There are also many occasions where tenants currently living in apartments get unwanted mail from senders they would like to blacklist, or from advertisers._


-SOLUTION:
We propose a mail sorter and shredder that would organize mail based on the names of the tenants and the senders that are allowed/blacklisted from the mail system. Names on the allowlist are sorted into the respective bins. Blacklisted names are sent to the shredder.
This would be done by scanning the mail, extracting the necessary information from the labels of the mail, and comparing all features to determine bin placement._


_SOLUTION COMPONENTS:
Raspberry Pi
Camera x2
Microcontroller
Laser Block sensor
Motors x3
Shredder_


_SUBSYSTEMS:
SUBSYSTEM 1: MAIL RECOGNITION/DETECTOR-
This component will consist of an optical switch connected to the main control unit that will determine if mail is placed properly in the scanner. It will also contain 2 cameras and light sources to capture both sides of the mail.
SUBSYSTEM 2: MAIN CONTROL UNIT-
Controls the image capturing of the camera based on the optical switch, and runs an OCR to determine the sender and receiver from the printed or handwritten text. It will then compares the data to names/aliases within a local database to determine the destination of the mail being processed. Further, it will send control signals to different electric motors in the organization system.
SUBSYSTEM 3: WEBSERVER-
We will run a webserver hosted on a raspberry pi. This web server will be responsible for updating the machine's internal filters.
SUBSYSTEM 4: ORGANIZATION SYSTEM-
This is the physical system that controls the directional movement of the documents such that it reaches the intended destination.
CRITERION FOR SUCCESS-
Mail sorter can sort mail into individual slots
Mail sorter can read mail and extract necessary information like addresses/names from images of mail.
Mail sorter settings can be set remotely
Mail sorter can shred_

# Week 4 (2/6):

Got project approved. 
Decided not to include shredder anymore due to increased risk if the mail is shredded by mistake. 

Worked on Project Proposal. **Image 1** depicts the idea of the apparatus and how it will function. We chose to use the ATmega328p microcontroller for motor control and a Raspberry Pi for webserver and OCR. 

For Motor control: 
_This is the physical system that controls the directional movement of the documents such that it reaches the intended destination.
Requirements:
This subsystem will consist of multiple paddles along with a dropoff chute for the mail once it has been scanned. The main requirement of the motor dropoff is that it only releases the mail once it has been successfully scanned, and when the paddles are in the precise orientation that allows the mail to enter its respective box. The paddles must allow for consistent routing to the appropriate boxes, even under a significant load.
Tolerance:
This subsystem may fail mechanically due to the physical limitations of the materials used to construct the sorter. If there are any unwanted gaps in the system for the mail to fall into the wrong chute, it may diminish the use of our system. This can be mitigated through design choices and calibration of the motors controlling the paddles/latches. We will also have to run tests for the optimal timing of the mail release and paddle movement. _


We submitted **Image 3** to the machine shop and I wrote up the dimension description :
_For our physical design, the overall build will be composed of wood with a base dimension of 22.5 inches x 15.25 inches. The front of the apparatus will be covered with a see-through acrylic or plastic to be able to see the workings of the motorized parts and to make debugging much simpler. At the entryway of the mail, there will be a 0.5 inch opening to fit the size of our mail and have it sit upright for the picture to be taken properly. At the bottom, on both sides of each mailbox, there will be a 1 inch gap saved for the sensors to be placed. As can be seen in the diagram, there is more than enough space in the corners of the module to fit the power source input, and raspberry pi. This setup will include at least 5 inches of space in length to support wiring between the components._


# Week 5 (2/13):

We worked on our Initial Design Document where we used **Image 4** as our Block Diagram.

# Week 6 (2/20):

Worked on our Team Contract. 

# Week 7 (2/27):

We had Design Reviews where we were adivsed to re-write it to explicitly include Requirements and Verifications for each Subsystem. We were also told to create a proper Block Diagram with clear data and power flow this can be seen from **Image 5**. I updated the requirements and verification of the Motor Control subsystem to be:  
_This is the physical system that controls the directional movement of the documents such that it reaches the intended destination. This subsystem will consist of multiple paddles along with a dropoff chute for the mail._
_Requirements:_
- _The motor dropoff only releases the mail once it has been successfully scanned. _
- _The paddles are in the precise orientation that allows the mail to enter its respective box._
- _The mail should remain in the slot if the prior mail has not yet reached it’s destination._ 

_Verification:_
- _Run a piece of mail through the system, and verify using the system log stored on the raspberry pi that the image was processed and the mail slot determined before the motors moved._
- _Run a piece of given mail through the system and visually check that the paddles get set to the correct position._
- _This requirement can be tested by modifying the motors in the sorting subsystem. If we allow one of the motors to block the mail from entering the box and place another mail in the divot, we will then be able to check if the mail has left recognition module._

# Week 8 (3/6):

Got laser receiver orders and talked with machine shop to make holes for lasers to fit in and finalize entire design. 

# Week 9 (3/13):

_SPRING BREAK_

# Week 10 (3/20):

Began researching the programming of the ATmega328. Become familiar the testing environment for the controlling of the different motors and processing of different light sensor signals.

Found that I can use the Arduino IDE to program the ATmega.

Chose to use servo motors instead of step motors because of easier customization. 
_After careful consideration, we have decided to switch from stepper motors to servo motors. This is because servo motors have the ability to generate speeds that are two to four times faster than those of stepper motors. Unlike stepper motors, servo motors operate under a closed-loop system, where they constantly receive feedback on their position. This makes them capable of operating at higher speeds and generating higher peak torque. In addition, servo motors are also more efficient, with efficiencies ranging between 80-90%. All of these factors made servo motors the clear choice for our needs, and we believe this change will greatly enhance the performance of our system_

# Week 11 (3/27):

Complete a sample program that handles the control logic between the different light sensors and simultaneously changes the PWM frequencies of the different motors based on the control signal given by the raspberry pi. **Image 2** Helped me know what pins to use on the microcontroller for the motor. Successfully moved the motor from 45 to 135 degrees in a loop. Also incorporated delays. 

```
#include <Servo.h>

Servo right;

int R_pin = 6; //J5

void setup() {
right.attach(R_pin);

right.write(180);
}

void loop() {
  right.write(45);
  delay(1000);
  right.write(135);
  delay(5000);
}
```

# Week 12 (4/3):

Worked with Sahas on getting the Rasberry pi and ATmega on one breadboard together along with test motors and sensors. At this time, given a signal to where the mail should arrive, the different PWM signals of the ATmega should give the correct output to the different motors. 

Worked with the full set of motors on the apparatus made by the machine shop as shown on **Image 6**. Wrote sample code to control all 5 motors in a sequence to guide mail to each mailbox. Used **Image 2** pinout to connect pins on the ATmega328p on the breadboard and noted to Sahas to edit the PCB to change a PWM pin. 

```
#Sample motor control
#include <Servo.h>
#define LL_PIN 3
#define RL_PIN 5
#define M_PIN 6
#define L_PIN 10
#define R_PIN 9

#define LL_CLOSED 100
#define LL_OPEN 160
#define RL_CLOSED 90
#define RL_OPEN 20

#define L_45 55
#define L_135 110
#define R_45 55
#define R_135 100
#define M_45 45
#define M_135 135

Servo left_latch;
Servo right_latch;
Servo middle;
Servo left;
Servo right;


void setup() {

  left_latch.attach(LL_PIN);
  right_latch.attach(RL_PIN);
  middle.attach(M_PIN);
  left.attach(L_PIN);
  right.attach(R_PIN);

}

void reset(){
  left_latch.write(LL_CLOSED);
  right_latch.write(RL_CLOSED);
  delay(1000);
  middle.write(180);
  left.write(90);
  right.write(90);
  
  delay(5000);

}

void mailbox1(){
  left.write(L_135);
  middle.write(M_135);
  delay(500);
  left_latch.write(LL_OPEN);
  right_latch.write(RL_OPEN);

  delay(5000);
}

void mailbox2(){
  left.write(L_45);
  middle.write(M_135);
  delay(500);
  left_latch.write(LL_OPEN);
  right_latch.write(RL_OPEN);

  delay(5000);
}

void mailbox3(){
  right.write(R_135);
  middle.write(M_45);
  delay(500);
  left_latch.write(LL_OPEN);
  right_latch.write(RL_OPEN);

  delay(5000);
}

void mailbox4(){
  right.write(R_45);
  middle.write(M_45);
  delay(500);
  left_latch.write(LL_OPEN);
  right_latch.write(RL_OPEN);

  delay(5000);
}

void loop() {

  reset();

  mailbox1();

  reset();

  mailbox2();

  reset();

  mailbox3();

  reset();

  mailbox4();


}
```



# Week 13 (4/10):

Worked on researching communication between ATmega and Raspberry Pi. Used **[2]** as a refernce to sample test communication between the Arduino IDE and Raspberry Pi through Serial Communication. 

Code to test communication between Pi and Arduino IDE:

```
#define BTN_PIN 2

void setup() {
  Serial.begin(9600);
  pinMode(BTN_PIN, INPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print("Estab\n");
  }

  if(digitalRead(BTN_PIN) == LOW){
    Serial.println("Ready");
  }

String box_num = Serial.readStringUntil('\n');
  
}
```



# Week 14 (4/17):

Place all the items in their appropriate postions on the final PCB and test for any errors within the mechanical design. Tune any parameters for change.
Finalized code for Motor control and took into account laser sensors. Fine tuned angles for the motors to easily move mail through sorter. Made sure motors waited for mail to go past mailbox sensor before resetting and allows Pi to read new mail. 

Spent hours in the lab crimping wires and connecting pins to new PCB. 

Final Motor Control Code:

```
#include <Servo.h>
#include <string.h>

#define LL_CLOSED 100
#define LL_OPEN 160
#define RL_CLOSED 90
#define RL_OPEN 20

#define L_45 55
#define L_135 110
#define R_45 55
#define R_135 100
#define M_45 55
#define M_135 135
#define NEUTRAL 90

#define LL_SERVO_PIN PD3
#define RL_SERVO_PIN PD5
#define M_SERVO_PIN PD6
#define L_SERVO_PIN 9
#define R_SERVO_PIN 10

#define TOP_LASER_PIN PC4
#define BOX_1_LASER_PIN PC3
#define BOX_2_LASER_PIN PC2
#define BOX_3_LASER_PIN PC1
#define BOX_4_LASER_PIN PC0

#define MAX_INT 2147483647

Servo left_latch;
Servo right_latch;
Servo middle;
Servo left;
Servo right;


int top_laser = 1;
int box_1_laser = 1;
int box_2_laser = 1;
int box_3_laser = 1;
int box_4_laser = 1;


int timeout = 0;
int sum = 0;
int box_number;
int seq = 0;

char bytes[100] = "";
String incomingBytes;


typedef enum{
  WAITING_FOR_CONNECTION,
  WAITING_FOR_MAIL,
  WAITING_FOR_PI,
  WAITING_FOR_DROP
}MailState;

MailState state = WAITING_FOR_CONNECTION;

void setup() {
  
  Serial.begin(9600);
  
  //Assign pins to motor
  left_latch.attach(LL_SERVO_PIN);
  right_latch.attach(RL_SERVO_PIN);
  middle.attach(M_SERVO_PIN);
  left.attach(L_SERVO_PIN);
  right.attach(R_SERVO_PIN);
  
  //SETTING LASER PIN TO INPUT
  pinMode(TOP_LASER_PIN, INPUT);
  pinMode(BOX_1_LASER_PIN, INPUT);
  pinMode(BOX_2_LASER_PIN, INPUT);
  pinMode(BOX_3_LASER_PIN, INPUT);
  pinMode(BOX_4_LASER_PIN, INPUT);

  // reset servos to neutral pos
  reset_servo();
}

void reset_servo(){
  left_latch.write(LL_CLOSED);
  right_latch.write(RL_CLOSED);
  delay(1000);
  middle.write(NEUTRAL);
  left.write(NEUTRAL);
  right.write(NEUTRAL);
  delay(5000);
}



void send_to_box_1(){
    // STEP 1: Conrol inside servos
    left.write(L_135);
    middle.write(M_135);
    delay(1000);
    // STEP 2: Control latch servos
    left_latch.write(LL_OPEN);
    right_latch.write(RL_OPEN);
    delay(1500);
}

void send_to_box_2(){
  // STEP 1: Conrol inside servos
  left.write(L_45);
  middle.write(M_135);
  delay(100);
  // STEP 2: Control latch servos
  left_latch.write(LL_OPEN);
  right_latch.write(RL_OPEN);
  delay(1500);

}

void send_to_box_3(){
// STEP 1: Conrol inside servos
  right.write(R_135);
  middle.write(M_45);
  delay(100);
  // STEP 2: Control latch servos
  left_latch.write(LL_OPEN);
  right_latch.write(RL_OPEN);
  delay(1500);


}

void send_to_box_4(){
// STEP 1: Conrol inside servos
  right.write(R_45);
  middle.write(M_45);
  delay(100);
  // STEP 2: Control latch servos
  left_latch.write(LL_OPEN);
  right_latch.write(RL_OPEN);
  delay(1000);

}


int validString(char* bytes){
  int ret = strncmp(bytes, "Box: ", 5);
  if (ret == 0){
    return 1;
  }
  return ret;
}

int parseString(char* bytes){
  return atoi((char*)(bytes+5));
}

void loop() {
  while(state == WAITING_FOR_CONNECTION){
    incomingBytes = Serial.readStringUntil('\n');
    if (incomingBytes == "Begin"){
      state = WAITING_FOR_MAIL;
      Serial.println("Estab\n");
    }else{
      state = WAITING_FOR_CONNECTION;
    }
  }

  while (state == WAITING_FOR_MAIL){
    // Mail has shown up on the sensor
    reset_servo();
    memset(bytes, '\0', 100);
    box_number = -1;
    incomingBytes = "";
    if ((top_laser = analogRead(TOP_LASER_PIN)) > 512){
      Serial.printf("Ready\n", top_laser);
      state = WAITING_FOR_PI;
    }
  }

  while (state == WAITING_FOR_PI){
    incomingBytes = Serial.readStringUntil('\n');
    incomingBytes.toCharArray(bytes, 100);
    // Check for a valid string
    if (validString(bytes) == 1){
      box_number = parseString(bytes);
      switch (box_number){
        case 1:
          send_to_box_1();
          state = WAITING_FOR_DROP;

          break;
        case 2:
          send_to_box_2();
          state = WAITING_FOR_DROP;
          break;
        case 3:
          send_to_box_3();
          state = WAITING_FOR_DROP;
          break;
        case 4:
          send_to_box_4();
          state = WAITING_FOR_DROP;
          break;
        default:
          Serial.printf("\tInvalid Box Number: %d\n", box_number);
          state = WAITING_FOR_PI;
          break;
      }
    }else{
      Serial.printf("\tInvalid, Recieved:%s\n", bytes);
      state = WAITING_FOR_PI;
    }
  }

  while (state == WAITING_FOR_DROP){
    
    box_1_laser = analogRead(BOX_1_LASER_PIN);
    box_2_laser = analogRead(BOX_2_LASER_PIN);
    box_3_laser = analogRead(BOX_3_LASER_PIN);
    box_4_laser = analogRead(BOX_4_LASER_PIN);
    sum =  box_1_laser + box_2_laser + box_3_laser;
    // We have something blocking one of the sensors so we send the values of the lasers to the pi for debugging
    if (sum > 1536){
      Serial.printf("Mail is blocking sensor!! Box 1: %d\tBox 2: %d\tBox 3: %d\tBox 4: %d\tSum: %d\n", box_1_laser, box_2_laser, box_3_laser, box_4_laser, sum);
      state = WAITING_FOR_MAIL;
      sum = 0;
    }else{
      if (box_number == 4){
        delay(5000);        
        Serial.printf("Mail is blocking sensor!! Box 1: %d\tBox 2: %d\tBox 3: %d\tBox 4: %d\tSum: %d\n", box_1_laser, box_2_laser, box_3_laser, box_4_laser, sum);
        state = WAITING_FOR_MAIL;
      }else if (box_1_laser > 512){
        // Serial.println("Mail: 1 \n");
        Serial.printf("Mail is blocking sensor!! Box 1: %d\tBox 2: %d\tBox 3: %d\tBox 4: %d\tSum: %d\n", box_1_laser, box_2_laser, box_3_laser, box_4_laser, sum);
        state = WAITING_FOR_MAIL;
      }else if (box_2_laser > 512){
        // Serial.println("Mail: 2 \n");
        Serial.printf("Mail is blocking sensor!! Box 1: %d\tBox 2: %d\tBox 3: %d\tBox 4: %d\tSum: %d\n", box_1_laser, box_2_laser, box_3_laser, box_4_laser, sum);
        state = WAITING_FOR_MAIL;
      }else if (box_3_laser > 512){
        // Serial.println("Mail: 3 \n");
        Serial.printf("Mail is blocking sensor!! Box 1: %d\tBox 2: %d\tBox 3: %d\tBox 4: %d\tSum: %d\n", box_1_laser, box_2_laser, box_3_laser, box_4_laser, sum);
        state = WAITING_FOR_MAIL;
      }else if (timeout >= MAX_INT-10){
        Serial.println("Mail timed out.\n");
        state = WAITING_FOR_MAIL;
        timeout = 0;
      }else{
        timeout++;
      }
    }
    sum = 0;
  }



}

//TODO: Check is laser interface is right.
```

# Week 15 (4/24):

Fine-tuned everything for Final Demo. Troubleshooted every loose connection. Had trouble with one of the sensors in the mailbox but hard-codded the mail entry for that mox for the Final Demo. 

# Week 16 (5/1):

Finished Final Presentation. 


# Citations:

[1] 	“ATMEGA328 - Microchip Technology,” MicroChip. [Online]. Available: https://www.microchip.com/en-us/product/ATmega328. [Accessed: 30-Mar-2023]. 

[2] Ed, “Raspberry pi arduino serial communication - everything you need to know ,” The Robotics Back-End, 30-Jan-2023. [Online]. Available: https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/. [Accessed: 04-May-2023]. 

[2]	L. George, “Interfacing servo motor with Atmega32 Atmel AVR Microcontroller,” electroSome, 01-Apr-2018. [Online]. Available: https://electrosome.com/interfacing-servo-motor-with-atmega32-microcontroller/. [Accessed: 29-Mar-2023]. 

[3] 	“Stepper Motors vs. Servo Motors,” ISL Products. [Online]. Available: https://islproducts.com/design-note/stepper-motors-vs-servo-motors/#:~:text=Servo%20motors%20can%20generate%20speeds,and%20generate%20higher%20peak%20torque. [Accessed: 29-Mar-2023]. 

[4] 	Z. Khodzhaev, “Monitoring Different Sensors with ATmega328 Microprocessor,” Research Gate, Jun-2016. [Online]. Available: https://www.researchgate.net/publication/325154131_Monitoring_Different_Sensors_with_ATmega328_Microprocessor. [Accessed: 29-Mar-2023]. 

