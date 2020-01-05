#author: hanshiqiang365 （微信公众号：韩思工作室）

import os
from ffmpy3 import FFmpeg

changefile = 'Sakura_Draw.mp4'
outputfile = 'Sakura_Draw.mp4.wav'

ff = FFmpeg(inputs={changefile: None},outputs={outputfile: '-vn -ar 44100 -ac 2 -ab 192 -f wav'})
print(ff.cmd)
ff.run()

        
