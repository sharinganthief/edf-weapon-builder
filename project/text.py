import json
import os
language = "en"
with open("./data/text.json", "r", encoding="utf8") as f: textData = json.load(f)

def getText(key):
    global language
    if language == "en":
        textData[key] = key
        return key
    if key not in textData:
        textData[key] = key
        return f"[EN] {key}"
    elif language not in textData[key]:
        return f"[EN] {key}"
    else:
        return textData[key][language]

def setLanguage(l):
    global language
    language = l
