# -*- coding: utf-8 -*-
ScriptName = "ShoutOut"
Website = "https://tharealnino.rocks"
Description = "ShoutOuts, limited to known streamers"
Creator = "ThaRealNino"
Version = "1.0.5"
Command = "!so <username>"

import json
import os
import codecs

settings = {}
intermediate = {}
streamerList = {};

def Init():
    global settings
    global streamerList
    global intermediate
    
    with codecs.open(os.path.join(os.path.dirname(__file__), "shoutout_settings.json"), encoding='utf-8-sig') as json_file:
        settings = json.load(json_file, encoding='utf-8-sig')
        
    if os.path.isfile(settings["shoutout_file"]):
        with open(settings["shoutout_file"]) as settingsFile:
            intermediate = settingsFile.readlines()
            
        for dataset in intermediate:
            tupel = dataset.split("|")
            streamerList[tupel[0]] = tupel[1]
    return

def Execute(data):
    if data.GetParam(0).lower() != "!so":
        return
    
    cleanName = data.GetParam(1).replace('@','').lower()
    
    sent = False
    
    for key in streamerList.keys():
        if key == cleanName:
            sendMessage(streamerList[cleanName])
            sent = True
            break
    
    if (sent == False):
        sendMessage(settings["dontKnow"])
    
    return

def Tick():
    return
    
def sendMessage(message):
    Parent.SendStreamMessage(message)
    return