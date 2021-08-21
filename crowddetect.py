import conf,email_conf
from boltiot import Email,Sms,Bolt
import json,time
#conf,email_conf contains keys required
threshold=#no of max people in mall

mybolt=Bolt(conf.API_KEY,conf.DEVICE_ID)
sms=Sms(conf.SID,conf.AUTH_TOKEN,conf.TO_NUMBER,conf.FROM_NUMBER)
mailer=Email(email_conf.MAILGUN_API_KEY,email_conf.SANDBOX_URL,email_conf.SENDER_EMAIL,email_conf.RECEPIENT_EMAIL)
count=0#no of people in mall or public place
while True:
    print("Reading sensor Value:")
    response=mybolt.digitalRead("0")
    data=json.loads(response)
    print("Sensor value is:"+str(data['value']))
    try:
        sensor_value=int(data['value'])
        if sensor_value==1:
            print("Person entered")
            count=count+1
            print("No of persons in mall at present:"+str(count))
            mybolt.digitalWrite('2','HIGH')
        else:
            print("No one entered")
            mybolt.digitalWrite('2','LOW')
        if count>threshold:
            mybolt.digitalWrite('1','HIGH')
            mybolt.digitalWrite('2','HIGH')
            print("Making request to Twillio to send sms")
            response1=sms.send_sms("The no of people in the mall has reached the threshold:"+str(threshold))
            print("Making request to Mailgun to send Email")
            response2=mailer.send_email("Crowd Increased","The no of people in the mall has reached the threshold:"+str(threshold))
    except Exception as e:
        print("error occured:",e)
    if count>threshold:
        break
    mybolt.digitalWrite('2','LOW')
    time.sleep(10)
print("Crowd has to be reduced!!")
mybolt.digitalWrite('1','LOW')
mybolt.digitalWrite('2','LOW')
            
