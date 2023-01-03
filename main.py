# File: main.py
# Function: hoofdprogramma van de interval generator
#           
# Opmerking: Dit script vereist de aanwezigheid van pygame
#            zie http://www.pygame.org/download.shtml
#            install Ubuntu 20.04/22.04 
#            sudo apt-get install python3-pygame
#            sudo apt-get install python3-pygame-sdl2
# 
#            Dit script vereist de aanwezigheid van timidity
#            install Ubuntu 20.04/22.04 
#            sudo apt-get install timidity
#
#            timidity vereist de aanwezigheid van freepats
#            sudo apt install freepats
#            zie ook https://askubuntu.com/questions/1237960/how-to-use-timidity-in-ubuntu-18-04

# Werkt tegen music21 versie 7.1.0

# Letop er vindt nog geen input validatie plaats in het script. !!!!


import music_utils as mu
import random as rnd
import music21 as m
import time as ti

# Constants
# Status Naming conventions Constants: 
# BASE = 0.25 # round Note durations to multiples of base factors. Round 1/4 notes to base=0.25 and 1/8 notes to base=0.125 0.0625, 0,03125 etc
SCOREPATH = "/home/claude/Documents/sources/python/python3/cx1964ReposPubWritingMusicalMelody"
# Export de MuseScore File in musicxml (uncompressed music xml format musicxml extention)
MUSESCOREFILE = "C_major_scale_ascending_mixed_duration.musicxml" # in musicxml uncompressed
MUSESCOREPROG='MuseScore-4.0.0-x86_64.appimage'
MUSESCOREPROGPATH='/home/claude/Applications/'
SCORE_TITLE="python3 Writing Musical Melody"
COMPOSER="cx1964"

mu.set_environment(MUSESCOREPROGPATH, MUSESCOREPROG)

modeProperties = mu.get_mode_properties('phrygian')
finalis      = modeProperties['finalis']
ambititus    = modeProperties['ambititus']
scaleDegrees = modeProperties['scaleDegrees']
# debug
#print('finalis:', finalis)
#print('ambititus:', ambititus)
#print('scaleDegrees:', scaleDegrees)


# Test
print('# Doc: https://en.wikipedia.org/wiki/Mode_(music)')
scale = mu.generate_mode('dorian', 'd' )
print('dorian ', 'scale:', scale )
print('\n')

scale = mu.generate_mode('dorian', 'c' )
print('dorian ', 'scale:', scale )
print('\n')

scale = mu.generate_mode('phrygian', 'c' )
print('phrygian ', 'scale:', scale )
print('\n')

scale = mu.generate_mode('lydian', 'c' )
print('lydian ', 'scale:', scale )
print('\n')

scale = mu.generate_mode('mixolydian', 'c' )
print('mixolydian ', 'scale:', scale )
print('\n')

scale = mu.generate_mode('aeolian', 'c' )
print('aeolian ', 'scale:', scale )
print('\n')

scale = mu.generate_mode('locrian', 'c' )
print('locrian ', 'scale:', scale )
print('\n')
# Test
#print("\n")
#print("debug  in main.py")
#print("onderstaande code weg halen")
#print("Test function generate_scale()")
#s=mu.generate_scale('c')
#print(s)
#s=mu.generate_scale('g')
#print(s)
#s=mu.generate_scale('a')
#print(s)
#x=mu.generate_scale('c#')
#x=mu.generate_scale('c++')
#x=mu.generate_scale('h')
#x=mu.generate_scale('k')

print("Finished")
