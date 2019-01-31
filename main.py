import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


from picamera import PiCamera

from time import sleep



import RPi.GPIO as GPIO
import dht11
import time
import datetime
camera = PiCamera()

GPIO.setwarnings(False)



GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)

GPIO.setup(24, GPIO.OUT)

instance = dht11.DHT11(pin=14)

pwm = GPIO.PWM(24, 50)

pwm.start(7.5)

while(1):

               
           
        for i in range(0,180):
            DC=1./18.*(i)+2
            pwm.ChangeDutyCycle(DC)
            if GPIO.input(23):
                    pwm.stop()
                   
                    
                    print("  FIREEEEEE   ")
                    
                    result = instance.read()
                    print("Last valid input: " + str(datetime.datetime.now()))
                    print("Temperature: %d C" % result.temperature)
                    print("Humidity: %d %%" % result.humidity)

                    print('Taking picture')
                    print('3')
                    time.sleep(1)
                    print('2')
                    time.sleep(1)
                    print('1')

                    camera.start_preview()

                    camera.capture('/home/pi/Desktop/Project/image.jpg')
                    camera.stop_preview()

                    print('Picture taken')

                    print('Mail Sending .....')
                
                    
                    
                    email_user = 'kyctnn@gmail.com'
                    email_password = 'limon26kaya'
                    email_send = 'kyctnn@gmail.com'

                    subject = 'subject'

                    msg = MIMEMultipart()
                    msg['From'] = email_user
                    msg['To'] = email_send
                    msg['Subject'] = subject
                    result = instance.read()

                    body = ' test'
                    msg.attach(MIMEText(body,'plain'))

                    filename='image.jpg'
                    attachment  =open(filename,'rb')

                    part = MIMEBase('application','octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',"attachment; filename= "+filename)

                    msg.attach(part)
                    text = msg.as_string()
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email_user,email_password)


                    server.sendmail(email_user,email_send,text)
                    print('Mail Sended')
                    server.quit()
                    pwm = GPIO.PWM(24, 50)

                    pwm.start(7.5)
                     
            time.sleep(.02)
        for i in range(180,0,-1):
            DC=1./18.*(i)+2
            pwm.ChangeDutyCycle(DC)
            if GPIO.input(23):
                    pwm.stop(DC)
                    
                    print(" FIREEEEEE  ")

                    result = instance.read()
                    print("Last valid input: " + str(datetime.datetime.now()))
                    print("Temperature: %d C" % result.temperature)
                    print("Humidity: %d %%" % result.humidity)

                    print('Taking picture')
                    print('3')
                    time.sleep(1)
                    print('2')
                    time.sleep(1)
                    print('1')
                    

                    camera.start_preview()

                    camera.capture('/home/pi/Desktop/Project/image.jpg')
                    camera.stop_preview()

                    print('Picture taken')

                    print('Mail Sending .....')
                    
                    email_user = 'kyctnn@gmail.com'
                    email_password = 'limon26kaya'
                    email_send = 'kyctnn@gmail.com'

                    subject = 'subject'

                    msg = MIMEMultipart()
                    msg['From'] = email_user
                    msg['To'] = email_send
                    msg['Subject'] = subject
                    result = instance.read()

                    body = ' test'
                    msg.attach(MIMEText(body,'plain'))

                    filename='image.jpg'
                    attachment  =open(filename,'rb')

                    part = MIMEBase('application','octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',"attachment; filename= "+filename)

                    msg.attach(part)
                    text = msg.as_string()
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email_user,email_password)


                    server.sendmail(email_user,email_send,text)
                    print('Mail Sended')
                    server.quit()
                    pwm = GPIO.PWM(24, 50)

                    pwm.start(7.5)
                 
            time.sleep(.02)
        
            

pwm.stop()
GPIO.cleanup()

