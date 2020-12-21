# -*- coding: utf-8 -*-
ScriptName = "Schelle"
Website = "https://tharealnino.rocks"
Description = "Einfach mal ein paar Respektschellen im Chat verteilen"
Creator = "ThaRealNino"
Version = "1.0.0"
Command = "!schelle <user>"

import json
import os
import codecs

settings = {}

Schelle = [
            "{U1} will {U2} eine Schelle verpassen, haut aber daneben. Typisch.",
            "{U1} klatscht {U2} komplett aus der Realität. {U2} steht so schnell nicht wieder auf.",
            "Selbst das lange Singledasein hat den Arm von {U1} nicht genug trainiert, um {U2} sicher zu treffen. Daneben.",
            "{U2} hat den Schlag kommen sehen, konnte ihm aber nicht ausweichen. {U1} kann den Schmerz, den diese deftige Schelle verursacht, in den Augen von {U2} genießen.",
            "Gute Ausführung, keine groben Patzer, eine grundsolide Schelle von {U1} trifft {U2} mitten ins Gesicht.",
            "{U2} kassiert eine astreine Schelle von {U1}, bleibt allerdings komplett unbeeindruckt. An Stelle von {U1} würde ich jetzt weglaufen",
            "{U1} will {U2} eine kräftige Schelle verpassen, hat allerdings kaum trainiert. Es reicht nur für einen jämmerlichen Klaps auf die Wange",
            "{U1} langt kräftig zu und bringt {U2} zum Weinen. Die Schelle hat gesessen!",
            "Durch die heftige Schelle von {U1} taumelt {U2} und stolpert über einen Hocker. {U1} lacht aus vollem Hals und kriegt fast keine Luft mehr"
]

def Init():
    global settings
    global message
    
    with codecs.open(os.path.join(os.path.dirname(__file__), "schelle_settings.json"), encoding='utf-8-sig') as json_file:
        settings = json.load(json_file, encoding='utf-8-sig')
    
    return

def Execute(data):
    if data.GetParam(0).lower() != "!schelle":
        return
    
    if Parent.IsOnUserCooldown(ScriptName, Command, data.User):
        remainingTime = Parent.GetUserCooldownDuration(ScriptName, Command, data.User)
        sendMessage("@" + data.User + ": Dein Arm ist für noch genau " + str(remainingTime) + " Sekunden zu schwach für eine weitere Schelle")
        return
        
    if "@" not in data.GetParam(1):
        if settings["shallPickRandom"] == True:
            receiver = "@" + Parent.GetDisplayName(Parent.GetRandomActiveUser()).lower()
            chance = Parent.GetRandom(0,len(Schelle) -1)
            message = Schelle[chance].replace("{U2}", receiver).replace("{U1}", "@" + data.User)
        else:
            message = "@" + data.User + " ist zu doof zum Markieren. @" + data.User + " kassiert dafür selber eine Schelle."
    else:
        receiver = data.GetParam(1).lower()
        message = Schelle[chance].replace("{U2}", receiver).replace("{U1}", "@" + data.User)
        
    sendMessage(message)
    
    Parent.AddUserCooldown(ScriptName, Command, data.User, 120)
    return

def Tick():
    return
    
def sendMessage(message):
    Parent.SendStreamMessage(message)
    return