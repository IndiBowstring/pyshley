import json

discordSettings = json.load(open("pyshley/conf/discordConfig.json", "r"))
foundrySettings = json.load(open("pyshley/conf/foundryConfig.json", "r"))

token = discordSettings['token']
prefix = discordSettings['prefix']
adminIDList = discordSettings['adminIDList']
gmIDList = discordSettings['gmIDList']
botChannelList = discordSettings['botChannelList']
gmChannelList = discordSettings['gmChannelList']
