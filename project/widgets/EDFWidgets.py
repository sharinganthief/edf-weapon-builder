import tkinter as tk
from tkinter import ttk
import webbrowser
import subprocess
import sys
import time
from text import *
import dataHelper as d
import jsonBuilder as j
from widgets.widgets import *
from math import pi, cos, sin

try:
    from PIL import ImageTk, Image
except:
    userChoice = input("Required package 'pillow' is not installed in your python installation, would you like to install it? (y/n)")
    if userChoice.lower() == "y" or userChoice.lower() == "yes":
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
            time.sleep(3)
            from PIL import ImageTk, Image
        except:
            input("Please ensure that you have installed pip when you installed python. If not you can reinstall or repair your installation and install pip\nPress enter to quit.")
            quit()
    else: quit()


sounds = j.loadDataFromJson("./data/Sounds.json")
labelwidth = 20
inputwidth = 25

allModels = j.loadDataFromJson("./data/sorted all models.json")

def degreesToRadians(d, *args):
    return d * pi / 180


def radiansToDegrees(r, *args):
    return r * 180 / pi


class VectorFromAngleWidget(tk.LabelFrame):
    def __init__(self, parent, labelText):
        tk.LabelFrame.__init__(self, parent, text=labelText)
        self.horizAngle = AngleWidget(self, "Horizontal Angle")
        self.vertAngle = AngleWidget(self, "Vertical Angle")
        self.vectorX = FreeInputWidget(self, "X", float)
        self.vectorY = FreeInputWidget(self, "Y", float)
        self.vectorZ = FreeInputWidget(self, "Z", float)

        self.vectorX.input.configure(state="disabled")
        self.vectorY.input.configure(state="disabled")
        self.vectorZ.input.configure(state="disabled")

        self.horizAngle.pack()
        self.vertAngle.pack()
        self.vectorX.pack()
        self.vectorY.pack()
        self.vectorZ.pack()

        self.horizAngle.input.inputVar.trace_add("write", self.updateVector)
        self.vertAngle.input.inputVar.trace_add("write", self.updateVector)

    def updateVector(self, *args):
        self.vectorX.setValue(round(cos(self.horizAngle.input.inputVar.get() + pi/2) * sin(self.vertAngle.input.inputVar.get() + pi/2), 4))
        self.vectorY.setValue(round(cos(self.vertAngle.input.inputVar.get() + pi/2), 4) * -1)
        self.vectorZ.setValue(round(sin(self.horizAngle.input.inputVar.get() + pi/2) * sin(self.vertAngle.input.inputVar.get() + pi/2), 4))


class AngleWidget(tk.LabelFrame):
    def __init__(self, parent, labeltext, minimum=-180, maximum=180):
        tk.LabelFrame.__init__(self, parent, text=labeltext)
        self.input = SliderWidget(self, "Angle (degrees)", min=minimum, max=maximum, resolution=1)
        # self.input = FreeInputWidget(self, "Angle (degrees)", float)
        self.radianDisplay = FreeInputWidget(self, "Angle (radians)", float)
        self.radianDisplay.input.configure(state="disabled")
        self.input.inputVar.trace_add("write", self.updateRadianDisplay)

        self.input.pack()
        self.radianDisplay.pack()

    def updateRadianDisplay(self, *args):
        self.radianDisplay.setValue(degreesToRadians(self.input.value()))

    def value(self):
        return self.radianDisplay.value()

    def setValue(self, v):
        self.input.setValue(radiansToDegrees(v))

class SoundWidget(tk.LabelFrame):

    def __init__(self, parent, label, returnNoneOr0, tooltip=""):
        # global classDict


        tk.LabelFrame.__init__(self, parent)

        self.label = tk.Label(self, text=getText(label))
        if tooltip != "":
            self.tooltip = ToolTip(self.label, text=getText(tooltip))
            newText = self.label.cget("text")+"⍰"
            self.label.configure(underline=True, text=newText)

        self.config(labelwidget=self.label)

#        makeLabelClickable()
        self.returnNoneOr0 = returnNoneOr0
        self.unknownValue1 = FreeInputWidget(self, "Unknown Sound Int 1", int, tooltip="Varies between 0, 1, and 2")
#         self.soundChoice = DropDownWidget(self, getText("Sound"), str, {getText("Choose a weapon category"): ""})
#         # disableInput(self.soundChoice)
#         self.categoryChoice = DropDownWidget(self, getText("Weapon Category"), str, {getText("Choose a class"): ""}, command=self.updateSounds)
#         disableInput(self.categoryChoice)
#         self.classChoice = DropDownWidget(self, getText("Class"), str, classDict, command=self.updateCategories)
#         self.noiseTypeChoice = DropDownWidget(self, getText("Sound Type"), str, {getText(key): key for key in sounds}, command=self.updateClasses)#lambda: self.classChoice.config(options=classDict))
#
#         self.soundStringDisplay = FreeInputWidget(self, getText("sound value"), str)
#         disableInput(self.soundStringDisplay)
        self.soundChoice = MultiDropDownWidget(self, "Sound", sounds)
        self.volumeSlider = SliderWidget(self, "Volume", 0, 1, initialValue=1.0)
        self.dampeningSlider = SliderWidget(self, "Dampening?", 0, 2)
        self.unknownValue2 = FreeInputWidget(self, "Unknown Sound float 1", float, initialValue=2, tooltip="Always 2 or 1")
        self.unknownValue3 = FreeInputWidget(self, "Unknown Sound float 2", float, initialValue=25, tooltip="Always 25 or less commonly 20")


        self.enableOrDisableInputs()
        self.soundChoice.valueLabel.inputVar.trace_add("write", self.enableOrDisableInputs)

        self.unknownValue1.pack()
        self.soundChoice.pack()
        self.volumeSlider.pack()
        self.dampeningSlider.pack()
        self.unknownValue2.pack()
        self.unknownValue3.pack()
        # tk.Button(self, command=lambda:print(self.value())).pack()

    def enableOrDisableInputs(self, *args):
        if self.soundChoice.valueLabel.inputVar.get() == "None":
            disableInput(self.unknownValue1)
            disableInput(self.volumeSlider)
            disableInput(self.dampeningSlider)
            disableInput(self.unknownValue2)
            disableInput(self.unknownValue3)
        else:
            enableInput(self.unknownValue1)
            enableInput(self.volumeSlider)
            enableInput(self.dampeningSlider)
            enableInput(self.unknownValue2)
            enableInput(self.unknownValue3)

    def value(self):
        if self.soundChoice.valueLabel.inputVar.get() != "None":
            return [self.unknownValue1.value(),
                    self.soundChoice.value(),
                    self.volumeSlider.value(),
                    self.dampeningSlider.value(),
                    self.unknownValue2.value(),
                    self.unknownValue3.value()
                    ]
        else:
            return self.returnNoneOr0

    def setValue(self, l):
        if not isinstance(l, list):
            self.soundChoice.setValue("None")
        else:
            self.unknownValue1.setValue(l[0])
            self.soundChoice.setValue(l[1])
            self.volumeSlider.setValue(l[2])
            self.dampeningSlider.setValue(l[3])
            self.unknownValue2.setValue(l[4])
            self.unknownValue3.setValue(l[5])


class BasicParamsWidget(tk.LabelFrame):
    def __init__(self, parent):
        accDict = {
            "Perfect": 0,
            "S++": 0.0005,
            "S+": 0.0025,
            "S": 0.005,
            "A+": 0.01,
            "A": 0.015,
            "A-": 0.02,
            "B+": 0.03,
            "B": 0.05,
            "B-": 0.1,
            "C+": 0.15,
            "C": 0.2,
            "C-": 0.25,
            "D": 0.3,
            "E": 0.4,
            "F": 0.5,
            "G": 0.6,
            "I": 0.8,
            "J": 1.0,
            "K": 1.2,
            "L": 1.4
        }
        tk.LabelFrame.__init__(self, parent, text=getText("Basic Parameters"))

        self.currentClass = "Ranger"

        self.col1 = tk.Frame(self)
        self.col2 = tk.Frame(self)
        self.col3 = tk.Frame(self)

        self.ammoCount = StarStructOrFlatWidget(self.col1, "Magazine size", "AmmoCount", int, restrictPositive=True, initialvalue=100)
        self.fireInterval = StarStructOrFlatWidget(self.col1, "Frames between shots", "FireInterval", int, restrictPositive=True, initialvalue=5, inverse=True)
        self.ammoDamage = StarStructOrFlatWidget(self.col1, "Damage", "AmmoDamage", float, initialvalue=100)

        self.falloffFrame = tk.LabelFrame(self.col1, text=getText("Damage Falloff"))
        self.minDamage = SliderWidget(self.falloffFrame, labeltext="Minimum Damage (%)", min=0, max=1, initialValue=1.0)
        self.falloffFactor = FreeInputWidget(self.falloffFrame, "Falloff Factor", float, initialValue=1.0, tooltip="How quickly the damage falls off. 1 is typical, 4 is very harsh.\nNegative values can cause intense damage ramp up.\nThe exact formula is still being determined")

        self.isPenetrate = CheckBoxWidget(self.col1, "Penetrating ammo", 0, 1)
        self.fireCount = StarStructOrFlatWidget(self.col2, "Number of projectiles", "FireCount", int, restrictPositive=True, initialvalue=1)
        self.ammoExplosion = StarStructOrFlatWidget(self.col2, "Explosion radius (m)", "AmmoExplosion", float, restrictPositive=True, initialvalue=0.0)

        self.reloadTime = StarStructOrFlatWidget(self.col2, "Reload time/credits", "ReloadTime", int, p1=1, p2=0.5, inverse=True, restrictPositive=1, initialvalue=60)
        self.reloadInit = SliderWidget(self.col2, "% Reloaded at mission start", 0, 1, resolution=0.01,
                                       initialValue=1.0, tooltip="Guns are normally 100%, Vehicles are normally 50%")
        self.reloadType = DropDownWidget(self.col2, "Reload type", {"Normal": 0, "Over Time": 1, "Credits": 2})

        self.burstFrame = tk.LabelFrame(self.col3, text=getText("Burst settings"))
        self.fireBurstCount = FreeInputWidget(self.burstFrame, "Burst count", int, restrictPositive=True, initialValue=1)
        self.fireBurstInterval = FreeInputWidget(self.burstFrame, "Burst interval", int, initialValue=5, restrictPositive=True)

        self.secondaryFireOptions = {
            "None": 0,
            "Zoom": 1,
            "Activate": 2,
            "Activate and reload": 3,
            "Boost jump (Fencer)": 4,
            "Dash (Fencer)": 5,
            "Shield Reflect (Fencer)": 6
        }

        self.secondaryFireType = DropDownWidget(self.col3, "Secondary Fire Type", self.secondaryFireOptions)
        self.secondaryFireParameter = FreeInputWidget(self.col3, "Zoom Multiplication", float, restrictPositive=True, initialValue=None)

        self.ammoLifetime = FreeInputWidget(self.col3, "Shot lifetime in frames", int, restrictPositive=True, initialValue=60)
        self.ammoSpeed = StarStructOrFlatWidget(self.col3, "Ammo speed", "AmmoSpeed", float, initialvalue=10, tooltip="Meters per frame")

        self.accToolTip = "Spread angle in radians\n"
        for key, value in accDict.items():
            self.accToolTip += f"{key}: {value}\n"
        self.fireAccuracy = StarStructOrFlatWidget(self.col3, "Accuracy", "FireAccuracy", float, p1=3, p2=1,
                                                   restrictPositive=True, tooltip=self.accToolTip, initialvalue=0.05)

        # callback to updateShotsPerSecondVar whenever fireInterval value is changed
        self.shotsPerSecondVar = tk.DoubleVar(self, 0)
        self.shotsPerSecond = FreeInputWidget(self.col1, "Shots per second", float)
        self.shotsPerSecond.input.config(textvariable=self.shotsPerSecondVar, state="disabled")
        self.fireInterval.baseValue.inputVar.trace_add("write", self.updateShotsPerSecondVar)

        # callback to updateRangeVar whenever ammoLifetime or ammoSpeed are changed
        self.range = FreeInputWidget(self.col3, "Range", float)
        self.rangeVar = tk.StringVar(self, 0)
        self.range.input.config(textvariable=self.rangeVar, state="disabled")
        self.ammoLifetime.inputVar.trace_add("write", self.updateRangeVar)
        # self.ammoSpeed.inputVar.trace_add("write", self.updateRangeVar)
        self.ammoSpeed.baseValue.inputVar.trace_add("write", self.updateRangeVar)

        # callback to updateReloadSVar whenever reloadTime is changed
        self.reloadTimeSVar = tk.DoubleVar(self, 0)
        self.reloadTimeSeconds = FreeInputWidget(self.col2, "Reload time in seconds", str)
        self.reloadTimeSeconds.input.config(textvariable=self.reloadTimeSVar, state="disabled")
        self.reloadTime.baseValue.inputVar.trace_add("write", self.updateReloadSVar)

        # callback to updateSecFireParam when SecondaryFireType is changed
        self.secondaryFireType.dropDownDisplayed.trace_add("write", self.updateSecFireParameter)
        self.updateSecFireParameter()




        self.valueDict = {}

        # col1
        self.ammoCount.pack()
        self.fireInterval.pack()
        self.shotsPerSecond.pack()
        self.ammoDamage.pack()
        self.minDamage.pack()
        self.falloffFactor.pack()
        self.falloffFrame.pack()
        self.isPenetrate.pack()
        # col2
        self.fireCount.pack()
        self.ammoExplosion.pack()
        self.reloadTime.pack()
        self.reloadTimeSeconds.pack()
        self.reloadInit.pack()
        self.reloadType.pack()
        # col3
        self.fireBurstCount.pack()
        self.fireBurstInterval.pack()
        self.burstFrame.pack()
        self.secondaryFireType.pack()
        self.secondaryFireParameter.pack()
        self.ammoLifetime.pack()
        self.ammoSpeed.pack()
        self.range.pack()

        self.fireAccuracy.pack()

        self.col1.grid(row=0, column=0, sticky="N")
        self.col2.grid(row=0, column=1, sticky="N")
        self.col3.grid(row=0, column=2, sticky="N")
        self.updateRangeVar()
        self.updateReloadSVar()
        self.updateShotsPerSecondVar()

    def updateSecFireParameter(self, *args):
        if self.secondaryFireType.value() == 1:
            self.secondaryFireParameter.input.config(state="normal", bg="white")
            self.secondaryFireParameter.setValue(2)
        else:
            self.secondaryFireParameter.input.config(state="disabled", bg="blue")
            # self.secondaryFireParameter.setValue(None)

    def updateSecondaryOptionsBasedOnClass(self, c):
        if c == "Fencer":
            self.secondaryFireOptions = {
                "None": 0,
                "Zoom": 1,
                "Activate": 2,
                "Activate and reload": 3,
                "Boost jump (Fencer)": 4,
                "Dash (Fencer)": 5,
                "Shield Reflect (Fencer)": 6
            }
        elif c == "Vehicle Weapon":
            self.secondaryFireOptions = {
                "None": 0
            }
        else:
            self.secondaryFireOptions = {
                "None": 0,
                "Zoom": 1,
                "Activate": 2,
                "Activate and reload": 3
            }
        self.secondaryFireType.replaceOptionMenuNoCmd(self.secondaryFireOptions)

    def updateReloadSVar(self, *args):
        self.reloadTimeSVar.set(self.reloadTime.value()/60.0)


    def updateRangeVar(self, *args):
        self.rangeVar.set(str(self.ammoLifetime.value() * self.ammoSpeed.value()) + "m")


    def updateShotsPerSecondVar(self, *args):
        self.shotsPerSecondVar.set(60 / (self.fireInterval.value() + 1))


    def getValuesDict(self):
        return{
            "AmmoCount": self.ammoCount.value(),
            "FireInterval": self.fireInterval.value(),
            "AmmoDamage": self.ammoDamage.value(),
            "AmmoIsPenetrate": self.isPenetrate.value(),
            "AmmoDamageReduce": [self.minDamage.value(), self.falloffFactor.value()],
            "ReloadTime": self.reloadTime.value(),
            "ReloadInit": self.reloadInit.value(),
            "ReloadType": self.reloadType.value(),
            "SecondaryFire_Type": self.secondaryFireType.value(),
            "SecondaryFire_Parameter": self.secondaryFireParameter.value() if self.secondaryFireType.value() == 1 else None,
            "FireCount": self.fireCount.value(),
            "FireBurstCount": self.fireBurstCount.value(),
            "FireBurstInterval": self.fireBurstInterval.value(),
            "AmmoExplosion": self.ammoExplosion.value(),
            "ReloadTime": self.reloadTime.value(),
            "AmmoLifetime": self.ammoLifetime.value(),
            "AmmoSpeed": self.ammoSpeed.value(),
            "FireAccuracy": self.fireAccuracy.value()
        }
        # return self.valueDict


class MuzzleFlashWidget(tk.LabelFrame):

    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Muzzle Flash"))
        self.muzzleFlashOptions = {
            "None": "",
            "Flash 1": "MuzzleFlash01",
            "Flash 2": "MuzzleFlash02",
            "Smoke": "MuzzleSmoke01",
            "Laser 1": "LaserMuzzleFlash01",
            "Laser 2": "LaserMuzzleFlash02",
            "Laser 3": "LaserMuzzleFlash03",
            "Piercer": "PileBunkerMuzzleFlash01",
            "Vehicle Railgun": "MuzzleFlashRailGun"
        }
        self.muzzleFlashType = DropDownWidget(self, "Muzzle flash type", self.muzzleFlashOptions)
        self.muzzleFlashType.pack()
        self.paramsWidget = None
        self.muzzleFlashType.dropDownDisplayed.trace_add("write", self.replaceMuzzleFlashParamsWidget)

    def replaceMuzzleFlashParamsWidget(self, *args):
        if self.paramsWidget is not None:
            self.paramsWidget.pack_forget()
            self.paramsWidget.destroy()
        if self.muzzleFlashType.value() == "":
            self.paramsWidget = None
        elif self.muzzleFlashType.value() == "MuzzleFlash01":
            self.paramsWidget = self.MuzzleFlash01Widget(self)
            self.paramsWidget.pack()
        elif self.muzzleFlashType.value() == "MuzzleFlash02":
            self.paramsWidget = self.MuzzleFlash02Widget(self)
            self.paramsWidget.pack()
        elif self.muzzleFlashType.value() == "MuzzleSmoke01":
            self.paramsWidget = self.MuzzleSmokeWidget(self)
            self.paramsWidget.pack()
        elif self.muzzleFlashType.value() == "LaserMuzzleFlash01" or self.muzzleFlashType.value() == "LaserMuzzleFlash03":
            self.paramsWidget = self.LaserMuzzleFlash0103Widget(self)
            self.paramsWidget.pack()
        elif self.muzzleFlashType.value() == "LaserMuzzleFlash02":
            self.paramsWidget = self.LaserMuzzleFlash02Widget(self)
            self.paramsWidget.pack()
        elif self.muzzleFlashType.value() == "PileBunkerMuzzleFlash01":
            self.paramsWidget = self.PileBunkerMuzzleFlash01Widget(self)
            self.paramsWidget.pack()
        elif self.muzzleFlashType.value() == "MuzzleFlashRailGun":
            self.paramsWidget = self.MuzzleFlashRailGunWidget(self)
            self.paramsWidget.pack()

    class MuzzleFlash01Widget(tk.LabelFrame):
        def __init__(self, parent):
            tk.LabelFrame.__init__(self, parent, text=getText("Muzzle flash parameters"))
            self.muzzleFlashTexture = 'マズルフラッシュ01.dds'
            self.forwardSparkLength = FreeInputWidget(self, "Fwd spark length", float, initialValue=2)
            self.sparkWidth = FreeInputWidget(self, "Spark width", float, initialValue=0.2)
            self.value3 = FreeInputWidget(self, "Unknown float", float, initialValue=0.125, tooltip="roughly 0~2?")
            self.numberOfSparks = FreeInputWidget(self, "Number of sparks", int, initialValue=2,
                                                  tooltip="varies from 1-6")
            self.sideSparkLength = FreeInputWidget(self, "Side spark length", float, initialValue=1,
                                                   tooltip="hovers around 1~2")
            self.value6 = FreeInputWidget(self, "Unknown float", float, initialValue=0.05,
                                          tooltip="hovers around 0.05~0.07")
            self.value7 = FreeInputWidget(self, "Unknown int", int, initialValue=4, tooltip="always 4 here")
            self.color = ColorWidget(self, "Color")
            self.value9 = FreeInputWidget(self, "Unknown float", float, initialValue=-0.2, tooltip="Usually -0.2 or 0")

            self.forwardSparkLength.pack()
            self.sparkWidth.pack()
            self.value3.pack()
            self.numberOfSparks.pack()
            self.sideSparkLength.pack()
            self.value6.pack()
            self.value7.pack()
            self.color.pack()
            self.value9.pack()

        def value(self):
            return [self.muzzleFlashTexture, self.forwardSparkLength.value(), self.sparkWidth.value(), self.value3.value(), self.numberOfSparks.value(), self.sideSparkLength.value(),
                    self.value6.value(), self.value7.value(), self.color.value(), self.value9.value()]

        def setValue(self, l):
            self.forwardSparkLength.setValue(l[1])
            self.sparkWidth.setValue(l[2])
            self.value3.setValue(l[3])
            self.numberOfSparks.setValue(l[4])
            self.sideSparkLength.setValue(l[5])
            self.value6.setValue(l[6])
            self.value7.setValue(l[7])
            self.color.setValue(l[8])
            self.value9.setValue(l[9])

    class MuzzleFlash02Widget(tk.LabelFrame):
        def __init__(self, parent):
            tk.LabelFrame.__init__(self, parent, text=getText("Muzzle flash parameters"))
            self.muzzleFlashTexture = 'マズルフラッシュパターン.dds'
            self.forwardSparkLength = FreeInputWidget(self, "Fwd spark length", float, initialValue=2)
            self.sparkWidth = FreeInputWidget(self, "Spark width", float, initialValue=0.2)
            self.value3 = FreeInputWidget(self, "Unknown float", float, initialValue=0.125, tooltip="Always 0.125")
            self.numberOfSparks = FreeInputWidget(self, "Number of sparks?", int, initialValue=2)
            self.sideSparkLength = FreeInputWidget(self, "Side spark length", float, initialValue=0.5)
            self.value6 = FreeInputWidget(self, "Spark scale?", float, initialValue=0.09,
                                          tooltip="values around 0.4 or above create violent, ugly sparks")
            self.value7 = FreeInputWidget(self, "Unknown int", int, initialValue=2,
                                          tooltip="1, 2, or 4, No observed change")
            self.color = ColorWidget(self, "Color")
            self.value9 = FreeInputWidget(self, "Unknown float", float, initialValue=-0.2, tooltip="Usually -0.2 or 0")

            self.forwardSparkLength.pack()
            self.sparkWidth.pack()
            self.value3.pack()
            self.numberOfSparks.pack()
            self.sideSparkLength.pack()
            self.value6.pack()
            self.value7.pack()
            self.color.pack()
            self.value9.pack()

        def value(self):
            return [self.muzzleFlashTexture, self.forwardSparkLength.value(), self.sparkWidth.value(), self.value3.value(), self.numberOfSparks.value(), self.sideSparkLength.value(),
                    self.value6.value(), self.value7.value(), self.color.value(), self.value9.value()]

        def setValue(self, l):
            if not isinstance(l, list):
                print(l)
            self.muzzleFlashTexture = l[0]
            self.forwardSparkLength.setValue(l[1])
            self.sparkWidth.setValue(l[2])
            self.value3.setValue(l[3])
            self.numberOfSparks.setValue(l[4])
            self.sideSparkLength.setValue(l[5])
            self.value6.setValue(l[6])
            self.value7.setValue(l[7])
            self.color.setValue(l[8])
            self.value9.setValue(l[9])

    class LaserMuzzleFlash02Widget(tk.LabelFrame):
        def __init__(self, parent):
            tk.LabelFrame.__init__(self, parent, text=getText("Muzzle flash parameters"))
            self.muzzleFlashTexture = 'マズルフラッシュパターン.dds'
            self.forwardSparkLength = FreeInputWidget(self, "Fwd spark length", float, initialValue=2)
            self.sparkWidth = FreeInputWidget(self, "Spark width", float, initialValue=0.2)
            self.value3 = FreeInputWidget(self, "Unknown float", float, initialValue=0.125, tooltip="Always 0.125")
            self.numberOfSparks = FreeInputWidget(self, "Number of sparks", int, initialValue=2)
            self.sideSparkLength = FreeInputWidget(self, "Side spark length", float, initialValue=0.5)
            self.value6 = FreeInputWidget(self, "Unknown float", float, initialValue=0.09)
            self.value7 = FreeInputWidget(self, "Unknown int", int, initialValue=2, tooltip="1, 2, or 4")
            self.color = ColorWidget(self, "Color")
            self.value9 = FreeInputWidget(self, "Unknown float", float, initialValue=-0.2, tooltip="Usually -0.2 or 0")

            self.forwardSparkLength.pack()
            self.sparkWidth.pack()
            self.value3.pack()
            self.numberOfSparks.pack()
            self.sideSparkLength.pack()
            self.value6.pack()
            self.value7.pack()
            self.color.pack()
            self.value9.pack()

        def value(self):
            return [self.muzzleFlashTexture, self.forwardSparkLength.value(), self.sparkWidth.value(), self.value3.value(), self.numberOfSparks.value(), self.sideSparkLength.value(),
                    self.value6.value(), self.value7.value(), self.color.value(), self.value9.value()]

        def setValue(self, l):
            self.forwardSparkLength.setValue(l[1])
            self.sparkWidth.setValue(l[2])
            self.value3.setValue(l[3])
            self.numberOfSparks.setValue(l[4])
            self.sideSparkLength.setValue(l[5])
            self.value6.setValue(l[6])
            self.value7.setValue(l[7])
            self.color.setValue(l[8])
            self.value9.setValue(l[9])

    class LaserMuzzleFlash0103Widget(tk.LabelFrame):
        def __init__(self, parent):
            tk.LabelFrame.__init__(self, parent, text=getText("LaserMuzzleFlash01/03"))
            self.texture = "Particle3_k.dds"
            self.uv1 = FreeInputWidget(self, "Spark size(?)", float, initialValue=1.0)
            self.color = ColorWidget(self, "Muzzle flash color")
            self.uv2 = FreeInputWidget(self, "Spark count(?)", int, tooltip="Probably number of sparks")
            self.uv1.pack()
            self.color.pack()
            self.uv2.pack()

        def value(self):
            return [self.texture, self.uv1.value(), self.color.value(), self.uv2.value()]

        def setValue(self, l):
            self.texture = l[0]
            self.uv1.setValue(l[1])
            self.color.setValue(l[2])
            self.uv2.setValue(l[3])

    class PileBunkerMuzzleFlash01Widget(tk.LabelFrame):
        def __init__(self, parent):
            tk.LabelFrame.__init__(self, parent, text=getText("Blasthole muzzle flash"))
            self.color = ColorWidget(self, "Some color")
            self.color.setValue([4.0, 3.0, 2.0, 1.0])
            self.uv1 = FreeInputWidget(self, "Unknown float", float, initialValue=2.0)
            self.uv2 = FreeInputWidget(self, "Unknown float", float, initialValue=-1.0)
            self.uv3 = FreeInputWidget(self, "Unknown float", float, initialValue=-1.0)
            self.uv4 = FreeInputWidget(self, "Unknown float", float, initialValue=0.0)
            self.uv5 = FreeInputWidget(self, "Unknown int", int, initialValue=15)
            self.uv6 = FreeInputWidget(self, "Unknown float", float, initialValue=0.0)
            self.uv7 = FreeInputWidget(self, "Unknown float", float, initialValue=0.4)
            self.uv8 = FreeInputWidget(self, "Unknown float", float, initialValue=0.15)

            self.color.pack()
            self.uv1.pack()
            self.uv2.pack()
            self.uv3.pack()
            self.uv4.pack()
            self.uv5.pack()
            self.uv6.pack()
            self.uv7.pack()
            self.uv8.pack()

        def value(self):
            return [self.color.value(), [self.uv1.value(), self.uv2.value(), self.uv3.value(), self.uv4.value()],
                    self.uv5.value(), self.uv6.value(), self.uv7.value(), self.uv8.value()]

        def setValue(self, l):
            self.color.setValue(l[0])
            self.uv1.setValue(l[1][0])
            self.uv2.setValue(l[1][1])
            self.uv3.setValue(l[1][2])
            self.uv4.setValue(l[1][3])
            self.uv5.setValue(l[2])
            self.uv6.setValue(l[3])
            self.uv7.setValue(l[4])
            self.uv8.setValue(l[5])

    class MuzzleFlashRailGunWidget(tk.LabelFrame):
        def __init__(self, parent):
            tk.LabelFrame.__init__(self, parent, text="MuzleFlashRailgun")

            self.color = ColorWidget(self, "Color")
            self.uv1 = FreeInputWidget(self, "Unknown float", float)
            self.uv2 = FreeInputWidget(self, "Unknown float", float)
            self.uv3 = FreeInputWidget(self, "Unknown float", float)
            self.uv4 = FreeInputWidget(self, "Unknown float", float)

            self.uv5 = FreeInputWidget(self, "Unknown float", float)
            self.uv6 = FreeInputWidget(self, "Unknown float", float)
            self.uv7 = FreeInputWidget(self, "Unknown float", float)

            self.uv8 = FreeInputWidget(self, "Unknown float", float)
            self.uv9 = FreeInputWidget(self, "Unknown float", float)
            self.uv10 = FreeInputWidget(self, "Unknown float", float)

            self.uv11 = FreeInputWidget(self, "Unknown float", float)
            self.uv12 = FreeInputWidget(self, "Unknown int", int)
            self.uv13 = FreeInputWidget(self, "Unknown int", int)

            self.color.pack()
            self.uv1.pack()
            self.uv2.pack()
            self.uv3.pack()
            self.uv4.pack()
            self.uv5.pack()
            self.uv6.pack()
            self.uv7.pack()
            self.uv8.pack()
            self.uv9.pack()
            self.uv10.pack()
            self.uv11.pack()
            self.uv12.pack()
            self.uv13.pack()

        def value(self):
            return [self.color.value(),
                    [self.uv1.value(), self.uv2.value(), self.uv3.value(), self.uv4.value()],
                    [self.uv5.value(), self.uv6.value(), self.uv7.value()],
                    [self.uv8.value(), self.uv9.value(), self.uv10.value()],
                    self.uv11.value(), self.uv12.value(), self.uv13.value()]

        def setValue(self, l):
            self.color.setValue(l[0])
            self.uv1.setValue(l[1][0])
            self.uv2.setValue(l[1][1])
            self.uv3.setValue(l[1][2])
            self.uv4.setValue(l[1][3])
            self.uv5.setValue(l[2][0])
            self.uv6.setValue(l[2][1])
            self.uv7.setValue(l[2][2])
            self.uv8.setValue(l[3][0])
            self.uv9.setValue(l[3][1])
            self.uv10.setValue(l[3][2])
            self.uv11.setValue(l[5])
            self.uv12.setValue(l[6])
            self.uv13.setValue(l[7])

    class MuzzleSmokeWidget(tk.LabelFrame):
        def __init__(self, parent):
            tk.LabelFrame.__init__(self, parent, text=getText("Muzzle Smoke"))

            self.uv1 = FreeInputWidget(self, "Unknown float", float)
            self.uv2 = FreeInputWidget(self, "Unknown float", float)
            self.color = ColorWidget(self, "Color")
            self.uv3 = FreeInputWidget(self, "Unknown float", float)

            self.uv4 = FreeInputWidget(self, "Unknown float", float)
            self.uv5 = FreeInputWidget(self, "Unknown float", float)
            self.uv6 = FreeInputWidget(self, "Unknown float", float)

            self.uv1.pack()
            self.uv2.pack()
            self.color.pack()
            self.uv3.pack()
            self.uv4.pack()
            self.uv5.pack()
            self.uv6.pack()

        def value(self):
            return [
                self.uv1.value(),
                self.uv2.value(),
                self.color.value(),
                self.uv3.value(),
                [self.uv4.value(), self.uv5.value(), self.uv6.value()]]

        def setValue(self, l):
            self.uv1.setValue(l[0])
            self.uv2.setValue(l[1])
            self.color.setValue(l[2])
            self.uv3.setValue(l[3])
            self.uv4.setValue(l[4][0])
            self.uv5.setValue(l[4][1])
            self.uv6.setValue(l[4][2])


class GunModelWidget(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="Gun Model")
        self.animationData = j.loadDataFromJson("./data/model-based data.json")
        self.sortedModels = j.loadDataFromJson("./data/sorted weapon models.json")
        self.modelOptions = {}
        for key in self.animationData:
            if key != "0":
                self.modelOptions[key.split("/")[2]] = key

        self.currentClass = ""
        self.aimOptions = {"No Class Selected": ""}
        self.reloadOptions = {"No Class Selected": ""}
        self.changeOptions = {"No Class Selected": ""}
        self.baseOptions = {"No Class Selected": ""}
        self.fireAnimationOptions = {"No Class Selected": ""}

        self.weaponIconOptions = {self.animationData[key]['WeaponIcon']:self.animationData[key]['WeaponIcon'] for key in self.animationData}


        self.AimAnimation = DropDownWidget(self, "Aim Animation", self.aimOptions)
        self.BaseAnimation = DropDownWidget(self, "Base Animation", self.baseOptions)
        self.ChangeAnimation = DropDownWidget(self, "Change Animation", self.changeOptions)
        self.ReloadAnimation = DropDownWidget(self, "Reload Animation", self.reloadOptions)
        self.firingAnimation = DropDownWidget(self, "Firing animation", self.fireAnimationOptions)

        self.WeaponIcon = DropDownWidget(self, "Weapon Icon", self.weaponIconOptions)

        self.iconpath = "./data/images/icons/"

        self.WeaponIcon.dropDownDisplayed.trace_add("write", self.updateWeaponIconImg)

        self.iconImg = ImageTk.PhotoImage(Image.open(f"{self.iconpath}{self.WeaponIcon.value().split('/')[3][:-4]}.png"))
        self.iconImgPanel = ttk.Label(self, image=self.iconImg)
        
        self.RABChoice = DropDownWidget(self, "Model choice", self.modelOptions)
        # self.RABChoice = DropDownWidget(self, getText("Model choice"), str, self.modelOptions, command=self.updateOptions)
        self.RABChoice = MultiDropDownWidget(self, "Models", self.sortedModels)

        self.RABChoice.valueLabel.inputVar.trace_add("write", self.updateOptions)

        self.ModelConstraint = DropDownWidget(self, "Model Constraint", {
            str(self.animationData[self.RABChoice.value()]['ModelConstraint']):
                self.animationData[self.RABChoice.value()]['ModelConstraint']})
        # disableInput(self.ModelConstraint)

        self.RABChoice.pack()
        self.AimAnimation.pack()
        self.BaseAnimation.pack()
        self.ChangeAnimation.pack()
        self.ReloadAnimation.pack()
        self.firingAnimation.pack()
        self.WeaponIcon.pack()
        self.iconImgPanel.pack()
        self.ModelConstraint.pack()

        self.updateOptions()
        self.updateWeaponIconImg()
        self.RABChoice.valueLabel.inputVar.trace_add("write", self.getModelRelatedInfo)
    
    def updateWeaponIconImg(self, *args):
        name = self.WeaponIcon.value().split('/')[3][:-4]
        # print(name)
        if name == "":
            name = "none"
        self.iconImg = ImageTk.PhotoImage(Image.open(f"{self.iconpath}{name}.png"))
        self.iconImgPanel.config(image=self.iconImg)

    def updateOptions(self, *args):
        r = self.RABChoice.value()
        if self.animationData[r]['AimAnimation'] in self.aimOptions.values():
            self.AimAnimation.setValue(self.animationData[r]['AimAnimation'])
        if self.animationData[r]['BaseAnimation'] in self.baseOptions.values():
            self.BaseAnimation.setValue(self.animationData[r]['BaseAnimation'])
        if self.animationData[r]['ChangeAnimation'] in self.changeOptions.values():
            self.ChangeAnimation.setValue(self.animationData[r]['ChangeAnimation'])
        if self.animationData[r]['ReloadAnimation'] in self.reloadOptions.values():
            self.ReloadAnimation.setValue(self.animationData[r]['ReloadAnimation'])
        if self.animationData[r]['custom_parameter'][0] in self.fireAnimationOptions.values():
            self.firingAnimation.setValue(self.animationData[r]['custom_parameter'][0])
        if self.animationData[r]['WeaponIcon'] in self.weaponIconOptions.values():
            self.WeaponIcon.setValue(self.animationData[r]['WeaponIcon'])

        self.ModelConstraint.setValue(self.animationData[r]['ModelConstraint'])

    def classChange(self, c, *args):
        self.currentClass = c
        try:
            if c == "Ranger":
                self.aimOptions = {
                    "Normal gun": "aim",
                    "Grenade": "aim_no_ik",
                    "None": "",
                }
                self.baseOptions = {
                    "Assault": "assault",
                    "Waist": "waist",
                    "Sniper": "sniper",
                    "Shoulder": "shoulder",
                    "Throw": "throw",
                    "None": "none"
                }
                self.changeOptions = {
                    "Assault 1": "assault_change1",
                    "Waist 1": "waist_change1",
                    "Sniper 1": "sniper_change1",
                    "Shoulder 1": "shoulder_change1",
                    "Throw 1": "throw_change1",
                    "None": "",
                }
                self.reloadOptions = {
                    "Assault 1": "assault_reload1",
                    "Assault 2": "assault_reload2",
                    "Waist 1": "waist_reload1",
                    "Waist 2": "waist_reload2",
                    "Waist 3": "waist_reload3",
                    "Waist 4": "waist_reload4",
                    "Sniper 1": "sniper_reload1",
                    "Sniper 2": "sniper_reload2",
                    "Shoulder 1": "shoulder_reload1",
                    "Throw 1": "throw_reload1",
                    "None": ""
                }
            elif c == "Wing Diver":
                self.aimOptions = {
                    "Normal gun": "aim",
                    "Grenade": "aim_no_ik",
                    "None": "",
                }
                self.baseOptions = {
                    "Waist": "waist",
                    "Sniper": "sniper",
                    "Throw": "throw",
                    "None": "none",
                    "hand": "hand"
                }
                self.changeOptions = {
                    "Waist 1": "waist_change1",
                    "Waist 2": "waist_change2",
                    "Sniper 1": "sniper_change1",
                    "Throw 1": "throw_change1",
                    "Hand 1": "hand_change1",
                    "None": "",

                }
                self.reloadOptions = {
                    "Waist 1": "waist_reload1",
                    "Sniper 1": "sniper_reload1",
                    "Throw 1": "throw_reload1",
                    "Hand 1": "hand_reload1",
                    "None": ""
                }
            elif c == "Air Raider":
                self.aimOptions = {
                    "Normal gun": "aim",
                    "Grenade/Deployable": "aim_no_ik",
                    "None": "",
                    "hand": "hand"
                }
                self.baseOptions = {
                    "Assault": "assault",
                    "Throw": "throw",
                    "None": "none",
                    "Turret": "bag",
                    "Deployable": "mine"
                }
                self.changeOptions = {
                    "Assault 1": "assault_change1",
                    "Throw 1": "throw_change1",
                    "Hand 1": "hand_change1",
                    "Turret": "bag_change1",
                    "Deployable": "mine_change1"
                }
                self.reloadOptions = {
                    "Assault 1": "assault_reload1",
                    "Assault 2": "assault_reload2",
                    "Hand 1": "hand_reload1",
                    "Throw 1": "throw_reload1",
                    "Turret": "bag_reload1",
                    "Deployable": "mine_reload1"
                }
            elif c == "Fencer":
                self.aimOptions = {
                    "Normal Fencer Gun": "aim_waist",
                    "Melee Weapon": "aim_hammer",
                    "Piercers": "aim_pile",
                    "Shield": "aim_shield",
                    "Shoulder Mounted Aim": "aim_attach",
                    "Shoulder Mounted Fixed": "aim_attach_no_ik",
                    "None": "",
                }
                self.baseOptions = {
                    "None": "none",
                    "Base": "base"
                }
                self.changeOptions = {
                    "Waist 1": "waist_change1",
                    "Melee": "hammer_change1",
                    "Piercer": "pile_change1",
                    "Shield": "shield_change1",
                    "None": ""

                }
                self.reloadOptions = {
                    "Waist 1": "waist_reload1",
                    "Melee": "hammer_reload1",
                    "Piercers": "pile_reload1",
                    "Shield": "shield_reload",
                    "None": ""
                }
            elif c == "Vehicle Weapon":
                self.aimOptions = {
                    "None": "",
                }
                self.baseOptions = {
                    "None": "none",
                    "Waist": "waist"
                }
                self.reloadOptions = {
                    "None": ""
                }
                self.changeOptions = {
                    "None": ""
                }
            else:
                raise ValueError("The updated class provided to the ModelWidget should be one of the 4 classes or 'Vehicle Weapon'")
            self.AimAnimation.replaceOptionMenuNoCmd(self.aimOptions)
            self.BaseAnimation.replaceOptionMenuNoCmd(self.baseOptions);
            self.ReloadAnimation.replaceOptionMenuNoCmd(self.reloadOptions);
            self.ChangeAnimation.replaceOptionMenuNoCmd(self.changeOptions);
        except:
            pass

    def getModelRelatedInfo(self, *args):
        v = self.RABChoice.value()
        return self.animationData[v]

    def getValuesDict(self):
        return {
            "AimAnimation": self.AimAnimation.value(),
            "BaseAnimation": self.BaseAnimation.value(),
            "ChangeAnimation": self.ChangeAnimation.value(),
            "ReloadAnimation": self.ReloadAnimation.value(),
            "WeaponIcon": self.WeaponIcon.value(),
            "animation_model": self.makeAnimation_ModelData(),
            "ModelConstraint": self.animationData[self.RABChoice.value()]["ModelConstraint"],
        }

    def makeAnimation_ModelData(self):
        RAB = self.RABChoice.value()
        if RAB != "none":
            return [[RAB, self.animationData[RAB]['mdb']],
                    self.animationData[RAB]['cas'] if self.animationData[RAB]['cas'] != 0 else 0,
                    self.animationData[RAB]['mab']]
        else: return None


class ShellCaseWidget(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Shell Case Options"))
        self.shellModelOptions = {
            "None": "",
            "Normal": "app:/Weapon/ShellCase401.rab",
            "Large": "app:/Weapon/ShellCase401l.rab",
            "Huge": "app:/Weapon/ShellCase401sp.rab"
        }
        self.shellModel = DropDownWidget(self, "Shell model", self.shellModelOptions)
        self.shellSound = SoundWidget(self, "Shell impact sound", None)
        self.shellModel.dropDownDisplayed.trace_add("write", self.hideOrDisplaySound)
        self.shellModel.pack()
        self.shellSound.pack()


    def value(self):
        return ["ShellCase_RB" if self.shellModel.value() != "" else "",
                self.shellModel.value() if self.shellModel.value() != "" else "",
                self.shellSound.value() if self.shellModel.value() != "" else 0]

    def setValue(self, l):
        # print(l)
        self.shellModel.setValue(l[1])
        if self.shellModel.value() != "":
            self.shellSound.setValue(l[2])
            # self.shellSound.pack()
        # else: self.shellSound.pack_forget()

    def hideOrDisplaySound(self, *args):
        if self.shellModel.value() != "":
            self.shellSound.pack()
        else:
            self.shellSound.pack_forget()


class ColorWidget(tk.LabelFrame):
    def __init__(self, parent, labelText):
        tk.LabelFrame.__init__(self, parent, text=getText(labelText))
        self.red = SliderWidget(self, "Red", min=0, max=4, tooltip="Values above 1 cause a glow effect.")
        self.green = SliderWidget(self, "Green", min=0, max=4, tooltip="Values above 1 cause a glow effect.")
        self.blue = SliderWidget(self, "Blue", min=0, max=4, tooltip="Values above 1 cause a glow effect.")
        self.alpha = SliderWidget(self, "Alpha/Opacity", min=0, max=1)

        self.red.pack()
        self.green.pack()
        self.blue.pack()
        self.alpha.pack()


    def value(self):
        return [self.red.value(), self.green.value(), self.blue.value(), self.alpha.value()]

    def setValue(self, l):
        self.red.setValue(l[0])
        self.green.setValue(l[1])
        self.blue.setValue(l[2])
        self.alpha.setValue(l[3])


settingType = {
    "AmmoCount": 0,
    "FireCount": 4,
    "AmmoDamage": 8,
    "AmmoSpeed": 16,
    "FireAccuracy": 13,
    "ReloadTime": 21,
    "FireInterval": 25,
    "AmmoExplosion": 32,
    "LockOnRange": 36,
    "LockOnTime": 41,
    "EnergyChargeRequire": 45,
    "SwingSpeed": 80,
}


class StarStructOrFlatWidget(tk.Frame):
    # base value
    # type

    # "savedata position"? some int, either 0, 1, 2, or 3
    # max star level (clamped somehow) - either 5, 8, or 10
    # parameter1, either 0.2, 0.5, or 0.8
    # parameter2, either 0.125, 0.5, 0.7, 1, or 1.5
    # result = BASE_VALUE * (p1 * (TARGET_LEVEL / 5)^p2 - p1 + 1)

# implementing star-struct values is on hold until the "savedata position" is figured out more
    def __init__(self, parent, labeltext, varName, varType, p1=0.5, p2=0.5, initialvalue=0, restrictPositive=False, tooltip="", link="", inverse=False):
        tk.Frame.__init__(self, parent)
        self.flatOrStar = CheckBoxWidget(self, "Star-based", "flat", "star", labelwidth=9, tooltip="Whether this value is based off of a star level or not.", link="https://github.com/KCreator/Earth-Defence-Force-Documentation/wiki/Useful-Formulas-and-other-information#star-level-result-formula")
        self.inverse = inverse
        self.showing = False
        self.hideOrShowFrame = tk.Frame(self)
        self.hideButton = tk.Button(self.flatOrStar, text=getText("Hide"), command=self.hideStarStuff, state="disabled")
        self.showButton = tk.Button(self.flatOrStar, text=getText("Show"), command=self.showStarStuff, state="disabled")
        # self.childFrame = tk.Frame()

        self.baseValue = FreeInputWidget(self, labeltext, varType, initialValue=initialvalue, restrictPositive=restrictPositive, tooltip=tooltip, link=link)
        self.settingType = settingType[varName]
        self.saveDataPos = SpinBoxWidget(self, "Save Data Position", 0, 7, tooltip="WARNING! Altering this for an existing weapon may cause unexpected problems with your save!!\nParameters that share save data positions will have their star values synchronized.\nFor example, FireCount and AmmoDamage are usually linked as the number of projectiles and damage both raise at the same time.")
        self.saveDataPos.label.configure(bg="yellow")
        self.maxStarLevel = SpinBoxWidget(self, "Max Star Level", 0, 10, tooltip="WARNING! Altering this for an existing weapon may cause unexpected problems with your save!!\nTypically 8 or 10", initialValue=8)
        self.maxStarLevel.label.configure(bg="yellow")
        self.p1 = SliderWidget(self, "Differential Modifier", 0.01, 1, resolution=0.01, initialValue=p1,
                               tooltip="Large values increase the difference between the 0☆ and max☆ values\nUsually 0.5, sometimes higher.")
        self.p2 = SliderWidget(self, "Scaling Harshness", 0.01, 2, resolution=0.01, initialValue=p2,
                               tooltip="Affects how ☆ scales the stat.\n<1 = diminishing returns\n1 = linear growth\n>1=exponential scaling\nTypically 0.5")



        # self.hideOrShowFrame.pack()
        self.hideButton.grid(row=0, column=2)
        self.showButton.grid(row=0, column=3)

        self.baseValue.pack()
        self.flatOrStar.pack()

        # self.saveDataPos.pack()
        # self.maxStarLevel.pack()
        # self.p1.pack()
        # self.p2.pack()
        self.graph = Graph(self, x_min=0, x_max=self.maxStarLevel.value(), x_tick=1, y_tick=0.5, y_min=0, y_max=1, width=200, height=200)
        # self.graph.pack()

        self.flatOrStar.input.trace_add("write", self.showOrHideStarStuff)

        # update the graph whenever values it depends on are changed
        self.baseValue.inputVar.trace_add("write", self.updateGraph)
        self.maxStarLevel.inputVar.trace_add("write", self.updateGraph)
        self.p1.input.bind("<ButtonRelease-1>", self.updateGraph)
        self.p2.input.bind("<ButtonRelease-1>", self.updateGraph)


    def value(self):
        if self.flatOrStar.value() == "flat":
            return self.baseValue.value()
        elif self.flatOrStar.value() == "star":
            return [self.baseValue.value(),
                    self.settingType,
                    self.saveDataPos.value(),
                    self.maxStarLevel.value(),
                    self.p1.value(),
                    self.p2.value()]

    def updateGraph(self, *args):
        # print("updating graph")
        if self.flatOrStar.value() == "star":
            if self.baseValue.value() != 0:
                self.graph.pack_forget()
                self.graph.destroy()
                if not self.inverse:
                    self.graph = Graph(self, x_min=0,
                                       x_max=self.maxStarLevel.value(),
                                       x_tick=1,
                                       y_min=self.starAdjusted(0),
                                       y_max=self.starAdjusted(self.maxStarLevel.value()),
                                       y_tick=(self.starAdjusted(self.maxStarLevel.value()) - self.starAdjusted(0)) / self.maxStarLevel.value(),
                                       width=200, height=200)
                else:
                    self.graph = Graph(self, x_min=0,
                                       x_max=self.maxStarLevel.value(),
                                       x_tick=1,
                                       y_min=self.starAdjusted(self.maxStarLevel.value()),
                                       y_max=self.starAdjusted(0),
                                       y_tick=(self.starAdjusted(0) - self.starAdjusted(
                                           self.maxStarLevel.value())) / (self.maxStarLevel.value() + 1),
                                       width=200, height=200)
                # print(self.graph.y_tick)
                line = [(starLevel, self.starAdjusted(starLevel)) for starLevel in range(self.maxStarLevel.value()+1)]
                # print(line)
                self.graph.plot_line(line)
                self.graph.pack()
            else:
                self.graph.pack_forget()
                self.graph.destroy()
                self.graph = Graph(self, x_min=0,
                                   x_max=self.maxStarLevel.value(),
                                   x_tick=1,
                                   y_min=-1,
                                   y_max=1,
                                   y_tick=1,
                                   width=200, height=200)
            line = [(i, 0) for i in range(self.maxStarLevel.value()+1)]
            self.graph.plot_line(line)
            self.graph.pack()
        # self.graph2.pack()

    def showOrHideStarStuff(self, *args):
        if self.flatOrStar.value() == "flat":
            self.showing = False
            self.hideButton.configure(state="disabled")
            self.showButton.configure(state="disabled")
            self.hideOrShowFrame.pack_forget()
            self.saveDataPos.pack_forget()
            self.maxStarLevel.pack_forget()
            self.p1.pack_forget()
            self.p2.pack_forget()
            self.graph.pack_forget()
        elif self.flatOrStar.value() == "star":
            self.showing = True
            self.hideButton.configure(state="active")
            self.showButton.configure(state="active")
            self.hideOrShowFrame.pack()
            self.saveDataPos.pack()
            self.maxStarLevel.pack()
            self.p1.pack()
            self.p2.pack()
            # self.graph.pack()
            self.updateGraph()


    def hideStarStuff(self, *args):
        if self.showing is True and self.flatOrStar.value() == "star":
            self.saveDataPos.pack_forget()
            self.maxStarLevel.pack_forget()
            self.p1.pack_forget()
            self.p2.pack_forget()
            self.graph.pack_forget()
            self.showing = False

    def showStarStuff(self, *args):
        if self.showing is False and self.flatOrStar.value() == "star":
            self.saveDataPos.pack()
            self.maxStarLevel.pack()
            self.p1.pack()
            self.p2.pack()
            self.graph.pack()
            self.showing = True


    def starAdjusted(self, starLevel):
        # print(self.baseValue.value() * (self.p1.value() * (starLevel/5)**self.p2.value() - self.p1.value() + 1))
        # print(starLevel, (self.p1.value() * (starLevel/5)**self.p2.value() - self.p1.value() + 1))
        p1 = self.p1.value()
        if self.inverse:
            p1 = p1 * -1
        # print(starLevel, (-self.p1.value() * (starLevel / 5) ** self.p2.value() - self.p1.value() + 1))
        return self.baseValue.value() * (p1 * (starLevel / 5) ** self.p2.value() - p1 + 1)
        #
        # if not self.inverse:
        #     return self.baseValue.value() * (self.p1.value() * (starLevel / 5) ** self.p2.value() - self.p1.value() + 1)
        # else:
        #     return self.baseValue.value() * (-self.p1.value() * (starLevel/5)**self.p2.value() - self.p1.value() + 1)

