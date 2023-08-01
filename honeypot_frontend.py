import os
from os import system
import requests

# 禁用 Ctrl Z stty susp undef
# 启用 Ctrl Z stty susp ^Z

system("stty susp undef")

admin_key = "123456"

def get_responce(command):
    if (command == admin_key):
        exit()
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
    }
    command = {"cmd": command}
    output = requests.post(url = "http://127.0.0.1:9000/admin",json = command).json()
    return output["message"]



def attact_warning():
    pass

def anti_attact():
    pass

while True:
    attact_warning()
    anti_attact()
    try:
        command = input("[root@ubuntu ~]$ ")
        print(get_responce(command))

    except KeyboardInterrupt:
        print("")
    
