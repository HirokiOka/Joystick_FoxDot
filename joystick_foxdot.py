from FoxDot import *
import pygame
from pygame.locals import *
import time

def main():
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    print('joystick start')

    pygame.init()

    pan = 0
    formant = 0
    play0 = False
    play1 = False
    play2 = False
    play3 = False


    while True:
        eventlist = pygame.event.get()

        for e in eventlist:
            if e.type == QUIT:
                return

            if e.type == pygame.locals.JOYHATMOTION:
                x, y = joystick0.get_hat(0)
                p = x
                if y == 1:
                    Clock.bpm += 10
                elif y == -1:
                    Clock.bpm -= 10
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                print('button:' + str(e.button))
                if e.button == 0:
                    if play0 == False:
                        d1 >> play("x-o-", pan=pan, formant=formant)
                        play0 = True
                    else:
                        d1.stop()
                        play0 = False

                elif e.button == 1:
                    if play1 == False:
                        p1 >> saw(P[:6].shuffle(100), dur=1/4, pan=pan, formant=formant).penta()
                        play1 = True
                    else:
                        p1.stop()
                        play1 = False

                elif e.button == 2:
                    if play2 == False:
                        b1 >> bass(dur=4, pan=pan, formant=formant)
                        play2 = True
                    else:
                        b1.stop()
                        play2 = False

                elif e.button == 3:
                    if play3 == False:
                        f1 >> snick(dur=4).spread()
                        play3 = True
                    else:
                        f1.stop()
                        play3 = False

                elif e.button == 4:
                    Root.default -= 1
                elif e.button == 5:
                    Root.default +=1
                elif e.button == 8:
                    Clock.bpm = 120
                    Root.default = 0
                elif e.button == 10:
                    formant += 1
                elif e.button == 13:
                    Clock.bpm = 120
                    Root.default = 0
                    formant = 0
                    Clock.clear()

        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except pygame.error:
        print('joystickが見つかりませんでした．')
