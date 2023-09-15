import json

# should be able to build a proper weapon json file
import os

varNames = ['AimAnimation', 'AmmoAlive', 'AmmoClass', 'AmmoColor', 'AmmoCount', 'AmmoDamage', 'AmmoDamageReduce',
            'AmmoExplosion', 'AmmoGravityFactor', 'AmmoHitImpulseAdjust', 'AmmoHitSe', 'AmmoHitSizeAdjust',
            'AmmoIsPenetration', 'AmmoModel', 'AmmoOwnerMove', 'AmmoSize', 'AmmoSpeed', 'Ammo_CustomParameter',
            'Ammo_EquipVoice', 'AngleAdjust', 'BaseAnimation', 'ChangeAnimation', 'EnergyChargeRequire', 'ExtPrams',
            'FireAccuracy', 'FireBurstCount', 'FireBurstInterval', 'FireCondition', 'FireCount', 'FireInterval',
            'FireLoadSe', 'FireRecoil', 'FireSe', 'FireSpreadType', 'FireSpreadWidth', 'FireType', 'FireVector',
            'LockonAngle', 'LockonFailedTime', 'LockonHoldTime', 'LockonRange', 'LockonTargetType', 'LockonTime',
            'LockonType', 'Lockon_AutoTimeOut', 'Lockon_DistributionType', 'Lockon_FireEndToClear', 'ModelConstraint',
            'MuzzleFlash', 'MuzzleFlash_CustomParameter', 'ReloadAnimation', 'ReloadInit', 'ReloadTime', 'ReloadType',
            'SecondaryFire_Parameter', 'SecondaryFire_Type', 'ShellCase', 'ShellCaseDischargeSe',
            'ShellCase_CustomParameter', 'Sight_animation_model', 'WeaponIcon', 'animation_model', 'custom_parameter',
            'name.cn', 'name.en', 'name.ja', 'name.kr', 'resource', 'use_underground', 'xgs_scene_object_class']

secondaryFireOptions = {
        "None": 0,
        "Zoom": 1,
        "Activate": 2,
        "Activate and Reload": 3,
        "Jumpjets (Fencer)": 4,
        "Dash (Fencer)": 5,
        "Shield Reflect (Fencer)": 6
      }
ammoClassOptions = [
        "LightningBullet01",
        "LaserBullet01",
        "LaserBullet02",
        "LaserBullet03",
        "FlameBullet01",
        "FlameBullet02",
        "SpiderStringBullet01",
        "SpiderStringBullet02",
        "ShockWaveBullet01",
        "SlashWaveBullet01",
        "HomingLaserBullet01",
        "BeamBullet01",
        "DecoyBullet01",
        "NeedleBullet01",
        "BarrierBullet01",
        "ClusterBullet01",
        "AcidBullet01",
        "NapalmBullet01",
        "GrenadeBullet01",
        "MissileBullet01",
        "MissileBullet02",
        "RocketBullet01",
        "RocketBullet02",
        "SolidBullet01",
        "SolidBullet02",
        "SmokeCandleBullet01",
        "ShieldBashBullet01",
        "SentryGunBullet01",
        "TargetMarkerBullet01",
        "SupportUnitBullet01",
        "PileBunkerBullet01",
        "PlasmaBullet01"
      ]
# need to test if having extra data in things that don't include it is bad
# Optional Variables:
# resource - unknown whether this is necessary for weapons to function. some include it, some don't,
# when I've removed it from one weapon it didn't seem to affect anything
#
# Sight_animation_model - remove completely to get rid of the aiming reticle
# ModelConstraint & animation_model - absent from support equipment like Ranger armor, wing diver cores, and fencer cells

initialD = {"endian": "LE",
            "variables": [],
            "meta": {}}


def raiseValError(s, val):
    raise ValueError(f"{s} was provided when trying to build the weapon json.\n value: {val}, type: {type(val)}")


def ProcessValue(param):
    # return ("{:.16f}".format(param)).rstrip("0.")
    decimals = len(str(param).split(".")[1])
    if decimals == 0:
        return int(param)
    return param




def valueToTypeValueDict(v, n=""):
    valDict = {}
    # special cases since nested "name" variables aren't preserved in easydata
    if n == "ExtPrams":
        if v == 1:
            v = [1]
        if len(v) == 1:
            return{
                      "name": "ExtPrams",
                      "type": "ptr",
                      "value": [{"type": "float", "value": v[0]}]
                    }
        elif len(v) == 2:
            return {
                "name": "ExtPrams",
                "type": "ptr",
                "value": [{"type": "float", "value": v[0]}]
            }
        elif len(v) == 6:
            return {
            "name": "ExtPrams",
            "type": "ptr",
            "value": [
                {
                    "type": "ptr",
                    "value": [
                        {
                            "type": "float",
                            "value": v[0]
                        },
                        {
                            "type": "int",
                            "value": 80
                        },
                        {
                            "type": "int",
                            "value": v[2]
                        },
                        {
                            "type": "int",
                            "value": v[3]
                        },
                        {
                            "type": "float",
                            "value": v[4]
                        },
                        {
                            "type": "float",
                            "value": v[5]
                        }
                    ]
                }
            ]
        }
        else:
            raise ValueError("Unexpected extpram count cap'n")
    if n == "Ammo_CustomParameter":
        if v is None or len(v) == 0:
            return {"name": "Ammo_CustomParameter", "type": "ptr", "value": None}
        else:
            valDict['name'] = "Ammo_CustomParameter"
            valDict['type'] = "ptr"
            valDict['value'] = []
            for index in range(0, len(v) ):
                valDict['value'].append(valueToTypeValueDict(v[index]))
            return valDict

    if n == "resource":
        if v is None:
            return None
        else:
            return {
                "name": "resource",
                "type": "ptr",
                "value": v
            }
    if n == "EnergyChargeRequire":
        if v == -1:
            return None
        elif len(v) == 2:
            return {
                "name": "EnergyChargeRequire",
                "type": "ptr",
                "value": [
                        {
                          "type": "float",
                          "value": v[0]
                        },
                        {
                          "type": "float",
                          "value": v[1]
                        }
                ]
            }
        elif len(v) == 6:
            return {
                "name": "EnergyChargeRequire",
                "type": "ptr",
                "value": [
                    {
                        "type": "ptr",
                        "value": [
                            {
                                "type": "float",
                                "value": v[0]
                            },
                            {
                                "type": "int",
                                "value": v[1]
                            },
                            {
                                "type": "int",
                                "value": v[2]
                            },
                            {
                                "type": "int",
                                "value": v[3]
                            },
                            {
                                "type": "float",
                                "value": v[4]
                            },
                            {
                                "type": "float",
                                "value": v[5]
                            }
                        ]
                    }
                ]
            }
        elif len(v) == 7:
            return {
                "name": "EnergyChargeRequire",
                "type": "ptr",
                "value": [
                    {
                        "type": "ptr",
                        "value": [
                            {
                                "type": "float",
                                "value": v[0]
                            },
                            {
                                "type": "int",
                                "value": v[1]
                            },
                            {
                                "type": "int",
                                "value": v[2]
                            },
                            {
                                "type": "int",
                                "value": v[3]
                            },
                            {
                                "type": "float",
                                "value": v[4]
                            },
                            {
                                "type": "float",
                                "value": v[5]
                            }
                        ]
                    },
                    {
                        "type": "float",
                        "value": v[6]['value']
                    }
                ],

            }
        else:
            raise ValueError("Unexpected extpram count cap'n")
    if n == "AmmoColor":
        return{
            "type": "ptr",
            "name": "AmmoColor",
            "value": [
                {"type": "float",
                 "name": "Red",
                 "value": ProcessValue(v[0])},
                {"type": "float",
                 "name": "Green",
                 "value": ProcessValue(v[1])},
                {"type": "float",
                 "name": "Blue",
                 "value": ProcessValue(v[2])},
                {"type": "float",
                 "name": "Alpha",
                 "value": ProcessValue(v[3])},
            ]
        }
    elif n == "animation_model":
        return{
            "type": "ptr",
            "name": "animation_model",
            "value": [
                {"type": "ptr",
                 "value": [
                     {"type": "string",
                      "value": v[0][0]},
                     {"type": "string",
                      "value": v[0][1]}
                 ]
                 },
                {
                    "type": "string" if isinstance(v[1], str) else "int",
                    "value": v[1]
                },
                {
                    "type": "extra",
                    "value": v[2]
                 }
            ]
        }

    if isinstance(v, list):
        t = "ptr"
        newV = []
        for e in v:
            newV.append(valueToTypeValueDict(e))
        v = newV
    elif v is None:
        t = "ptr"
    elif isinstance(v, dict):
        return v
    elif isinstance(v, int):
        t = "int"
    elif isinstance(v, float):
        t = "float"
    elif isinstance(v, str):
        t = "string"
    else:
        raise ValueError(f"name: {n} value:{v} type:{type(v)} which is not supported in the EDF weapon json format")
    valDict["type"] = t
    if n != "":
        valDict["name"] = n
    # "options" aren't preserved in easyData so they are restored here
    if n == "AmmoClass":
        valDict["options"] = ammoClassOptions
    elif n == "SecondaryFire_Type":
        valDict["options"] = secondaryFireOptions

    valDict["value"] = v
    if n == "resource":
        valDict['value'][0]["name"] = "path"
        valDict['value'][0]["value"] = valDict['value'][0].pop("value")

    return valDict


def easyToTypeValue(d):
    variables = []
    ignoreVars = []
    for k in d:
        variables.append(valueToTypeValueDict(d[k], n=k))

    return {
        "endian": "LE",
        "format": "SGO",
        "version": 258,
        "variables": variables,
  #       "meta": {
  #           "help": "For examples of these values, open WEAPONTABLE.SGO and WEAPONTEXT.SGO",
  #           "id": None,
  #           "level": None,
  #           "category": None,
  #           "unlockState": None,
  #           "dropRateModifier": None,
  #           "description": None
  # }
    }


def easyDictSecondPass(c):
    if isinstance(c, list):
        v = []
        for e in c:
            v.append(easyDictSecondPass(e))
        return v
    # print(c)
    if c['type'] == 'ptr':
        v = []
        if c['value'] is None:
            return None
        else:
            for e in c['value']:
                # print(e)
                v.append(easyDictSecondPass(e))
    elif c['type'] == "int":
        v = c['value']
    elif c['type'] == "float":
        v = float(c['value'])
    elif c['type'] == "string":
        v = c['value']
    elif c['type'] == 'extra':
        v = c['value']['data']
    return v


def typeValueToEasyDict(c):
    if isinstance(c, list):
        v = []
        for e in c:
            v.append(typeValueToEasyDict(e))
        return v
    if c['type'] == 'ptr':
        v = []
        for e in c.values():
            v.append(typeValueToEasyDict(e))
    elif c['type'] == "int":
        v = c['value']
    elif c['type'] == "float":
        v = float(c['value'])
    elif c['type'] == "string":
        v = c['value']
    return v


def makeEasyData(weaponData):
    # takes data from weapon files loaded from loadFromJson or dataHelper.getWeaponDataFromDir and converts them to easydata
    easyData = {}
    # take batch of weapons from dataHelper.getWeaponDataFromDir
    if "endian" not in weaponData:
        for weapon in weaponData:
            easyData[weapon] = makeEasyData(weaponData[weapon])
            #easyData[weapon] = weaponToEasyData(weaponData[weapon])
    else:
        for i in range(len(weaponData['variables'])):
            # i = weapon['data']['variables'].index(var)
            v = weaponData['variables'][i]['name']
            if weaponData['variables'][i]['type'] == "float":
                easyData[v] = float(weaponData['variables'][i]['value'])
            else:
                easyData[v] = weaponData['variables'][i]['value']
        for key in easyData:
            if isinstance(easyData[key], list):
                easyData[key] = easyDictSecondPass(easyData[key])
    return easyData


# def weaponToEasyData(weaponData):
#     easyData = {}
#     for i in range(len(weaponData['variables'])):
#         # i = weapon['data']['variables'].index(var)
#         v = weaponData['variables'][i]['name']
#         if weaponData['variables'][i]['type'] == "float":
#             easyData[v] = float(weaponData['variables'][i]['value'])
#         else:
#             easyData[v] = weaponData['variables'][i]['value']
#     for key in easyData:
#         if isinstance(easyData[key], list):
#             easyData[key] = easyDictSecondPass(easyData[key])
#     return easyData


def easyWeaponDataToJson(eData, filepath):
    variables = []
    for key in eData:
        variables.append(valueToTypeValueDict(eData[key], key))
    d = {"endian": "LE", "variables": variables, "meta": {"": ""}}
    writeToJson(d, filepath)


def loadDataFromJson(filepath):
    f = open(filepath, "r", encoding="utf8")
    jsonData = json.load(f)
    f.close()
    return jsonData


def writeToJson(data, filepath):
    f = open(filepath, "w", encoding="utf8")
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.close()


def writeEasyDataToDirectory(e, dir):
    for weaponName, data in e.items():
        sgoData = easyToTypeValue(data)
        writeToJson(sgoData ,f"./{dir}/{weaponName}.json")

def batchModify(e, stats, modification):
    for key, value in e.items():
        for stat in stats:

            print(key, stat, e[key][stat])
            if isinstance(e[key][stat], list):
                statType = type(e[key][stat][0])
                e[key][stat][0] = statType(eval(f"e[key][stat][0]{modification}"))
            else:
                statType = type(e[key][stat])
                e[key][stat] = statType(eval(f"e[key][stat]{modification}"))
            print(key, stat, e[key][stat])

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

def loadEasyDir(path):
    d = makeEasyData(getWeaponDataFromDir(path))
    return d

def getACFromFolder(dir):
    weaps = makeEasyData(getWeaponDataFromDir(dir))
    data = {w["name.en"]: w["Ammo_CustomParameter"] for w in weaps.values()}
    return data