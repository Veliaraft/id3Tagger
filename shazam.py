#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ShazamAPI import Shazam

'''audio_recognize returns a list of values in next perfomance:
- Name(title)
- Artist(subtitle)
- Album(album)
- Label(label)
- Year(year)
- Genre(genre)
- Link for image(image)
Accepts names of files as parameters (example: 'a.mp3')
'''

def audio_recognize(fileName):
    mp3_file_content_to_recognize = open(fileName, 'rb').read()
    shazam = Shazam(mp3_file_content_to_recognize)
    recognize_generator = shazam.recognizeSong()
    try:
        resp = next(recognize_generator)[1]['track']
        id3 = dict()
        id3['title'] = resp['title']
        id3['subtitle'] = resp['subtitle']
        for i in resp['sections'][0]['metadata']:
            if i['title'] == 'Альбом':
                id3['album'] = i['text']
            elif i['title'] == 'Лейбл':
                id3['label'] = i['text']
            elif i['title'] == 'Выпущено':
                id3['year'] = i['text']
        id3['genre'] = resp['genres']['primary']
        id3['image'] = resp['share']['image']
        return id3
    except:
        return 0