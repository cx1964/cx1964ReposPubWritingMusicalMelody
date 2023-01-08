# file: t1.py

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

import random
s = m.stream.Stream()
for i in range(6):
    msr = m.stream.Measure(number=i + 1)
    if i % 3 == 0: # verdeel in 3en
       msr.append(m.layout.SystemLayout(isNew=True))
    msr.append(m.note.Rest(type='whole'))
    s.append(msr)
    for msr in s.getElementsByClass('Measure'):
        offsets = [x * .25 for x in range(16)]
        random.shuffle(offsets)
        offsets = offsets[:4]
        for o in offsets:
            te = m.expressions.TextExpression(o)
            te.style = 'bold'
            te.justify = 'center'
            #te.enclosure = 'rectangle'
            msr.insert(o, te)
s.show()