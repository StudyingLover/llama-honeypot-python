import os
import requests

# 禁用 Ctrl Z stty susp undef
# 启用 Ctrl Z stty susp ^Z

admin_key = "123456"

def get_responce(command):
    if (command == admin_key):
        exit()
    output = requests.post("http://127.0.0.1:9000/admin/"+command).json()
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
    
