# # import tkinter as tk
# # from tkinter import ttk
#
import os

from idna import unicode

if __name__ == '__main__':
    os.chdir("C:\\Users\\Phi\\source\\repos\\edf-weapon-builder\\project")
# end if
# import tkinter as tk
# # import tkinter.ttk as ttk
#
# from jsonBuilder import *
# from widgets.widgets import *
# from widgets.EDFWidgets import *
from widgets.tabs import *
from tkinter import filedialog
import logging

# from functools import partial
# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_UI = os.path.join(PROJECT_PATH, "newproject")

global labelwidth
labelwidth = 20


class MainWindow(tk.Frame):
    def __init__(self, parent, width, height):
        self.customParamData = None
        self.muzzleFlashCustomParameters = None
        global language
        tk.Frame.__init__(self, parent, width=width, height=height)
        cfgSettings = loadConfig()
        setLanguage(cfgSettings["language"])

        self.widgetDict = {}
        self.stringEntryTest = FreeInputWidget(self, labeltext="test string", inputType="string")
        self.notebook = MainNotebook(self)
        self.notebook.pack(side="left", fill="both", expand=True)
        self.classChoiceVar = self.notebook.classTab.classChoice.dropDownDisplayed
        # self.testLabel = tk.Label(self.notebook.tab1, textvariable=self.intEntryTest.entryBoxVar.get(), relief="raised")
        # self.testButton = tk.Button(self, text="print", command=lambda: print(self.createWeaponEasyData()))
        self.testButton = tk.Button(self, text="Write to file", command=lambda: self.writeWeaponToJson())
        self.testButton.pack()
        self.updateTextFile = tk.Button(self, text="Update text json", command=self.updateText)
        self.updateTextFile.pack()
        self.loadTextFile = tk.Button(self, text="Load from file", command=lambda: self.loadWeaponFromJson())
        self.loadTextFile.pack()
        # self.testLabel.pack()

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
                                             filetypes=[("json files", ".json")])
        except Exception:
            logging.exception("Exception when reading json")
        # end try
        if file is not None:
            with open(file.name, encoding='utf-8') as fh:
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
                                                       filetypes=[("json files", ".json")])
        except Exception:
            logging.exception("Exception when writing json")
        # end try
        if filename != "":
            j.writeToJson(j.easyToTypeValue(self.createWeaponEasyData()), filename)
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
        eData["FireRecoil"] = n.basicParamsTab.basicParamsWidget.fireRecoil.value()
        eData["FireSe"] = n.soundsTab.fireSound.value()
        eData["FireSpreadType"] = n.classTab.fireSpreadType.value()
        eData["FireSpreadWidth"] = n.classTab.fireSpreadWidth.value()
        if n.classTab.xgsChoice.value() != "Weapon_Throw":
            eData["FireType"] = 0
        else:
            fire_type = n.basicParamsTab.basicParamsWidget.fireType.value()
            eData["FireType"] = fire_type if fire_type > 0 else 1
        # end if
        if n.classTab.fireVector.vectorX.value() == 0 and n.classTab.fireVector.vectorY.value() == 0 and n.classTab.fireVector.vectorZ.value() == 0:
            fireVector = None
        else:
            fireVector = [n.classTab.fireVector.vectorX.value(), n.classTab.fireVector.vectorY.value(),
                          n.classTab.fireVector.vectorZ.value()]
        # end if
        eData["FireVector"] = fireVector
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
        eData["ShellCase_CustomParameter"] = None  # Always null
        if n.appearanceTab.sightAnimationModel.value() != "missingSight_animation_model":
            s = n.appearanceTab.sightAnimationModel.value()
            eData["Sight_animation_model"] = [[f"app:/HUD/{s}.rab", f"{s}.mdb"], 0, 0]
        # end if
        eData["WeaponIcon"] = n.appearanceTab.gunModelWidget.WeaponIcon.value()
        if n.classTab.xgsChoice.value() != "Weapon_Accessory":
            eData["animation_model"] = n.appearanceTab.gunModelWidget.makeAnimation_ModelData()
        # end if
        if self.muzzleFlashCustomParameters is not None:
            eData["custom_parameter"] = self.customParamData
        if self.muzzleFlashCustomParameters is not None:
            eData["MuzzleFlash_CustomParameter"] = self.muzzleFlashCustomParameters
        eData["name.cn"] = n.classTab.cnName.value()
        eData["name.en"] = n.classTab.enName.value()
        eData["name.ja"] = n.classTab.jaName.value()
        eData["name.kr"] = n.classTab.krName.value()
        eData["use_underground"] = n.classTab.useUnderground.value()
        eData["xgs_scene_object_class"] = n.classTab.xgsChoice.value()
        return eData
    # end def createWeaponEasyData

    def loadWeaponEasyData(self, data, index):

        n = self.notebook
        for value in data['variables']:
            print(value)
            try:
                val = value['value']
                match value['name']:
                    case 'AimAnimation':
                        # self.animationData[r]['AimAnimation']
                        n.appearanceTab.gunModelWidget.AimAnimation.setValue()
                    case 'AmmoAlive':
                        n.basicParamsTab.basicParamsWidget.ammoLifetime.setValue(val)
                    case 'AmmoClass':
                        n.classTab.AmmoClass.setValue(val)
                    case 'AmmoColor':
                        red = float(val[0]['value'])
                        green = float(val[0]['value'])
                        blue = float(val[0]['value'])
                        alpha = float(val[0]['value'])
                        n.appearanceTab.ammoColor.red.input.set(red)
                        n.appearanceTab.ammoColor.green.input.set(green)
                        n.appearanceTab.ammoColor.blue.input.set(blue)
                        n.appearanceTab.ammoColor.alpha.input.set(alpha)
                    case 'AmmoCount':
                        if value["type"] == "int":
                            n.basicParamsTab.basicParamsWidget.ammoCount.baseValue.setValue(int(val))
                            n.basicParamsTab.basicParamsWidget.ammoCount.flatOrStar.setValue(False)
                        elif value["type"] == "ptr":
                            n.basicParamsTab.basicParamsWidget.ammoCount.flatOrStar.setValue(True)
                            n.basicParamsTab.basicParamsWidget.ammoCount.baseValue.setValue(int(val[0]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoCount.saveDataPos.setValue(float(val[2]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoCount.maxStarLevel.setValue(float(val[3]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoCount.p1.setValue(float(val[4]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoCount.p2.setValue(float(val[5]['value']))
                    case 'Ammo_EquipVoice':
                        if value['value'] is not None:
                            n.soundsTab.ammoEquipFullVoice.value(value['value'][0]['value'])
                            n.soundsTab.ammoEquipEmptyVoice.value(value['value'][1]['value'])
                    case 'AmmoDamage':
                        if value["type"] == "int":
                            n.basicParamsTab.basicParamsWidget.ammoDamage.baseValue.setValue(float(val))
                            n.basicParamsTab.basicParamsWidget.ammoDamage.flatOrStar.setValue(False)
                        elif value["type"] == "ptr":
                            n.basicParamsTab.basicParamsWidget.ammoDamage.flatOrStar.setValue(True)
                            n.basicParamsTab.basicParamsWidget.ammoDamage.baseValue.setValue(float(val[0]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoDamage.saveDataPos.setValue(float(val[2]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoDamage.maxStarLevel.setValue(float(val[3]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoDamage.p1.setValue(float(val[4]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoDamage.p2.setValue(float(val[5]['value']))
                    case 'AmmoDamageReduce':
                        n.basicParamsTab.basicParamsWidget.minDamage.setValue(val[0]['value'])
                        n.basicParamsTab.basicParamsWidget.falloffFactor.setValue(val[1]['value'])
                    case 'AmmoExplosion':
                        if value["type"] == "int":
                            n.basicParamsTab.basicParamsWidget.ammoExplosion.baseValue.setValue(float(val))
                            n.basicParamsTab.basicParamsWidget.ammoExplosion.flatOrStar.setValue(False)
                        elif value["type"] == "ptr":
                            n.basicParamsTab.basicParamsWidget.ammoExplosion.flatOrStar.setValue(True)
                            n.basicParamsTab.basicParamsWidget.ammoExplosion.baseValue.setValue(float(val[0]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoExplosion.saveDataPos.setValue(float(val[2]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoExplosion.maxStarLevel.setValue(float(val[3]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoExplosion.p1.setValue(float(val[4]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoExplosion.p2.setValue(float(val[5]['value']))
                    case 'AmmoGravityFactor':
                        n.classTab.ammoGravityFactor.setValue(val)
                    case 'AmmoHitImpulseAdjust':
                        n.classTab.ammoHitImpulseAdjust.setValue(val)
                    case 'AmmoHitSe':
                        n.soundsTab.impactSound.setValue(val)
                    case 'AmmoHitSizeAdjust':
                        n.classTab.ammoHitSizeAdjust.setValue(val)
                    case 'AmmoIsPenetration':
                        n.basicParamsTab.basicParamsWidget.isPenetrate.setValue(val)
                    case 'AmmoModel':
                        n.appearanceTab.ammoModel.setValue(val)
                    case 'AmmoOwnerMove':
                        n.classTab.ammoOwnerMove.setValue(val)
                    case 'AmmoSize':
                        n.classTab.ammoSize.setValue(val)
                    case 'AmmoSpeed':
                        if value["type"] == "int":
                            n.basicParamsTab.basicParamsWidget.ammoSpeed.baseValue.setValue(float(val))
                            n.basicParamsTab.basicParamsWidget.ammoSpeed.flatOrStar.setValue(False)
                        elif value["type"] == "ptr":
                            n.basicParamsTab.basicParamsWidget.ammoSpeed.flatOrStar.setValue(True)
                            n.basicParamsTab.basicParamsWidget.ammoSpeed.baseValue.setValue(float(val[0]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoSpeed.saveDataPos.setValue(float(val[2]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoSpeed.maxStarLevel.setValue(float(val[3]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoSpeed.p1.setValue(float(val[4]['value']))
                            n.basicParamsTab.basicParamsWidget.ammoSpeed.p2.setValue(float(val[5]['value']))
                    case 'Ammo_CustomParameter':
                        n.classTab.ammoCust.setValue(val)
                    case 'AngleAdjust':
                        n.appearanceTab.angleAdjust.setValue(val)
                    case 'BaseAnimation':
                        n.appearanceTab.gunModelWidget.BaseAnimation.setValue(val)
                    case 'ChangeAnimation':
                        n.appearanceTab.gunModelWidget.ChangeAnimation.setValue(val)
                    case 'FireAccuracy':
                        if value["type"] == "int":
                            n.basicParamsTab.basicParamsWidget.fireAccuracy.baseValue.setValue(float(val))
                            n.basicParamsTab.basicParamsWidget.fireAccuracy.flatOrStar.setValue(False)
                        elif value["type"] == "ptr":
                            n.basicParamsTab.basicParamsWidget.fireAccuracy.flatOrStar.setValue(True)
                            n.basicParamsTab.basicParamsWidget.fireAccuracy.baseValue.setValue(float(val[0]['value']))
                            n.basicParamsTab.basicParamsWidget.fireAccuracy.saveDataPos.setValue(float(val[2]['value']))
                            n.basicParamsTab.basicParamsWidget.fireAccuracy.maxStarLevel.setValue(float(val[3]['value']))
                            n.basicParamsTab.basicParamsWidget.fireAccuracy.p1.setValue(float(val[4]['value']))
                            n.basicParamsTab.basicParamsWidget.fireAccuracy.p2.setValue(float(val[5]['value']))
                    case 'FireBurstCount':
                        n.basicParamsTab.basicParamsWidget.fireBurstCount.setValue(val)
                    case 'FireBurstInterval':
                        n.basicParamsTab.basicParamsWidget.fireBurstInterval.setValue(val)
                    case 'FireCount':
                        n.basicParamsTab.basicParamsWidget.fireCount.setValue(val)
                    case 'FireInterval':
                        if value["type"] == "int":
                            n.basicParamsTab.basicParamsWidget.fireInterval.baseValue.setValue(int(val))
                            n.basicParamsTab.basicParamsWidget.fireInterval.flatOrStar.setValue(False)
                        elif value["type"] == "ptr":
                            n.basicParamsTab.basicParamsWidget.fireInterval.flatOrStar.setValue(True)
                            n.basicParamsTab.basicParamsWidget.fireInterval.baseValue.setValue(int(val[0]['value']))
                            n.basicParamsTab.basicParamsWidget.fireInterval.saveDataPos.setValue(float(val[2]['value']))
                            n.basicParamsTab.basicParamsWidget.fireInterval.maxStarLevel.setValue(float(val[3]['value']))
                            n.basicParamsTab.basicParamsWidget.fireInterval.p1.setValue(float(val[4]['value']))
                            n.basicParamsTab.basicParamsWidget.fireInterval.p2.setValue(float(val[5]['value']))
                    case 'FireLoadSe':
                        n.soundsTab.reloadSound.setValue(val)
                    case 'FireSe':
                        n.soundsTab.fireSound.setValue(val)
                    case 'FireSpreadType':
                        n.classTab.fireSpreadType.setValue(val)
                    case 'FireSpreadWidth':
                        n.classTab.fireSpreadWidth.setValue(val)
                    case 'LockonAngle':
                        n.lockonTab.lockonAngleH.setValue(float(val[0]['value']))
                        n.lockonTab.lockonAngleV.setValue(float(val[1]['value']))
                    case 'LockonFailedTime':
                        n.lockonTab.lockonFailedTime.setValue(val)
                    case 'LockonHoldTime':
                        n.lockonTab.lockonHoldTime.setValue(val)
                    case 'LockonRange':
                        n.lockonTab.lockonRange.setValue(val)
                    case 'LockonTargetType':
                        n.lockonTab.lockonTargetType.setValue(val)
                    case 'LockonTime':
                        n.lockonTab.lockonTime.setValue(val)
                    case 'LockonType':
                        n.lockonTab.lockonType.setValue(val)
                    case 'Lockon_AutoTimeOut':
                        n.lockonTab.lockonAutoTimeout.setValue(val)
                    case 'Lockon_DistributionType':
                        n.lockonTab.lockonDistributionType.setValue(val)
                    case 'Lockon_FireEndToClear':
                        n.lockonTab.lockonFireEndToClear.setValue(val)
                    case 'ModelConstraint':
                        n.appearanceTab.gunModelWidget.ModelConstraint.setValue(val)
                    case 'MuzzleFlash':
                        n.appearanceTab.muzzleFlash.muzzleFlashType.setValue(val)
                    case 'ReloadAnimation':
                        n.appearanceTab.gunModelWidget.ReloadAnimation.setValue(val)
                    case 'ReloadInit':
                        n.basicParamsTab.basicParamsWidget.reloadInit.setValue(val)
                    case 'ReloadTime':
                        if value["type"] == "int":
                            n.basicParamsTab.basicParamsWidget.reloadTime.baseValue.setValue(int(val))
                            n.basicParamsTab.basicParamsWidget.reloadTime.flatOrStar.setValue(False)
                        elif value["type"] == "ptr":
                            n.basicParamsTab.basicParamsWidget.reloadTime.flatOrStar.setValue(True)
                            n.basicParamsTab.basicParamsWidget.reloadTime.baseValue.setValue(int(val[0]['value']))
                            n.basicParamsTab.basicParamsWidget.reloadTime.saveDataPos.setValue(float(val[2]['value']))
                            n.basicParamsTab.basicParamsWidget.reloadTime.maxStarLevel.setValue(float(val[3]['value']))
                            n.basicParamsTab.basicParamsWidget.reloadTime.p1.setValue(float(val[4]['value']))
                            n.basicParamsTab.basicParamsWidget.reloadTime.p2.setValue(float(val[5]['value']))
                    case 'ReloadType':
                        n.basicParamsTab.basicParamsWidget.reloadType.setValue(val)
                    case 'FireType':
                        n.classTab.xgsChoice.setValue(val)
                    case 'FireVector':
                        if value['value'] is not None:
                            n.classTab.fireVector.vectorX.setValue(float(value['value'][0]['value']))
                            n.classTab.fireVector.vectorY.setValue(float(value['value'][1]['value']))
                            n.classTab.fireVector.vectorZ.setValue(float(value['value'][2]['value']))
                            n.classTab.fireVector.updateInputs()
                    case 'SecondaryFire_Type':
                        n.basicParamsTab.basicParamsWidget.secondaryFireType.setValue(val)
                    case 'ShellCase':
                        n.appearanceTab.shellCase.setValue(val)
                    case 'ShellCaseDischargeSe':
                        n.soundsTab.shellCaseDischargeSound.setValue()
                    case 'ShellCase_CustomParameter':
                        # None  # Always null
                        continue
                    case 'Sight_animation_model':
                        n.appearanceTab.sightAnimationModel.setValue([[f"app:/HUD/{val}.rab", f"{val}.mdb"], 0, 0])
                    case 'WeaponIcon':
                        n.appearanceTab.gunModelWidget.WeaponIcon.setValue(val)
                    case 'animation_model':
                        self.notebook.appearanceTab.gunModelWidget.RABChoice.setValue(value['value'][0]['value'][0]['value'])
                        n.appearanceTab.gunModelWidget.makeAnimation_ModelData()
                        self.notebook.appearanceTab.gunModelWidget.updateOptions()
                        self.notebook.appearanceTab.gunModelWidget.RABChoice.reconstructChildren(index)
                    case 'name.cn':
                        n.classTab.cnName.setValue(val)
                    case 'name.en':
                        n.classTab.enName.setValue(val)
                    case 'name.ja':
                        n.classTab.jaName.setValue(val)
                    case 'name.kr':
                        n.classTab.krName.setValue(val)
                    case 'use_underground':
                        n.classTab.useUnderground.setValue(val)
                    case 'xgs_scene_object_class':
                        n.classTab.xgsChoice.setValue(val)
                    case 'custom_parameter':
                        n.customParamData = val
                    case 'SecondaryFire_Parameter':
                        n.basicParamsTab.basicParamsWidget.secondaryFireParameter.setValue(
                            val) if n.basicParamsTab.basicParamsWidget.secondaryFireType.setValue(
                            val) == 1 else None
                    case "MuzzleFlash":
                        flash_type = val
                        if flash_type != "":
                            n.appearanceTab.muzzleFlash.muzzleFlashType.setvalue(flash_type)
                        else:
                            n.appearanceTab.muzzleFlash.muzzleFlashType.setvalue(None)
                    case 'MuzzleFlash_CustomParameter':
                        n.muzzleFlashCustomParameters = val
                    case 'EnergyChargeRequire':
                        if value['value'][0]["type"] == "float":
                            n.basicParamsTab.basicParamsWidget.energyChargeRequire.baseValue.setValue(float(val))
                            n.basicParamsTab.basicParamsWidget.energyChargeRequire.flatArray.setValue(True)
                            n.basicParamsTab.basicParamsWidget.energyChargeRequire.flatOrStar.setValue(False)

                        elif value['value'][0]["type"] == "ptr":
                            n.basicParamsTab.basicParamsWidget.energyChargeRequire.flatOrStar.setValue(True)
                            n.basicParamsTab.basicParamsWidget.energyChargeRequire.baseValue.setValue(float(val[0]['value'][0]['value']))
                            n.basicParamsTab.basicParamsWidget.energyChargeRequire.saveDataPos.setValue(float(val[0]['value'][2]['value']))
                            n.basicParamsTab.basicParamsWidget.energyChargeRequire.maxStarLevel.setValue(float(val[0]['value'][3]['value']))
                            n.basicParamsTab.basicParamsWidget.energyChargeRequire.p1.setValue(float(val[0]['value'][4]['value']))
                            n.basicParamsTab.basicParamsWidget.energyChargeRequire.p2.setValue(float(val[0]['value'][5]['value']))
                    case 'ExtPrams':
                        if value[0]["type"] == "float":
                            n.basicParamsTab.basicParamsWidget.extPrams.baseValue.setValue(float(val))
                            n.basicParamsTab.basicParamsWidget.extPrams.flatArray.setValue(False)
                        elif value[0]["type"] == "ptr":
                            n.basicParamsTab.basicParamsWidget.extPrams.baseValue.setValue(
                                float(val[0][0]['value']))
                            n.basicParamsTab.basicParamsWidget.extPrams.saveDataPos.setValue(
                                float(val[0][2]['value']))
                            n.basicParamsTab.basicParamsWidget.extPrams.maxStarLevel.setValue(
                                float(val[0][3]['value']))
                            n.basicParamsTab.basicParamsWidget.extPrams.p1.setValue(
                                float(val[0][4]['value']))
                            n.basicParamsTab.basicParamsWidget.extPrams.p2.setValue(
                                float(val[0][5]['value']))
                    case 'FireCondition':
                        continue  # Always 0
                    case 'FireRecoil':
                        n.basicParamsTab.basicParamsWidget.fireRecoil.setValue(float(val))
                    # if n.classTab.xgsChoice.value() != "Weapon_Accessory":
                    # eData["animation_model"] = n.appearanceTab.gunModelWidget.makeAnimation_ModelData()
                    case _:
                        continue
            except:
                print("An exception occurred")
            finally:
                print("The 'try except' is finished")
        # end for
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
