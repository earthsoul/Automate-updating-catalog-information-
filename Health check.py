#!/usr/bin/env python3
# check the system statistics every 60 seconds, send an email if issue found"""
import shutil
import psutil
import emails
import time
import socket
import os

def check_cpu():
    """Report an error if CPU usage is over 80%"""
    if psutil.cpu_percent(interval=1) > 80:
        print("Error - CPU usage is over 80%")
        send_email("Error - CPU usage is over 80%")

def check_disk():
    """Report an error if available disk space is lower than 20%"""
    if psutil.disk_usage('/').percent > 80:
        print("Error - Available disk space is less than 20%")
        send_email("Error - Available disk space is less than 20%")

def check_memory():
    """Report an error if available memory is less than 500MB"""
    if psutil.virtual_memory().available / 1000000 < 500:
        print("Error - Available memory is less than 500MB")
        send_email("Error - Available memory is less than 500MB")

def check_host():
    """Report an error if the hostname "localhost" cannot be resolved to 127.0.0.1"""
    if socket.gethostbyname('localhost') != "127.0.0.1":
        print("Error - localhost cannot be resolved to 127.0.0.1")
        send_email("Error - localhost cannot be resolved to 127.0.0.1")

def send_email(subject):
    """send an email containing error message"""
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_sans_attachment(sender, receiver, subject, body)
    emails.send(message)

while True:
    check_cpu()
    check_disk()
    check_memory()
    check_host()
    time.sleep(60)