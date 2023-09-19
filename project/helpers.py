from widgets.ammoCustWidgets import *

def getVariable(variables, var_name):
    print("Handling - " + var_name)
    return next(
        (obj for obj in variables if obj['name'] == var_name),
        None
    )

def getAndSetVariable(variables, var_name, ret, star=False, is_list=False, ops=None, var_type=None):
    ret[var_name] = None
    try:
        temp = getVariable(variables, var_name)
        if temp is None:
            return
        val = temp['value']
        if val is None:
            return
        if not star:
            if is_list:
                if isinstance(val, list):
                    ret[var_name] = temp
                    return
            if ops is not None:
                arr = []
                for idx, val_type in enumerate(ops):
                    arr.append(val_type(val[idx]['value']))
                ret[var_name] = arr
                return

            base_val = temp['value']
            ret[var_name] = var_type(base_val) if var_type is not None else base_val
            return

        try:
            valueType = temp['value'][0]["type"]
            if len(temp['value']) <= 2 and (valueType == "float" or valueType == 'int'):
                val = int(temp['value'][0]["value"])
                ret[var_name] = [val, val]
                return
        except:
            x = None

        if temp["type"] == "int":
            value = int(val)
            ret[var_name] = value
            return

        if temp['type'] == 'float':
            value = float(val)
            ret[var_name] = value
            return

        if temp["type"] == "ptr":
            objVal = val
            # should only happen with extPrams
            subVal = isinstance(val[0]['value'], list)
            if subVal:
                objVal = val[0]['value']
            init_value = objVal[0]['value']
            init_type = objVal[0]['type']

            base_value = init_value

            match init_type:
                case 'int':
                    base_value = int(init_value)
                case 'float':
                    base_value = float(init_value)

            if base_value is None:
                raise ValueError(f"Un-parseable type found for base value {init_type}")
            ret[var_name] = [ base_value,
                     int(objVal[1]['value']),
                     int(objVal[2]['value']),
                     int(objVal[3]['value']),
                     float(objVal[4]['value']),
                     float(objVal[5]['value'])
                     ]

            if subVal:
                if len(val) == 2:
                    ret[var_name].append(val[1])
                if len(val) > 2:
                    raise ValueError("Too many unexpected vals for star type var cap'n")
    except Exception as e:
        print(e)

def load_weapon_easy_data(file):
    if file is None:
        return

    if file.lower().endswith("sgo"):
        destFileName = file + '.base.json'
        args = ['./tools/sgott.exe', file, destFileName]
        subprocess.call(args)
        file = destFileName

    with open(file, encoding='utf-8') as fh:

        data = json.load(fh)

        print('Loading')
        varStore = data['variables']
        ret = {}
        getAndSetVariable(varStore, 'AimAnimation', ret)
        getAndSetVariable(varStore, 'AmmoAlive', ret)
        getAndSetVariable(varStore, 'AmmoClass', ret)

        getAndSetVariable(varStore, 'AmmoColor', ret, ops=[float,float, float, float])

        getAndSetVariable(varStore, 'AmmoCount', ret,star=True)

        getAndSetVariable(varStore, 'AmmoDamage', ret,star=True)

        getAndSetVariable(varStore, 'AmmoDamageReduce', ret, ops=[float, float])

        getAndSetVariable(varStore, 'AmmoExplosion', ret, star=True)

        getAndSetVariable(varStore, 'AmmoGravityFactor', ret, var_type=float)

        getAndSetVariable(varStore, 'AmmoHitImpulseAdjust', ret, var_type=float)

        getAndSetVariable(varStore, 'AmmoHitSe', ret)

        getAndSetVariable(varStore, 'AmmoHitSizeAdjust', ret, var_type=float)

        getAndSetVariable(varStore, 'AmmoIsPenetration', ret)

        getAndSetVariable(varStore, 'AmmoModel', ret)

        getAndSetVariable(varStore, 'AmmoOwnerMove', ret, var_type=float)

        getAndSetVariable(varStore, 'AmmoSize', ret, var_type=float)

        getAndSetVariable(varStore, 'AmmoSpeed', ret,star=True)

        ammoClass = ret['AmmoClass']

        subProjectile = ammoClass in subProjectileAmmoOptions
        ammoCustWidget = ammoCustWidgetFromAmmoClass(None, ammoClass, subProjectile)

        ammo_custom_param = getVariable(varStore, "Ammo_CustomParameter")
        ammo_custom_param_val = ammo_custom_param['value']
        if ammo_custom_param_val is not None:
            ammoCustWidget.setValue(ammo_custom_param_val)

        ret['Ammo_CustomParameter'] = ammoCustWidget.value()

        getAndSetVariable(varStore, 'Ammo_EquipVoice', ret, ops=[str,str])

        getAndSetVariable(varStore, 'AngleAdjust', ret, var_type=float)

        getAndSetVariable(varStore, 'BaseAnimation', ret)

        getAndSetVariable(varStore, 'ChangeAnimation', ret)

        getAndSetVariable(varStore, 'EnergyChargeRequire', ret, star=True)

        getAndSetVariable(varStore, 'ExtPrams', ret,star=True)

        getAndSetVariable(varStore, 'FireAccuracy', ret, star=True)

        getAndSetVariable(varStore, 'FireBurstCount', ret)

        getAndSetVariable(varStore, 'FireBurstInterval', ret,star=True)

        getAndSetVariable(varStore, 'FireCondition', ret, var_type=int)

        getAndSetVariable(varStore, 'FireCount', ret, star=True)

        getAndSetVariable(varStore, 'FireInterval', ret,star=True)

        getAndSetVariable(varStore, 'FireLoadSe', ret)

        getAndSetVariable(varStore, 'FireRecoil', ret)

        getAndSetVariable(varStore, 'FireSe', ret)

        getAndSetVariable(varStore, 'FireSpreadType', ret)

        getAndSetVariable(varStore, 'FireSpreadWidth', ret, var_type=float)

        getAndSetVariable(varStore, 'FireType', ret)

        getAndSetVariable(varStore, 'FireVector', ret, ops=[float, float, float])

        getAndSetVariable(varStore, 'LockonAngle', ret, ops=[float, float])

        getAndSetVariable(varStore, 'LockonFailedTime', ret)

        getAndSetVariable(varStore, 'LockonHoldTime', ret)

        getAndSetVariable(varStore, 'LockonRange', ret,star=True)

        getAndSetVariable(varStore, 'LockonTargetType', ret)

        getAndSetVariable(varStore, 'LockonTime', ret,star=True)

        getAndSetVariable(varStore, 'LockonType', ret)

        getAndSetVariable(varStore, 'Lockon_AutoTimeOut', ret)

        getAndSetVariable(varStore, 'Lockon_DistributionType', ret)

        getAndSetVariable(varStore, 'Lockon_FireEndToClear', ret)

        getAndSetVariable(varStore, 'ModelConstraint', ret)

        getAndSetVariable(varStore, 'MuzzleFlash', ret)

        # getAndSetVariable(varStore, 'MuzzleFlash_CustomParameter', ret)
        muzzleKey = 'MuzzleFlash_CustomParameter'
        muzzleVal = getVariable(varStore, muzzleKey)
        if muzzleVal is not None:
            ret[muzzleKey] = muzzleVal

        getAndSetVariable(varStore, 'ReloadAnimation', ret)

        getAndSetVariable(varStore, 'ReloadInit', ret, var_type=float)

        getAndSetVariable(varStore, 'ReloadTime', ret,star=True)

        getAndSetVariable(varStore, 'ReloadType', ret)

        getAndSetVariable(varStore, 'SecondaryFire_Parameter', ret)

        getAndSetVariable(varStore, 'SecondaryFire_Type', ret)

        getAndSetVariable(varStore, 'ShellCase', ret)

        getAndSetVariable(varStore, 'ShellCaseDischargeSe', ret)


        ret['ShellCase_CustomParameter'] = None

        SightAnimationModel = getVariable(varStore, 'Sight_animation_model')

        if SightAnimationModel is not None:
            SightAnimationModelVal = SightAnimationModel['value']
            ret['Sight_animation_model'] = [
                [
                    SightAnimationModelVal[0]['value'][0]['value'],
                    SightAnimationModelVal[0]['value'][1]['value'],
                ],
                int(SightAnimationModelVal[1]['value']),
                int(SightAnimationModelVal[2]['value']),
            ]

        getAndSetVariable(varStore, 'WeaponIcon', ret)

        animationModel = getVariable(varStore, 'animation_model')

        if animationModel is not None:
            animationModelVal = animationModel['value']
            # ret['rabChoice'] = animationModelVal[0]['value'][0]['value']
            ret['animation_model'] = [
                [
                    animationModelVal[0]['value'][0]['value'],
                    animationModelVal[0]['value'][1]['value'],
                ],
                animationModelVal[1]['value'],
                animationModelVal[2]['value'],
            ]

        getAndSetVariable(varStore, 'custom_parameter', ret)

        getAndSetVariable(varStore, 'name.cn', ret)

        getAndSetVariable(varStore, 'name.en', ret)

        getAndSetVariable(varStore, 'name.ja', ret)

        getAndSetVariable(varStore, 'name.kr', ret)

        getAndSetVariable(varStore, 'resource', ret)

        getAndSetVariable(varStore, 'use_underground', ret)

        getAndSetVariable(varStore, 'xgs_scene_object_class', ret)

        print('Loaded')
    return ret


# end def loadWeaponEasyData


# end def loadWeaponFromJson

def write_weapon_to_json_file(weapon_data, file_name, include_options=True):
    if file_name != "":
        # always need to write json
        convert = file_name.lower().endswith("sgo")
        json_file_name = file_name + ".new.json" if convert else file_name

        j.writeToJson(j.easyToTypeValue(weapon_data, include_options), json_file_name)

        # TODO - re-enable
        # if not convert:
        #     return
        #
        # args = ['./tools/sgott.exe', json_file_name, file_name]
        # subprocess.call(args)

    # end if
# end def writeWeaponToJson