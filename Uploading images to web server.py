#!/usr/bin/env python3
import requests, os

#in my case student-01-f9769aec489f
user = os.environ.get('USER')
#images directory
path = '/home/'+user+'/supplier-data/images/'

def upload(path): 
  for pic in os.listdir(path): 
    if pic.endswith('.jpeg'): 
      url = "http://localhost/upload/"
      with open(path+pic, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
  return 


if __name__ == '__main__': 
  upload(path)