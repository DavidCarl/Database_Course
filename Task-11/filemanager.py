import json


def loadFile(path):
    with open(path) as json_file:
        return json.load(json_file)