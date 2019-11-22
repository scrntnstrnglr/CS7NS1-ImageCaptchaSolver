# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:15:59 2019

@author: SIDDHARTHA
"""

from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

audio = AudioCaptcha(voicedir='C:\\Users\\SIDDHARTHA\\Downloads\\19301936-project3\\Audio')

data = audio.generate('1234')
audio.write('1234', 'out.wav')