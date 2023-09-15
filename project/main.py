import os

if __name__ == '__main__':
    currDir = os.getcwd()
    if not currDir.endswith('project'):
        os.chdir(".\project")

from widgets.tabs import *
from tkinter import filedialog
import logging

global labelwidth
labelwidth = 20

def set_star_data(field, value, val):
    try:
        if len(value['value']) <= 2 and value['value'][0]["type"] == "float" :
            field.baseValue.setValue(int(value['value'][0]["value"]))
            field.flatOrStar.setValue('flat')
            field.flatArray = True
            return
    except:
        x = None

    if value["type"] == "ptr":
        objVal = val
        # should only happen with extPrams
        subVal = isinstance(val[0]['value'], list)
        if subVal:
            objVal = val[0]['value']
        init_value = objVal[0]['value']
        init_type = objVal[0]['type']

        # if subVal:
        #     init_type = 'int'
        base_value = float(init_value) if init_type == 'float' else int(objVal[0]['value']) if init_type == 'int' else None
        if base_value is None:
            raise ValueError(f"Un-parseable type found for base value {init_type}")
        field.baseValue.setValue(base_value)
        field.saveDataPos.inputVar.set(int(objVal[2]['value']))
        # field.saveDataPos.input.set(int(objVal[2]['value']))
        field.maxStarLevel.inputVar.set(int(objVal[3]['value']))
        # field.maxStarLevel.input.set(int(objVal[3]['value']))
        field.p1.setValue(float(objVal[4]['value']))
        field.p2.setValue(float(objVal[5]['value']))
        #field.settingType = (None if settingType.get(value['name']) is None else settingType[value['name']])

        if subVal:
            if len(val) == 2:
                field.extra = val[1]
            if len(val) > 2:
                raise ValueError("Too many unexpected vals for star type var cap'n")

        field.flatArray = False
        field.flatOrStar.setValue('star')

    elif value["type"] == "int":
        field.baseValue.setValue(int(val))
        field.flatOrStar.setValue('flat')
    elif value['type'] == 'float':
        field.baseValue.setValue(float(val))
        field.flatOrStar.setValue('flat')
        field.flatArray = False

def get_variable(variables, var_name):
    print("Handling - " + var_name)
    return next(
        (obj for obj in variables if obj['name'] == var_name),
        None
    )

class MainWindow(tk.Frame):
    def __init__(self, parent, width, height):
        self.customParamData = None
        self.muzzleFlashCustomParameters = None
        global language
        tk.Frame.__init__(self, parent, width=width, height=height)
        cfgSettings = loadConfig()
        setLanguage(cfgSettings["language"])

        self.widgetDict = {}
        self.notebook = MainNotebook(self)
        self.notebook.pack(side="left", fill="both", expand=True)
        self.classChoiceVar = self.notebook.classTab.classChoice.dropDownDisplayed
        self.testButton = tk.Button(self, text="Write to file", command=lambda: self.writeWeaponToJson())
        self.testButton.pack()
        self.updateTextFile = tk.Button(self, text="Update text json", command=self.updateText)
        self.updateTextFile.pack()
        self.loadTextFile = tk.Button(self, text="Load from file", command=lambda: self.loadWeaponFromJson())
        self.loadTextFile.pack()

        self.classChoiceVar.trace_add("write", self.updateWidgetsDependingOnClass)
        self.notebook.classTab.AmmoClass.dropDownDisplayed.trace_add("write", self.updateWidgetsDependingOnAmmoClass)
    # end def __init__

    def updateText(self, *args):
        curDir = os.path.abspath(".")
        filename = ""
        try:
            filename = tk.filedialog.asksaveasfilename(initialdir=curDir, title=getText("Choose file name"),
                                                       filetypes=[("json files", ".json")])
        except Exception:
            logging.exception("Exception when writing json")
        # end try
        if filename != "":
            j.writeToJson(textData, filename)
        # end if
    # end def updateText

    def loadWeaponFromJson(self):
        curDir = os.path.abspath(".")
        file = None
        try:
            file = tk.filedialog.askopenfile(initialdir=curDir, title=getText("Choose file name"),
                                             filetypes=[("SGO", ".sgo"), ("json", ".json")])
        except Exception:
            logging.exception("Exception when reading json")
        # end try
        if file is not None:
            fileName = file.name
            if file.name.lower().endswith("sgo"):
                destFileName = fileName + '.json'
                args = ['./tools/sgott.exe', fileName, destFileName]
                subprocess.call(args)
                fileName = destFileName

            with open(fileName, encoding='utf-8') as fh:
                weaponClass = "Ranger"
                index = 0
                fileName = os.path.basename(file.name)
                if fileName.startswith("P"):
                    weaponClass = "Wing Diver"
                    index = 1
                elif fileName.startswith("E"):
                    weaponClass = "Air Raider"
                    index = 2
                elif fileName.startswith("H"):
                    weaponClass = "Fencer"
                    index = 3

                self.notebook.appearanceTab.gunModelWidget.currentClass = weaponClass
                #self.notebook.appearanceTab.gunModelWidget.updateOptions()

                self.notebook.classTab.classChoice.setValue(weaponClass)
                data = json.load(fh)

                self.loadWeaponEasyData(data, index)
            # end with
        # end if
    # end def loadWeaponFromJson
        # reverse write for load

    def writeWeaponToJson(self):
        curDir = os.path.abspath(".")
        filename = ""
        try:
            filename = tk.filedialog.asksaveasfilename(initialdir=curDir, title=getText("Choose file name"),
                                                       filetypes=[("SGO", ".sgo"), ("json", ".json")])
        except Exception:
            logging.exception("Exception when writing json")
        # end try
        if filename != "":
            # always need to write json
            convert = filename.lower().endswith("sgo")
            jsonFileName = filename + ".json" if convert else filename

            j.writeToJson(j.easyToTypeValue(self.createWeaponEasyData()), jsonFileName)

            if not convert:
                return

            args = ['./tools/sgott.exe', jsonFileName, filename]
            subprocess.call(args)

        # end if
    # end def writeWeaponToJson
        # print(filename)

    def updateWidgetsDependingOnClass(self, *args):
        self.notebook.appearanceTab.gunModelWidget.classChange(self.classChoiceVar.get())
        self.notebook.basicParamsTab.basicParamsWidget.updateSecondaryOptionsBasedOnClass(self.classChoiceVar.get())
    # end def updateWidgetsDependingOnClass

    def updateWidgetsDependingOnXGS(self, *args):
        pass
    # end def updateWidgetsDependingOnXGS

    def updateWidgetsDependingOnAmmoClass(self, *args):
        ac = self.notebook.classTab.AmmoClass.value()
        if ac in bulletsWithModels:
            self.notebook.appearanceTab.ammoModel.enableInput()
            if ac == "SmokeCandleBullet01":
                self.notebook.appearanceTab.ammoModel.setValue("app:/WEAPON/e_throw_marker01.rab")
                self.notebook.appearanceTab.ammoModel.disableInput()
            elif ac == "SmokeCandleBullet02":
                self.notebook.appearanceTab.ammoModel.setValue("app:/WEAPON/bullet_marker_gun.rab")
                self.notebook.appearanceTab.ammoModel.disableInput()
            # end if
        else:
            self.notebook.appearanceTab.ammoModel.disableInput()
        # end if
        if ac == "SentryGunBullet01":
            self.notebook.appearanceTab.gunModelWidget.RABChoice.setValue("app:/Weapon/e_sentrygun_normal01.rab")
            self.notebook.basicParamsTab.basicParamsWidget.secondaryFireType.setValue(2)
        # end if
    # end def updateWidgetsDependingOnAmmoClass

    def createWeaponEasyData(self, *args):
        n = self.notebook
        eData = {}
        eData["AimAnimation"] = n.appearanceTab.gunModelWidget.AimAnimation.value()
        eData["AmmoAlive"] = n.basicParamsTab.basicParamsWidget.ammoLifetime.value()
        eData["AmmoClass"] = n.classTab.AmmoClass.value()
        eData["AmmoColor"] = n.appearanceTab.ammoColor.value()
        eData["AmmoCount"] = n.basicParamsTab.basicParamsWidget.ammoCount.value()
        eData["AmmoDamage"] = n.basicParamsTab.basicParamsWidget.ammoDamage.value()
        eData["AmmoDamageReduce"] = [n.basicParamsTab.basicParamsWidget.minDamage.value(),
                                     n.basicParamsTab.basicParamsWidget.falloffFactor.value()]
        eData["AmmoExplosion"] = n.basicParamsTab.basicParamsWidget.ammoExplosion.value()
        eData["AmmoGravityFactor"] = n.classTab.ammoGravityFactor.value()
        eData["AmmoHitImpulseAdjust"] = n.classTab.ammoHitImpulseAdjust.value()
        eData["AmmoHitSe"] = n.soundsTab.impactSound.value()
        eData["AmmoHitSizeAdjust"] = n.classTab.ammoHitSizeAdjust.value()
        eData["AmmoIsPenetration"] = n.basicParamsTab.basicParamsWidget.isPenetrate.value()
        eData[
            "AmmoModel"] = n.appearanceTab.ammoModel.value() if self.notebook.classTab.AmmoClass.value() in bulletsWithModels else 0
        eData["AmmoOwnerMove"] = n.classTab.ammoOwnerMove.value()
        eData["AmmoSize"] = n.classTab.ammoSize.value()
        eData["AmmoSpeed"] = n.basicParamsTab.basicParamsWidget.ammoSpeed.value()
        eData["Ammo_CustomParameter"] = n.classTab.ammoCust.value()
        if eData["AmmoClass"] == "SmokeCandleBullet01":
            if n.classTab.useUnderground.value() == 1:
                eData["Ammo_CustomParameter"].append(1)
            # end if
        # end if
        eData["Ammo_EquipVoice"] = [n.soundsTab.ammoEquipFullVoice.value(),
                                    n.soundsTab.ammoEquipEmptyVoice.value()] if n.soundsTab.ammoEquipFullVoice.value() is not None and n.soundsTab.ammoEquipEmptyVoice.value() is not None else None
        eData["AngleAdjust"] = n.appearanceTab.angleAdjust.value()
        eData["BaseAnimation"] = n.appearanceTab.gunModelWidget.BaseAnimation.value()
        eData["ChangeAnimation"] = n.appearanceTab.gunModelWidget.ChangeAnimation.value()
        eData["EnergyChargeRequire"] = n.basicParamsTab.basicParamsWidget.energyChargeRequire.value()
        eData["ExtPrams"] = n.basicParamsTab.basicParamsWidget.extPrams.value()
        eData["FireAccuracy"] = n.basicParamsTab.basicParamsWidget.fireAccuracy.value()
        eData["FireBurstCount"] = n.basicParamsTab.basicParamsWidget.fireBurstCount.value()
        eData["FireBurstInterval"] = n.basicParamsTab.basicParamsWidget.fireBurstInterval.value()
        eData["FireCondition"] = 0  # Always 0
        eData["FireCount"] = n.basicParamsTab.basicParamsWidget.fireCount.value()
        eData["FireInterval"] = n.basicParamsTab.basicParamsWidget.fireInterval.value()
        eData["FireLoadSe"] = n.soundsTab.reloadSound.value()
        eData["FireRecoil"] = n.classTab.fireRecoil.inputVar.get()
        eData["FireSe"] = n.soundsTab.fireSound.value()
        eData["FireSpreadType"] = n.classTab.fireSpreadType.value()
        eData["FireSpreadWidth"] = n.classTab.fireSpreadWidth.value()
        if n.classTab.xgsChoice.value() != "Weapon_Throw":
            eData["FireType"] = 0
        else:
            if hasattr(n.basicParamsTab.basicParamsWidget, 'fireType'):
                fire_type = n.basicParamsTab.basicParamsWidget.fireType.value()
                eData["FireType"] = fire_type if fire_type > 0 else 1
            else:
                eData["FireType"] = 0
        # end if

        eData["FireVector"] = n.classTab.fireVector.get_value()
        eData["LockonAngle"] = [n.lockonTab.lockonAngleH.value(), n.lockonTab.lockonAngleV.value()]
        eData["LockonFailedTime"] = n.lockonTab.lockonFailedTime.value()
        eData["LockonHoldTime"] = n.lockonTab.lockonHoldTime.value()
        eData["LockonRange"] = n.lockonTab.lockonRange.value()
        eData["LockonTargetType"] = n.lockonTab.lockonTargetType.value()
        eData["LockonTime"] = n.lockonTab.lockonTime.value()
        eData["LockonType"] = n.lockonTab.lockonType.value()
        # if n.classTab.xgsChoice.value() == "Weapon_HomingShoot" else 0
        eData["Lockon_AutoTimeOut"] = n.lockonTab.lockonAutoTimeout.value()
        eData["Lockon_DistributionType"] = n.lockonTab.lockonDistributionType.value()
        eData["Lockon_FireEndToClear"] = n.lockonTab.lockonFireEndToClear.value()
        eData["ModelConstraint"] = n.appearanceTab.gunModelWidget.ModelConstraint.value()
        eData["MuzzleFlash"] = n.appearanceTab.muzzleFlash.muzzleFlashType.value()
        eData[
            "MuzzleFlash_CustomParameter"] = n.appearanceTab.muzzleFlash.paramsWidget.value() \
            if n.appearanceTab.muzzleFlash.muzzleFlashType.value() != "" else None
        eData["ReloadAnimation"] = n.appearanceTab.gunModelWidget.ReloadAnimation.value()
        eData["ReloadInit"] = n.basicParamsTab.basicParamsWidget.reloadInit.value()
        eData["ReloadTime"] = n.basicParamsTab.basicParamsWidget.reloadTime.value()
        eData["ReloadType"] = n.basicParamsTab.basicParamsWidget.reloadType.value()
        eData[
            "SecondaryFire_Parameter"] = n.basicParamsTab.basicParamsWidget.secondaryFireParameter.value() \
            if n.basicParamsTab.basicParamsWidget.secondaryFireType.value() == 1 else None
        eData["SecondaryFire_Type"] = n.basicParamsTab.basicParamsWidget.secondaryFireType.value()
        eData["ShellCase"] = n.appearanceTab.shellCase.value()
        eData["ShellCaseDischargeSe"] = n.soundsTab.shellCaseDischargeSound.value()
        eData["ShellCase_CustomParameter"] = None # Always null

        if n.appearanceTab.sightAnimationModel.value() != "missingSight_animation_model":
            s = n.appearanceTab.sightAnimationModel.value()
            eData["Sight_animation_model"] = [[f"app:/HUD/{s}.rab", f"{s}.mdb"], 0, 0]
        # end if
        eData["WeaponIcon"] = n.appearanceTab.gunModelWidget.WeaponIcon.value()
        if n.classTab.xgsChoice.value() != "Weapon_Accessory":
            eData["animation_model"] = n.appearanceTab.gunModelWidget.makeAnimation_ModelData()
        # end if
        if self.customParamData is not None:
            eData["custom_parameter"] = self.customParamData
        if self.muzzleFlashCustomParameters is not None:
            eData["MuzzleFlash_CustomParameter"] = self.muzzleFlashCustomParameters
        eData["name.cn"] = n.classTab.cnName.value()
        eData["name.en"] = n.classTab.enName.value()
        eData["name.ja"] = n.classTab.jaName.value()
        eData["name.kr"] = n.classTab.krName.value()

        if n.resource is not None:
            eData["resource"] = n.resource

        eData["use_underground"] = n.classTab.useUnderground.value()
        eData["xgs_scene_object_class"] = n.classTab.xgsChoice.value()
        return eData
    # end def createWeaponEasyData

    def loadWeaponEasyData(self, data, index):

        print('Loading')
        n = self.notebook
        vars = data['variables']
        try:
            AimAnimation = get_variable(vars, 'AimAnimation')
            if AimAnimation is not None:
                # self.animationData[r]['AimAnimation']
                AimAnimationVal = AimAnimation['value']
                n.appearanceTab.gunModelWidget.AimAnimation.setValue(AimAnimationVal)

            AmmoAlive = get_variable(vars, 'AmmoAlive')

            if AmmoAlive is not None:
                AmmoAliveVal = AmmoAlive['value']
                n.basicParamsTab.basicParamsWidget.ammoLifetime.setValue(AmmoAliveVal)

            AmmoClass = get_variable(vars, 'AmmoClass')

            if AmmoClass is not None:
                AmmoClassVal = AmmoClass['value']
                n.classTab.AmmoClass.setValue(AmmoClassVal)

            AmmoColor = get_variable(vars, 'AmmoColor')

            if AmmoColor is not None:
                AmmoColorVal = AmmoColor['value']
                red = float(AmmoColorVal[0]['value'])
                green = float(AmmoColorVal[1]['value'])
                blue = float(AmmoColorVal[2]['value'])
                alpha = float(AmmoColorVal[3]['value'])
                n.appearanceTab.ammoColor.red.inputVar.set(red)
                n.appearanceTab.ammoColor.green.inputVar.set(green)
                n.appearanceTab.ammoColor.blue.inputVar.set(blue)
                n.appearanceTab.ammoColor.alpha.inputVar.set(alpha)

            AmmoCount = get_variable(vars, 'AmmoCount')

            if AmmoCount is not None:
                AmmoCountVal = AmmoCount['value']
                set_star_data(n.basicParamsTab.basicParamsWidget.ammoCount, AmmoCount, AmmoCountVal)

            Ammo_EquipVoice = get_variable(vars, 'Ammo_EquipVoice')

            if Ammo_EquipVoice is not None:
                Ammo_EquipVoiceVal = Ammo_EquipVoice['value']
                if Ammo_EquipVoiceVal is not None:
                    n.soundsTab.ammoEquipFullVoice.setValue(Ammo_EquipVoiceVal[0]['value'])
                    n.soundsTab.ammoEquipEmptyVoice.setValue(Ammo_EquipVoiceVal[1]['value'])

            AmmoDamage = get_variable(vars, 'AmmoDamage')

            if AmmoDamage is not None:
                AmmoDamageVal = AmmoDamage['value']
                set_star_data(n.basicParamsTab.basicParamsWidget.ammoDamage, AmmoDamage, AmmoDamageVal)

            AmmoDamageReduce = get_variable(vars, 'AmmoDamageReduce')

            if AmmoDamageReduce is not None:
                AmmoDamageReduceVal = AmmoDamageReduce['value']
                reduceVal = float(AmmoDamageReduceVal[0]['value'])
                fallOffVal = int(AmmoDamageReduceVal[1]['value'])
                n.basicParamsTab.basicParamsWidget.minDamage.inputVar.set(reduceVal)
                n.basicParamsTab.basicParamsWidget.minDamage.setValue(reduceVal)
                n.basicParamsTab.basicParamsWidget.falloffFactor.setValue(fallOffVal)

            AmmoExplosion = get_variable(vars, 'AmmoExplosion')

            if AmmoExplosion is not None:
                AmmoExplosionVal = AmmoExplosion['value']
                set_star_data(n.basicParamsTab.basicParamsWidget.ammoExplosion, AmmoExplosion, AmmoExplosionVal)

            AmmoGravityFactor = get_variable(vars, 'AmmoGravityFactor')

            if AmmoGravityFactor is not None:
                AmmoGravityFactorVal = AmmoGravityFactor['value']
                n.classTab.ammoGravityFactor.setValue(AmmoGravityFactorVal)

            AmmoHitImpulseAdjust = get_variable(vars, 'AmmoHitImpulseAdjust')

            if AmmoHitImpulseAdjust is not None:
                AmmoHitImpulseAdjustVal = AmmoHitImpulseAdjust['value']
                n.classTab.ammoHitImpulseAdjust.setValue(AmmoHitImpulseAdjustVal)

            AmmoHitSe = get_variable(vars, 'AmmoHitSe')

            if AmmoHitSe is not None:
                AmmoHitSeVal = AmmoHitSe['value']
                n.soundsTab.impactSound.setValue(AmmoHitSeVal)

            AmmoHitSizeAdjust = get_variable(vars, 'AmmoHitSizeAdjust')

            if AmmoHitSizeAdjust is not None:
                AmmoHitSizeAdjustVal = AmmoHitSizeAdjust['value']
                n.classTab.ammoHitSizeAdjust.setValue(AmmoHitSizeAdjustVal)

            AmmoIsPenetration = get_variable(vars, 'AmmoIsPenetration')

            if AmmoIsPenetration is not None:
                AmmoIsPenetrationVal = AmmoIsPenetration['value']
                n.basicParamsTab.basicParamsWidget.isPenetrate.setValue(AmmoIsPenetrationVal)

            AmmoModel = get_variable(vars, 'AmmoModel')

            if AmmoModel is not None:
                AmmoModelVal = AmmoModel['value']
                n.appearanceTab.ammoModel.setValue(AmmoModelVal)

            AmmoOwnerMove = get_variable(vars, 'AmmoOwnerMove')

            if AmmoOwnerMove is not None:
                AmmoOwnerMoveVal = AmmoOwnerMove['value']
                n.classTab.ammoOwnerMove.setValue(AmmoOwnerMoveVal)

            AmmoSize = get_variable(vars, 'AmmoSize')

            if AmmoSize is not None:
                AmmoSizeVal = AmmoSize['value']
                n.classTab.ammoSize.setValue(AmmoSizeVal)

            AmmoSpeed = get_variable(vars, 'AmmoSpeed')

            if AmmoSpeed is not None:
                AmmoSpeedVal = AmmoSpeed['value']
                set_star_data(n.basicParamsTab.basicParamsWidget.ammoSpeed, AmmoSpeed, AmmoSpeedVal)

            Ammo_CustomParameter = get_variable(vars, 'Ammo_CustomParameter')

            AngleAdjust = get_variable(vars, 'AngleAdjust')

            if AngleAdjust is not None:
                AngleAdjustVal = AngleAdjust['value']
                n.appearanceTab.angleAdjust.setValue(AngleAdjustVal)

            BaseAnimation = get_variable(vars, 'BaseAnimation')

            if BaseAnimation is not None:
                BaseAnimationVal = BaseAnimation['value']
                n.appearanceTab.gunModelWidget.BaseAnimation.setValue(BaseAnimationVal)

            ChangeAnimation = get_variable(vars, 'ChangeAnimation')

            if ChangeAnimation is not None:
                ChangeAnimationVal = ChangeAnimation['value']
                n.appearanceTab.gunModelWidget.ChangeAnimation.setValue(ChangeAnimationVal)

            FireAccuracy = get_variable(vars, 'FireAccuracy')

            if FireAccuracy is not None:
                FireAccuracyVal = FireAccuracy['value']
                set_star_data(n.basicParamsTab.basicParamsWidget.fireAccuracy, FireAccuracy, FireAccuracyVal)

            FireBurstCount = get_variable(vars, 'FireBurstCount')

            if FireBurstCount is not None:
                FireBurstCountVal = FireBurstCount['value']

                n.basicParamsTab.basicParamsWidget.fireBurstCount.setValue(FireBurstCountVal)

            FireBurstInterval = get_variable(vars, 'FireBurstInterval')

            if FireBurstInterval is not None:
                FireBurstIntervalVal = FireBurstInterval['value']
                set_star_data(n.basicParamsTab.basicParamsWidget.fireBurstInterval, FireBurstInterval, FireBurstIntervalVal)

            FireCount = get_variable(vars, 'FireCount')

            if FireCount is not None:
                FireCountVal = FireCount['value']
                if isinstance(FireCountVal, list):
                    set_star_data(n.basicParamsTab.basicParamsWidget.fireCount, FireCount, FireCountVal)
                else:
                    n.basicParamsTab.basicParamsWidget.fireCount.baseValue.setValue(int(FireCountVal))

            FireInterval = get_variable(vars, 'FireInterval')
            if FireInterval is not None:
                FireIntervalVal = FireInterval['value']
                set_star_data(n.basicParamsTab.basicParamsWidget.fireInterval, FireInterval, FireIntervalVal)

            FireLoadSe = get_variable(vars, 'FireLoadSe')

            if FireLoadSe is not None:
                FireLoadSeVal = FireLoadSe['value']
                n.soundsTab.reloadSound.setValue(FireLoadSeVal)

            FireSe = get_variable(vars, 'FireSe')

            if FireSe is not None:
                FireSeVal = FireSe['value']
                n.soundsTab.fireSound.setValue(FireSeVal)

            FireSpreadType = get_variable(vars, 'FireSpreadType')

            if FireSpreadType is not None:
                FireSpreadTypeVal = FireSpreadType['value']
                n.classTab.fireSpreadType.setValue(FireSpreadTypeVal)

            FireSpreadWidth = get_variable(vars, 'FireSpreadWidth')

            if FireSpreadWidth is not None:
                FireSpreadWidthVal = FireSpreadWidth['value']
                n.classTab.fireSpreadWidth.inputVar.set(float(FireSpreadWidthVal))
                n.classTab.fireSpreadWidth.setValue(FireSpreadWidthVal)


            LockonAngle = get_variable(vars, 'LockonAngle')

            if LockonAngle is not None:
                LockonAngleVal = LockonAngle['value']
                n.lockonTab.lockonAngleH.setValue(float(LockonAngleVal[0]['value']))
                n.lockonTab.lockonAngleV.setValue(float(LockonAngleVal[1]['value']))

            LockonFailedTime = get_variable(vars, 'LockonFailedTime')

            if LockonFailedTime is not None:
                LockonFailedTimeVal = LockonFailedTime['value']
                n.lockonTab.lockonFailedTime.setValue(LockonFailedTimeVal)

            LockonHoldTime = get_variable(vars, 'LockonHoldTime')

            if LockonHoldTime is not None:
                LockonHoldTimeVal = LockonHoldTime['value']

                n.lockonTab.lockonHoldTime.setValue(LockonHoldTimeVal)

            LockonRange = get_variable(vars, 'LockonRange')

            if LockonRange is not None:
                LockonRangeVal = LockonRange['value']
                if isinstance(LockonRangeVal, list):
                    set_star_data(n.lockonTab.lockonRange, LockonRange, LockonRangeVal)
                else:
                    n.lockonTab.lockonRange.baseValue.setValue(int(LockonRangeVal))

            LockonTargetType = get_variable(vars, 'LockonTargetType')

            if LockonTargetType is not None:
                LockonTargetTypeVal = LockonTargetType['value']

                n.lockonTab.lockonTargetType.setValue(LockonTargetTypeVal)

            LockonTime = get_variable(vars, 'LockonTime')

            if LockonTime is not None:
                LockonTimeVal = LockonTime['value']
                if isinstance(LockonTimeVal, list):
                    set_star_data(n.lockonTab.lockonTime, LockonTime, LockonTimeVal)
                else:
                    n.lockonTab.lockonTime.baseValue.setValue(int(LockonTimeVal))

            LockonType = get_variable(vars, 'LockonType')

            if LockonType is not None:
                LockonTypeVal = LockonType['value']
                n.lockonTab.lockonType.setValue(LockonTypeVal)

            Lockon_AutoTimeOut = get_variable(vars, 'Lockon_AutoTimeOut')

            if Lockon_AutoTimeOut is not None:
                Lockon_AutoTimeOutVal = Lockon_AutoTimeOut['value']
                n.lockonTab.lockonAutoTimeout.setValue(Lockon_AutoTimeOutVal)

            Lockon_DistributionType = get_variable(vars, 'Lockon_DistributionType')

            if Lockon_DistributionType is not None:
                Lockon_DistributionTypeVal = Lockon_DistributionType['value']
                n.lockonTab.lockonDistributionType.setValue(Lockon_DistributionTypeVal)

            Lockon_FireEndToClear = get_variable(vars, 'Lockon_FireEndToClear')

            if Lockon_FireEndToClear is not None:
                Lockon_FireEndToClearVal = Lockon_FireEndToClear['value']
                n.lockonTab.lockonFireEndToClear.setValue(Lockon_FireEndToClearVal)

            ReloadAnimation = get_variable(vars, 'ReloadAnimation')

            if ReloadAnimation is not None:
                ReloadAnimationVal = ReloadAnimation['value']
                n.appearanceTab.gunModelWidget.ReloadAnimation.setValue(ReloadAnimationVal)

            ReloadInit = get_variable(vars, 'ReloadInit')

            if ReloadInit is not None:
                ReloadInitVal = ReloadInit['value']
                n.basicParamsTab.basicParamsWidget.reloadInit.setValue(ReloadInitVal)

            ReloadTime = get_variable(vars, 'ReloadTime')
            if ReloadTime is not None:
                ReloadTimeVal = ReloadTime['value']
                if isinstance(ReloadTimeVal, list):
                    set_star_data(n.basicParamsTab.basicParamsWidget.reloadTime, ReloadTime, ReloadTimeVal)
                else:
                    n.basicParamsTab.basicParamsWidget.reloadTime.baseValue.setValue(int(ReloadTimeVal))

            ReloadType = get_variable(vars, 'ReloadType')

            if ReloadType is not None:
                ReloadTypeVal = ReloadType['value']
                n.basicParamsTab.basicParamsWidget.reloadType.setValue(ReloadTypeVal)

            FireType = get_variable(vars, 'FireType')
            if FireType is not None:
                FireTypeVal = FireType['value']
                n.classTab.xgsChoice.setValue(FireTypeVal)

            FireVector = get_variable(vars, 'FireVector')
            if FireVector is not None:
                FireVectorVal = FireVector['value']
                if FireVectorVal is not None:
                    n.classTab.fireVector.vectorX.setValue(float(FireVectorVal[0]['value']))
                    n.classTab.fireVector.vectorY.setValue(float(FireVectorVal[1]['value']))
                    n.classTab.fireVector.vectorZ.setValue(float(FireVectorVal[2]['value']))
                    n.classTab.fireVector.updateInputs()

            SecondaryFire_Type = get_variable(vars, 'SecondaryFire_Type')

            if SecondaryFire_Type is not None:
                SecondaryFire_TypeVal = SecondaryFire_Type['value']
                n.basicParamsTab.basicParamsWidget.secondaryFireType.setValue(SecondaryFire_TypeVal)

            ShellCase = get_variable(vars, 'ShellCase')

            if ShellCase is not None:
                ShellCaseVal = ShellCase['value']
                n.appearanceTab.shellCase.setValue(ShellCaseVal)

            ShellCaseDischargeSe = get_variable(vars, 'ShellCaseDischargeSe')
            if ShellCaseDischargeSe is not None:
                ShellCaseDischargeSeVal = ShellCaseDischargeSe['value']
                n.soundsTab.shellCaseDischargeSound.setValue(ShellCaseDischargeSeVal)

            # ShellCase_CustomParameter = get_variable(vars, 'ShellCase_CustomParameter')
            # ShellCase_CustomParameterVal = ShellCase_CustomParameter['value']
            # if ShellCase_CustomParameter is not None:
            #     # None  # Always null
            #     continue

            Sight_animation_model = get_variable(vars, 'Sight_animation_model')

            if Sight_animation_model is not None:
                Sight_animation_modelVal = Sight_animation_model['value'][0]['value']
                mdb = Sight_animation_modelVal[1]['value']
                mdbVal = str.replace(mdb, '.mdb','')
                mdbLower = str.lower(mdbVal)
                n.appearanceTab.sightAnimationModel.setValue(mdbLower)

            WeaponIcon = get_variable(vars, 'WeaponIcon')
            if WeaponIcon is not None:
                WeaponIconVal = WeaponIcon['value']
                n.appearanceTab.gunModelWidget.WeaponIcon.setValue(WeaponIconVal)

            nameCn = get_variable(vars, 'name.cn')
            if nameCn is not None:
                nameCnVal = nameCn['value']
                n.classTab.cnName.setValue(nameCnVal)

            nameEn = get_variable(vars, 'name.en')
            if nameEn is not None:
                nameEnVal = nameEn['value']
                n.classTab.enName.setValue(nameEnVal)

            nameJa = get_variable(vars, 'name.ja')

            if nameJa is not None:
                nameJaVal = nameJa['value']
                n.classTab.jaName.setValue(nameJaVal)

            nameKr = get_variable(vars, 'name.kr')
            if nameKr is not None:
                nameKrVal = nameKr['value']
                n.classTab.krName.setValue(nameKrVal)

            use_underground = get_variable(vars, 'use_underground')
            if use_underground is not None:
                use_undergroundVal = use_underground['value']
                n.classTab.useUnderground.setValue(use_undergroundVal)

            xgs_scene_object_class = get_variable(vars, 'xgs_scene_object_class')
            if xgs_scene_object_class is not None:
                xgs_scene_object_classVal = xgs_scene_object_class['value']
                n.classTab.xgsChoice.setValue(xgs_scene_object_classVal)

            custom_parameter = get_variable(vars, 'custom_parameter')
            if custom_parameter is not None:
                custom_parameterVal = custom_parameter['value']
                self.customParamData = custom_parameterVal

            SecondaryFire_Parameter = get_variable(vars, 'SecondaryFire_Parameter')
            if SecondaryFire_Parameter is not None:
                SecondaryFire_ParameterVal = SecondaryFire_Parameter['value']
                n.basicParamsTab.basicParamsWidget.secondaryFireParameter.setValue(
                    SecondaryFire_ParameterVal) if n.basicParamsTab.basicParamsWidget.secondaryFireType.setValue(
                    SecondaryFire_ParameterVal) == 1 else None

            MuzzleFlash = get_variable(vars, 'MuzzleFlash')
            if MuzzleFlash is not None:
                MuzzleFlashVal = MuzzleFlash['value']
                if MuzzleFlashVal != "":
                    n.appearanceTab.muzzleFlash.muzzleFlashType.setValue(MuzzleFlashVal)

            MuzzleFlash_CustomParameter = get_variable(vars, 'MuzzleFlash_CustomParameter')
            if MuzzleFlash_CustomParameter is not None:
                MuzzleFlash_CustomParameterVal = MuzzleFlash_CustomParameter['value']
                self.muzzleFlashCustomParameters = MuzzleFlash_CustomParameterVal

            EnergyChargeRequire = get_variable(vars, 'EnergyChargeRequire')
            if EnergyChargeRequire is not None:
                EnergyChargeRequireVal = EnergyChargeRequire['value']
                set_star_data(n.basicParamsTab.basicParamsWidget.energyChargeRequire, EnergyChargeRequire, EnergyChargeRequireVal)

            ExtPrams = get_variable(vars, 'ExtPrams')
            if ExtPrams is not None:
                ExtPramsVal = ExtPrams['value']
                set_star_data(n.basicParamsTab.basicParamsWidget.extPrams, ExtPrams, ExtPramsVal)

            # FireCondition = get_variable(vars, 'FireCondition')
            # FireConditionVal = FireCondition['value']
            # if FireCondition is not None:
            #     continue  # Always 0

            n.classTab.fireRecoil.inputVar.set(0.0)
            n.classTab.fireRecoil.input.set(0.0)

            FireRecoil = get_variable(vars, 'FireRecoil')
            if FireRecoil is not None:
                FireRecoilVal = FireRecoil['value']
                n.classTab.fireRecoil.inputVar.set(float(FireRecoilVal))
                n.classTab.fireRecoil.input.set(float(FireRecoilVal))
            # if n.classTab.xgsChoice.value() != "Weapon_Accessory":
            # eData["animation_model"] = n.appearanceTab.gunModelWidget.makeAnimation_ModelData()

            # TODO - determine how to determine sub projectile or not, default to True for now
            # default params
            Ammo_CustomParameterVal = None
            ammoClass = n.classTab.AmmoClass.value()

            # set the val if we have something
            if Ammo_CustomParameter is not None:
                Ammo_CustomParameterVal = Ammo_CustomParameter['value']

            # if we do not have a val, we are not sub TODO - confirm
            if Ammo_CustomParameterVal is not None:
                subProjectile = ammoClass in subProjectileAmmoOptions
            else:
                subProjectile = False

            # set the widget based on the class
            n.classTab.ammoCust = ammoCustWidgetFromAmmoClass(n.classTab.canvas, ammoClass, subProjectile)

            print("Handling - Ammo_CustomParameter")
            # set the widget value if we have one
            if Ammo_CustomParameterVal is not None:
                n.classTab.ammoCust.setValue(Ammo_CustomParameterVal)

            animation_model = get_variable(vars, 'animation_model')

            if animation_model is not None:
                animation_modelVal = animation_model['value']
                rabChoice = animation_modelVal[0]['value'][0]['value']
                n.appearanceTab.gunModelWidget.RABChoice.setValue(rabChoice)
                n.appearanceTab.gunModelWidget.makeAnimation_ModelData()

            ModelConstraint = get_variable(vars, 'ModelConstraint')

            if ModelConstraint is not None:
                ModelConstraintVal = ModelConstraint['value']
                n.appearanceTab.gunModelWidget.ModelConstraint = DropDownWidget(self, "Model Constraint", {
                    str(n.appearanceTab.gunModelWidget.animationData[n.appearanceTab.gunModelWidget.RABChoice.value()][
                            'ModelConstraint']):
                        n.appearanceTab.gunModelWidget.animationData[n.appearanceTab.gunModelWidget.RABChoice.value()][
                            'ModelConstraint']})
                n.appearanceTab.gunModelWidget.ModelConstraint.setValue(ModelConstraintVal[0]['value'])

            self.notebook.appearanceTab.gunModelWidget.updateOptions()

            # Mapped but not displayed
            n.resource = None
            resource = get_variable(vars, 'resource')
            if resource is not None:
                resource = resource['value']
                n.resource = resource

        except:
            e = sys.exc_info()[0]
            print(e)

            print('Loaded')
        return
    # end def loadWeaponEasyData

    def makeCustomParamData(self, *args):
        c = ["assault_recoil1", 1, 0, 1.0]
        return c
    # end def makeCustomParamData
# end class MainWindow
        # c.append()


# class WindowMenus(tk.Menu):
#     def __init__(self, parent):
#         tk.Menu.__init__(self, parent)
#         self.parent = parent
#
#         self.fileMenu = tk.Menu(self, tearoff=0)
#         self.fileMenu.add_command(label=getText("Write weapon data to json"), command=dummy)
#         self.fileMenu.add_command(label="test", command=dummy())
#         self.fileMenu.add_command(label="test", command=dummy())
#         self.fileMenu.add_command(label="test", command=dummy())
#         self.add_cascade(label="File", menu=self.fileMenu)


class MainNotebook(ttk.Notebook):
    def __init__(self, parent):
        ttk.Notebook.__init__(self, parent)
        self.parent = parent
        self.resource = None
        # self.tab1 = StandardWeaponTab(self, 600, 400, "tab1")
        # self.tab2 = StandardWeaponTab(self, 600, 300, "tab2")
        self.classTab = ClassTab(self)
        self.basicParamsTab = BasicParamsTab(self)
        self.lockonTab = LockonTab(self)
        self.soundsTab = SoundsTab(self)
        self.appearanceTab = AppearanceTab(self)

        self.add(self.classTab, text=getText("Class and ammo"))
        self.add(self.basicParamsTab, text=getText("Basic stats"))
        self.add(self.lockonTab, text=getText("Lock-on"))
        self.add(self.appearanceTab, text=getText("Appearance"))
        self.add(self.soundsTab, text=getText("Sounds"))
    # end def __init__
        # self.add(self.tab1, text="tab1")
        # self.add(self.tab2, text="tab2")
        # self.appearanceTab.gunModelWidget.RABChoice.valueLabel.inputVar.trace_add("write", self.updateRABDependentWidgets)

    def updateRABDependentWidgets(self, *args):
        # animations and weapon icon and sight are handled in
        pass
    # end def updateRABDependentWidgets
# end class MainNotebook


def loadConfig():
    configOptions = {}
    try:
        with open("./config.ini", "r") as cfg:
            cfgLines = cfg.readlines()
            for line in cfgLines:
                try:
                    splitline = line.split("=")
                    configOptions[splitline[0]] = splitline[1]
                except:
                    print(f"{line} in config improperly formatted, expected 'setting=value'")
                # end try
            # end for
        # end with
    except:
        with open("./config.ini", "w") as cfg:
            cfg.write("language=en")
        # end with
        configOptions["language"] = "en"
    # end try

    return configOptions
# end def loadConfig


if __name__ == '__main__':
    # allEasy = loadDataFromJson("./data/allEasy.json")
    root = tk.Tk()
    root.title('Weapon builder')
    mainWindow = MainWindow(root, 1000, 800)
    mainWindow.pack(side="top", fill="both", expand=True)
    # force the height/width
    mainWindow.pack_propagate(0)
    root.mainloop()
# end if
