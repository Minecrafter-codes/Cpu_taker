# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:30:54 2022

@author: Asus
"""
# This requires Pygame Mixer and a sound to work
from pygame import mixer
from threading import Thread #uses Thread to do the trick


############################ Warning ########

# This ting is so loud. Pleas lower the volume first before executing it


#########################


mixer.init()
mixer.set_num_channels(10)


def thread():
    
    mixer.Sound.play(mixer.Sound('death.wav'))
    t = Thread(target=thread)
    t.start()
    t = Thread(target=threads)
    t.start()
    
def threads():
    
    mixer.Sound.play(mixer.Sound('death.wav'))
    t = Thread(target=threads)
    t.start()
    t = Thread(target=thread)
    t.start()


def py():
    import pygame
    pygame.init()
    pygame.display.set_mode((300, 300))
    while True:
        pygame.event.get()
        pygame.display.update()

#t = Thread(target=py)
#t.start()

def fo():
    while True:
        for i in range(100):
            l = Thread(target=loop)
            l.start()

def loop():
    while True:
        t = Thread(target=thread)
        t2 = Thread(target=threads)
        t3 = Thread(target=fo)
        t.start()
        t2.start()
        t3.start()
        
for i in range(100):
    l = Thread(target=loop)
    l.start()

while True:
    t = Thread(target=thread)
    t2 = Thread(target=threads)
    t.start()
    t2.start()
    
