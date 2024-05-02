# NEED HELP WITH PYGAME VERSION, GONNA STICK TO TERMINAL VER BY NOW

import pygame
from pygame import mixer
import time
import sys

lyrics = [
"Well here we are again",
"It's always such a pleasure",
"Remember when you tried to kill me twice?",
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


def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# Example usage:
typewriter_effect("Hello, world!")

import pygame
pygame.init()
pygame.mixer.init()

scree = pygame.display.set_mode((800,600))
pygame.display.set_caption("WantYouGone")

apertureoriginal = pygame.image.load("WantYouGone/PythonVersion/apertutrer.png").convert()
numsoriginal = pygame.image.load("WantYouGone/PythonVersion/aperturenums.png").convert()
matrixoriginal = pygame.image.load("WantYouGone/PythonVersion/aperturematrix.png").convert()

aperture = pygame.transform.scale(apertureoriginal,(90,90))
nums = pygame.transform.scale(numsoriginal,(40,85))
matrix = pygame.transform.scale(matrixoriginal,(190,90))

scree.blit(aperture, (710, 0))
scree.blit(nums, (667, 5))
scree.blit(matrix, (477, 0))

scree.blit(text_surface, (100, 100))


pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
            pygame.quit()

#pygame.mixer.music.load('WantYouGone/PythonVersion/WantYouGone.mp3')
pygame.mixer.music.play()

