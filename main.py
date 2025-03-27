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

def followLine(speed:int, speed_slow:int):
    
    # On teste si les capteurs infrarouge frontaux L1 et R1 détecte la bande noire
    if line_sensor(LineSensor.M)== WHITE:
        # On est sur la bande noire, on continue tout droit.
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
        motor_run(Motor.LEFT, speed )
    
    elif line_sensor(LineSensor.L1)==BLACK and line_sensor(LineSensor.M)==BLACK:
        display.show("V")
        motor_run(Motor.RIGHT, speed, MOTOR_BACKWARD)
        utime.sleep_ms(200)
        motor_run(Motor.LEFT, speed_slow)
        utime.sleep_ms(150)
       
   elif line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.M)==BLACK:
        display.show("X")
        motor_run(Motor.LEFT, speed, MOTOR_BACKWARD)
        utime.sleep_ms(200)
        motor_run(Motor.RIGHT, speed_slow)
        utime.sleep_ms(150)    

    utime.sleep_ms(50)

while True:
    if Init:
        # Vitesse maximale des moteurs (min:0, max:255)
        speed:int = 20   #70
        speed_slow:int = 5 #15

        display.show("1")
        utime.sleep_ms(3000)
        Init = False

    followLine(speed, speed_slow)
