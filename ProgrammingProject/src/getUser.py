import json


def makeJSON(users):
    jsondump = json.dumps(users)

    with open('src/data/users.json', 'r+') as file:
        file.writelines(jsondump)