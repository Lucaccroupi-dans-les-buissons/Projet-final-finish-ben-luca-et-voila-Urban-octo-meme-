from microbit import*
from maprincess import *
from protocole import *
import utime

'''
   /''''^''''\
  /  L1 M R1  \
 |             |
 |L2         R2|
o|.............|o
+9
'''
# Constantes
WHITE = 0
BLACK = 1
MOTOR_BACKWARD = 1

#radio
userId = 0
destId = 1

# Variable globale
Init = True
true = True

def followLine(speed:int, speed_slow:int):
    
    if line_sensor(LineSensor.R2)== BLACK and line_sensor(LineSensor.M) == BLACK :
        # On tourne 90° à gauche
        display.show("L")
        motor_stop()
        utime.sleep_ms(500)
        motor_run(Motor.RIGHT, speed)
        motor_run(Motor.LEFT, speed, MOTOR_BACKWARD)
        utime.sleep_ms(500)
        led_rgb(rgb(255,255,255))
        
    elif line_sensor(LineSensor.R2)== WHITE and line_sensor(LineSensor.L2) == WHITE :
        # On tourne 90° à droite       
        display.show("R")
        motor_stop()
        utime.sleep_ms(500)
        motor_run(Motor.RIGHT, speed, MOTOR_BACKWARD)
        motor_run(Motor.LEFT, speed)
        utime.sleep_ms(500)
        led_rgb(rgb(255,255,255))
        
    elif line_sensor(LineSensor.R1)== WHITE and line_sensor(LineSensor.R2)== BLACK:
        # On est entre les bandes noires, on continue tout droit.
        display.show(Image.HAPPY)
        motor_run(Motor.LEFT, speed)
        motor_run(Motor.RIGHT, speed)
        led_rgb(rgb(255,255,255))
        
    elif line_sensor(LineSensor.R2) == WHITE and line_sensor(LineSensor.L2) == BLACK:        
        # On est sorti à gauche, il faut revenir un peu sur la droite.
        display.show("D") 
        motor_run(Motor.RIGHT, speed_slow)
        motor_run(Motor.LEFT, speed)
        led_rgb(rgb(255,50,50))
        
    elif line_sensor(LineSensor.R1) == BLACK:
        # On est sorti à droite, il faut revenir un peu sur la gauche.
        display.show("G")
        motor_run(Motor.RIGHT, speed)
        motor_run(Motor.LEFT, speed_slow)
        led_rgb(rgb(255,0,0))
        
    utime.sleep_ms(50)

while True:
    if Init:
        # Vitesse maximale des moteurs (min:0, max:255)
        speed:int = 70   #70
        speed_slow:int = 15 #15
        led_rgb(rgb(255,255,255))
        for k in range(3,0,-1):
            display.show(k)
            utime.sleep_ms(500)
        Init = False
        
    while true:
        followLine(speed, speed_slow)
        if 3 < ultrasonic() < 8:
            true = False
            
    motor_stop()
    led_rgb(rgb(0,255,0))
    send_msg(1,[1],userId, destId)
    