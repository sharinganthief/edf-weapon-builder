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


# def describeDataTypes(filepath):
#     f = open(filepath, "r", encoding="utf8")
#     data = json.load(f)
#     f.close()
#     possibleTypes = []
#     for entry in data:
#         struct = []
#         try:
#             for value in entry[0]:
#                 struct.append(typeDict[str(type(value['value']))])
#         except:
#             struct = typeDict[str(type(entry[0]))]
#         if len(possibleTypes) == 0:
#             possibleTypes.append([struct, entry[2]])
#         else:
#             for i in range(len(possibleTypes)):
#                 #print(f"{struct} == {possibleTypes[i][0]}?: {struct == possibleTypes[i][0]}")
#                 if struct == possibleTypes[i][0]:
#                     possibleTypes[i][1] += entry[2]
#                     break
#                 else:
#                     possibleTypes.append([struct, entry[2]])
#
#     return possibleTypes
#


# def describeDataTypes(filepath):
#     f = open(filepath, "r", encoding="utf8")
#     data = json.load(f)
#     f.close()
#     dataTypes = []
#     for entry in data:
#         try:
#             structTypes = []
#             for v in entry[0]:
#                 structTypes.append(str(type(v['value'])))
#             for i in range(len(dataTypes)):
#                 print(f"{structTypes} != {dataTypes[i][0]}? {structTypes != dataTypes[i][0]}")
#                 if structTypes != dataTypes[i][0]:
#                     dataTypes.append([structTypes, entry[2]])
#                     break
#                 else:
#                     dataTypes[i][1] += entry[2]
#             # if structTypes not in dataTypes:
#             #     dataTypes.append([structTypes, entry[2]])
#             # else:
#             #     dataTypes[dataTypes.index(structTypes)][1] += entry[2]
#         except:
#             structTypes = str(type(entry[0]))
#             if structTypes not in dataTypes:
#                 dataTypes.append([structTypes, entry[2]])
#             else:
#                 dataTypes[dataTypes.index(structTypes)][1] += entry[2]
#     return dataTypes


# def describeDataTypes(filepath):
#     f = open(filepath, "r", encoding="utf8")
#     data = json.load(f)
#     f.close()
#     dataTypes = []
#     for entry in data:
#         try:
#             structTypes = []
#             for v in entry[0]:
#                 structTypes.append(str(type(v['value'])))
#             if structTypes not in dataTypes:
#                 dataTypes.append(structTypes)
#         except:
#             structTypes = str(type(entry[0]))
#             if structTypes not in dataTypes:
#                 dataTypes.append(structTypes)
#
#     return dataTypes

def describeDataTypes(filepath):
    f = open(filepath, "r", encoding="utf8")
    data = json.load(f)
    f.close()
    possibleTypes = []
    # possibleTypes = []
    # elements = [structType, weapons] ex. [int, "aweapon001"] [[int, float, float], "aweapon002", "aweapon003"], etc
    # for entry in data:
    # entry format = [variable value, count of weapons with this value, [list of weapons that have this value]]
    # convert entry[0] to its type data
    for entry in data:
        struct = []
        try:
            for value in entry[0]:
                struct.append(str(type(value['value'])))
        except:
            struct = typeDict[str(type(entry[0]))]
# if possibleTypes empty, add [typedata, entry[2]]
        if len(possibleTypes) == 0:
            possibleTypes.append([struct, entry[2]])
# if possibleTypes not empty, check each element[0] of possibleTypes and compare it to typedata of the current entry
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
# if there is a match, append entry[2] to possibleTypes element[1]
# if there is no match, append [typedata, entry[2]] to possibleTypes
# return possibleTypes



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


# def easyDictSecondPass(c):
#     if isinstance(c, list):
#         v = []
#         for e in c:
#             v.append(easyDictSecondPass(e))
#         return v
#     if c['type'] == 'ptr':
#         v = []
#         if c['value'] is None:
#             return None
#         else:
#             for e in c['value']:
#                 # print(e)
#                 v.append(easyDictSecondPass(e))
#     elif c['type'] == "int":
#         v = c['value']
#     elif c['type'] == "float":
#         v = float(c['value'])
#     elif c['type'] == "string":
#         v = c['value']
#     elif c['type'] == 'extra':
#         v = c['value']['data']
#     return v
#
#
# def makeEasyData(weaponData):
#     easyData = {}
#     if "endian" not in weaponData:
#         for weapon in weaponData:
#             easyData[weapon] = {}
#             # easyData[weapon]["IGN"] = weapon['IGName']
#             # print(weaponData[weapon])
#             for i in range(len(weaponData[weapon]['variables'])):
#                 # i = weapon['data']['variables'].index(var)
#                 v = weaponData[weapon]['variables'][i]['name']
#                 if weaponData[weapon]['variables'][i]['type'] == "float":
#                     easyData[weapon][v] = float(weaponData[weapon]['variables'][i]['value'])
#                 else:
#                     easyData[weapon][v] = weaponData[weapon]['variables'][i]['value']
#         for key in easyData:
#             if isinstance(easyData[key], list):
#                 easyData[key] = easyDictSecondPass(easyData[key])
#     else:
#         for i in range(len(weaponData['variables'])):
#             # i = weapon['data']['variables'].index(var)
#             v = weaponData['variables'][i]['name']
#             if weaponData['variables'][i]['type'] == "float":
#                 easyData[v] = float(weaponData['variables'][i]['value'])
#             else:
#                 easyData[v] = weaponData['variables'][i]['value']
#         for key in easyData:
#             if isinstance(easyData[key], list):
#                 easyData[key] = easyDictSecondPass(easyData[key])
#     return easyData


# def getCasData(d):
#     # takes easyData dictionary
#     casData = {}
#     for w in d.values():
#         casData["No model"] = []
#         try:
#             if w['animation_model'][0]['value'][1]['value'] not in casData:
#                 casData[w['animation_model'][0]['value'][1]['value']] = w['animation_model'][1]['value']
#             # else:
#             #     if w['animation_model'][2]['value']['data'] not in casData[
#             #         w['animation_model'][0]['value'][1]['value']]:
#             #         casData[w['animation_model'][0]['value'][1]['value']].append(w['animation_model'][1]['value'])
#         except:
#             print(f"{w['name.en']} has no model")
#             casData["No model"].append(w['name.en'])
#     return casData
#
#
# def getMabData(d):
#     # takes easyData dictionary
#     mabData = {}
#     for w in d.values():
#         mabData["No model"] = []
#         # try:
#         if w['animation_model'][2]['value']['data'] not in mabData:
#             mabData[w['animation_model'][0]['value'][1]['value']] = w['animation_model'][2]['value']['data']
#             # else:
#             #     if w['animation_model'][2]['value']['data'] not in mabData[w['animation_model'][0]['value'][1]]:
#             #         mabData[w['animation_model'][0]['value'][1]['value']].append(w['animation_model'][1]['value'])
#         # except:
#         #     print("something happened")
#     return mabData
#
#
# def getAimData(d):
#     # takes easyData dictionary
#     aimData = {}
#     for w in d.values():
#         aimData["No model"] = []
#         try:
#             if w['animation_model'][0]['value'][1]['value'] not in aimData:
#                 aimData[w['animation_model'][0]['value'][1]['value']] = w['AimAnimation']
#             # else:
#             #     if w['animation_model'][2]['value']['data'] not in aimData[
#             #         w['animation_model'][0]['value'][1]['value']]:
#             #         aimData[w['animation_model'][0]['value'][1]['value']].append(w['animation_model'][1]['value'])
#         except:
#             print(f"{w['name.en']} has no model")
#             aimData["No model"].append(w['name.en'])
#     return aimData


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
    

# def loadDataFromJson(filepath):
#     f = open(filepath, "r", encoding="utf8")
#     jsonData = json.load(f)
#     f.close()
#     return jsonData
#
#
# def writeToJson(data, filepath):
#     f = open(filepath, "w", encoding="utf8")
#     json.dump(data, f, ensure_ascii=False, indent=2)
#     f.close()


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
                        uniqueData[primaryKey][sk][value] = [k, entry["name.en"]]
                else:
                    uniqueData[primaryKey][sk][value].append([k, entry["name.en"]])
    return uniqueData


# def RABSorter(modelData):
#     sM2 =
#     for k, v in modelData.items():
#         c = k[12]
#     if c == "s":
#
#         if k[14] == "a":
#
#         sM2["Ranger"]["Assault Rifles"][k] = k
#     elif k[14:16] == "sh":
#
#     sM2["Ranger"]["Shotguns"][k] = k
#     elif k[14:16] == "sn":
#
#     sM2["Ranger"]["Snipers"][k] = k
#     elif k[14] == "r":
#
#     sM2["Ranger"]["Rocket Launchers"][k] = k
#     elif k[14] == "m":
#
#     sM2["Ranger"]["Missile Launchers"][k] = k
#     elif k[14] == "g":
#
#     sM2["Ranger"]["Grenade Launcher"][k] = k
#     else:
#
#     sM2["Ranger"]["Other"][k] = k
#     elif c == "p":
#
#     if k[14] == "t":
#
#         sM2["Wing Diver"]["Thunder Bow"][k] = k
#     elif k[14] == "r":
#
#     sM2["Wing Diver"]["Rapier"][k] = k
#     elif k[14:17] == "laz":
#
#     sM2["Wing Diver"]["Laser"][k] = k
#     elif k[14:17] == "lan":
#
#     sM2["Wing Diver"]["Lance"][k] = k
#     elif k[14] == "p":
#
#     sM2["Wing Diver"]["Particle Gun"][k] = k
#     elif k[14] == "g":
#
#     sM2["Wing Diver"]["Grenade"][k] = k
#     elif k[14] == "h":
#
#     sM2["Wing Diver"]["Homing"][k] = k
#     elif k[14] == "s":
#
#     sM2["Wing Diver"]["Sniper"][k] = k
#     elif k[14] == "l":
#
#     sM2["Wing Diver"]["Plasma Launcher"][k] = k
#     else:
#
#     sM2["Wing Diver"]["Other"][k] = k
#     elif c == "e":
#
#     if k[14:16] == "th":
#
#         sM2["Air Raider"]["Throwable"][k] = k
#     elif k[14:16] == "ta" or k[14] == "m":
#
#     sM2["Air Raider"]["Marker Launcher"][k] = k
#     elif k[14:16] == "se":
#
#     sM2["Air Raider"]["Turret"][k] = k
#     elif k[14:16] == "su":
#
#     sM2["Air Raider"]["Support"][k] = k
#     else:
#
#     print(f"no air raider category for {k}")
#     elif c == "h":
#
#     if k[14] == "i":
#
#         sM2["Fencer"]["Melee"][k] = k
#     elif k[14] == "p":
#
#     sM2["Fencer"]["Piercers"][k] = k
#     elif k[14] == "s" or k[14] == "e":
#
#     sM2["Fencer"]["Shield"][k] = k
#     elif k[14] == "c":
#
#     sM2["Fencer"]["Cannon"][k] = k
#     elif k[14] == "g":
#
#     sM2["Fencer"]["Gatling"][k] = k
#     elif k[14] == "m":
#
#     sM2["Fencer"]["Missile"][k] = k
#     elif k[14] == "a":
#
#     sM2["Fencer"]["Shoulder Mounted"][k] = k
#     else:
#
#     sM2["Fencer"]["Other"][k] = k
#     elif c == "v" or "V":
#
#     sM2["Vehicle"][k] = k
#
#     j.writeToJson(sM2, "./data/sortedModels2.json")


# import jsonBuilder as j
# data = getWeaponDataFromDir("./data/weapondata")
# edata = j.makeEasyData(data)
# u = uniqueDataByKey("AmmoClass", ["Ammo_CustomParameter", "xgs_scene_object_class"], edata)
# uModels = uniqueDataByKey("animation_model", ["ModelConstraint"], edata)
# print("done")
# re = [1,2,[3,4,[5,6],[7],8],9,10]


def flatten(S):
    # https://stackoverflow.com/questions/12472338/flattening-a-list-recursively?lq=1
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


# print(flatten(re))
# data = getWeaponDataFromDir("./Weapondata")
# eData = makeEasyData(data)
# u = uniqueDataByKey("AimAnimation", ["AmmoClass", "AmmoCount"], eData)
# aData = getAllAnimData(eData)
# print("done")
# f = open("model and animation data.json", "w", encoding="utf8")
# json.dump(aData, f, indent=4)
# f.close()

# os.chdir("./variable data/")
# varFilepaths = os.listdir("unique values per variable")
# mainDict = {}
# for filepath in varFilepaths:
#     print(f"./unique values per variable/{filepath}")
#     mainDict[filepath] = describeDataTypes(f"./unique values per variable/{filepath}")
# for key in mainDict:
#     z = open(f"./data structure per variable/{key}", "w", encoding="utf-8")
#     json.dump(mainDict[key], z, indent=4)
#     z.close()
# print(mainDict)

#describeDataTypes("./variable data/ammocount.json")