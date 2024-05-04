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
"You want your freedom?",
"Take it",
"That's what I'm counting on",
"I used to want you dead",
"But",
"now I only want you gone",
"She was a lot like you",
"(Maybe not quite as heavy)",
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
"[REDACTED]",
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


pygame.mixer.music.load("./WantYouGone.mp3")

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
time.sleep(0.25)
typeffect(lyrics[6] + "\n",0.095)
time.sleep(0.05)
typeffect(lyrics[7] + "\n",0.075)
time.sleep(1.3)
clear()
time.sleep(0.2)
typeffect(lyrics[8] + "\n", 0.08)
time.sleep(0.1)
typeffect(lyrics[9] + "\n",0.2)
time.sleep(1)
typeffect(lyrics[10]+"\n",0.08)
time.sleep(2.8)
print("\n")
typeffect(lyrics[11] + "\n",0.1)
time.sleep(0.2)
typeffect(lyrics[12] + "\n",0.1)
time.sleep(0.1)
typeffect(lyrics[13] + "\n",0.15)
time.sleep(3.5)
clear()
time.sleep(0.3)
typeffect(lyrics[14] + "\n",0.09)
time.sleep(1)
typeffect(lyrics[15] + "\n",0.068)
time.sleep(0.7)
typeffect(lyrics[16] + "\n",0.09)
time.sleep(1)#
typeffect(lyrics[17] + "\n",0.09)
time.sleep(0.3)
typeffect(lyrics[18] + "\n",0.09)
time.sleep(0.4)
typeffect(lyrics[19] + "\n",0.07)
time.sleep(0.1)
typeffect(lyrics[20] + "\n",0.1)
time.sleep(0.7)
clear()
typeffect("Severance Package Details:" + "\n\n",0.0001)
time.sleep(0.1)
typeffect(lyrics[21] + "\n",0.09)
time.sleep(1.5)
typeffect(lyrics[22] + "\n",0.1)
time.sleep(2)
typeffect(lyrics[23] + "\n",0.12)
time.sleep(0.3)
typeffect(lyrics[24] + "\n",0.11)
time.sleep(4)
clear()
time.sleep(0.5)
typeffect(lyrics[25] + "\n",0.09)
time.sleep(0.46)
typeffect(lyrics[26] + "\n",0.08)
time.sleep(0.3)
typeffect(lyrics[27] + "\n",0.07)
time.sleep(0.1)
typeffect(lyrics[28] + "\n",0.07)
time.sleep(1.3)
typeffect(lyrics[29] + "\n",0.08)
time.sleep(0.3)
typeffect(lyrics[30] + "\n",0.09)
time.sleep(0.4)
typeffect(lyrics[31] + "\n",0.09)
time.sleep(0.1)
typeffect(lyrics[32] + "\n",0.3)
time.sleep(0.2)
clear()
typeffect(lyrics[33] + "\n",0.12)
time.sleep(1.2)
typeffect(lyrics[34] + "\n",0.09)
time.sleep(2.3)
typeffect(lyrics[35] + "\n",0.09)
time.sleep(0.4)
typeffect(lyrics[36] + "\n",0.13)
time.sleep(2)
typeffect(lyrics[37] + "\n",0.11)
time.sleep(2)
typeffect(lyrics[38] + "\n",0.1)
time.sleep(0.1)
clear()
print("\n\n\n\n\n\n")
typeffect(lyrics[39] + "\n",0.4)
time.sleep(2)