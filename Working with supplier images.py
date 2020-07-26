#!/usr/bin/env python3

import os
from PIL import Image

user = os.environ.get('USER')
path = "/home/"+user+"/supplier-data/images/"

newsize = 600 ,400
for file in os.listdir(path):
    if file.endswith('.tiff'):
       a,b =os.path.splitext(file)
       nfile = a + '.jpeg'
       im = Image.open(file).convert('RGB')
       im.resize((newsize)).save(path + nfile)