#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import listdir
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import re, shutil
import os

import shazam

matches = [r'.+\.mp3', r'.+\.wav', r'.+\.ogg']

filesList = listdir()

def __create_folder_if_not_exists__(name):
    try:
        os.mkdir(name)
    except:
        pass

for i in filesList:
    for j in matches:
        if re.match(j, i):
            tags = shazam.audio_recognize(i)
            if tags == 0:
                __create_folder_if_not_exists__('Untagged')
                shutil.move(i, 'Untagged/' + i)
                break
            else:
                mp3 = MP3File(i)
                mp3.song = tags['title']
                mp3.artist = tags['subtitle']
                mp3.album = tags['album']
                mp3.year = tags['year']
                mp3.copyright = tags['label']
                mp3.save()
                os.rename(i, tags['subtitle'] + ' - ' + tags['title'] + j.replace('+\.', ''))
                break