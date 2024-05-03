import pygame
import sys
import time
import os

lyrics = [
"Well here we are again",
"It's always such a pleasure",
"Remember when you tried","to kill me twice?",
"Oh how we laughed and laughed",
"Except I wasn't laughing",
"Under the circumstances",
"I've been shockingly nice",
"You want your freedom? Take it",
"That's what I'm counting on",
"I used to want you dead",
"But now I only want you gone",
"She was a lot like you",
"Maybe not quite as heavy",
"Now little Caroline is in here too",
"One day they woke me up",
"So I could live forever",
"It's such a shame the same",
"Will never happen to you",
"You've got your short sad life left",
"That's what I'm counting on",
"I'll let you get right to it",
"Now I only want you gone",
"Goodbye my only friend",
"Oh, did you think I meant you?",
"That would be funny",
"if it weren't so sad",
"Well you have been replaced",
"I don't need anyone now",
"When I delete you maybe",
"I'll stop feeling so bad",
"Go make some new disaster",
"That's what I'm counting on",
"You're someone else's problem",
"Now I only want you gone",
"Now I only want you gone",
"Now I only want you",
"gone"
]
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def typeffect(text, speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
        
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
pygame.init()
pygame.mixer.init()


pygame.mixer.music.load("WantYouGone/PythonVersion/WantYouGone.mp3")

pygame.mixer.music.play()

    
clear()
time.sleep(0.3)
typeffect("Forms FORM-29827281-12-2:\n",0.1)
time.sleep(0.3)
typeffect("Notice of Dismissal\n\n",0.1)
time.sleep(0.2)
typeffect(lyrics[0] + "\n",0.085)
time.sleep(0.3)
typeffect(lyrics[1] + "\n",0.066)
time.sleep(0.5)
typeffect(lyrics[2] + "\n",0.07)
time.sleep(0.15)
typeffect(lyrics[3] + "\n",0.1)
time.sleep(1)
typeffect(lyrics[4] + "\n",0.07)
time.sleep(0.6)
typeffect(lyrics[5] + "\n",0.09)