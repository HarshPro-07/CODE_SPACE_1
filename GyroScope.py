from time import sleep
import keyboard

x, y = 0, 0
dx, dy = 5, 5   #*Rate of Change in angles

def PrintStatus (x, y) :
    print(f'x : {x} :: y : {y}', end = '\r')

while True :
    if keyboard.is_pressed('x') :
        if keyboard.is_pressed('+') :
            if x >= 360 :
                sleep(0.1)
                x = 0
                x = x + dx
            else :
                x = x + dx  
        elif keyboard.is_pressed('-') :
            if x <= -360 :
                sleep(0.1)
                x = 0
                x = x - dx
            else :
                x = x - dx

    elif keyboard.is_pressed('y') :
        if keyboard.is_pressed('+') :
            if y >= 360 :
                sleep(0.1)
                y = 0
                y = y + dx
            else :
                y = y + dy
        elif keyboard.is_pressed('-') :
            if y <= -360 :
                sleep(0.1)
                y = 0
                y = y - dy
            else :
                y = y - dx

    PrintStatus(x, y)
    sleep(0.1)
