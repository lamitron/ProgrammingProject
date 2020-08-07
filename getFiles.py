import json
import os


def make_user_file(users):
    jsondump = json.dumps(users)

    with open('data/users.json', 'w+') as file:
        if os.path.getsize('data/users.json') != 0:
            file.write(',')
        file.writelines(jsondump)


def get_user_file():
    with open('data/users.json', 'r+') as file:
        fileout = file.read()
    
    return json.loads(fileout)


def get_songs():
    with open('data/songs.json', 'r') as file:
        fileout = file.read()

    return json.loads(fileout)


def get_scores():
    with open('data/scores.json', 'r+') as file:
        fileout = file.read()

    return json.loads(fileout)


def write_scores(scores):
    with open('data/scores.json', 'w') as file:
        file.write(json.dumps(scores))
