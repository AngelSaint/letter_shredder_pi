NOTEBOOK : I was in charge of the Mail Sorting subsystem

# Week 2 (1/23):

Wrote up project idea for self udjusting heated jacket on the Web Board:
My thoughts included having a sensor that would measure body temperature and adjust the temperature accordingly. It would auto-adjust itself when the ideal temperature is reached and gradually lower itself as to not overheat the person wearing it. There can even be buttons the wearer can press to manually adjust the temperature for further comfort.

Didn't get project approved by TA.

Found groupmates: Sahas Munamala (sahasrm2) and Angelo Santos (angelos4)

# Week 3 (1/30):

Worked on different project for a automatic Mail shredder and sorter that would read the address on mail and sort to mail box using OCR we found (https://tesseract-ocr.github.io/).

__TEAM MEMBERS:
Angelo Santos (angelos4)
Sahas Munamala (sahasrm2)
Lisa Pachikara (lisamp2)
PROBLEM
It is common for many residents to encounter mail that does not belong to them from prior tenants. The documents may contain personal information about that tenant that could risk security threats and negative legal implications. There are also many occasions where tenants currently living in apartments get unwanted mail from senders they would like to blacklist, or from advertisers.

SOLUTION
We propose a mail sorter and shredder that would organize mail based on the names of the tenants and the senders that are allowed/blacklisted from the mail system. Names on the allowlist are sorted into the respective bins. Blacklisted names are sent to the shredder.

This would be done by scanning the mail, extracting the necessary information from the labels of the mail, and comparing all features to determine bin placement.

SOLUTION COMPONENTS
Raspberry Pi
Camera x2
Microcontroller
Laser Block sensor
Motors x3
Shredder
SUBSYSTEMS
SUBSYSTEM 1: MAIL RECOGNITION/DETECTOR
This component will consist of an optical switch connected to the main control unit that will determine if mail is placed properly in the scanner. It will also contain 2 cameras and light sources to capture both sides of the mail.

SUBSYSTEM 2: MAIN CONTROL UNIT
Controls the image capturing of the camera based on the optical switch, and runs an OCR to determine the sender and receiver from the printed or handwritten text. It will then compares the data to names/aliases within a local database to determine the destination of the mail being processed. Further, it will send control signals to different electric motors in the organization system.

SUBSYSTEM 3: WEBSERVER
We will run a webserver hosted on a raspberry pi. This web server will be responsible for updating the machine's internal filters.

SUBSYSTEM 4: ORGANIZATION SYSTEM
This is the physical system that controls the directional movement of the documents such that it reaches the intended destination.

CRITERION FOR SUCCESS
Mail sorter can sort mail into individual slots
Mail sorter can read mail and extract necessary information like addresses/names from images of mail.
Mail sorter settings can be set remotely
Mail sorter can shred__

# Week 4 (2/6):

Got project approved. 
Decided not to include shredder anymore due to increased risk if the mail is shredded by mistake. 

Worked on Project Proposal. **Image 1** depicts the idea of the apparatus and how it will function. We chose to use the ATmega328p microcontroller for motor control and a Raspberry Pi for webserver and OCR. 

For Motor control: 
__This is the physical system that controls the directional movement of the documents such that it reaches the intended destination.
Requirements:
This subsystem will consist of multiple paddles along with a dropoff chute for the mail once it has been scanned. The main requirement of the motor dropoff is that it only releases the mail once it has been successfully scanned, and when the paddles are in the precise orientation that allows the mail to enter its respective box. The paddles must allow for consistent routing to the appropriate boxes, even under a significant load.
Tolerance:
This subsystem may fail mechanically due to the physical limitations of the materials used to construct the sorter. If there are any unwanted gaps in the system for the mail to fall into the wrong chute, it may diminish the use of our system. This can be mitigated through design choices and calibration of the motors controlling the paddles/latches. We will also have to run tests for the optimal timing of the mail release and paddle movement. __


We submitted **Image 3** to the machine shop and I wrote up the dimension description :
__For our physical design, the overall build will be composed of wood with a base dimension of 22.5 inches x 15.25 inches. The front of the apparatus will be covered with a see-through acrylic or plastic to be able to see the workings of the motorized parts and to make debugging much simpler. At the entryway of the mail, there will be a 0.5 inch opening to fit the size of our mail and have it sit upright for the picture to be taken properly. At the bottom, on both sides of each mailbox, there will be a 1 inch gap saved for the sensors to be placed. As can be seen in the diagram, there is more than enough space in the corners of the module to fit the power source input, and raspberry pi. This setup will include at least 5 inches of space in length to support wiring between the components.__


# Week 5 (2/13):


# Week 6 (2/20):

# Week 7 (2/27):

# Week 8 (3/6):

# Week 9 (3/13):

# Week 10 (3/20):

# Week 11 (3/27):

# Week 12 (4/3):

# Week 13 (4/10):

# Week 14 (4/17):

# Week 15 (4/24):

# Week 16 (5/1):