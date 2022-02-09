import json

discordSettings = json.load(open("pyshley/conf/discordConfig.json", "r"))
foundrySettings = json.load(open("pyshley/conf/foundryConfig.json", "r"))

gmIDList = discordSettings['gmIDList']
