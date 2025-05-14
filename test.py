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
 

labyrinthe = [
[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,  100,  100,  100,  100,  100,  100,  100,  100,  100],
[100, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,    0],
[100, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,    0],
[100, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  100],
[100, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  100],
[100, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  100],
[100, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  100], 
[100, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  100],
[100, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  100],
[100, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  100],
[100, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  100],
[100, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  100],
[100, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11,  100],
[100, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12,  100],
[100, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13,  100],
[100, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14,  100],
[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
]
i = 15
j = 2
position = labyrinthe[i][j]
direction = 1
# 1 = droite / 2 = haut / 3 = bas / 4 = gauche
# départ = 33 du bas
print(position)
while True:
    led_rgb(rgb(255, 255, 255))
    print(line_sensor_data(LineSensor.M))
    sleep(1000)
    #200+  = blanc
    # 100 - 200 = ligne
    #-100 = noir
    if 100 < line_sensor_data(LineSensor.M) < 200:
       if direction == 1:
           if position < labyrinthe[i][j + 1]:
               motor_run(Motor.ALL, 30)
               utime.sleep_ms(1000)
               motor_stop()
               j = j + 1
               position = labyrinthe[i][j]
            else:
                utime.sleep_ms(500)
                motor_run(Motor.RIGHT, speed, MOTOR_BACKWARD)
                motor_run(Motor.LEFT, speed)
                utime.sleep_ms(500)
                direction = 2
       elif direction == 2:
           if position < labyrinthe[i - 1][j]:
               motor_run(Motor.ALL, 30)
               utime.sleep_ms(1000)
               motor_stop()
               i = i - 1
               position = labyrinthe[i][j]
            else:
                utime.sleep_ms(500)
                motor_run(Motor.RIGHT, speed, MOTOR_BACKWARD)
                motor_run(Motor.LEFT, speed)
                utime.sleep_ms(500)
                direction = 4
       elif direction == 3:
           if position < labyrinthe[i + 1][j]:
               motor_run(Motor.ALL, 30)
               utime.sleep_ms(1000)
               motor_stop()
               i = i + 1
               position = labyrinthe[i][j]
            else:
                utime.sleep_ms(500)
                motor_run(Motor.RIGHT, speed, MOTOR_BACKWARD)
                motor_run(Motor.LEFT, speed)
                utime.sleep_ms(500)
                direction = 3
       elif direction == 4:
           if position < labyrinthe[i][j - 1]:
               motor_run(Motor.ALL, 30)
               utime.sleep_ms(1000)
               motor_stop()
               j = j - 1
               position = labyrinthe[i][j]
           
    elif line_sensor(LineSensor.M) == BLACK:
        if direction == 1:
            labyrinthe[i][j + 1] = 100
            for k in range(j):
                labyrinthe[i][j] = labyrinthe[i][j] + 2
        elif direction == 2:
            labyrinthe[i - 1][j] = 100
            for k in range(i,0,-1):
                labyrinthe[i][j] = labyrinthe[i][j] + 2
        elif direction == 3:
            labyrinthe[i + 1][j] = 100
            for k in range(i):
                labyrinthe[i][j] = labyrinthe[i][j] + 2
        elif direction == 4:
            labyrinthe[i][j - 1] = 100
            for k in range(j,0,-1):
                labyrinthe[i][j] = labyrinthe[i][j] + 2