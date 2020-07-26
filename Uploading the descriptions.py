#! /usr/bin/env python3
import os
import requests

#will vary
student = os.environ.get('USER')
#ip address of site
ip = "104.198.238.7"
dir = r"/home/{}/supplier-data/descriptions".format(student)
post_url = "http://{}/fruits/".format(ip)

def processFiles(dir, post_url):
    """iterate over all text files in directory"""
    for file in os.listdir(dir):  # iterate over the dir
        f, e = os.path.splitext(file)  # find out the file extension
        if e == ".txt":  # if it's a text file
            dict = convertToDict(file)  # convert the file to the dict
            response = requests.post(post_url, json=dict)  # make a POST request
            if response.status_code != 201:
                print("Failed {}".format(response.status_code))

def convertToDict(file):
    """convert text file to a dictionary"""
    dict = {}
    with open(os.path.join(dir, file), 'r') as f:
        dict['name'] = f.readline()
        weight, lbs = f.readline().split(" ")
        dict['weight'] = int(weight)
        dict['description'] = f.readline()
        f, e = os.path.splitext(file)
        image = f + ".jpeg"
        dict['image_name'] = image
    return dict

processFiles(dir, post_url)