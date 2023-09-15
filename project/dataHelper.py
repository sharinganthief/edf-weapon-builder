import json
import collections
import os

# f = open("easyData.json", "r", encoding="utf8")
# data = json.load(f)
# f.close()

def describeData(filepath):
    f = open(filepath, "r", encoding="utf8")
    data = json.load(f)
    f.close()
    for entry in data:
        print(entry[0])



typeDict = {
    "<class 'int'>": "int",
    "<class 'float'>": "float",
    "<class 'str'>": "string",
    "<class 'NoneType'>": "None",
    "<class 'list'>": "list"
}

def describeDataTypes(filepath):
    f = open(filepath, "r", encoding="utf8")
    data = json.load(f)
    f.close()
    possibleTypes = []
    for entry in data:
        struct = []
        try:
            for value in entry[0]:
                struct.append(str(type(value['value'])))
        except:
            struct = typeDict[str(type(entry[0]))]
        if len(possibleTypes) == 0:
            possibleTypes.append([struct, entry[2]])
        else:
            existingStructs = [item[0] for item in possibleTypes]
            # print(struct, existingStructs)
            if struct in existingStructs:
                # print(possibleTypes)
                # print(existingStructs.index(struct))
                possibleTypes[existingStructs.index(struct)][1]+=entry[2]
            else:
                possibleTypes.append([struct, entry[2]])
    return possibleTypes

def getWeaponDataFromDir(directory):
    weaponData = {}
    filesToRead = os.listdir(directory)
    for file in filesToRead:
        if file[-4:] != "json":
            pass
        else:
            with open(f"{directory}/{file}", "r", encoding="utf8") as wf:
                wdata = json.load(wf)
                enNameIndex = 0
                internalName = file[:-5]
                for var in wdata['variables']:
                    if var['name'] == "name.en":
                        enNameIndex = wdata['variables'].index(var)
                        break
                IGName = wdata['variables'][enNameIndex]['value']
                weaponData[internalName] = wdata
    return weaponData

def getAllAnimData(e):
    modelAnimationData = {}
    for w in e.values():
        try:
            aimAnimation = w['AimAnimation']
        except:
            aimAnimation = "missingAimAnimation"
        try:
            sightAnimationModel = w["Sight_animation_model"]
        except:
            sightAnimationModel = "missingSight_animation_model"
        try:
            weaponIcon = w["WeaponIcon"]
        except:
            weaponIcon = "missingweaponIcon value"
        try:
            baseAnimation = w['BaseAnimation']
        except:
            baseAnimation = "missingBaseAnimation"
        try:
            changeAnimation = w['ChangeAnimation']
        except:
            changeAnimation = "missingChangeAnimation"
        try:
            reloadAnimation = w['ReloadAnimation']
        except:
            reloadAnimation = "missingReloadAnimation"
        try:
            mdb = w['animation_model'][0][1]
        except:
            mdb = "missinganimation_model"
        try:
            rabData = w['animation_model'][0][0]
        except:
            rabData = "missingrab data"
        try:
            casData = w['animation_model'][1]
        except:
            casData = "missingcas data"
        try:
            mabData = w['animation_model'][2]
        except:
            mabData = "missingmab data"
        try:
            ammoModel = w['AmmoModel']
        except:
            ammoModel = "missingAmmoModel"
        try:
            ammoColor = w["AmmoColor"]
        except:
            ammoColor = "missingAmmoColor"
        try:
            muzzleFlash = w["MuzzleFlash"]
        except:
            muzzleFlash = "missing MuzzleFlash"
        try:
            muzzleFlashParams = w["MuzzleFlash_CustomParameter"]
        except:
            muzzleFlashParams = "missing MuzzleFlash_CustomParameter"
        try:
            fireSE = w['FireSe']
        except:
            fireSE = "missingFireSE"
        try:
            impactSE = w["AmmoHitSe"]
        except:
            impactSE = "missingAmmoHitSe"
        try:
            reloadSE = w["FireLoadSe"]
        except:
            reloadSE = "missingFireLoadSe"
        try: modelConstraint = w['ModelConstraint']
        except: modelConstraint = "missing ModelConstraint"
        try: shellCase = w["ShellCase"]
        except: shellCase = "missing ShellCase"
        try: shellCaseDischargeSe = w["ShellCaseDischargeSe"]
        except: shellCaseDischargeSe = "missing ShellCaseDischargeSe"
        customParameter = w["custom_parameter"]



        modelAnimationData[rabData] = {
            "AimAnimation": aimAnimation,
            "BaseAnimation": baseAnimation,
            "ChangeAnimation": changeAnimation,
            "ReloadAnimation": reloadAnimation,
            "WeaponIcon": weaponIcon,
            "AmmoModel": ammoModel,
            "AmmoColor": ammoColor,
            "MuzzleFlash": muzzleFlash,
            "MuzzleFlash_CustomParameter": muzzleFlashParams,
            "Sight_animation_model": sightAnimationModel,
            "ShellCase": shellCase,
            "ShellCaseDischargeSe": shellCaseDischargeSe,
            "ModelConstraint": modelConstraint,
            "cas": casData,
            "mab": mabData,
            "mdb": mdb,
            "FireSe": fireSE,
            "AmmoHitSe": impactSE,
            "FireLoadSe": reloadSE,
            "custom_parameter": customParameter}
    return modelAnimationData

def uniqueDataByKey(key, subkeys, easyData):
    uniqueData = {}
    for k in easyData.keys():
        entry = easyData[k]
        # add every unique value of the primary key to uniqueData as keys
        # the value of them should be a dictionary with keys equal to the subkeys
        # the values of those subkeys will be a list containing unique values of the subkeys
        k = str(k)
        try:
            primaryKey = entry[key]
        except:
            primaryKey = f"{key} absent"
        if isinstance(primaryKey, list) or isinstance(primaryKey, dict):
            primaryKey = str(primaryKey)
        if primaryKey not in uniqueData:
            subDictionary = {}
            for sk in subkeys:
                try:
                    value = str(entry[sk])
                    subDictionary[sk] = {value: [k]}
                except:
                    subDictionary[sk] = {f"{sk} absent": [k]}
            uniqueData[primaryKey] = subDictionary
        else:
            for sk in subkeys:
                try:
                    value = str(entry[sk])
                except:
                    value = f"{sk} absent"
                if value not in uniqueData[primaryKey][sk].keys():
                    try:
                        uniqueData[primaryKey][sk][value] = [k, entry["name.en"]]
                    except:
                        try:
                            uniqueData[primaryKey][sk][value] = [k, entry["name"]] # edf 4
                        except:
                            uniqueData[primaryKey][sk][value] = [k, "no name"]
                else:
                    try:
                        uniqueData[primaryKey][sk][value].append([k, entry["name.en"]])
                    except:
                        try:
                            uniqueData[primaryKey][sk][value] = [k, entry["name"]]  # edf 4
                        except:
                            uniqueData[primaryKey][sk][value] = [k, "no name"]
    return uniqueData

def flatten(S):
    # https://stackoverflow.com/questions/12472338/flattening-a-list-recursively?lq=1
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])