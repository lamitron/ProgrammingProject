import json
import os


def makeuserfile(users):
    jsondump = json.dumps(users)

    with open('data/users.json', 'w+') as file:
        if os.path.getsize('data/users.json') != 0:
            file.write(',')
        file.writelines(jsondump)


def getuserfile():
    with open('data/users.json', 'r+') as file:
        fileout = file.read()
    
    return json.loads(fileout)

def getsongs():
    with open('data/songs.json', 'r') as file:
        fileout = file.read()

    return json.loads(fileout)
