# File: main.py
# Function: python script tbv tonen van een genereerde Cantus Firmus melody volgens de regels van het Contrapunt
# Opmerking: 
#            

import music21 as m
import music_utils
from datetime import datetime
##import random


# ###  BEGIN Instellingen ###
tonica='c'
mode='dorian'
numNotes=20 # Max 20 en veelvoud van 4 ivm 4/4 maat
startOnTonic=True 
stopOnTonic=False

key_signature = m.key.Key('C') #  lowercase = minor key.
maxIntervalGrootte=4 # In aantal k2.  4 => G3 # max interval tussen de noten
onderDrukVoorTekens = True # boolean
aantalKwartNotenInMaat=4

score_title = "Gegenereerde Cantus Firmus "
subtitle = "sources: git clone https://github.com/cx1964/cx1964ReposPubWritingMusicalMelody.git"
composer = 'Claude la Fontaine'
# ###  EINDE Instellingen ###

time_signature = str(aantalKwartNotenInMaat)+"/4"

# Instellen van de Environment
# Zie: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html#usersguide-24-environment
env = m.environment.UserSettings()
env.delete()
env.create()
# set environmment
env['autoDownload'] = 'allow'
env['lilypondPath'] = '/usr/bin/lilypond'
#env['musescoreDirectPNGPath'] = 'musescore.mscore'  # Deze variant gebruiken indien musescore als package geinstalleerd is
env['musescoreDirectPNGPath'] = '/home/claude/Applications/MuseScore-4.0.0-x86_64.appimage' # Deze variant gebruiken indien musescore als appimage is geinstalleerd
# env['musicxmlPath'] = '/usr/bin/musescore3'  # Deze variant gebruiken indien musescore als package geinstalleerd is
env['musicxmlPath'] = '/home/claude/Applications/MuseScore-4.0.0-x86_64.appimage' # Deze variant gebruiken indien musescore als appimage is geinstalleerd


# Set Meta Data in estimated score
meta_data = m.metadata.Metadata()
meta_data.title = score_title

# YYYY/mm/dd
d1 = datetime.today().strftime("%Y/%m/%d")
meta_data.date = str(d1)
meta_data.composer = 'Mode: '+mode+ '          Gegenereerd door: '+ composer+" ("+str(d1)+")"
#meta_data.copywrite = 'bla' # composer+" ("+str(d1)+")"

# Create score
# zie: https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html
genScore = m.stream.Stream()

upperStaffClef=m.clef.TrebleClef()
lowerStaffClef=m.clef.BassClef()

myPart = m.stream.Part()
myPart_UpperStaff = m.stream.Part()
# set Clef UpperStaff
myPart_UpperStaff.append(upperStaffClef)

# set TimeSignature UpperStaff
myPart_UpperStaff.append(m.meter.TimeSignature(time_signature))
    
# set keySignature UpperStaff
myPart_UpperStaff.append(key_signature)
    
myPart_LowerStaff = m.stream.Part()
# set Clef UpperStaff
myPart_LowerStaff.append(lowerStaffClef)

# set TimeSignature LowerStaff
myPart_LowerStaff.append(m.meter.TimeSignature(time_signature))
    
# set keySignature LowerStaff
myPart_LowerStaff.append(key_signature)

# Do not use a Measure object
# If you use a Time Signature object without a Measure object
# when adding a notes, to a stream, measures are filled
# automatically bases on note lengths
myNote = m.note.Note()

myPart_UpperStaff.partName="Piano Upper"
#myPart_LowerStaff.partName="Piano Lower"

# ToDo

# ### Maak de noten ###
cf = music_utils.generate_modal_melody(mode, tonica, numNotes, startOnTonic, stopOnTonic)
cnt=0

for i in range(0, (len(cf)), 1):
   nootStr=cf[cnt]
   myNote=m.note.Note(nootStr, type="quarter")
   myPart_UpperStaff.insert(cnt, myNote) 
   cnt=cnt+1           

# Voeg Upperstaff aan bladmuziek 
genScore.insert(0, meta_data)
genScore.insert(1, myPart_UpperStaff)
# Toon de genereerde bladmuziek
# maak pdf aan
genScore.write('musicxml.pdf', fp="./output.pdf")

# roep musescore aan
genScore.show()
### Einde Code
 