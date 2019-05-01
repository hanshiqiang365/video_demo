#author: hanshiqiang365 （微信公众号：韩思工作室）

from PIL import Image, ImageSequence
import os

filename= "avengers3_snappingfinger"

os.system(f'ffmpeg -i {filename}.mp4 -f gif {filename}.gif')
with Image.open(f'{filename}.gif') as im:
    if im.is_animated:
        frames = [f.copy() for f in ImageSequence.Iterator(im)]
        frames.reverse() 
        frames[0].save(f'reversed_{filename}.gif', save_all=True, append_images=frames[1:])

os.system(f'ffmpeg -f gif -i reversed_{filename}.gif -vf scale=420:-2,format=yuv420p  reversed_{filename}.mp4')
