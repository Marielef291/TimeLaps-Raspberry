#!/usr/bin/env python
# -*- coding: utf-8 -*-

from picamera import PiCamera
from time import sleep, strftime
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw

##Date and time recovery in 2 different formats
date=datetime.today().strftime('%d.%m.%Y_%H-%M-%S')
date2=datetime.today().strftime('%d/%m/%Y')
#saving in variables in both folders for saving photos
dossier= "/home/pi/TL1/"
dossier2= "/home/pi/TL2/"
##"dossier" vwill correspond to photos without dates, and "dossier2" will correspond to photos with dates

#####################################################################

##Photo Capture
camera = PiCamera()
camera.resolution = (1437,1080)
sleep(5) #gives the camera time to adjust to the light
camera.capture(dossier+date+'.jpg')


######################################################################
##Adding the date to the photo
## recovery of the photo in the first folder, then additions of the registered font

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
img = Image.open(dossier+date+'.jpg')
draw = ImageDraw.Draw(img)
draw.text((1171, 1030),date2,(0,0,0),font=font)
img.save(dossier2+date+'.jpg')

