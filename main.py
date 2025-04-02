from microbit import*
from maprincess import *
import utime

'''
   /''''^''''\
  /  L1 M R1  \
 |             |
 |L2         R2|
o|.............|o

'''
# Constantes
WHITE = 0
BLACK = 1
MOTOR_FORWARD = 0
MOTOR_BACKWARD = 1

# Variable globale
Init = True

#code pas optimisé mais qui est censé marcher
def turnRight(speed:int, speed_slow:int):
    motor_run(Motor.RIGHT, speed, MOTOR_BACKWARD)
    utime.sleep_ms(200)
    motor_run(Motor.LEFT, speed_slow)
    utime.sleep_ms(150)
    
def turnLeft(speed:int, speed_slow:int):
    motor_run(Motor.LEFT, speed, MOTOR_BACKWARD)
    utime.sleep_ms(200)
    motor_run(Motor.RIGHT, speed_slow)
    utime.sleep_ms(150)
    
def U_turn(speed:int, speed_slow:int):
    motor_run(Motor.LEFT, speed, MOTOR_BACKWARD)
    motor_run(Motor.RIGHT, speed)
    utime.sleep_ms(200)


def followLine(speed:int, speed_slow:int):
    if line_sensor(LineSensor.M)== WHITE:
        # On est sur le noir on continue tout droit.
        display.show(Image.HAPPY)
        motor_run(Motor.LEFT, speed)
        motor_run(Motor.RIGHT, speed)

    elif line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.R1)==BLACK:        
        # On est sorti à gauche, il faut revenir un peu sur la droite.
        display.show("G") 
        motor_run(Motor.RIGHT, speed)
        motor_run(Motor.LEFT, speed_slow)

    elif line_sensor(LineSensor.L1)==BLACK and line_sensor(LineSensor.R1)==WHITE:
        # On est sorti à droite, il faut revenir un peu sur la gauche.
        display.show("D")
        motor_run(Motor.RIGHT, speed_slow)
        motor_run(Motor.LEFT, speed)
    
    elif line_sensor(LineSensor.L1)==BLACK and line_sensor(LineSensor.M)==BLACK:
        display.show("R")
        turnRight(speed:int, speed_slow:int)
       
    elif line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.M)==BLACK:
        display.show("L")
        turnLeft(speed:int, speed_slow:int)   

    utime.sleep_ms(50)



# Vitesse maximale des moteurs (min:0, max:255)
speed:int = 70   #70 de base
speed_slow:int = 15 #15 de base

while True:
    if Init:
        for k in range (3,0,-1):
           display.show("k")
           utime.sleep_ms(1000)
          
        Init = False

    followLine(speed, speed_slow)
