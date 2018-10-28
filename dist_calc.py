import RPi.GPIO as G
import time

G.setmode(G.BCM)

speed = 0.0343 #in cm/microS

trig, echo = 16,18

G.setup(trig, OUT)
G.setup(echo, IN)

G.output(trig, True)
time.sleep(0.000002)
G.output(trig, False)

while G.input(echo) == 0:
	pulse_start = time.time()

while G.input(echo) == 1:
	pulse_end = time.time()

time_taken = pulse_end - pulse_start

distace = (time_taken * speed)/2.0

print "Object is", distace, "centimeters away"
time.sleep(1)

GPIO.cleanup()
