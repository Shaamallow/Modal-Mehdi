import pygame, numpy, random, time, platform, os, string, re, math
from pygame.constants import *
from math import * 
'''
Constants
'''


#Choix du systeme d'exploitation.
# Globals
fullscreen=False
refresh = 85
system = platform.system()
print('system:', system)
if system == 'Windows':    # tested with Windows 7
   os.environ['SDL_VIDEODRIVER'] = 'windows'
elif system == 'Darwin':   # tested with MacOS 10.5 and 10.6
   os.environ['SDL_VIDEODRIVER'] = 'Quartz'

bg = (127, 127, 127)
black = (0, 0, 0)
fg = (255, 255, 255)
W, H = 1024, 768
res = (W, H)
center_screen = (W/2, H/2)
letPerSec = .75
blipDur = 100
postRespDur = 200
feedbackDur = 2000

#en millisecondes : contrôle la durée du blanc
halflife=3000

pygame.init()
if fullscreen:
    screen = pygame.display.set_mode(res, HWSURFACE | FULLSCREEN | DOUBLEBUF)
    strict=True
else:
    screen = pygame.display.set_mode(res)

pygame.mouse.set_visible(False)
police=pygame.font.SysFont("Times", 80)

screen.fill(bg)
pygame.display.flip()


maxWidth = max([police.render(w.encode('utf-8'), 1, fg).get_rect().width for w in string.ascii_uppercase])
maxHeight=  max([police.render(w.encode('utf-8'), 1, fg).get_rect().height for w in string.ascii_uppercase])
marginX, marginYTop, marginYBottom = 150, 150, 200
ncols, nrows = 2, 2 

# Met le programme en pause pour un certain temps, en millisecondes.
pygame.time.wait(500)

## Fixation cross
x = police.render('+', 1, black)
rectx = x.get_rect()
rectx.center = center_screen

## Question mark : Affichage du point d'interrogation
ptdint = police.render('?', 1, black)
rectptdint = ptdint.get_rect()
rectptdint.center = center_screen

#Conserver les disques noirs pour aider à garder le rythme pendant l'interval
# de retention.
def doTrial (dur, nBlips, nLetters, feedback=True):
    ## The parameters are:
    ## - dur: duration of a trial
    ## - nBlips: number of metronome black disks
    ## - nLetters: the letters
    
    #Affichage des lettres
    for i in range(nLetters):
        stim = lList[i%(lenLetters+lenNums)]
        screen.fill(bg)
        screen.blit(stim[1], stim[2])
        pygame.display.flip()
        pygame.time.wait(blipDur)
        screen.fill(bg)
        pygame.display.flip()
        pygame.time.wait(int(1000./letPerSec) - blipDur)
        
    #Affichage des disques : tâche de rétention  
    for i in range(nBlips):
        screen.fill(bg)
        # stim = lList[(i+nLetters)%(lenLetters+lenNums)]
        # screen.blit(stim[1], stim[2])
        pygame.draw.circle(screen, black, center_screen, 25)
        pygame.display.flip()
        pygame.time.wait(blipDur)
        screen.fill(bg)
        pygame.display.flip()
        pygame.time.wait(int(1000./letPerSec) - blipDur)
    startLet = (nBlips+nLetters+1)%(lenLetters+lenNums)
    screen.fill(bg)
    pygame.display.flip()
    pygame.time.wait(dur)
    # t0 = pygame.time.get_ticks()
    # i = 0
    # while pygame.time.get_ticks() - t0 < dur:
    #     stim = lList[(i+nLetters+nBlips)%(lenLetters+lenNums)]
    #     screen.fill(bg)
    #     screen.blit(x, rectx)
    #     screen.blit(stim[1], stim[2])
    #     pygame.display.flip()
    #     pygame.time.wait(blipDur)
    #     screen.fill(bg)
    #     pygame.display.flip()
    #     pygame.time.wait(int(1000./letPerSec) - blipDur)
    #     i=i+1
        

    screen.fill(bg)
    screen.blit(ptdint, rectptdint)
    pygame.display.flip()
    done, t0 = False, pygame.time.get_ticks()
    pygame.event.clear()

    
    while not done:
        ev = pygame.event.wait()
        if ev.type == KEYDOWN:
            if re.search(ev.unicode, string.ascii_lowercase):
                done, resp , rt = True, ev.unicode, pygame.time.get_ticks() - t0
                screen.fill(bg)
                print(resp.upper())
                try:
                    respN = stims.index(resp.upper())
                    screen.blit(lList[respN][1], lList[respN][2])
                except:
                    respN = 99
                    roh = police.render(resp.upper(), 1, (255, 0, 0))
                    rohRect = roh.get_rect()
                    rohRect.center = center_screen
                    screen.blit(roh, rohRect)

                pygame.display.flip()
                pygame.time.wait(1000)
    

    screen.fill(bg)
    pygame.display.flip()
    pygame.time.wait(postRespDur)

    tnum = int( ((dur/1000.) * letPerSec + startLet) % lenStims )

    if feedback:
        screen.fill(bg)
        screen.blit(lList[tnum][1], lList[tnum][2])
        pygame.display.flip()
        pygame.time.wait(feedbackDur)


    error = abs(tnum - respN)

    return(resp, error, respN, tnum, rt)



for i in range(10):
    lenLetters = random.randint(5,5)
    lenNums = 0
    lenStims = lenLetters+lenNums
    letters = string.ascii_uppercase
    l = [letters[i] for i in random.sample(list(range(26)), lenLetters)]
    n = [str(i) for i in random.sample(list(range(10)), lenNums)]
    stims=n+l
    random.shuffle(stims)
    lettersRendered = [police.render(i, 1, black) for i in stims]
    lettersRect = [i.get_rect() for i in lettersRendered]

    for i in lettersRect:
        i.center = center_screen

    lList = list(zip(stims, lettersRendered, lettersRect))

    dur = int( numpy.random.exponential(halflife) )
    print(dur)
    nLetters = 3 * (lenLetters+lenNums)
    nBlips = random.randint(2, 6)
    screen.fill(bg)
    pygame.display.flip()
    resp, error, respN, tnum, rt = doTrial(dur, nBlips, nLetters)
    print(resp, error, respN, rt)
    pygame.time.wait(2500)
    screen.fill(bg)
    pygame.display.flip()
    