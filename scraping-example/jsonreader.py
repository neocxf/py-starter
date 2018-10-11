import json

with open("config.json") as handle:
    dictDump = json.loads(handle.read())
    print(dictDump)
