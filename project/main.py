import os

import helpers

if __name__ == '__main__':
    currDir = os.getcwd()
    if not currDir.endswith('project'):
        os.chdir(".\project")

from widgets.tabs import *
from tkinter import filedialog
import logging

global labelwidth
labelwidth = 20

def set_star_data(field, value):
    try:
        if isinstance(value, int) or isinstance(value, float) or (isinstance(value, list) and len(value) <= 2):
            if isinstance(value, int) or isinstance(value, float):
                # if isinstance(value, int):
                #     field.flatArray = True
                # elif isinstance(value, float):
                #     field.flatArray = False
                    val = value
                    field.flatArray = False
            else:
                val = value[0]
                field.flatArray = True
            field.baseValue.setValue(val)
            field.flatOrStar.setValue('flat')
            return


        field.baseValue.setValue(value[0])
        field.saveDataPos.inputVar.set(value[2])

        field.maxStarLevel.inputVar.set(value[3])
        field.p1.setValue(value[4])
        field.p2.setValue(value[5])
        if len(value) == 7:
            field.extra = value[6]

        field.flatArray = False
        field.flatOrStar.setValue('star')
    except Exception as e:
        print(e)


def get_variable(variables, var_name):
    print("Handling - " + var_name)
    if var_name in variables:
        return variables[var_name]
    else:
        return None
    # return next(
    #     (obj for obj in variables if obj['name'] == var_name),
    #     None
    # )

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
        self.loadWeaponFromJsonFile(file.name)

    def reset_weapon_data(self):
        self.notebook = MainNotebook(self)

    def loadWeaponFromJsonFile(self, file):

        weaponClass = "Ranger"
        index = 0
        fileName = os.path.basename(file)
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

        self.notebook.classTab.classChoice.setValue(weaponClass)

        res = helpers.load_weapon_easy_data(file)
        self.loadWeaponEasyData(res)
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
        self.writeWeaponToJsonFile(filename)

    def writeWeaponToJsonFile(self, filename, include_options=True):
        if filename != "":
            # always need to write json
            convert = filename.lower().endswith("sgo")
            jsonFileName = filename + ".new.json" if convert else filename

            easyWeaponData = self.createWeaponEasyData()
            # j.writeToJson(easyWeaponData, filename + ".easy.json")
            j.writeToJson(j.easyToTypeValue(easyWeaponData, include_options), jsonFileName)

            # if not convert:
            #     return
            #
            # args = ['./tools/sgott.exe', jsonFileName, filename]
            # subprocess.call(args)

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

    def loadWeaponEasyData(self, data):
        print('Loading')
        n = self.notebook
        try:
            AimAnimation = get_variable(data, 'AimAnimation')
            if AimAnimation is not None:
                n.appearanceTab.gunModelWidget.AimAnimation.setValue(AimAnimation)

            AmmoAlive = get_variable(data, 'AmmoAlive')

            if AmmoAlive is not None:
                n.basicParamsTab.basicParamsWidget.ammoLifetime.setValue(AmmoAlive)

            AmmoClass = get_variable(data, 'AmmoClass')

            if AmmoClass is not None:
                n.classTab.AmmoClass.setValue(AmmoClass)

            AmmoColor = get_variable(data, 'AmmoColor')

            if AmmoColor is not None:
                red = float(AmmoColor[0])
                green = float(AmmoColor[1])
                blue = float(AmmoColor[2])
                alpha = float(AmmoColor[3])
                n.appearanceTab.ammoColor.red_input.inputVar.set(red)
                n.appearanceTab.ammoColor.red = red

                n.appearanceTab.ammoColor.green_input.inputVar.set(green)
                n.appearanceTab.ammoColor.green = green

                n.appearanceTab.ammoColor.blue_input.inputVar.set(blue)
                n.appearanceTab.ammoColor.blue = blue

                n.appearanceTab.ammoColor.alpha_input.inputVar.set(alpha)
                n.appearanceTab.ammoColor.alpha = alpha

            AmmoCount = get_variable(data, 'AmmoCount')

            if AmmoCount is not None:
                set_star_data(n.basicParamsTab.basicParamsWidget.ammoCount, AmmoCount)

            Ammo_EquipVoice = get_variable(data, 'Ammo_EquipVoice')

            if Ammo_EquipVoice is not None:
                    n.soundsTab.ammoEquipFullVoice.setValue(Ammo_EquipVoice[0])
                    n.soundsTab.ammoEquipEmptyVoice.setValue(Ammo_EquipVoice[1])

            AmmoDamage = get_variable(data, 'AmmoDamage')

            if AmmoDamage is not None:
                set_star_data(n.basicParamsTab.basicParamsWidget.ammoDamage, AmmoDamage)

            AmmoDamageReduce = get_variable(data, 'AmmoDamageReduce')

            if AmmoDamageReduce is not None:

                reduceVal = float(AmmoDamageReduce[0])
                fallOffVal = int(AmmoDamageReduce[1])
                n.basicParamsTab.basicParamsWidget.minDamage.inputVar.set(reduceVal)
                n.basicParamsTab.basicParamsWidget.minDamage.setValue(reduceVal)
                n.basicParamsTab.basicParamsWidget.falloffFactor.setValue(fallOffVal)

            AmmoExplosion = get_variable(data, 'AmmoExplosion')

            if AmmoExplosion is not None:
                set_star_data(n.basicParamsTab.basicParamsWidget.ammoExplosion, AmmoExplosion)

            AmmoGravityFactor = get_variable(data, 'AmmoGravityFactor')

            if AmmoGravityFactor is not None:

                n.classTab.ammoGravityFactor.setValue(AmmoGravityFactor)

            AmmoHitImpulseAdjust = get_variable(data, 'AmmoHitImpulseAdjust')

            if AmmoHitImpulseAdjust is not None:

                n.classTab.ammoHitImpulseAdjust.setValue(AmmoHitImpulseAdjust)

            AmmoHitSe = get_variable(data, 'AmmoHitSe')

            if AmmoHitSe is not None:

                n.soundsTab.impactSound.setValue(AmmoHitSe)

            AmmoHitSizeAdjust = get_variable(data, 'AmmoHitSizeAdjust')

            if AmmoHitSizeAdjust is not None:

                n.classTab.ammoHitSizeAdjust.setValue(AmmoHitSizeAdjust)

            AmmoIsPenetration = get_variable(data, 'AmmoIsPenetration')

            if AmmoIsPenetration is not None:

                n.basicParamsTab.basicParamsWidget.isPenetrate.setValue(AmmoIsPenetration)

            AmmoModel = get_variable(data, 'AmmoModel')

            if AmmoModel is not None:

                n.appearanceTab.ammoModel.setValue(AmmoModel)

            AmmoOwnerMove = get_variable(data, 'AmmoOwnerMove')

            if AmmoOwnerMove is not None:

                n.classTab.ammoOwnerMove.setValue(AmmoOwnerMove)

            AmmoSize = get_variable(data, 'AmmoSize')

            if AmmoSize is not None:

                n.classTab.ammoSize.setValue(AmmoSize)

            AmmoSpeed = get_variable(data, 'AmmoSpeed')

            if AmmoSpeed is not None:

                set_star_data(n.basicParamsTab.basicParamsWidget.ammoSpeed, AmmoSpeed)

            Ammo_CustomParameter = get_variable(data, 'Ammo_CustomParameter')

            AngleAdjust = get_variable(data, 'AngleAdjust')

            if AngleAdjust is not None:

                n.appearanceTab.angleAdjust.setValue(AngleAdjust)

            BaseAnimation = get_variable(data, 'BaseAnimation')

            if BaseAnimation is not None:

                n.appearanceTab.gunModelWidget.BaseAnimation.setValue(BaseAnimation)

            ChangeAnimation = get_variable(data, 'ChangeAnimation')

            if ChangeAnimation is not None:

                n.appearanceTab.gunModelWidget.ChangeAnimation.setValue(ChangeAnimation)

            FireAccuracy = get_variable(data, 'FireAccuracy')

            if FireAccuracy is not None:

                set_star_data(n.basicParamsTab.basicParamsWidget.fireAccuracy, FireAccuracy)

            FireBurstCount = get_variable(data, 'FireBurstCount')

            if FireBurstCount is not None:


                n.basicParamsTab.basicParamsWidget.fireBurstCount.setValue(FireBurstCount)

            FireBurstInterval = get_variable(data, 'FireBurstInterval')

            if FireBurstInterval is not None:

                set_star_data(n.basicParamsTab.basicParamsWidget.fireBurstInterval, FireBurstInterval)

            FireCount = get_variable(data, 'FireCount')

            if FireCount is not None:
                if isinstance(FireCount, list):
                    set_star_data(n.basicParamsTab.basicParamsWidget.fireCount, FireCount)
                else:
                    n.basicParamsTab.basicParamsWidget.fireCount.baseValue.setValue(int(FireCount))

            FireInterval = get_variable(data, 'FireInterval')
            if FireInterval is not None:
                set_star_data(n.basicParamsTab.basicParamsWidget.fireInterval, FireInterval)

            FireLoadSe = get_variable(data, 'FireLoadSe')

            if FireLoadSe is not None:
                n.soundsTab.reloadSound.setValue(FireLoadSe)

            FireSe = get_variable(data, 'FireSe')

            if FireSe is not None:
                n.soundsTab.fireSound.setValue(FireSe)

            FireSpreadType = get_variable(data, 'FireSpreadType')

            if FireSpreadType is not None:
                n.classTab.fireSpreadType.setValue(FireSpreadType)

            FireSpreadWidth = get_variable(data, 'FireSpreadWidth')

            if FireSpreadWidth is not None:
                n.classTab.fireSpreadWidth.inputVar.set(float(FireSpreadWidth))
                n.classTab.fireSpreadWidth.setValue(FireSpreadWidth)


            LockonAngle = get_variable(data, 'LockonAngle')

            if LockonAngle is not None:
                n.lockonTab.lockonAngleH.setValue(float(LockonAngle[0]))
                n.lockonTab.lockonAngleV.setValue(float(LockonAngle[1]))

            LockonFailedTime = get_variable(data, 'LockonFailedTime')

            if LockonFailedTime is not None:
                n.lockonTab.lockonFailedTime.setValue(LockonFailedTime)

            LockonHoldTime = get_variable(data, 'LockonHoldTime')

            if LockonHoldTime is not None:
                n.lockonTab.lockonHoldTime.setValue(LockonHoldTime)

            LockonRange = get_variable(data, 'LockonRange')

            if LockonRange is not None:
                if isinstance(LockonRange, list):
                    set_star_data(n.lockonTab.lockonRange, LockonRange)
                else:
                    n.lockonTab.lockonRange.baseValue.setValue(int(LockonRange))

            LockonTargetType = get_variable(data, 'LockonTargetType')

            if LockonTargetType is not None:
                n.lockonTab.lockonTargetType.setValue(LockonTargetType)

            LockonTime = get_variable(data, 'LockonTime')

            if LockonTime is not None:
                if isinstance(LockonTime, list):
                    set_star_data(n.lockonTab.lockonTime, LockonTime)
                else:
                    n.lockonTab.lockonTime.baseValue.setValue(int(LockonTime))

            LockonType = get_variable(data, 'LockonType')

            if LockonType is not None:
                n.lockonTab.lockonType.setValue(LockonType)

            Lockon_AutoTimeOut = get_variable(data, 'Lockon_AutoTimeOut')

            if Lockon_AutoTimeOut is not None:

                n.lockonTab.lockonAutoTimeout.setValue(Lockon_AutoTimeOut)

            Lockon_DistributionType = get_variable(data, 'Lockon_DistributionType')

            if Lockon_DistributionType is not None:

                n.lockonTab.lockonDistributionType.setValue(Lockon_DistributionType)

            Lockon_FireEndToClear = get_variable(data, 'Lockon_FireEndToClear')

            if Lockon_FireEndToClear is not None:

                n.lockonTab.lockonFireEndToClear.setValue(Lockon_FireEndToClear)

            ReloadAnimation = get_variable(data, 'ReloadAnimation')

            if ReloadAnimation is not None:

                n.appearanceTab.gunModelWidget.ReloadAnimation.setValue(ReloadAnimation)

            ReloadInit = get_variable(data, 'ReloadInit')

            if ReloadInit is not None:

                n.basicParamsTab.basicParamsWidget.reloadInit.setValue(ReloadInit)

            ReloadTime = get_variable(data, 'ReloadTime')
            if ReloadTime is not None:

                if isinstance(ReloadTime, list):
                    set_star_data(n.basicParamsTab.basicParamsWidget.reloadTime, ReloadTime)
                else:
                    n.basicParamsTab.basicParamsWidget.reloadTime.baseValue.setValue(int(ReloadTime))

            ReloadType = get_variable(data, 'ReloadType')

            if ReloadType is not None:

                n.basicParamsTab.basicParamsWidget.reloadType.setValue(ReloadType)

            FireType = get_variable(data, 'FireType')
            if FireType is not None:

                n.classTab.xgsChoice.setValue(FireType)

            FireVector = get_variable(data, 'FireVector')
            if FireVector is not None:

                if FireVector is not None:
                    n.classTab.fireVector.vectorX.setValue(float(FireVector[0]))
                    n.classTab.fireVector.vectorY.setValue(float(FireVector[1]))
                    n.classTab.fireVector.vectorZ.setValue(float(FireVector[2]))
                    n.classTab.fireVector.updateInputs()

            SecondaryFire_Type = get_variable(data, 'SecondaryFire_Type')

            if SecondaryFire_Type is not None:

                n.basicParamsTab.basicParamsWidget.secondaryFireType.setValue(SecondaryFire_Type)

            ShellCase = get_variable(data, 'ShellCase')

            if ShellCase is not None:

                n.appearanceTab.shellCase.setValue(ShellCase)

            ShellCaseDischargeSe = get_variable(data, 'ShellCaseDischargeSe')
            if ShellCaseDischargeSe is not None:

                n.soundsTab.shellCaseDischargeSound.setValue(ShellCaseDischargeSe)

            # ShellCase_CustomParameter = get_variable(data, 'ShellCase_CustomParameter')

            # if ShellCase_CustomParameter is not None:
            #     # None  # Always null
            #     continue

            Sight_animation_model = get_variable(data, 'Sight_animation_model')

            if Sight_animation_model is not None:

                mdb = Sight_animation_model[0][1]
                mdbVal = str.replace(mdb, '.mdb','')
                mdbLower = str.lower(mdbVal)
                n.appearanceTab.sightAnimationModel.setValue(mdbLower)

            WeaponIcon = get_variable(data, 'WeaponIcon')
            if WeaponIcon is not None:
                n.appearanceTab.gunModelWidget.WeaponIcon.setValue(WeaponIcon)

            nameCn = get_variable(data, 'name.cn')
            if nameCn is not None:
                n.classTab.cnName.setValue(nameCn)

            nameEn = get_variable(data, 'name.en')
            if nameEn is not None:
                n.classTab.enName.setValue(nameEn)

            nameJa = get_variable(data, 'name.ja')

            if nameJa is not None:
                n.classTab.jaName.setValue(nameJa)

            nameKr = get_variable(data, 'name.kr')
            if nameKr is not None:
                n.classTab.krName.setValue(nameKr)

            use_underground = get_variable(data, 'use_underground')
            if use_underground is not None:
                n.classTab.useUnderground.setValue(use_underground)

            xgs_scene_object_class = get_variable(data, 'xgs_scene_object_class')
            if xgs_scene_object_class is not None:
                n.classTab.xgsChoice.setValue(xgs_scene_object_class)

            custom_parameter = get_variable(data, 'custom_parameter')
            if custom_parameter is not None:
                self.customParamData = custom_parameter

            SecondaryFire_Parameter = get_variable(data, 'SecondaryFire_Parameter')
            if SecondaryFire_Parameter is not None:
                n.basicParamsTab.basicParamsWidget.secondaryFireParameter.setValue(
                    SecondaryFire_Parameter) if n.basicParamsTab.basicParamsWidget.secondaryFireType.setValue(
                    SecondaryFire_Parameter) == 1 else None

            MuzzleFlash = get_variable(data, 'MuzzleFlash')
            if MuzzleFlash is not None and MuzzleFlash is not "":
                n.appearanceTab.muzzleFlash.muzzleFlashType.setValue(MuzzleFlash)

            MuzzleFlash_CustomParameter = get_variable(data, 'MuzzleFlash_CustomParameter')
            if MuzzleFlash_CustomParameter is not None:
                self.muzzleFlashCustomParameters = MuzzleFlash_CustomParameter

            EnergyChargeRequire = get_variable(data, 'EnergyChargeRequire')
            if EnergyChargeRequire is not None:
                set_star_data(n.basicParamsTab.basicParamsWidget.energyChargeRequire, EnergyChargeRequire)

            ExtPrams = get_variable(data, 'ExtPrams')
            if ExtPrams is not None:
                set_star_data(n.basicParamsTab.basicParamsWidget.extPrams, ExtPrams)

            # FireCondition = get_variable(data, 'FireCondition')

            # if FireCondition is not None:
            #     continue  # Always 0

            n.classTab.fireRecoil.inputVar.set(0.0)
            n.classTab.fireRecoil.input.set(0.0)

            FireRecoil = get_variable(data, 'FireRecoil')
            if FireRecoil is not None:
                n.classTab.fireRecoil.inputVar.set(float(FireRecoil))
                n.classTab.fireRecoil.input.set(float(FireRecoil))
            # if n.classTab.xgsChoice.value() != "Weapon_Accessory":
            # eData["animation_model"] = n.appearanceTab.gunModelWidget.makeAnimation_ModelData()

            # TODO - determine how to determine sub projectile or not, default to True for now
            # default params
            Ammo_CustomParameterVal = None
            ammoClass = n.classTab.AmmoClass.value()

            # set the val if we have something
            if Ammo_CustomParameter is not None:
                subProjectile = ammoClass in subProjectileAmmoOptions
            else:
                subProjectile = False

            # set the widget based on the class
            n.classTab.ammoCust = ammoCustWidgetFromAmmoClass(n.classTab.canvas, ammoClass, subProjectile)

            print("Handling - Ammo_CustomParameter")
            # set the widget value if we have one
            if Ammo_CustomParameter is not None:
                n.classTab.ammoCust.setValue(Ammo_CustomParameter)

            animation_model = get_variable(data, 'animation_model')

            if animation_model is not None:
                rabChoice = animation_model[0][0]
                n.appearanceTab.gunModelWidget.RABChoice.setValue(rabChoice)
                n.appearanceTab.gunModelWidget.makeAnimation_ModelData()

            ModelConstraint = get_variable(data, 'ModelConstraint')

            if ModelConstraint is not None:

                n.appearanceTab.gunModelWidget.ModelConstraint = DropDownWidget(self, "Model Constraint", {
                    str(n.appearanceTab.gunModelWidget.animationData[n.appearanceTab.gunModelWidget.RABChoice.value()][
                            'ModelConstraint']):
                        n.appearanceTab.gunModelWidget.animationData[n.appearanceTab.gunModelWidget.RABChoice.value()][
                            'ModelConstraint']})
                n.appearanceTab.gunModelWidget.ModelConstraint.setValue(ModelConstraint[0])

            self.notebook.appearanceTab.gunModelWidget.updateOptions()

            # Mapped but not displayed
            n.resource = None
            resource = get_variable(data, 'resource')
            if resource is not None:
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
def init(loop=True):
    root = tk.Tk()
    root.title('Weapon builder')
    mainWindow = MainWindow(root, 1000, 800)
    mainWindow.pack(side="top", fill="both", expand=True)
    # force the height/width
    mainWindow.pack_propagate(0)
    if loop:
        root.mainloop()
    return mainWindow

if __name__ == '__main__':
    # allEasy = loadDataFromJson("./data/allEasy.json")
    init()
# end if
