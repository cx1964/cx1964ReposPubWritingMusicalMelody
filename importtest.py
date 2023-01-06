# File: importtest.py
# Function: python script tbv inlezen van een musicxml file
# Opmerking: gebruik dit script om te kijken hoe in MuseScore4 opgemaakte muziek er in musicxml eruit ziet in music21
#    

import music21 as m


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



bladmuziek = m.converter.parse('/home/claude/Desktop/sources/python/python3/cx1964ReposPubWritingMusicalMelody/importtest.ms4.musicxml', format='musicxml')


bladmuziek.write('musicxml.pdf', fp="./importtest.pdf")
# Toon bladmuziek
# mbv show('text') kijk naar de layout
bladmuziek.show('text')    