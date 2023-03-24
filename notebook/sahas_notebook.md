## 2/13 - Week 1

After submitting the proposal, this week was mainly used to gather information about parts we can use and start writing the design document. We have decided to make a mail sorter that can sort mail based on images it takes, then guide the mail to the correct box using gravity. Here is our example design

![Dimensioned Drawing](sahas_images/image14.png)

Me and Angelo spent the weekend developing this dimensioned drawing so we can hand it over to the machine shop for fabrication. The mail will be held up by two acrylic pieces, then dropped through a gate into the system. The paddles will flip in the direction necessary to guide the mail to the slot. At the end, a laser break system is used to determine if the mail has crossed the threshold, and the system is ready to take in the next piece of mail.


## 2/20 - Week 2

This week was spent mainly sourcing parts for our design. We are heavily relying on amazon to ship us items in two days or less for the more common parts. We are currently looking at Mouser and Digikey for smaller, more obscure parts, but we are trying to limit that as much as possible. Also, we are still writing out our design document. There are lots of small sections that require figures we don’t have. 

## 2/27 - Week 3

We had our design review this week. We brought our design and images to the table, and were largely okay’d. We had to make some changes to the document, such as adding a requirements and verification section for each of the subsystems. Other than that, work was ready to start for the project. The first step was the PCB design. Using KiCad and Google, I mocked up an example schematic that would work for our design. Here is the schematic:

![First Schematic Drawing](sahas_images/image6.png)

The PCB has not been routed yet, but the design is there. We have not been able to test the schematic on the breadboard as we do not have a lot of the necessary components to build the circuit.

## 3/6 - Week 4

This week there was a lot of back and forth on the design with the machine shop. As the deadline for revisions to the work was Friday and right before break, we were scrambling to make sure the machine shop has everything they needed from us. We supplied the dimensioned drawing, with some small changes, and brought them some example parts so they could start development over the weekend. Also, this week, our first PCB was ordered (pictured). We still have not had a chance to test the circuit on a breadboard so this is just a shot in the dark.

![First PCB Drawing](sahas_images/image15.png)


## 3/20 - Week 5

Over break, no progress was made on the side of our team. We checked in with the machine shop, and progress has started on the design, but it is far from done. This week, we still haven’t received the PCB so progress was made on other subsystems. Work for the OCR subsystem has begun. I created a jupyter notebook and python environment with all the necessary libraries. I am able to take pictures with a USB webcam, and process them before sending to pytesseract OCR. This is the temporary code for the image processing pipeline.

![OCR Pipeline](sahas_images/image16.png)

First the image is converted to grayscale to reduce the amount of data by a factor of 3. Then, the image is cut to size based on where we expect the text to be. Next, A threshold is applied to convert the grayscale images to completely white or black pixels. Finally, a deskew is applied to make sure the lines are properly horizontal for the OCR to recognize. I played around with a few more filters, such as dilate and erode, but the improvement was small. Rather than leave it in with little idea of what it is doing, I decided to remove dilate/erode from the pipeline. I was following instructions from this link: Optical Character Recognition | OCR Text Recognition (analyticsvidhya.com)





