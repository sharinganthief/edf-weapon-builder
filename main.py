# import tkinter as tk
# from tkinter import ttk

import os
import tkinter as tk
# import tkinter.ttk as ttk

from jsonBuilder import *
from widgets.widgets import *
from widgets.EDFWidgets import *
from widgets.tabs import *
from tkinter import filedialog

from functools import partial

# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_UI = os.path.join(PROJECT_PATH, "newproject")

global labelwidth
labelwidth = 20

def dummy():
    pass


class MainWindow(tk.Frame):
    def __init__(self, parent, width, height):
        tk.Frame.__init__(self, parent, width=width, height=height)
        self.widgetDict = {}
        self.activeTab = ''
        # self.tabs = ["1", "2", "3", "4"]
        self.stringEntryTest = FreeInputWidget(self, labeltext="test string", inputType="string")
        self.notebook = MainNotebook(self)
        self.notebook.pack(side="left", fill="both", expand=True)
        # self.notebook.tab(3,state="disabled")
        self.classChoiceVar = self.notebook.classTab.classChoice.dropDownDisplayed
        self.classChoiceVar.trace_add("write", self.updateWidgetsDependingOnClass)
        # self.testLabel = tk.Label(self.notebook.tab1, textvariable=self.intEntryTest.entryBoxVar.get(), relief="raised")
        # self.testButton = tk.Button(self, text="print", command=lambda: print(self.createWeaponEasyData()))
        self.testButton = tk.Button(self, text="Write to file", command=lambda: self.writeWeaponToJson())
        self.testButton.pack()
        # self.testLabel.pack()

    def writeWeaponToJson(self):
        curDir = os.path.abspath(".")
        try:
            filename = tk.filedialog.asksaveasfilename(initialdir=curDir, title=getText("Choose file name"),
                                                       filetypes=[("json files", ".json")])
            j.writeToJson(j.easyToTypeValue(self.createWeaponEasyData()), filename)
        except:
            pass
        print(filename)

    def updateWidgetsDependingOnXGS(self, *args):
        pass

    def updateWidgetsDependingOnClass(self, *args):
        self.notebook.appearanceTab.gunModelWidget.classChange(self.classChoiceVar.get())
        self.notebook.basicParamsTab.basicParamsWidget.updateSecondaryOptionsBasedOnClass(self.classChoiceVar.get())

    def createWeaponEasyData(self, *args):
        n = self.notebook
        eData = {}
        eData["AimAnimation"] = n.appearanceTab.gunModelWidget.AimAnimation.value()
        eData["AmmoAlive"] = n.basicParamsTab.basicParamsWidget.ammoLifetime.value()
        eData["AmmoClass"] = n.classTab.AmmoClass.value()
        eData["AmmoColor"] = n.appearanceTab.ammoColor.value()
        eData["AmmoCount"] = n.basicParamsTab.basicParamsWidget.ammoCount.value()
        eData["AmmoDamage"] = n.basicParamsTab.basicParamsWidget.ammoDamage.value()
        eData["AmmoDamageReduce"] = [n.basicParamsTab.basicParamsWidget.minDamage.value(), n.basicParamsTab.basicParamsWidget.falloffFactor.value()]
        eData["AmmoExplosion"] = n.basicParamsTab.basicParamsWidget.ammoExplosion.value()
        eData["AmmoGravityFactor"] = n.ammoOptionsTab.ammoGravityFactor.value()
        eData["AmmoHitImpulseAdjust"] = n.ammoOptionsTab.ammoHitImpulseAdjust.value()
        eData["AmmoHitSe"] = n.soundsTab.impactSound.value()
        eData["AmmoHitSizeAdjust"] = n.ammoOptionsTab.ammoHitSizeAdjust.value()
        eData["AmmoIsPenetration"] = n.basicParamsTab.basicParamsWidget.isPenetrate.value()
        eData["AmmoModel"] = n.appearanceTab.ammoModel.value()
        eData["AmmoOwnerMove"] = n.ammoOptionsTab.ammoOwnerMove.value()
        eData["AmmoSize"] = n.ammoOptionsTab.ammoSize.value()
        eData["AmmoSpeed"] = n.basicParamsTab.basicParamsWidget.ammoSpeed.value()
        eData["Ammo_CustomParameter"] = n.classTab.test.value()
        eData["Ammo_EquipVoice"] = [n.soundsTab.ammoEquipFullVoice.value(), n.soundsTab.ammoEquipEmptyVoice.value()] if n.soundsTab.ammoEquipFullVoice.value() is not None and n.soundsTab.ammoEquipEmptyVoice.value() is not None else None
        eData["AngleAdjust"] = n.appearanceTab.angleAdjust.value()
        eData["BaseAnimation"] = n.appearanceTab.gunModelWidget.BaseAnimation.value()
        eData["ChangeAnimation"] = n.appearanceTab.gunModelWidget.ChangeAnimation.value()
        eData["EnergyChargeRequire"] = [-1, -1]  # TODO
        eData["ExtPrams"] = [1]  # TODO
        eData["FireAccuracy"] = n.basicParamsTab.basicParamsWidget.fireAccuracy.value()
        eData["FireBurstCount"] = n.basicParamsTab.basicParamsWidget.fireBurstCount.value()
        eData["FireBurstInterval"] = n.basicParamsTab.basicParamsWidget.fireBurstInterval.value()
        eData["FireCondition"] = 0  # Always 0
        eData["FireCount"] = n.basicParamsTab.basicParamsWidget.fireCount.value()
        eData["FireInterval"] = n.basicParamsTab.basicParamsWidget.fireInterval.value()
        eData["FireLoadSe"] = n.soundsTab.reloadSound.value()
        eData["FireRecoil"] = 0.0  # TODO
        eData["FireSe"] = n.soundsTab.fireSound.value()
        eData["FireSpreadType"] = n.ammoOptionsTab.fireSpreadType.value()
        eData["FireSpreadWidth"] = n.ammoOptionsTab.fireSpreadWidth.value()
        if n.classTab.xgsChoice.value() != "Weapon_Throw":
            eData["FireType"] = 0
        else:
            eData["FireType"] = 1  # TODO 1 = impact detonation 2 = fuse detonation for thrown grenade weapons
        if n.ammoOptionsTab.fireVector.vectorX.value() == 0 and n.ammoOptionsTab.fireVector.vectorY.value() == 0 and n.ammoOptionsTab.fireVector.vectorZ.value() == 0:
            fireVector = None
        else:
            fireVector = [n.ammoOptionsTab.fireVector.vectorX.value(), n.ammoOptionsTab.fireVector.vectorY.value(), n.ammoOptionsTab.fireVector.vectorZ.value()]
        eData["FireVector"] = fireVector
        eData["LockonAngle"] = [n.lockonTab.lockonAngleH.value(), n.lockonTab.lockonAngleV.value()]
        eData["LockonFailedTime"] = n.lockonTab.lockonFailedTime.value()
        eData["LockonHoldTime"] = n.lockonTab.lockonHoldTime.value()
        eData["LockonRange"] = n.lockonTab.lockonRange.value()
        eData["LockonTargetType"] = n.lockonTab.lockonTargetType.value()
        eData["LockonTime"] = n.lockonTab.lockonTime.value()
        eData["LockonType"] = n.lockonTab.lockonType.value() # if n.classTab.xgsChoice.value() == "Weapon_HomingShoot" else 0
        eData["Lockon_AutoTimeOut"] = n.lockonTab.lockonAutoTimeout.value()
        eData["Lockon_DistributionType"] = n.lockonTab.lockonDistributionType.value()
        eData["Lockon_FireEndToClear"] = n.lockonTab.lockonFireEndToClear.value()
        eData["ModelConstraint"] = n.appearanceTab.gunModelWidget.ModelConstraint.value()
        eData["MuzzleFlash"] = n.appearanceTab.muzzleFlash.muzzleFlashType.value()
        eData["MuzzleFlash_CustomParameter"] = n.appearanceTab.muzzleFlash.paramsWidget.value() if n.appearanceTab.muzzleFlash.muzzleFlashType.value() != "" else None
        eData["ReloadAnimation"] = n.appearanceTab.gunModelWidget.ReloadAnimation.value()
        eData["ReloadInit"] = n.basicParamsTab.basicParamsWidget.reloadInit.value()
        eData["ReloadTime"] = n.basicParamsTab.basicParamsWidget.reloadTime.value()
        eData["ReloadType"] = n.basicParamsTab.basicParamsWidget.reloadType.value()
        eData["SecondaryFire_Parameter"] = n.basicParamsTab.basicParamsWidget.secondaryFireParameter.value() if n.basicParamsTab.basicParamsWidget.secondaryFireType.value() == 1 else None
        eData["SecondaryFire_Type"] = n.basicParamsTab.basicParamsWidget.secondaryFireType.value()
        eData["ShellCase"] = n.appearanceTab.shellCase.value()
        eData["ShellCaseDischargeSe"] = n.soundsTab.shellCaseDischargeSound.value()
        eData["ShellCase_CustomParameter"] = None  # Always null
        if n.appearanceTab.sightAnimationModel.value() != "missingSight_animation_model":
            s = n.appearanceTab.sightAnimationModel.value()
            eData["Sight_animation_model"] = [[f"app:/HUD/{s}.rab", f"{s}.mdb"], 0, 0]
        eData["WeaponIcon"] = n.appearanceTab.gunModelWidget.WeaponIcon.value()
        if n.classTab.xgsChoice.value() != "Weapon_Accessory":
            eData["animation_model"] = n.appearanceTab.gunModelWidget.makeAnimation_ModelData()
        eData["custom_parameter"] = self.makeCustomParamData() # TODO
        eData["name.cn"] = "Racer weapon"  # TODO
        eData["name.en"] = "Racer weapon"  # TODO
        eData["name.ja"] = "Racer weapon"  # TODO
        eData["name.kr"] = "Racer weapon"  # TODO
        eData["use_underground"] = 1
        eData["xgs_scene_object_class"] = n.classTab.xgsChoice.value()
        return eData

    def makeCustomParamData(self, *args):
        c = ["assault_recoil1", 1, 0, 1.0]
        return c
        # c.append()


class WindowMenus(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent

        self.fileMenu = tk.Menu(self, tearoff=0)
        self.fileMenu.add_command(label=getText("Write weapon data to json"), command=dummy)
        self.fileMenu.add_command(label="test", command=dummy())
        self.fileMenu.add_command(label="test", command=dummy())
        self.fileMenu.add_command(label="test", command=dummy())
        self.add_cascade(label="File", menu=self.fileMenu)


class MainNotebook(ttk.Notebook):
    def __init__(self, parent):
        ttk.Notebook.__init__(self, parent)
        self.parent = parent
        # self.tab1 = StandardWeaponTab(self, 600, 400, "tab1")
        # self.tab2 = StandardWeaponTab(self, 600, 300, "tab2")
        self.classTab = ClassTab(self)
        self.basicParamsTab = BasicParamsTab(self)
        self.ammoOptionsTab = AmmoOptionsTab(self)
        self.lockonTab = LockonTab(self)
        self.soundsTab = SoundsTab(self)
        self.appearanceTab = AppearanceTab(self)

        self.add(self.classTab, text=getText("Class"))
        self.add(self.basicParamsTab, text=getText("Basic Parameters"))
        self.add(self.ammoOptionsTab, text=getText("Ammo Options"))
        self.add(self.lockonTab, text=getText("Lock-on"))
        self.add(self.appearanceTab, text=getText("Appearance"))
        self.add(self.soundsTab, text=getText("Sounds"))
        # self.add(self.tab1, text="tab1")
        # self.add(self.tab2, text="tab2")
        # self.appearanceTab.gunModelWidget.RABChoice.valueLabel.inputVar.trace_add("write", self.updateRABDependentWidgets)

    def updateRABDependentWidgets(self, *args):
        # animations and weapon icon and sight are handled in
        pass


# class SoundsTab(tk.Frame):
#     def __init__(self, parent):
#         tk.Frame.__init__(self, parent)
#         self.fireSound = SoundWidget(self, "Firing Sound")
#         self.impactSound = SoundWidget(self, "Impact Sound")
#         self.reloadSound = SoundWidget(self, "Reload Sound")
#         self.fireSound.grid(row=0, column=0)
#         self.impactSound.grid(row=0, column=1)
#         self.reloadSound.grid(row=0, column=2)
#
#
# class appearanceTab(tk.Frame):
#     def __init__(self, parent):
#         tk.Frame.__init__(self, parent)
#         self.ModelWidget = ModelWidget(self)
#         self.ModelWidget.pack()
#         self.ModelWidget.classChange("Ranger")
#
#
# class StandardWeaponTab(tk.Frame):
#     def __init__(self, parent, width, height, text):
#         tk.Frame.__init__(self, parent, width=width, height=height)
#         self.parent = parent
#         self.label1 = tk.Label(self, text=text)
#         self.label1.pack()


if __name__ == '__main__':
    root = tk.Tk()
    mainWindow = MainWindow(root, 1000, 800)
    mainWindow.pack(side="top", fill="both", expand=True)
    # force the height/width
    mainWindow.pack_propagate(0)
    # menu = WindowMenus(root)
    # root.config(menu=menu)
    root.mainloop()

