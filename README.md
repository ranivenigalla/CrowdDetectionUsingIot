Introduction:
No one is oblivious of Corona Pandemic rechristen as COVID 19 by WHO that has wreaked havoc all around the globe. We are going through a precarious phase of life and death. So it becomes paramount that we keep ourselves safe and maintain good health. One way of restricting the spread of coronavirus is to maintain social distancing. We must watch out for those who show symptoms of flu, cough etc and refrain us from getting in contact with them.

The idea of this project is inspired by the ongoing crisis. It is important for the government and private places to take necessary steps in order to stop the further spread of the virus. It aims to detect the number of people entering or exiting a mall (or any public place) and if the value exceeds the threshold i.e max number of people in an area, then the respective staff or officials are alerted that more number of people have accumulated and it is dangerous. This helps the authorities in taking right decisions at that time and helps in controlling the spread of corona.

Steps or Procedure to be followed:
1) Get a 5V 1A mobile charger which has a micro-usb port and is usually used to charge your Android mobile. You can also use your laptop to power on the Bolt device.

2) Now that you have all the components, let's start with downloading the Bolt IoT mobile App and installing it in the mobile phone.

3) Download the ‘Bolt IoT’ App for Android or iOS.

4) You will need to create an account on the Bolt Cloud to control the Bolt device.

5) After creating the Bolt cloud account, you will see your Bolt device with status as 'ONLINE' on your account on the dashboard.

6) The output pin of PIR motion sensor should be connected with 0th GPIO pin and VCC of PIR sensor with VCC of bolt and GND(ground) of PIR sensor with GND pin of bolt.

7) Connect the shorter pin(-ve) to the GND of bolt device and longer(+ve) pin to 0th GPIO pin of bolt device.

8)Connect the +ve pin of Buzzer to digital pin 1 and -ve pin to GND.

9)Connect the longer pin(+ve) of LED to digital pin 2 and -ve pin to GND.

Working
Here the Python Script checks the output of PIR Sensor sent to the Bolt device from the Bolt Cloud for every 10 sec and if The PIR Sensor outputs 1 then it indicates that a new person has entered the mall, so it increments the count variable. Every time it reads a sensor value it checks if the count has reached the threshold. If it reaches the threshold, the LED and Buzzer are turned ON for 10 secs and then it requests the Twillio API to send message to concerned staff's phone number and requests the MailGun API to send notification to concerned staff's E-mail.

PIR(Passive Infrared Sensor):
PIR sensors allow you to sense motion, almost always used to detect whether a human has moved in or out of the sensor's range. They are small, inexpensive, low-power, easy to use and don't wear out. For that reason they are commonly found in appliances and gadgets used in homes or businesses. They are often referred to as PIR, Passive Infrared, Pyroelectric, or IR motion sensors.
The PIR sensor itself has two slots in it, each slot is made of a special material that is sensitive to IR. The lens used here is not really doing much and so we see that the two slots which could see past some distance (basically the sensitivity of the sensor). When the sensor is idle, both slots detect the same amount of IR, the ambient amount radiated from the room or walls or outdoors. When a warm body like a human or animal passes by, it first intercepts one half of the PIR sensor, which causes a positive differential change between the two halves. When the warm body leaves the sensing area, the reverse happens, whereby the sensor generates a negative differential change. These change pulses are what is detected.

Things used in this project:
Bolt wifi module
bolt android app
pir sensor
led
buzzer
twilio sms messaging api
mailgun mailing api
