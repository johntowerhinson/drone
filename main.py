import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

t1 = GPIO.PWM(7, 50)

t1.start(0)

t1.ChangeDutyCycle(5)
time.sleep(2)
t1.ChangeDutyCycle(10)
time.sleep(2)
t1.ChangeDutyCycle(5)
time.sleep(3)
t1.ChangeDutyCycle(5)
time.sleep(1)
t1.ChangeDutyCycle(6)
time.sleep(1)
t1.ChangeDutyCycle(7)
time.sleep(1)
t1.ChangeDutyCycle(8)
time.sleep(1)
t1.ChangeDutyCycle(9)
time.sleep(1)
t1.ChangeDutyCycle(10)
time.sleep(1)
t1.ChangeDutyCycle(9)
time.sleep(1)
t1.ChangeDutyCycle(8)
time.sleep(1)
t1.ChangeDutyCycle(7)
time.sleep(1)
t1.ChangeDutyCycle(6)
time.sleep(1)
t1.ChangeDutyCycle(5)
time.sleep(1)

t1.stop()

GPIO.cleanup()
quit()

