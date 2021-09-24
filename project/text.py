import json
import os
language = "en"
with open("./text.json", "r", encoding="utf8") as f: textData = json.load(f)



def getText(key):
    global language
    # if key[:4] == "[EN]":
    #     raise ValueError("double translation")
    if language == "en":
        textData[key] = key
        return key
    if key not in textData:
        textData[key] = key
        return f"[EN] {key}"
    elif language not in textData[key]:
        return f"[EN] {key}"
        # return f"{language} {textData['missing'][language]} {key}"
    else:
        return textData[key][language]

def setLanguage(l):
    global language
    language = l
