from widgets.EDFWidgets import *
from widgets.vehicleSummon import *
import math

# e = j.loadDataFromJson("./data/alleasy.json")
# u = d.uniqueDataByKey("AmmoClass", ["Ammo_CustomParameter"], e)
ammoCust = j.loadDataFromJson("./data/ammoCust.json")


def ammoCustWidgetFromAmmoClass(parent, ammoClass, isSubProjectile):
    if ammoClass == "SolidBullet01":
        return SolidBullet01(parent, isSubProjectile)
    elif ammoClass == "AcidBullet01":
        return AcidBullet01(parent)
    elif ammoClass == "BarrierBullet01":
        return BarrierBullet01(parent)
    elif ammoClass == "BombBullet01":
        return BombBullet01(parent)
    elif ammoClass == "BombBullet02":
        return BombBullet02(parent)
    elif ammoClass == "ClusterBullet01":
        return ClusterBullet01(parent)
    # elif ammoClass == "DecoyBullet01": #     return DecoyBullet01(parent)
    elif ammoClass == "FlameBullet02":
        return FlameBullet02(parent)
    elif ammoClass == "GrenadeBullet01":
        return GrenadeBullet01(parent)
    elif ammoClass == "HomingLaserBullet01":
        return HomingLaserBullet01(parent)
    elif ammoClass == "LaserBullet01":
        return LaserBullet01(parent)
    elif ammoClass == "LaserBullet02":
        return LaserBullet02(parent)
    elif ammoClass == "LaserBullet03":
        return LaserBullet03(parent)
    elif ammoClass == "LightningBullet01":
        return LightningBullet01(parent)
    elif ammoClass == "MissileBullet01":
        return MissileBullet01(parent, isSubProjectile)
    elif ammoClass == "MissileBullet02":
        return MissileBullet02(parent, isSubProjectile)
    elif ammoClass == "NapalmBullet01":
        return NapalmBullet01(parent, isSubProjectile)
    elif ammoClass == "NeedleBullet01":
        return NeedleBullet01(parent)
    elif ammoClass == "PileBunkerBullet01":
        return PileBunkerBullet01(parent, isSubProjectile)
    elif ammoClass == "PlasmaBullet01":
        return PlasmaBullet01(parent)
    elif ammoClass == "PulseBullet01":
        return PulseBullet01(parent)
    elif ammoClass == "RocketBullet01":
        return RocketBullet01(parent)
    elif ammoClass == "SentryGunBullet01":
        return SentryGunBullet01(parent, isSubProjectile)
    elif ammoClass == "ShieldBashBullet01":
        return ShieldBashBullet01(parent)
    elif ammoClass == "ShockWaveBullet01":
        return ShockWaveBullet01(parent)
    elif ammoClass == "SmokeCandleBullet01":
        return SmokeCandleBullet01(parent)
    elif ammoClass == "SmokeCandleBullet02":
        return SmokeCandleBullet02(parent)
    elif ammoClass == "SolidBullet01Rail":
        return SolidBullet01Rail(parent)
    elif ammoClass == "SolidExpBullet01":
        return SolidExpBullet01(parent)
    elif ammoClass == "SolidPelletBullet01":
        return SolidPelletBullet01(parent)
    elif ammoClass == "SpiderStringBullet02":
        return SpiderStringBullet02(parent)
    elif ammoClass == "SupportUnitBullet01":
        return SupportUnitBullet01(parent)
    elif ammoClass == "TargetMarkerBullet01":
        return TargetMarkerBullet01(parent)


subProjectileAmmoOptions = {
    "SolidBullet01": "SolidBullet01",
    # "None": "None",
    "AcidBullet01": "AcidBullet01",
    "BarrierBullet01": "BarrierBullet01",
    "BombBullet01": "BombBullet01",
    "BombBullet02": "BombBullet02",
    "ClusterBullet01": "ClusterBullet01",
    # "DecoyBullet01": "DecoyBullet01",
    "FlameBullet02": "FlameBullet02",
    "GrenadeBullet01": "GrenadeBullet01",
    "HomingLaserBullet01": "HomingLaserBullet01",
    "LaserBullet01": "LaserBullet01",
    "LaserBullet02": "LaserBullet02",
    "LaserBullet03": "LaserBullet03",
    "LightningBullet01": "LightningBullet01",
    "MissileBullet01": "MissileBullet01",
    "MissileBullet02": "MissileBullet02",
    "NapalmBullet01": "NapalmBullet01",
    "NeedleBullet01": "NeedleBullet01",
    "PileBunkerBullet01": "PileBunkerBullet01",
    "PlasmaBullet01": "PlasmaBullet01",
    "PulseBullet01": "PulseBullet01",
    "RocketBullet01": "RocketBullet01",
    "SentryGunBullet01": "SentryGunBullet01",
    "ShieldBashBullet01": "ShieldBashBullet01",
    "ShockWaveBullet01": "ShockWaveBullet01",
    "SmokeCandleBullet01": "SmokeCandleBullet01",
    "SmokeCandleBullet02": "SmokeCandleBullet02",
    "SolidBullet01Rail": "SolidBullet01Rail",
    "SolidExpBullet01": "SolidExpBullet01",
    "SolidPelletBullet01": "SolidPelletBullet01",
    "SpiderStringBullet02": "SpiderStringBullet02",
    "SupportUnitBullet01": "SupportUnitBullet01",
    "TargetMarkerBullet01": "TargetMarkerBullet01",
}


class AcidBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("AcidBullet01"))
        self.v1 = FreeInputWidget(self, "Unknown float", float, tooltip="-0.03 or -0.004", initialValue=-0.004)

        self.v1.pack()

    def value(self):
        return [self.v1.value()]

    def setValue(self, v):
        self.v1.setValue(v[0])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class BarrierBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("BarrierBullet01"))
        self.v1 = FreeInputWidget(self, "Unknown float", float)
        self.v2 = FreeInputWidget(self, "Unknown float", float)
        self.v3 = FreeInputWidget(self, "Unknown float", float)
        self.group1 = tk.LabelFrame(self, text=getText("Struct 1"))
        self.v4 = FreeInputWidget(self.group1, "Unknown float", float)
        self.v5 = FreeInputWidget(self.group1, "Unknown float", float)
        self.v6 = FreeInputWidget(self.group1, "Unknown float", float)
        self.group2 = tk.LabelFrame(self, text=getText("Struct 2"))
        self.v7 = FreeInputWidget(self.group2, "Unknown float", float)
        self.v8 = FreeInputWidget(self.group2, "Unknown float", float)
        self.v9 = FreeInputWidget(self.group2, "Unknown float", float)

        self.v1.pack()
        self.v2.pack()
        self.v3.pack()
        self.group1.pack()
        self.v4.pack()
        self.v5.pack()
        self.v6.pack()
        self.group2.pack()
        self.v7.pack()
        self.v8.pack()
        self.v9.pack()

    def value(self):
        return [self.v1.value(), self.v2.value(), self.v3.value(),
                [self.v4.value(), self.v5.value(), self.v6.value()],
                [self.v7.value(), self.v8.value(), self.v9.value()]]

    def setValue(self, l):
        self.v1.setValue(l[0])
        self.v2.setValue(l[1])
        self.v3.setValue(l[2])
        self.v4.setValue(l[3][0])
        self.v5.setValue(l[3][1])
        self.v6.setValue(l[3][2])
        self.v7.setValue(l[4][0])
        self.v8.setValue(l[4][1])
        self.v9.setValue(l[4][2])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class BombBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("BombBullet01"))
        self.bombOptions = {
            "C4/Mine": 0,
            "Patroller": 1,
            "Assault beetle": 2,
            "Roomba bomb (strange behavior)": 3
        }

        self.explosionOptions = {
            "Standard": 0,
            "Splendor": 1,
            "Sniper": 2
        }
        self.bombSoundOptions = {
            # [impact, armed, enemy detected, bounce sound]
            "Small limpet": ['武器リモート爆弾小着弾', 0, 0, 0],
            "Big limpet": ['武器リモート爆弾大着弾', 0, 0, 0],
            "Flechette": ['武器フレシェット着弾', 0, 0, 0],
            "Bomb a": ['武器Ｃ系爆弾接地Ａ', '武器起動可能', 0, 0],
            "Bomb b": ['武器Ｃ系爆弾接地Ｂ', '武器起動可能', 0, 0],
            "Bomb c": ['武器Ｃ系爆弾接地Ｃ', '武器起動可能', 0, 0],
            "Mine a": ['武器Ｃ系爆弾接地Ａ', '武器起動可能', '敵探知', 0],
            "Roomba": ['ルン爆弾ＧＯ', '武器起動可能', 0, 'ルン爆弾反射'],
            "Heavy roomba": ['ルン爆弾ＧＯ重い', '武器起動可能', 0, 'ルン爆弾反射重い'],
            "Beetle": ['むしむしボンバー張り付き', '武器起動可能', 0, 'むしむしボンバー跳ねる']
        }

        self.bombType = DropDownWidget(self, "Bomb type", self.bombOptions)
        self.isDetector = CheckBoxWidget(self, "Is detector", 0, 1)
        self.unknown1 = FreeInputWidget(self, "Unknown float", float, tooltip="Always 0.0", initialValue=0.0)
        self.primerDelay = FreeInputWidget(self, "Priming delay", int, restrictPositive=True,
                                           tooltip="In frames. Usually 0 for limpet, 30 for detectors")
        self.unknown2 = FreeInputWidget(self, "Unknown int", int, tooltip="Ranges from 0-5?")

        self.LEDFrame = tk.LabelFrame(self, text=getText("LED Position?"))
        self.LEDX = FreeInputWidget(self.LEDFrame, "X?", float, initialValue=0.0)
        self.LEDY = FreeInputWidget(self.LEDFrame, "Y?", float, initialValue=0.5)
        self.LEDZ = FreeInputWidget(self.LEDFrame, "Z?", float, initialValue=0.0)

        self.explosionType = DropDownWidget(self, "Explosion type", self.explosionOptions)
        self.explosionType.dropDownDisplayed.trace_add("write", self.enableOrDisableSplendor)

        self.splendorFrame = tk.LabelFrame(self, text=getText("Splendor configuration"))
        # self.hSpread = SliderWidget(self.splendorFrame, "Horizontal spread", 0, 1)
        # self.vSpread = SliderWidget(self.splendorFrame, "Vertical spread", 0, 1)
        self.hSpread = AngleWidget(self.splendorFrame, "Horizontal spread")
        self.vSpread = AngleWidget(self.splendorFrame, "Vertical spread")
        self.vAngle = AngleWidget(self.splendorFrame, "Vertical angle")

        self.flechetteCount = FreeInputWidget(self.splendorFrame, "Flechette count", int, restrictPositive=True)
        self.flechetteLifetime = FreeInputWidget(self.splendorFrame, "Flechette lifetime", int, restrictPositive=True)
        self.flechetteSize = FreeInputWidget(self.splendorFrame, "Flechette size", float, restrictPositive=True,
                                             initialValue=3.0)
        self.unknown3 = FreeInputWidget(self.splendorFrame, "Unknown int", int, tooltip="Always 1?", initialValue=1)

        self.armingSound = DropDownWidget(self, "Arming sound", self.bombSoundOptions)

        self.bombType.pack()
        self.isDetector.pack()
        self.unknown1.pack()
        self.primerDelay.pack()
        self.unknown2.pack()
        self.LEDFrame.pack()
        self.LEDX.pack()
        self.LEDY.pack()
        self.LEDZ.pack()
        self.explosionType.pack()
        self.splendorFrame.pack()
        self.hSpread.pack()
        self.vSpread.pack()
        self.vAngle.pack()
        self.flechetteCount.pack()
        self.flechetteLifetime.pack()
        self.flechetteSize.pack()
        self.unknown3.pack()
        self.armingSound.pack()

        self.enableOrDisableSplendor()

    def value(self):
        v = [self.bombType.value(), self.isDetector.value(), self.unknown1.value(), self.primerDelay.value(),
             self.unknown2.value(),
             [self.LEDX.value(), self.LEDY.value(), self.LEDZ.value()],
             self.explosionType.value()]
        if self.explosionType.value() == 1:
            v.append([[self.hSpread.value(),
                       self.vSpread.value(),
                       self.vAngle.value()],
                      self.flechetteCount.value(),
                      self.flechetteLifetime.value(),
                      self.flechetteSize.value(), [self.unknown3.value()]])
        else:
            v.append(None)

        v.append(self.armingSound.value())
        return v

    def setValue(self, l):
        self.bombType.setValue(l[0])
        self.isDetector.setValue(l[1])
        self.unknown1.setValue(l[2])
        self.primerDelay.setValue(l[3])
        self.unknown2.setValue(l[4])
        self.LEDX.setValue(l[5][0])
        self.LEDY.setValue(l[5][1])
        self.LEDZ.setValue(l[5][2])
        self.explosionType.setValue(l[6])
        if l[5] == 1:
            self.hSpread.setValue(l[7][0][0])
            self.vSpread.setValue(l[7][0][1])
            self.vAngle.setValue(l[7][0][2])
            self.flechetteCount.setValue(l[7][1])
            self.flechetteLifetime.setValue(l[7][2])
            self.flechetteSize.setValue(l[7][3])
            self.unknown3.setValue(l[7][4][0])
            self.enableSplendor()
        else:
            self.disableSplendor()
        self.armingSound.setValue(l[8])

    def enableOrDisableSplendor(self, *args):
        if self.explosionType.value() == 1:
            self.enableSplendor()
        else:
            self.disableSplendor()

    def enableSplendor(self):
        enableInput(self.hSpread.input)
        enableInput(self.vSpread.input)
        enableInput(self.vAngle.input)
        enableInput(self.flechetteCount)
        enableInput(self.flechetteLifetime)
        enableInput(self.flechetteSize)
        enableInput(self.unknown3)

    def disableSplendor(self):
        disableInput(self.hSpread.input)
        disableInput(self.vSpread.input)
        disableInput(self.vAngle.input)
        disableInput(self.flechetteCount)
        disableInput(self.flechetteLifetime)
        disableInput(self.flechetteSize)
        disableInput(self.unknown3)

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class BombBullet02(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("BombBullet02"))
        self.bombOptions = {
            "Limpet bomb": 0,
            "Patroller": 1,
            "Assault beetle": 2,
            "Roomba bomb (strange behavior)": 3
        }

        self.explosionOptions = {
            "Standard": 0,
            "Splendor": 1,
            "Sniper": 2
        }
        self.bombSoundOptions = {
            # [impact, armed, enemy detected, bounce sound]
            "Small limpet": ['武器リモート爆弾小着弾', 0, 0, 0],
            "Big limpet": ['武器リモート爆弾大着弾', 0, 0, 0],
            "Flechette": ['武器フレシェット着弾', 0, 0, 0],
            "Bomb a": ['武器Ｃ系爆弾接地Ａ', '武器起動可能', 0, 0],
            "Bomb b": ['武器Ｃ系爆弾接地Ｂ', '武器起動可能', 0, 0],
            "Bomb c": ['武器Ｃ系爆弾接地Ｃ', '武器起動可能', 0, 0],
            "Mine a": ['武器Ｃ系爆弾接地Ａ', '武器起動可能', '敵探知', 0],
            "Roomba": ['ルン爆弾ＧＯ', '武器起動可能', 0, 'ルン爆弾反射'],
            "Heavy roomba": ['ルン爆弾ＧＯ重い', '武器起動可能', 0, 'ルン爆弾反射重い'],
            "Beetle": ['むしむしボンバー張り付き', '武器起動可能', 0, 'むしむしボンバー跳ねる']
        }

        self.bombType = DropDownWidget(self, "Bomb type", self.bombOptions)
        self.isDetector = CheckBoxWidget(self, "Is detector", 0, 1)
        self.unknown1 = FreeInputWidget(self, "Unknown float", float, tooltip="Always 0.0", initialValue=0.0)
        self.primerDelay = FreeInputWidget(self, "Priming delay", int, restrictPositive=True,
                                           tooltip="In frames. Usually 0 for limpet, 30 for detectors")
        self.unknown2 = FreeInputWidget(self, "Unknown int", int, tooltip="Ranges from 0-5?")

        self.LEDFrame = tk.LabelFrame(self, text=getText("LED Position?"))
        self.LEDX = FreeInputWidget(self.LEDFrame, "X?", float, initialValue=0.0)
        self.LEDY = FreeInputWidget(self.LEDFrame, "Y?", float, initialValue=0.5)
        self.LEDZ = FreeInputWidget(self.LEDFrame, "Z?", float, initialValue=0.0)

        self.explosionType = DropDownWidget(self, "Explosion type", self.explosionOptions)
        self.explosionType.dropDownDisplayed.trace_add("write", self.enableOrDisableSplendor)

        self.splendorFrame = tk.LabelFrame(self, text=getText("Splendor configuration"))
        # self.hSpread = SliderWidget(self.splendorFrame, "Horizontal spread", 0, 1)
        # self.vSpread = SliderWidget(self.splendorFrame, "Vertical spread", 0, 1)
        self.hSpread = AngleWidget(self.splendorFrame, "Horizontal spread")
        self.vSpread = AngleWidget(self.splendorFrame, "Vertical spread")
        self.vAngle = AngleWidget(self.splendorFrame, "Vertical angle")

        self.flechetteCount = FreeInputWidget(self.splendorFrame, "Flechette count", int, restrictPositive=True)
        self.flechetteLifetime = FreeInputWidget(self.splendorFrame, "Flechette lifetime", int, restrictPositive=True)
        self.flechetteSpeed = FreeInputWidget(self.splendorFrame, "Flechette speed", float, restrictPositive=True)
        self.flechetteSize = FreeInputWidget(self.splendorFrame, "Flechette size", float, restrictPositive=True,
                                             initialValue=3.0)
        self.unknown3 = FreeInputWidget(self.splendorFrame, "Unknown int", int, tooltip="Always 1?", initialValue=1)

        self.armingSound = DropDownWidget(self, "Arming sound", self.bombSoundOptions)

        self.bombType.pack()
        self.isDetector.pack()
        self.unknown1.pack()
        self.primerDelay.pack()
        self.LEDFrame.pack()
        self.LEDX.pack()
        self.LEDY.pack()
        self.LEDZ.pack()
        self.explosionType.pack()
        self.splendorFrame.pack()
        self.hSpread.pack()
        self.vSpread.pack()
        self.vAngle.pack()
        self.flechetteCount.pack()
        self.flechetteLifetime.pack()
        self.flechetteSpeed.pack()
        self.flechetteSize.pack()
        self.unknown3.pack()
        self.armingSound.pack()
        self.enableOrDisableSplendor()

    def value(self):
        v = [self.bombType.value(), self.isDetector.value(), self.unknown1.value(), self.primerDelay.value(),
             self.unknown2.value(),
             [self.LEDX.value(), self.LEDY.value(), self.LEDZ.value()],
             self.explosionType.value()]
        if self.explosionType.value() == 1:
            v.append([[self.hSpread.value(),
                       self.vSpread.value(),
                       self.vAngle.value()],
                      self.flechetteCount.value(),
                      self.flechetteLifetime.value(),
                      self.flechetteSpeed.value(),
                      self.flechetteSize.value(),
                      [self.unknown3.value()]])
        else:
            v.append(None)

        v.append(self.armingSound.value())
        return v

    def setValue(self, l):
        print(len(l))
        self.bombType.setValue(l[0])
        self.isDetector.setValue(l[1])
        self.unknown1.setValue(l[2])
        self.primerDelay.setValue(l[3])
        self.unknown2.setValue(l[4])
        self.LEDX.setValue(l[5][0])
        self.LEDY.setValue(l[5][1])
        self.LEDZ.setValue(l[5][2])
        self.explosionType.setValue(l[6])
        if l[6] == 1:
            self.hSpread.setValue(l[7][0][0])
            self.vSpread.setValue(l[7][0][1])
            self.vAngle.setValue(l[7][0][2])
            self.flechetteCount.setValue(l[7][1])
            self.flechetteLifetime.setValue(l[7][2])
            self.flechetteSpeed.setValue(l[7][3])
            self.flechetteSize.setValue(l[7][4])
            self.unknown3.setValue(l[7][5][0])
            self.enableSplendor()
        else:
            self.disableSplendor()

        self.armingSound.setValue(l[8])

    def enableOrDisableSplendor(self, *args):
        if self.explosionType.value() == 1:
            self.enableSplendor()
        else:
            self.disableSplendor()

    def enableSplendor(self):
        enableInput(self.hSpread.input)
        enableInput(self.vSpread.input)
        enableInput(self.vAngle.input)
        enableInput(self.flechetteCount)
        enableInput(self.flechetteLifetime)
        enableInput(self.flechetteSize)
        enableInput(self.unknown3)

    def disableSplendor(self):
        disableInput(self.hSpread.input)
        disableInput(self.vSpread.input)
        disableInput(self.vAngle.input)
        disableInput(self.flechetteCount)
        disableInput(self.flechetteLifetime)
        disableInput(self.flechetteSize)
        disableInput(self.unknown3)

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class ClusterBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("ClusterBullet01"))

        self.clusterFrame = tk.Frame(self)

        self.momentumConservation = SliderWidget(self.clusterFrame, "Momentum conservation", 0, 1,
                                                 tooltip="1 = maintains full speed for its lifetime, lower = stops faster")
        self.projectileSpread = FreeInputWidget(self.clusterFrame, "Projectile spread?", float)
        self.projectileAccuracy = FreeInputWidget(self.clusterFrame, "Sub-projectile", float)
        self.directionOptions = {
            "Down": 0,
            "Up": 1,
            "Forward": 2,
            "Forward and up": 3,
            "Right": 4,
            "Left??": 5
        }
        self.projectileDirection = DropDownWidget(self.clusterFrame, "Projectile direction", self.directionOptions)
        self.homingFrame = tk.LabelFrame(self.clusterFrame, text=getText("Homing options"))
        self.homingEnabled = CheckBoxWidget(self.homingFrame, "Homing enabled", 0, 1)
        self.homingLockRadius = FreeInputWidget(self.homingFrame, "Homing lock radius", float, restrictPositive=True,
                                                initialValue=100.0)

        self.subProjectileWidget = SubProjectile(self)

        self.clusterFrame.grid(row=0, column=0, sticky="N")

        self.momentumConservation.pack()
        self.projectileSpread.pack()
        self.projectileAccuracy.pack()
        self.projectileDirection.pack()
        self.homingFrame.pack()
        self.homingEnabled.pack()
        self.homingLockRadius.pack()
        self.subProjectileWidget.grid(row=0, column=1, sticky="N")

    def value(self):
        v = [self.momentumConservation.value(),
             self.projectileSpread.value(),
             self.projectileAccuracy.value(),
             self.projectileDirection.value()]
        if self.homingEnabled.value() == 1:
            v.append([self.homingEnabled.value(), self.homingLockRadius.value()])
        else:
            v.append(0)
        v.append(self.subProjectileWidget.value())
        return v

    def setValue(self, l):
        self.momentumConservation.setValue(l[0])
        self.projectileSpread.setValue(l[1])
        self.projectileAccuracy.setValue(l[2])
        self.projectileDirection.setValue(l[3])
        if l[4] != 0:
            self.homingEnabled.setValue(l[4][0])
            self.homingLockRadius.setValue(l[4][1])
        else:
            self.homingEnabled.setValue(0)
            self.homingLockRadius.setValue(0)
        self.subProjectileWidget.setValue(l[5])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class SubProjectile(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Sub-Projectile"))
        self.parent = parent

        self.col1 = tk.Frame(self)

        self.unknownFrame1 = tk.LabelFrame(self.col1, text=getText("Unknown struct"))
        self.unknown1 = FreeInputWidget(self.unknownFrame1, "Unknown float", float)
        self.unknown2 = FreeInputWidget(self.unknownFrame1, "Unknown float", float)
        self.unknownFrame2 = tk.LabelFrame(self.col1, text=getText("Unknown struct"))
        self.unknown3 = FreeInputWidget(self.unknownFrame2, "Unknown float", float)
        self.unknown4 = FreeInputWidget(self.unknownFrame2, "Unknown float", float)
        self.projectileCount = FreeInputWidget(self.col1, "Sub-projectile count", int, restrictPositive=True,
                                               initialValue=20)
        self.projectileInterval = FreeInputWidget(self.col1, "Time between projectiles", int, restrictPositive=True,
                                                  initialValue=2)

        self.ammoSpeed = FreeInputWidget(self.col1, "Ammo speed", float)
        self.ammoGravity = FreeInputWidget(self.col1, "Ammo gravity factor", float)
        self.ammoScale = FreeInputWidget(self.col1, "Ammo scale", float)
        self.unknown5 = FreeInputWidget(self.col1, "Unknown float", float, tooltip="Maybe ammoHitSizeAdjust")
        self.explosionRadius = FreeInputWidget(self.col1, "Explosion radius", float)
        self.ammoLifetime = FreeInputWidget(self.col1, "Ammo lifetime", int)
        self.unknown6 = FreeInputWidget(self.col1, "Unknown int", int)
        self.unknown7 = FreeInputWidget(self.col1, "Unknown int", int)
        self.unknown8 = FreeInputWidget(self.col1, "Unknown int", int)
        self.ammoColor = ColorWidget(self.col1, "Ammo color")
        self.allModels = allModels
        self.ammoModel = MultiDropDownWidget(self.col1, "Ammo model", allModels)

        self.col2 = tk.Frame(self)

        self.ammoClass = DropDownWidget(self.col2, "Sub-projectile ammo type", subProjectileAmmoOptions)
        self.ammoClass.dropDownDisplayed.trace_add("write", self.updateAmmoCustWidget)

        self.sound1 = SoundWidget(self.col2, "Firing sound?", returnNoneOr0=0)
        self.sound2 = SoundWidget(self.col2, "Impact sound?", returnNoneOr0=0)

        self.customParamWidget = SolidBullet01(self, True)

        self.updateAmmoCustWidget()

        self.col1.grid(row=0, column=0, sticky="N")
        self.unknownFrame1.pack()
        self.unknown1.pack()
        self.unknown2.pack()
        self.unknownFrame2.pack()
        self.unknown3.pack()
        self.unknown4.pack()
        self.projectileCount.pack()
        self.projectileInterval.pack()
        self.ammoSpeed.pack()
        self.ammoGravity.pack()
        self.ammoScale.pack()
        self.unknown5.pack()
        self.explosionRadius.pack()
        self.ammoLifetime.pack()
        self.unknown6.pack()
        self.unknown7.pack()
        self.unknown8.pack()
        self.ammoColor.pack()
        self.ammoModel.pack()

        self.col2.grid(row=0, column=1, sticky="N")
        self.ammoClass.pack()
        self.sound1.pack()
        self.sound2.pack()

        self.customParamWidget.grid(row=0, column=2, sticky="N")

    def value(self):
        return [
            [self.unknown1.value(),
             self.unknown2.value()],
            [self.unknown3.value(),
             self.unknown4.value()],
            self.projectileCount.value(),
            self.projectileInterval.value(),
            self.ammoClass.value(),
            self.ammoSpeed.value(),
            self.ammoGravity.value(),
            self.ammoScale.value(),
            self.unknown5.value(),
            self.explosionRadius.value(),
            self.ammoLifetime.value(),
            self.unknown6.value(),
            self.ammoColor.value(),
            self.customParamWidget.value(),
            self.ammoModel.value(),
            self.unknown7.value(),
            self.unknown8.value(),
            self.sound1.value(),
            self.sound2.value()]

    def setValue(self, l):
        self.unknown1.setValue(l[0][0])
        self.unknown2.setValue(l[0][1])
        self.unknown3.setValue(l[1][0])
        self.unknown4.setValue(l[1][1])
        self.projectileCount.setValue(l[2])
        self.projectileInterval.setValue(l[3])
        self.ammoClass.setValue(l[4])
        self.ammoSpeed.setValue(l[5])
        self.ammoGravity.setValue(l[6])
        self.ammoScale.setValue(l[7])
        self.unknown5.setValue(l[8])
        self.explosionRadius.setValue(l[9])
        self.ammoLifetime.setValue(l[10])
        self.unknown6.setValue(l[11])
        self.ammoColor.setValue(l[12])
        self.customParamWidget.setValue(l[13])
        self.ammoModel.setValue(l[14])
        self.unknown7.setValue(l[15])
        self.unknown8.setValue(l[16])
        self.sound1.setValue(l[17])
        self.sound2.setValue(l[18])

    def updateAmmoCustWidget(self, *args):
        # print(self.ammoClass.value())
        if self.customParamWidget is not None:
            self.customParamWidget.grid_forget()
            self.customParamWidget.destroy()
            self.customParamWidget = None
        self.customParamWidget = ammoCustWidgetFromAmmoClass(self, self.ammoClass.value(), True)
        if self.customParamWidget is not None:
            self.customParamWidget.grid(row=0, column=2, sticky="N")

    # def test(self):
    #     testDict =
    #     testValues = [eval(key) for key in testDict.keys()]
    #     for v in testValues:
    #         self.setValue(v)
    #         if v != self.value():
    #             print(v)
    #             print(self.value())
    #             pass
    #         print(f"{v} == {self.value()} ? {v == self.value()}")


# class DecoyBullet01(tk.LabelFrame):
#     def __init__(self, parent):
#         tk.LabelFrame.__init__(self, parent, text=getText("DecoyBullet01"))
#
#     def value(self):
#         pass
#
#     def setValue(self):
#         pass


class FlameBullet02(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("FlameBullet02"))

        self.flameOptions = {
            "Regular flame": 0,
            "Dunno": 1,
            "Reverser stream": 2
        }
        self.flameType = DropDownWidget(self, "Flame type", self.flameOptions)
        self.unknown1 = FreeInputWidget(self, "Unknown float", float)
        self.unknown2 = FreeInputWidget(self, "Unknown float", float)
        self.unknown3 = FreeInputWidget(self, "Unknown int", int)
        self.colorFrame = tk.LabelFrame(self, text=getText("Color modification over time"))
        self.redChange = FreeInputWidget(self.colorFrame, "Red change", float)
        self.blueChange = FreeInputWidget(self.colorFrame, "Blue change", float)
        self.greenChange = FreeInputWidget(self.colorFrame, "Green change", float)
        self.alphaChange = FreeInputWidget(self.colorFrame, "Alpha change, float", float)

        self.flameType.pack()
        self.unknown1.pack()
        self.unknown2.pack()
        self.unknown3.pack()
        self.colorFrame.pack()
        self.redChange.pack()
        self.blueChange.pack()
        self.greenChange.pack()
        self.alphaChange.pack()

    def value(self):
        return [
            self.flameType.value(),
            self.unknown1.value(),
            self.unknown2.value(),
            self.unknown3.value(),
            [self.redChange.value(),
             self.blueChange.value(),
             self.greenChange.value(),
             self.alphaChange.value()]
        ]

    def setValue(self, l):
        self.flameType.setValue(l[0])
        self.unknown1.setValue(l[1])
        self.unknown2.setValue(l[2])
        self.unknown3.setValue(l[3])
        self.redChange.setValue(l[4][0])
        self.blueChange.setValue(l[4][1])
        self.greenChange.setValue(l[4][2])
        self.alphaChange.setValue(l[4][3])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class GrenadeBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("GrenadeBullet01"))

        self.detonationOptions = {
            "Impact": 0,
            "Time": 1,
            "Also impact?": 2,
            "Also impact??": 3,
            "Also impact???": 4
        }
        self.detonationType = DropDownWidget(self, "Detonation type", self.detonationOptions)
        self.unknown1 = FreeInputWidget(self, "Unknown float", float, initialValue=-0.004,
                                        tooltip="Always -0.004000000189989805. No observed effect.")
        self.unknown2 = FreeInputWidget(self, "Unknown float", float, initialValue=1.0,
                                        tooltip="Always 1.0. No observed effect.")
        self.bounceDampening = FreeInputWidget(self, "Bounce dampening", float, restrictPositive=True)
        self.smokeTrailNoise = SliderWidget(self, "Smoke trail noise", 0, 1)
        self.smokeTrailLifetime = FreeInputWidget(self, "Smoke trail lifetime", int, restrictPositive=True,
                                                  initialValue=60)
        self.fuseVariation = FreeInputWidget(self, "Fuse variation", int,
                                             tooltip="Timed grenades can have their fuse time extended by up to this amount to desynchronize the explosions")

        self.detonationType.pack()
        self.unknown1.pack()
        self.unknown2.pack()
        self.bounceDampening.pack()
        self.smokeTrailNoise.pack()
        self.smokeTrailLifetime.pack()
        self.fuseVariation.pack()

    def value(self):
        v = [
            self.detonationType.value(),
            self.unknown1.value(),
            self.unknown2.value(),
            self.bounceDampening.value(),
            self.smokeTrailNoise.value(),
            self.smokeTrailLifetime.value()]
        if self.fuseVariation.value() != 0:
            v.append(self.fuseVariation.value())
        return v

    def setValue(self, l):
        self.detonationType.setValue(l[0])
        self.unknown1.setValue(l[1])
        self.unknown2.setValue(l[2])
        self.bounceDampening.setValue(l[3])
        self.smokeTrailNoise.setValue(l[4])
        self.smokeTrailLifetime.setValue(l[5])
        if len(l) > 6:
            self.fuseVariation.setValue(l[6])
        else:
            self.fuseVariation.setValue(0)

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class HomingLaserBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("HomingLaserBullet01"))

        self.fireOptions = {
            "Straight": 1,
            "At target": 2,
            "Unknown": 3
        }
        self.fireDirection = DropDownWidget(self, "Initial firing direction", self.fireOptions)
        self.unknown2 = FreeInputWidget(self, "Unknown int", int, tooltip="No observed effect?")
        self.trailLength = FreeInputWidget(self, "Trail length", int)
        self.homingFactor = FreeInputWidget(self, "Homing factor?", float)
        self.homingFactor2 = SliderWidget(self, "Homing factor 2?", 0, 1)
        self.speedScale = FreeInputWidget(self, "Speed scale?", float)
        self.homingDelay = FreeInputWidget(self, "Homing delay", int)
        self.unknown6 = FreeInputWidget(self, "Unknown int", int, tooltip="No observed effect?")
        self.unknown7 = FreeInputWidget(self, "Unknown float", float, tooltip="No observed effect?")

        self.fireDirection.pack()
        self.unknown2.pack()
        self.trailLength.pack()
        self.homingFactor.pack()
        self.homingFactor2.pack()
        self.speedScale.pack()
        self.homingDelay.pack()
        self.unknown6.pack()
        self.unknown7.pack()

    def value(self):
        return [
            self.fireDirection.value(),
            self.unknown2.value(),
            self.trailLength.value(),
            self.homingFactor.value(),
            self.homingFactor2.value(),
            self.speedScale.value(),
            self.homingDelay.value(),
            self.unknown6.value(),
            self.unknown7.value(),
            None
        ]

    def setValue(self, l):
        self.fireDirection.setValue(l[0])
        self.unknown2.setValue(l[1])
        self.trailLength.setValue(l[2])
        self.homingFactor.setValue(l[3])
        self.homingFactor2.setValue(l[4])
        self.speedScale.setValue(l[5])
        self.homingDelay.setValue(l[6])
        self.unknown6.setValue(l[7])
        self.unknown7.setValue(l[8])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class LaserBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("LaserBullet01"))

        self.flareColor = ColorWidget(self, "Flare color")
        self.flareLightColor = ColorWidget(self, "Flare light color")
        self.flareScale = FreeInputWidget(self, "Flare scale", float, restrictPositive=True, initialValue=5)
        self.flareLightScale = FreeInputWidget(self, "Flare light scale", float, restrictPositive=True, initialValue=3)
        self.flareLife = FreeInputWidget(self, "Flare life", int, restrictPositive=True, initialValue=4)
        self.numLasers = FreeInputWidget(self, "Number of lasers", int, restrictPositive=True, initialValue=5)
        self.unknown1 = FreeInputWidget(self, "Unknown float", float)
        self.unknown2 = FreeInputWidget(self, "Unknown float", float, initialValue=1.5)
        self.laserSpreadSpeed = FreeInputWidget(self, "Laser spread speed", float, restrictPositive=True,
                                                initialValue=1.6)
        self.laserSpeed = FreeInputWidget(self, "Laser speed", float, restrictPositive=True, initialValue=0.5)
        self.laserSegments = FreeInputWidget(self, "Laser segments", int, restrictPositive=True, initialValue=20)
        self.unknown3 = FreeInputWidget(self, "Optional unknown float", float, tooltip="Set to 0 to exclude")

        self.flareColor.pack()
        self.flareLightColor.pack()
        self.flareScale.pack()
        self.flareLightScale.pack()
        self.flareLife.pack()
        self.numLasers.pack()
        self.unknown1.pack()
        self.unknown2.pack()
        self.laserSpreadSpeed.pack()
        self.laserSpeed.pack()
        self.laserSegments.pack()
        self.unknown3.pack()

    def value(self):
        v = [self.flareColor.value(),
             self.flareLightColor.value(),
             self.flareScale.value(),
             self.flareLightScale.value(),
             self.flareLife.value(),
             self.numLasers.value(),
             self.unknown1.value(),
             self.unknown2.value(),
             self.laserSpreadSpeed.value(),
             self.laserSpeed.value(),
             self.laserSegments.value()]
        if self.unknown3.value() != 0:
            v.append(self.unknown3.value())
        return v

    def setValue(self, l):
        self.flareColor.setValue(l[0])
        self.flareLightColor.setValue(l[1])
        self.flareScale.setValue(l[2])
        self.flareLightScale.setValue(l[3])
        self.flareLife.setValue(l[4])
        self.numLasers.setValue(l[5])
        self.unknown1.setValue(l[6])
        self.unknown2.setValue(l[7])
        self.laserSpreadSpeed.setValue(l[8])
        self.laserSpeed.setValue(l[9])
        self.laserSegments.setValue(l[10])
        if len(l) > 11:
            self.unknown3.setValue(l[11])
        else:
            self.unknown3.setValue(0)

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class LaserBullet02(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("LaserBullet02"))
        self.laserType = DropDownWidget(self, "Laser type", {"Simple laser": 0, "Pulse laser": 1, "Genocide gun": 2})
        self.laserType.pack()

    def value(self):
        return [self.laserType.value()]

    def setValue(self, v):
        self.laserType.setValue(v[0])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class LaserBullet03(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("LaserBullet03"))
        self.unknown1 = FreeInputWidget(self, "Unknown int", int, initialValue=0)
        self.unknown2 = FreeInputWidget(self, "Unknown float", float, initialValue=10.0)
        self.unknown1.pack()
        self.unknown2.pack()

    def value(self):
        return [self.unknown1.value(), self.unknown2.value()]

    def setValue(self, l):
        self.unknown1.setValue(l[0])
        self.unknown2.setValue(l[1])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class LightningBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("LightningBullet01"))
        self.initialNoise = FreeInputWidget(self, "Initial noise", float, initialValue=1.0,
                                            tooltip="Naturally 0.1-12.0")
        self.randomVelocity = FreeInputWidget(self, "Initial noise", float, initialValue=0.5,
                                              tooltip="How much the bolt's path will move randomly\nNaturally 0.1-0.75")
        self.curveNoise = FreeInputWidget(self, "Curve noise", float, initialValue=0.5,
                                          tooltip="How much the bolt will curve on itself\nNaturally 0.1-1.0")
        self.bounceFactor = FreeInputWidget(self, "Bounce factor", float, initialValue=1.0,
                                            tooltip="How much to modify the bolt's speed after bouncing")
        self.boltModifier = FreeInputWidget(self, "Bolt modifier", int, initialValue=5,
                                            tooltip="Appears to scale the bolt's iterations per frame. Higher values = faster bolt with more jagginess")
        self.optional1 = FreeInputWidget(self, "Unknown optional float", float, tooltip="Set to 0 to remove.")
        self.optional2 = FreeInputWidget(self, "Unknown optional float", float, tooltip="Set to 0 to remove.")

        self.initialNoise.pack()
        self.randomVelocity.pack()
        self.curveNoise.pack()
        self.bounceFactor.pack()
        self.boltModifier.pack()
        self.optional1.pack()
        self.optional2.pack()

    def value(self):
        v = [self.initialNoise.value(), self.randomVelocity.value(), self.curveNoise.value(), self.bounceFactor.value(),
             self.boltModifier.value()]
        if self.optional1.value() != 0:
            v.append(self.optional1.value())
        if self.optional2.value() != 0:
            v.append(self.optional2.value())
        return v

    def setValue(self, l):
        self.initialNoise.setValue(l[0])
        self.randomVelocity.setValue(l[1])
        self.curveNoise.setValue(l[2])
        self.bounceFactor.setValue(l[3])
        self.boltModifier.setValue(l[4])
        if len(l) > 5:
            self.optional1.setValue(l[5])
        else:
            self.optional1.setValue(0)
        if len(l) > 6:
            self.optional2.setValue(l[6])
        else:
            self.optional2.setValue(0)

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            # print(len(v))
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                # raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class MissileBullet01(tk.LabelFrame):
    def __init__(self, parent, isSubProjectile):
        tk.LabelFrame.__init__(self, parent, text=getText("MissileBullet01"))
        self.missileOption = DropDownWidget(self, "Missile type", {"Unguided": 0, "Guided 1?": 1, "Guided 2?": 2})
        self.unknown1 = CheckBoxWidget(self, "Dunno", 0, 1)
        self.unknown2 = FreeInputWidget(self, "Unknown int", int)

        self.struct1 = tk.LabelFrame(self, text="Unknown struct, vector?")
        self.unknown3 = FreeInputWidget(self.struct1, "Unknown float", float, tooltip="Always 0")
        self.unknown4 = FreeInputWidget(self.struct1, "Unknown float", float, tooltip="Always 0")
        self.unknown5 = FreeInputWidget(self.struct1, "Unknown float", float, initialValue=-0.05000000074505806,
                                        tooltip="Always -0.05000000074505806")

        self.accelerationRate = FreeInputWidget(self, "Acceleration rate", float, restrictPositive=True,
                                                initialValue=0.1, tooltip="0.01-6")
        self.turnRate = FreeInputWidget(self, "Turning rate", float, restrictPositive=True, initialValue=0.1,
                                        tooltip="0-0.8")
        self.topSpeed = FreeInputWidget(self, "Top speed", float, initialValue=1.5, tooltip="m/frame?")

        self.struct2 = tk.LabelFrame(self, text="Unknown struct")
        self.unknown6 = FreeInputWidget(self.struct2, "Unknown int", int, tooltip="0-90")
        self.unknown7 = FreeInputWidget(self.struct2, "Unknown float", float, initialValue=0.8,
                                        tooltip="Usually 0.8 or 0.98")

        self.homingDelay = FreeInputWidget(self, "Homing delay", int, restrictPositive=True)
        self.unknown8 = FreeInputWidget(self, "Unknown int", int, tooltip="0 or 5")

        self.enableStruct = CheckBoxWidget(self, "Enable struct", 0, 1)
        self.enableStruct.input.trace_add("write", self.enableOrDisableStruct3)
        self.struct3 = tk.LabelFrame(self, text=getText("Unknown struct"))
        self.unknown9 = FreeInputWidget(self.struct3, "Unknown float", float)
        self.unknown10 = FreeInputWidget(self.struct3, "Unknown float", float)

        if isSubProjectile:
            self.ignitionSound = SoundWidget(self, "Ignition sound", 0)
        else:
            self.ignitionSound = SoundWidget(self, "Ignition sound", None)

        self.missileOption.pack()
        self.unknown1.pack()
        self.unknown2.pack()
        self.struct1.pack()
        self.unknown3.pack()
        self.unknown4.pack()
        self.unknown5.pack()
        self.accelerationRate.pack()
        self.turnRate.pack()
        self.topSpeed.pack()
        self.struct2.pack()
        self.unknown6.pack()
        self.unknown7.pack()
        self.homingDelay.pack()
        self.unknown8.pack()
        self.enableStruct.pack()
        self.struct3.pack()
        self.unknown9.pack()
        self.unknown10.pack()
        self.ignitionSound.pack()

        # print(self.enableStruct.value())
        self.enableOrDisableStruct3()

    def enableOrDisableStruct3(self, *args):
        if self.enableStruct.value() == 0:
            disableInput(self.unknown9)
            disableInput(self.unknown10)
        else:
            enableInput(self.unknown9)
            enableInput(self.unknown10)

    def value(self):
        v = [
            self.missileOption.value(),
            self.unknown1.value(),
            self.unknown2.value(),
            [self.unknown3.value(),
             self.unknown4.value(),
             self.unknown5.value()],
            self.accelerationRate.value(),
            self.turnRate.value(),
            self.topSpeed.value(),
            [self.unknown6.value(),
             self.unknown7.value()],
            self.homingDelay.value(),
            self.unknown8.value()]
        # print(self.enableStruct.value())
        if self.enableStruct.value() == 1:
            v.append([self.unknown9.value(), self.unknown10.value()])
        else:
            v.append(None)

        v.append(self.ignitionSound.value())
        return v

    def setValue(self, l):
        self.missileOption.setValue(l[0])
        self.unknown1.setValue(l[1])
        self.unknown2.setValue(l[2])
        self.unknown3.setValue(l[3][0])
        self.unknown4.setValue(l[3][1])
        self.unknown5.setValue(l[3][2])
        self.accelerationRate.setValue(l[4])
        self.turnRate.setValue(l[5])
        self.topSpeed.setValue(l[6])
        self.unknown6.setValue(l[7][0])
        self.unknown7.setValue(l[7][1])
        self.homingDelay.setValue(l[8])
        self.unknown8.setValue(l[9])
        if l[10] is not None:
            self.enableStruct.setValue(True)
            self.unknown9.setValue(l[10][0])
            self.unknown10.setValue(l[10][1])
            self.enableOrDisableStruct3()
        else:
            self.enableStruct.setValue(False)
            self.enableOrDisableStruct3()

        self.ignitionSound.setValue(l[11])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class MissileBullet02(tk.LabelFrame):
    def __init__(self, parent, isSubProjectile):
        tk.LabelFrame.__init__(self, parent, text=getText("MissileBullet02"))

        self.col1 = tk.Frame(self)

        self.missileOption = DropDownWidget(self.col1, "Missile type", {"Unguided": 0, "Guided 1?": 1, "Guided 2?": 2})
        self.unknown1 = CheckBoxWidget(self.col1, "Dunno", 0, 1)
        self.unknown2 = FreeInputWidget(self.col1, "Unknown int", int)

        self.struct1 = tk.LabelFrame(self.col1, text="Unknown struct, vector?")
        self.unknown3 = FreeInputWidget(self.struct1, "Unknown float", float, tooltip="Always 0")
        self.unknown4 = FreeInputWidget(self.struct1, "Unknown float", float, tooltip="Always 0")
        self.unknown5 = FreeInputWidget(self.struct1, "Unknown float", float, initialValue=-0.05000000074505806,
                                        tooltip="Always -0.05000000074505806")

        self.accelerationRate = FreeInputWidget(self.col1, "Acceleration rate", float, restrictPositive=True,
                                                initialValue=1.5, tooltip="0.01-6")
        self.turnRate = FreeInputWidget(self.col1, "Turning rate", float, restrictPositive=True, initialValue=0.4,
                                        tooltip="0-0.8")
        self.topSpeed = FreeInputWidget(self.col1, "Top speed", float, initialValue=6, tooltip="m/frame?")

        self.struct2 = tk.LabelFrame(self.col1, text="Unknown struct")
        self.unknown6 = FreeInputWidget(self.struct2, "Unknown int", int, tooltip="0-90")
        self.unknown7 = FreeInputWidget(self.struct2, "Unknown float", float, initialValue=0.8,
                                        tooltip="Usually 0.8 or 0.98")

        self.homingDelay = FreeInputWidget(self.col1, "Homing delay", int, restrictPositive=True)
        self.unknown8 = FreeInputWidget(self.col1, "Unknown int", int, tooltip="0 or 5")

        self.enableStruct = CheckBoxWidget(self.col1, "Enable struct", 0, 1)
        self.enableStruct.input.trace_add("write", self.enableOrDisableStruct3)
        self.struct3 = tk.LabelFrame(self.col1, text=getText("Unknown struct"))
        self.unknown9 = FreeInputWidget(self.struct3, "Unknown float", float)
        self.unknown10 = FreeInputWidget(self.struct3, "Unknown float", float)

        if isSubProjectile:
            self.ignitionSound = SoundWidget(self.col1, "Ignition sound", 0)
        else:
            self.ignitionSound = SoundWidget(self.col1, "Ignition sound", None)

        self.col2 = tk.Frame(self)

        self.struct4 = tk.LabelFrame(self.col2, text=getText("Detonation type"))
        self.struct4Choice = DropDownWidget(self.struct4, "Struct type", {"Proximity": 0, "Timer": 1},
                                            tooltip="Alters the lengths and value types of the struct")
        self.struct4Choice.dropDownDisplayed.trace_add("write", self.updateStruct4Widgets)
        self.struct4Type1Int = FreeInputWidget(self.struct4, "Time (frames)", int, initialValue=120,
                                               tooltip="Only observed at 120")
        self.struct4Type0Float1 = FreeInputWidget(self.struct4, "Distance", float, initialValue=50.0, tooltip="50-70")
        self.struct4Type0Float2 = FreeInputWidget(self.struct4, "Unknown float", float, initialValue=0.75,
                                                  tooltip="0.75 or 1")

        self.struct5 = tk.LabelFrame(self.col2, text=getText("Unknown struct"))
        self.struct5Int = FreeInputWidget(self.struct5, "Unknown int", int,
                                          tooltip="0 or 2, likely some sort of option")
        self.struct5Float1 = FreeInputWidget(self.struct5, "Unknown float", float, tooltip="Always 0.0?")
        self.projectileSpread = AngleWidget(self.struct5, "Sub-projectile spread", minimum=0, maximum=360)

        self.struct6 = tk.LabelFrame(self.col2, text=getText("Unknown struct"))
        self.struct6Int = FreeInputWidget(self.struct6, "Unknown int", int,
                                          tooltip="0 or 1, likely some sort of option/flag")
        self.struct6Float = FreeInputWidget(self.struct6, "Unknown float", float, initialValue=1.0,
                                            tooltip="Always 1.0")

        self.subProjectile = SubProjectile(self)

        self.col1.grid(row=0, column=0, sticky="N")

        self.missileOption.pack()
        self.unknown1.pack()
        self.unknown2.pack()
        self.struct1.pack()
        self.unknown3.pack()
        self.unknown4.pack()
        self.unknown5.pack()
        self.accelerationRate.pack()
        self.turnRate.pack()
        self.topSpeed.pack()
        self.struct2.pack()
        self.unknown6.pack()
        self.unknown7.pack()
        self.homingDelay.pack()
        self.unknown8.pack()
        self.enableStruct.pack()
        self.struct3.pack()
        self.unknown9.pack()
        self.unknown10.pack()
        self.ignitionSound.pack()

        self.col2.grid(row=0, column=1, sticky="N")

        self.struct4.pack()
        self.struct4Choice.pack()
        self.struct4Choice.pack()
        self.struct4Type0Float1.pack()
        self.struct4Type0Float2.pack()
        # self.struct4Type1Int.pack()
        self.struct5.pack()
        self.struct5Int.pack()
        self.struct5Float1.pack()
        self.projectileSpread.pack()
        self.struct6.pack()
        self.struct6Int.pack()
        self.struct6Float.pack()

        self.subProjectile.grid(row=0, column=2, sticky="N")

        # print(self.enableStruct.value())
        self.enableOrDisableStruct3()

    def enableOrDisableStruct3(self, *args):
        if self.enableStruct.value() == 0:
            disableInput(self.unknown9)
            disableInput(self.unknown10)
        else:
            enableInput(self.unknown9)
            enableInput(self.unknown10)

    def updateStruct4Widgets(self, *args):
        if self.struct4Choice.value() == 0:
            self.struct4Type0Float1.pack()
            self.struct4Type0Float2.pack()
            self.struct4Type1Int.pack_forget()
        elif self.struct4Choice.value() == 1:
            self.struct4Type0Float1.pack_forget()
            self.struct4Type0Float2.pack_forget()
            self.struct4Type1Int.pack()
        else:
            raise ValueError("Unexpected value for struct4Choice")

    def value(self):
        v = [
            self.missileOption.value(),
            self.unknown1.value(),
            self.unknown2.value(),
            [self.unknown3.value(),
             self.unknown4.value(),
             self.unknown5.value()],
            self.accelerationRate.value(),
            self.turnRate.value(),
            self.topSpeed.value(),
            [self.unknown6.value(),
             self.unknown7.value()],
            self.homingDelay.value(),
            self.unknown8.value()]
        # print(self.enableStruct.value())
        if self.enableStruct.value() == 1:
            v.append([self.unknown9.value(), self.unknown10.value()])
        else:
            v.append(None)

        v.append(self.ignitionSound.value())

        if self.struct4Choice.value() == 0:
            v.append([self.struct4Choice.value(), self.struct4Type0Float1.value(), self.struct4Type0Float2.value()])
        elif self.struct4Choice.value() == 1:
            v.append([self.struct4Choice.value(), self.struct4Type1Int.value()])
        v.append([self.struct5Int.value(), self.struct5Float1.value(), self.projectileSpread.value()])
        v.append([self.struct6Int.value(), self.struct6Float.value()])
        v.append(self.subProjectile.value())
        return v

    def setValue(self, l):
        self.missileOption.setValue(l[0])
        self.unknown1.setValue(l[1])
        self.unknown2.setValue(l[2])
        self.unknown3.setValue(l[3][0])
        self.unknown4.setValue(l[3][1])
        self.unknown5.setValue(l[3][2])
        self.accelerationRate.setValue(l[4])
        self.turnRate.setValue(l[5])
        self.topSpeed.setValue(l[6])
        self.unknown6.setValue(l[7][0])
        self.unknown7.setValue(l[7][1])
        self.homingDelay.setValue(l[8])
        self.unknown8.setValue(l[9])
        if l[10] is not None:
            self.enableStruct.setValue(True)
            self.unknown9.setValue(l[10][0])
            self.unknown10.setValue(l[10][1])
            self.enableOrDisableStruct3()
        else:
            self.enableStruct.setValue(False)
            self.enableOrDisableStruct3()

        self.ignitionSound.setValue(l[11])
        if l[12][0] == 0:
            self.struct4Choice.setValue(l[12][0])
            self.struct4Type0Float1.setValue(l[12][1])
            self.struct4Type0Float2.setValue(l[12][2])
        elif l[12][0] == 1:
            self.struct4Choice.setValue(l[12][0])
            self.struct4Type1Int.setValue(l[12][1])
        self.struct5Int.setValue(l[13][0])
        self.struct5Float1.setValue(l[13][1])
        self.projectileSpread.setValue(l[13][2])
        self.struct6Int.setValue(l[14][0])
        self.struct6Float.setValue(l[14][1])
        self.subProjectile.setValue(l[15])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class NapalmBullet01(tk.LabelFrame):
    def __init__(self, parent, isSubProjectile):
        tk.LabelFrame.__init__(self, parent, text=getText("NapalmBullet01"))
        self.col1 = tk.Frame(self)
        self.unknown1 = FreeInputWidget(self.col1, "Unknown int", int, tooltip="Always 0")
        self.struct1 = tk.LabelFrame(self.col1, text=getText("Spread?"))
        self.hSpread = AngleWidget(self.struct1, "Horizontal?")
        self.vSpread = AngleWidget(self.struct1, "Vertical?")

        self.trailNoise = FreeInputWidget(self.col1, "Smoke trail noise", float, restrictPositive=True,
                                          initialValue=0.05)
        self.subProjectileSize = FreeInputWidget(self.col1, "Sub projectile size", int, restrictPositive=True,
                                                 initialValue=60)
        if isSubProjectile:
            self.emitterSound = SoundWidget(self.col1, "Ignition sound", 0)
        else:
            self.emitterSound = SoundWidget(self.col1, "Ignition sound", None)

        # self.emitterParams = tk.LabelFrame(self.col1, text=getText("Emitter settings"))
        # self.struct2 = tk.LabelFrame(self.emitterParams, text=getText("Unknown struct"))
        # self.unknown2 = FreeInputWidget(self.struct2, "Unknown float", float, tooltip="Always 0.0?")
        # self.unknown3 = FreeInputWidget(self.struct2, "Unknown float", float, tooltip="Always 0.0?")
        # self.struct3 = tk.LabelFrame(self.emitterParams, text=getText("Unknown struct"))
        # self.unknown4 = FreeInputWidget(self.struct3, "Unknown float", float, tooltip="Always 0.0?")
        # self.unknown5 = FreeInputWidget(self.struct3, "Unknown float", float, tooltip="Always 0.0?")
        # self.projectileCount = FreeInputWidget(self.emitterParams, "Projectile count", int, initialValue=120, restrictPositive=True)
        # self.projectileInterval = FreeInputWidget(self.emitterParams, "Projectile interval", int, initialValue=2, restrictPositive=True)
        #
        # self.projectileHitSound = SoundWidget(self.col1, )

        self.col2 = tk.Frame(self)
        self.col1.grid(row=0, column=0, sticky="N")
        self.subProjectile = SubProjectile(self.col2)

        self.unknown1.pack()
        self.struct1.pack()
        self.hSpread.pack()
        self.vSpread.pack()
        self.trailNoise.pack()
        self.subProjectileSize.pack()
        self.emitterSound.pack()
        self.col2.grid(row=0, column=1, sticky="N")
        self.subProjectile.pack()

    def value(self):
        return [
            self.unknown1.value(),
            [self.hSpread.value(),
             self.vSpread.value()],
            self.trailNoise.value(),
            self.subProjectileSize.value(),
            self.subProjectile.value(),
            self.emitterSound.value()]

    def setValue(self, l):
        self.unknown1.setValue(l[0])
        self.hSpread.setValue(l[1][0])
        self.vSpread.setValue(l[1][1])
        self.trailNoise.setValue(l[2])
        self.subProjectileSize.setValue(l[3])
        self.subProjectile.setValue(l[4])
        self.emitterSound.setValue(l[5])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class NeedleBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("NeedleBullet01"))
        self.unknown = FreeInputWidget(self, "Unknown int", int, tooltip="Always 1")
        self.unknown.pack()

    def value(self):
        return [self.unknown.value()]

    def setValue(self, l):
        self.unknown.setValue(l[0])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class PileBunkerBullet01(tk.LabelFrame):
    def __init__(self, parent, isSubProjectile):
        tk.LabelFrame.__init__(self, parent, text=getText("PileBunkerBullet01"))
        if isSubProjectile:
            self.hitSound = SoundWidget(self, "Hit sound", 0)
        else:
            self.hitSound = SoundWidget(self, "Hit sound", None)
        self.hitSound.pack()

    def value(self):
        return [self.hitSound.value()]

    def setValue(self, l):
        self.hitSound.setValue(l[0])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class PlasmaBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("PlasmaBullet01"))
        self.unknown1 = FreeInputWidget(self, "Plasma type?", int, tooltip="0 or 1")
        self.unknown2 = FreeInputWidget(self, "Unknown int", int, tooltip="Trail lifetime?. 6-30")
        self.unknown1.pack()
        self.unknown2.pack()

    def value(self):
        return [self.unknown1.value(), self.unknown2.value()]

    def setValue(self, l):
        self.unknown1.setValue(l[0])
        self.unknown2.setValue(l[1])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class PulseBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("PulseBullet01"))
        self.unknown1 = FreeInputWidget(self, "Unknown int", int)

        self.struct1 = tk.LabelFrame(self, text=getText("Unknown struct"))
        self.unknown2 = FreeInputWidget(self.struct1, "Unknown float", float)
        self.unknown3 = FreeInputWidget(self.struct1, "Unknown float", float)
        self.unknown4 = FreeInputWidget(self.struct1, "Unknown float", float)
        self.unknown5 = FreeInputWidget(self.struct1, "Unknown float", float)

        self.struct2 = tk.LabelFrame(self, text=getText("Unknown struct"))
        self.unknown6 = FreeInputWidget(self.struct2, "Unknown float", float)
        self.unknown7 = FreeInputWidget(self.struct2, "Unknown float", float)
        self.unknown8 = FreeInputWidget(self.struct2, "Unknown float", float)
        self.unknown9 = FreeInputWidget(self.struct2, "Unknown float", float)

        self.unknown10 = FreeInputWidget(self, "Unknown float", float)
        self.unknown11 = FreeInputWidget(self, "Unknown float", float)
        self.unknown12 = FreeInputWidget(self, "Unknown float", float)
        self.unknown13 = FreeInputWidget(self, "Unknown int", int)

        self.unknown1.pack()
        self.struct1.pack()
        self.unknown2.pack()
        self.unknown3.pack()
        self.unknown4.pack()
        self.unknown5.pack()
        self.struct2.pack()
        self.unknown6.pack()
        self.unknown7.pack()
        self.unknown8.pack()
        self.unknown9.pack()
        self.unknown10.pack()
        self.unknown11.pack()
        self.unknown12.pack()
        self.unknown13.pack()

    def value(self):
        return [
            self.unknown1.value(),
            [self.unknown2.value(),
             self.unknown3.value(),
             self.unknown4.value(),
             self.unknown5.value()],
            [self.unknown6.value(),
             self.unknown7.value(),
             self.unknown8.value(),
             self.unknown9.value()],
            self.unknown10.value(),
            self.unknown11.value(),
            self.unknown12.value(),
            self.unknown13.value()]

    def setValue(self, l):
        self.unknown1.setValue(l[0])
        self.unknown2.setValue(l[1][0])
        self.unknown3.setValue(l[1][1])
        self.unknown4.setValue(l[1][2])
        self.unknown5.setValue(l[1][3])
        self.unknown6.setValue(l[2][0])
        self.unknown7.setValue(l[2][1])
        self.unknown8.setValue(l[2][2])
        self.unknown9.setValue(l[2][3])
        self.unknown10.setValue(l[3])
        self.unknown11.setValue(l[4])
        self.unknown12.setValue(l[5])
        self.unknown13.setValue(l[6])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class RocketBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("RocketBullet01"))
        self.rocketType = DropDownWidget(self, "Explosion visual type",
                                         {"Regular": 0, "Mortar/howitzer": 1, "Explosions with massive smoke cloud": 2})
        self.smokeTrailLifetime = FreeInputWidget(self, "Smoke trail lifetime", int)
        self.ignitionDelay = FreeInputWidget(self, "Ignition delay", int)
        self.smokeTrailDrift = FreeInputWidget(self, "Smoke trail drift", float, initialValue=0.1,
                                               tooltip="How fast the smoke trail drifts backwards. Values closer to 1 or higher look strange.")

        self.rocketType.pack()
        self.smokeTrailLifetime.pack()
        self.ignitionDelay.pack()
        self.smokeTrailDrift.pack()

    def value(self):
        return [self.rocketType.value(),
                self.smokeTrailLifetime.value(),
                self.ignitionDelay.value(),
                self.smokeTrailDrift.value()]

    def setValue(self, l):
        self.rocketType.setValue(l[0])
        self.smokeTrailLifetime.setValue(l[1])
        self.ignitionDelay.setValue(l[2])
        self.smokeTrailDrift.setValue(l[3])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class SentryGunBullet01(tk.LabelFrame):
    def __init__(self, parent, isSubProjectile):
        tk.LabelFrame.__init__(self, parent, text=getText("SentryGunBullet01"))
        self.col1 = tk.Frame(self)
        self.friendlyFire = CheckBoxWidget(self.col1, "Friendly fire", 0, 1)
        self.unknown1 = ""
        self.unknown2 = 0
        self.unknown3 = FreeInputWidget(self.col1, "Unknown int", int, initialValue=8, tooltip="8 or 16")
        self.searchRange = FreeInputWidget(self.col1, "Search range", float, restrictPositive=True, initialValue=200.0)
        self.turnSpeed = FreeInputWidget(self.col1, "Turn speed", float, initialValue=0.05, restrictPositive=True,
                                         tooltip="Lowest = 0.0099, highest=0.075")
        self.unknown4 = FreeInputWidget(self.col1, "Unknown int", int,
                                        tooltip="0, 15, or 120, seemingly no pattern but I didn't check too much")
        self.firingBone = "spine"

        self.offsetFrame = tk.LabelFrame(self.col1, text="Bullet offset")
        self.offsetX = FreeInputWidget(self.offsetFrame, "X", float)
        self.offsetY = FreeInputWidget(self.offsetFrame, "Y", float, initialValue=0.25)
        self.offsetZ = FreeInputWidget(self.offsetFrame, "Z", float, initialValue=1.25)

        self.ammoClass = DropDownWidget(self.col1, "Ammo type", subProjectileAmmoOptions)
        self.ammoClass.dropDownDisplayed.trace_add("write", self.updateAmmoCustWidget)

        self.ammoCount = FreeInputWidget(self.col1, "Ammo", int, restrictPositive=True)
        self.fireInterval = FreeInputWidget(self.col1, "Fire interval", int, restrictPositive=True, initialValue=8)

        self.shotsPerSecondVar = tk.DoubleVar(self, 0)
        self.shotsPerSecond = FreeInputWidget(self.col1, "Shots per second", float)
        self.shotsPerSecond.input.config(textvariable=self.shotsPerSecondVar, state="disabled")
        self.fireInterval.inputVar.trace_add("write", self.updateShotsPerSecondVar)
        self.ammoLifetime = FreeInputWidget(self.col1, "Ammo lifetime?", int, restrictPositive=True, initialValue=20)

        # self.ammoSpeed = FreeInputWidget(self.col1, "Ammo speed (m/frame)", float, restrictPositive=True, initialValue=)
        self.range = FreeInputWidget(self.col1, "Range", float)
        self.rangeVar = tk.StringVar(self, 0)
        self.range.input.config(textvariable=self.rangeVar, state="disabled")
        self.ammoLifetime.inputVar.trace_add("write", self.updateRangeVar)

        self.ammoSpeed = FreeInputWidget(self.col1, "Ammo speed", float, restrictPositive=True, initialValue=20,
                                         tooltip="Ammo visual and initial hitbox size")
        self.ammoVisualMultiplier = FreeInputWidget(self.col1, "Ammo visual multiplier", float, restrictPositive=True,
                                                    initialValue=1)
        self.ammoHitboxMultiplier = FreeInputWidget(self.col1, "Ammo hitbox multiplier", float, restrictPositive=True,
                                                    initialValue=1)
        # self.ammoScale = FreeInputWidget(self.col1, "Ammo scale adjust", float, restrictPositive=True, initialValue=0.3, tooltip="Multiply ammo hitbox and hit effect size")

        self.col2 = tk.Frame(self)

        if isSubProjectile:
            self.firingSound = SoundWidget(self.col1, "Firing sound", 0)
        else:
            self.firingSound = SoundWidget(self.col1, "Firing sound", None)

        self.muzzleFlash = MuzzleFlashWidget(self.col2)

        self.ammoCustWidget = None

        self.col1.grid(row=0, column=0, sticky="N")
        self.friendlyFire.pack()
        # self.unknown1.pack()
        # self.unknown2.pack()
        self.unknown3.pack()
        self.searchRange.pack()
        self.turnSpeed.pack()
        self.unknown4.pack()
        self.offsetFrame.pack()
        self.offsetX.pack()
        self.offsetY.pack()
        self.offsetZ.pack()
        self.ammoClass.pack()
        self.ammoCount.pack()
        self.shotsPerSecond.pack()
        self.fireInterval.pack()
        self.ammoLifetime.pack()
        self.range.pack()
        self.ammoSpeed.pack()
        self.ammoVisualMultiplier.pack()
        self.ammoHitboxMultiplier.pack()
        self.firingSound.pack()
        self.col2.grid(row=0, column=1, sticky="N")
        self.muzzleFlash.pack()

        self.updateAmmoCustWidget()

    def updateRangeVar(self, *args):
        self.rangeVar.set(str(self.ammoLifetime.value() * self.ammoSpeed.value()) + "m")

    def updateShotsPerSecondVar(self, *args):
        self.shotsPerSecondVar.set(60 / (self.fireInterval.value() + 1))

    def updateAmmoCustWidget(self, *args):
        if self.ammoCustWidget is not None:
            self.ammoCustWidget.grid_forget()
            self.ammoCustWidget.destroy()
            self.ammoCustWidget = None
        self.ammoCustWidget = ammoCustWidgetFromAmmoClass(self, self.ammoClass.value(), True)
        if self.ammoCustWidget is not None:
            self.ammoCustWidget.grid(row=0, column=2, sticky="N")

    def value(self):
        v = [
            self.friendlyFire.value(),
            self.unknown1,
            self.unknown2,
            self.unknown3.value(),
            self.searchRange.value(),
            self.turnSpeed.value(),
            self.unknown4.value(),
            self.firingBone,
            [self.offsetX.value(),
             self.offsetY.value(),
             self.offsetZ.value()],
            self.ammoClass.value(),
            self.ammoCount.value(),
            self.fireInterval.value(),
            self.ammoLifetime.value(),
            self.ammoSpeed.value()]

        if self.ammoHitboxMultiplier.value() == self.ammoVisualMultiplier.value():
            v.append(self.ammoHitboxMultiplier.value())
        else:
            v.append([self.ammoVisualMultiplier.value(), self.ammoHitboxMultiplier.value()])
        v.append(self.ammoCustWidget.value())
        v.append(self.firingSound.value())
        v.append(self.muzzleFlash.muzzleFlashType.value())
        if self.muzzleFlash.muzzleFlashType.value() != "":
            v.append(self.muzzleFlash.paramsWidget.value())
        else:
            v.append(0)

        return v

    def setValue(self, l):
        self.friendlyFire.setValue(l[0])
        # self.unknown1.setValue(l[1])
        # self.unknown2.setValue(l[2])
        self.unknown3.setValue(l[3])
        self.searchRange.setValue(l[4])
        self.turnSpeed.setValue(l[5])
        self.unknown4.setValue(l[6])
        # self.firingBone.setValue(l[7])
        self.offsetX.setValue(l[8][0])
        self.offsetY.setValue(l[8][1])
        self.offsetZ.setValue(l[8][2])
        self.ammoClass.setValue(l[9])
        self.ammoCount.setValue(l[10])
        self.fireInterval.setValue(l[11])
        self.ammoLifetime.setValue(l[12])
        self.ammoSpeed.setValue(l[13])
        if isinstance(l[14], list):
            self.ammoVisualMultiplier.setValue(l[14][0])
            self.ammoHitboxMultiplier.setValue(l[14][1])
        else:
            self.ammoVisualMultiplier.setValue(l[14])
            self.ammoHitboxMultiplier.setValue(l[14])
        self.ammoCustWidget.setValue(l[15])
        self.firingSound.setValue(l[16])
        self.muzzleFlash.muzzleFlashType.setValue(l[17])
        if l[17] != "":
            self.muzzleFlash.paramsWidget.setValue(l[18])
        # else:
        #     self.muzzleFlash.paramsWidget

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class ShieldBashBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("ShieldBashBullet01"))
        self.unknown1 = FreeInputWidget(self, "Unknown int", int, tooltip="Always 0")
        self.unknown2 = FreeInputWidget(self, "Unknown float", float, tooltip="0.25 or 0.5")
        self.unknown1.pack()
        self.unknown2.pack()

    def value(self):
        return [self.unknown1.value(), self.unknown2.value()]

    def setValue(self, l):
        self.unknown1.setValue(l[0])
        self.unknown2.setValue(l[1])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class ShockWaveBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("ShockWaveBullet01"))
        self.shockwaveType = DropDownWidget(self, "Shockwave type",
                                            {"None/Force blade": None, "Regular": 0, "Crater shockwave": 1,
                                             "Vibro roller": 2})
        self.shockwaveType.dropDownDisplayed.trace_add("write", self.addOrRemoveUnknown)
        self.unknown = FreeInputWidget(self, "Unknown int", int)

        self.shockwaveType.pack()

    def addOrRemoveUnknown(self, *args):
        if self.shockwaveType.value() is None:
            self.unknown.pack_forget()
        else:
            self.unknown.pack()

    def value(self):
        if self.shockwaveType.value() is None:
            return None
        else:
            return [self.shockwaveType.value(), self.unknown.value()]

    def setValue(self, l):
        if l is not None:
            self.shockwaveType.setValue(l[0])
            self.unknown.setValue(l[1])
        else:
            self.shockwaveType.setValue(None)

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class SmokeCandleBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Vehicle summon"))
        self.col1 = tk.Frame(self)
        self.col2 = tk.Frame(self)
        self.col3 = tk.Frame(self)
        self.col4 = tk.Frame(self)
        self.weaponWidgets = []
        self.unknown1 = FreeInputWidget(self.col1, "Unknown float", float, initialValue=0.05000000074505806,
                                        tooltip="Always 0.05000000074505806?")
        self.smokeLifetime = FreeInputWidget(self.col1, "Smoke lifetime/size", int, initialValue=180,
                                             restrictPositive=True)
        self.summonDelay = FreeInputWidget(self.col1, "Summon delay", int, initialValue=120, restrictPositive=True)
        self.summonType = FreeInputWidget(self.col1, "Summon type", int, initialValue=1, tooltip="Always 1?")
        transportOptions = {"Normal transport": ["app:/Object/v508_transport.sgo", "app:/Object/v509_transportbox.sgo"],
                            "Barga transport": ["app:/Object/v508_transport_formation.sgo", 0]}
        self.transporter = DropDownWidget(self.col1, "Transport vehicle", transportOptions)

        self.vehicleSGO = MultiDropDownWidget(self.col1, "Vehicle type", vehicleSGOS)
        self.weaponMultiplier = FreeInputWidget(self.col1, "Weapon damage multiplier", float, restrictPositive=True,
                                                initialValue=5.0)
        self.HP = FreeInputWidget(self.col1, "Vehicle hp", float, initialValue=10000.0)
        self.vehicleParams = TankParams(self.col1)
        self.voices = ['輸送部隊目標確認', '輸送部隊発射', '輸送部隊攻撃後']

        self.vehicleSGO.valueLabel.inputVar.trace_add("write", self.updateParamsAndWeapons)

        self.col1.grid(row=0, column=0, sticky="N")
        self.col2.grid(row=0, column=1, sticky="N")
        self.col3.grid(row=0, column=2, sticky="N")
        self.col4.grid(row=0, column=3, sticky="N")
        self.unknown1.pack()
        self.smokeLifetime.pack()
        self.summonDelay.pack()
        self.summonType.pack()
        self.transporter.pack()
        self.vehicleSGO.pack()
        self.HP.pack()
        self.weaponMultiplier.pack()
        self.vehicleParams.pack()

        self.updateParamsAndWeapons()

    def value(self):
        v = [self.unknown1.value(), self.smokeLifetime.value(), self.summonDelay.value(), self.summonType.value(),
             [self.transporter.value()[0], self.transporter.value()[1], self.vehicleSGO.value(),
              [[self.HP.value() / self.baseHP, self.weaponMultiplier.value()]]], self.voices]
        if self.vehicleSGO.value() in vehicleSGOS["Tank"].values():
            v[4][3].append(self.vehicleParams.value())
            v[4][3].append([w.value() for w in self.weaponWidgets])
        elif self.vehicleSGO.value() == "app:/Object/Vehicle401_Striker.sgo":  # Grape
            v[4][3].append(self.vehicleParams.value())
            v[4][3].append([w.value() for w in self.weaponWidgets])
        elif self.vehicleSGO.value() == 'app:/Object/v507_rescuetank.sgo' or \
                self.vehicleSGO.value() == 'app:/Object/v507_rescuetank_siawase.sgo':  # Caliban
            v[4][3].append(self.vehicleParams.value()[0])
            v[4][3].append(self.vehicleParams.value()[1])
            v[4][3].append(['app:/weapon/v_507_RescueUnit01.sgo'])
        elif self.vehicleSGO.value() == 'app:/Object/Vehicle402_Rocket.sgo':  # Naegling
            v[4][3].append(self.vehicleParams.value())
            v[4][3].append([w.value() for w in self.weaponWidgets])
        elif self.vehicleSGO.value() == 'app:/Object/v506_heli.sgo':  # Eros
            v[4][3].append(self.vehicleParams.value()[0])
            v[4][3].append(self.vehicleParams.value()[1])
            v[4][3].append([w.value() for w in self.weaponWidgets])
        elif self.vehicleSGO.value() == 'app:/Object/Vehicle409_heli.sgo':  # Nereid
            v[4][3].append(self.vehicleParams.value()[0])
            v[4][3].append(self.vehicleParams.value()[1])
            v[4][3].append([w.value() for w in self.weaponWidgets])
            v[4][3].append(self.vehicleParams.value()[2])
        elif self.vehicleSGO.value() == 'app:/Object/Vehicle410_heli.sgo':  # Brute
            v[4][3].append(self.vehicleParams.value()[0])
            v[4][3].append(self.vehicleParams.value()[1])
            v[4][3].append([w.value() for w in self.weaponWidgets])
        elif self.vehicleSGO.value() in vehicleSGOS["Nix"].values():  # Nix
            v[4][3].append(self.vehicleParams.value()[0])
            v[4][3].append(self.vehicleParams.value()[1])
            v[4][3].append(self.vehicleParams.value()[2])
            v[4][3].append([w.value() for w in self.weaponWidgets])
            v[4][3].append(self.vehicleParams.value()[3])
        elif self.vehicleSGO.value() == 'app:/Object/Vehicle407_bigbegaruta.sgo':
            v[4][3].append(self.vehicleParams.value()[0])
            v[4][3].append(self.vehicleParams.value()[1])
            v[4][3].append(self.vehicleParams.value()[2])
            v[4][3].append([w.value() for w in self.weaponWidgets])
            v[4][3].append(self.vehicleParams.value()[3])
        elif self.vehicleSGO.value() == 'app:/Object/v512_keiTruck_bgp.sgo':  # Truck
            pass
        elif self.vehicleSGO.value() == 'app:/Object/v503_bike.sgo' or \
                self.vehicleSGO.value() == 'app:/Object/v503_bike_omegaz.sgo':  # Bike
            pass

        return v

    def setValue(self, l):
        pass

    def updateParamsAndWeapons(self, *args):
        def replaceParamsAndRemoveWeapons(self, paramType):
            if not isinstance(self.vehicleParams, paramType):
                self.vehicleParams.pack_forget()
                self.vehicleParams.destroy()
                self.vehicleParams = paramType(self.col1)
                self.vehicleParams.pack()
            for weaponWidget in self.weaponWidgets:
                weaponWidget.pack_forget()
                weaponWidget.destroy()
            self.weaponWidgets.clear()

        if self.vehicleSGO.value() == "app:/Object/v505_tank.sgo" or \
                self.vehicleSGO.value() == 'app:/Object/v505_tank_edf4.sgo' or \
                self.vehicleSGO.value() == 'app:/Object/v505_tank_edf5.sgo':  # Blacker
            self.baseHP = 1000.0
            replaceParamsAndRemoveWeapons(self, TankParams)
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Main Cannon", True, True, self.weaponMultiplier))
            self.weaponWidgets[0].grid(row=0, column=0, sticky="N")
            self.weaponWidgets[0].setValue(["app:/weapon/v_505tank_cannon01.sgo", [0.1, 0.05], [40, 0.004, 0.1]])

        elif self.vehicleSGO.value() == 'app:/Object/Vehicle403_Tank.sgo':  # Railgun
            self.baseHP = 1200.0
            replaceParamsAndRemoveWeapons(self, TankParams)
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Main Cannon", True, True, self.weaponMultiplier,
                                                               recoilType="BodyRecoil"))
            self.weaponWidgets.append(
                VehicleWeaponChoice(self, "Side gun 1", True, True, self.weaponMultiplier, recoilType="AimRecoil"))
            self.weaponWidgets.append(
                VehicleWeaponChoice(self, "Side gun 2", True, True, self.weaponMultiplier, recoilType="AimRecoil"))
            for i in range(len(self.weaponWidgets)):
                self.weaponWidgets[i].grid(row=0, column=i, sticky="N")
            self.weaponWidgets[0].setValue(["app:/weapon/v_403tank_cannon01.sgo", [0.1, 0.05], [40, 0.004, 0.1]])
            self.weaponWidgets[1].setValue(['app:/weapon/v_403tank_machinegun.sgo', [0.0, 0.0026], [90.0, 0.01, 0.01]])
            self.weaponWidgets[2].setValue(['app:/weapon/v_403tank_machinegun.sgo', [0.0, 0.0026], [90.0, 0.01, 0.01]])

        elif self.vehicleSGO.value() == 'app:/Object/v510_maser.sgo':  # EMC
            self.baseHP = 1000.0
            replaceParamsAndRemoveWeapons(self, TankParams)
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Main Cannon", True, True, self.weaponMultiplier))
            self.weaponWidgets[0].grid(row=0, column=0, sticky="N")
            self.weaponWidgets[0].setValue(["app:/weapon/v_510_maser_thunder01.sgo", [0, 0], [15.0, 0.01, 0.05]])

        elif self.vehicleSGO.value() == "app:/Object/Vehicle404_bigtank.sgo":  # Titan
            self.baseHP = 4800.0
            replaceParamsAndRemoveWeapons(self, TankParams)
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Main Cannon", True, True, self.weaponMultiplier))
            self.weaponWidgets.append(
                VehicleWeaponChoice(self.col3, "Left primary gun", True, True, self.weaponMultiplier))
            self.weaponWidgets.append(
                VehicleWeaponChoice(self.col4, "Right primary gun", True, True, self.weaponMultiplier))
            self.weaponWidgets.append(
                VehicleWeaponChoice(self.col2, "Driver secondary gun", True, False, self.weaponMultiplier))
            self.weaponWidgets.append(
                VehicleWeaponChoice(self.col3, "Left secondary gun", True, False, self.weaponMultiplier))
            self.weaponWidgets.append(
                VehicleWeaponChoice(self.col4, "Right secondary gun", True, False, self.weaponMultiplier))
            self.weaponWidgets[0].pack()  #.grid(row=0, column=0, sticky="N")
            self.weaponWidgets[3].pack()  #.grid(row=1, column=0, sticky="N")
            self.weaponWidgets[1].pack()  #.grid(row=0, column=1, sticky="N")
            self.weaponWidgets[4].pack()  #.grid(row=1, column=1, sticky="N")
            self.weaponWidgets[2].pack()  #.grid(row=0, column=2, sticky="N")
            self.weaponWidgets[5].pack()  #.grid(row=1, column=2, sticky="N")
            self.weaponWidgets[0].setValue(['app:/weapon/v_404bigtank_maincannon.sgo', [1.0, 3.0],
                                            [10.0, 0.009999999776482582, 0.10000000149011612]])
            self.weaponWidgets[1].setValue(['app:/weapon/v_404bigtank_subcannonsolid.sgo', [0.05000000074505806, 0.5],
                                            [50.0, 0.009999999776482582, 0.10000000149011612]])
            self.weaponWidgets[2].setValue(['app:/weapon/v_404bigtank_subcannonsolid.sgo', [0.05000000074505806, 0.5],
                                            [50.0, 0.009999999776482582, 0.10000000149011612]])
            self.weaponWidgets[3].setValue(['app:/weapon/v_404bigtank_gatling.sgo', [0.0, 0.0]])
            self.weaponWidgets[4].setValue(['app:/weapon/v_404bigtank_sidemissile_l.sgo', [0.0, 0.0]])
            self.weaponWidgets[5].setValue(['app:/weapon/v_404bigtank_sidemissile_r.sgo', [0.0, 0.0]])

        elif self.vehicleSGO.value() == "app:/Object/Vehicle401_Striker.sgo":  # Grape
            self.baseHP = 650.0
            replaceParamsAndRemoveWeapons(self, GrapeParams)
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Turret", True, True, self.weaponMultiplier))
            self.weaponWidgets[0].setValue(['app:/weapon/v_401striker_cannon02.sgo', [0.009999999776482582, 0.10000000149011612], [180.0, 0.012000000104308128, 0.05000000074505806]])
            self.weaponWidgets[0].grid(row=0, column=0, sticky="N")

        elif self.vehicleSGO.value() == 'app:/Object/v507_rescuetank.sgo' or \
                self.vehicleSGO.value() == 'app:/Object/v507_rescuetank_siawase.sgo':  # Caliban
            self.baseHP = 1500.0
            replaceParamsAndRemoveWeapons(self, CalibanParams)

        elif self.vehicleSGO.value() == 'app:/Object/Vehicle402_Rocket.sgo':  # Naegling
            self.baseHP = 300.0
            replaceParamsAndRemoveWeapons(self, TankParams)
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Missile Pod", True, True, self.weaponMultiplier))
            self.weaponWidgets[0].setValue(['app:/weapon/v_402rocket_rocketcannon.sgo', [0.02500000037252903, 0.10000000149011612], [90.0, 0.007499999832361937, 0.05000000074505806]])
            self.weaponWidgets[0].grid(row=0, column=0, sticky="N")

        elif self.vehicleSGO.value() == 'app:/Object/v506_heli.sgo':  # Eros
            self.baseHP = 600.0

        elif self.vehicleSGO.value() == 'app:/Object/Vehicle409_heli.sgo':  # Nereid
            self.baseHP = 300.0

        elif self.vehicleSGO.value() == 'app:/Object/Vehicle410_heli.sgo':  # Brute
            self.baseHP = 1800.0

        elif self.vehicleSGO.value() in vehicleSGOS["Nix"].values():
            self.baseHP = 1200.0
            if not isinstance(self.vehicleParams, NixParams):
                replaceParamsAndRemoveWeapons(self, NixParams)
                self.weaponWidgets.append(VehicleWeaponChoice(self.col3, "Right hand", True, False, self.weaponMultiplier))
                self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Left hand", True, False, self.weaponMultiplier))
                self.weaponWidgets.append(VehicleWeaponChoice(self.col3, "Right lower arm", True, False, self.weaponMultiplier))
                self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Left lower arm", True, False, self.weaponMultiplier))
                self.weaponWidgets.append(VehicleWeaponChoice(self.col3, "Right shoulder", True, False, self.weaponMultiplier))
                self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Left shoulder", True, False, self.weaponMultiplier))
                self.weaponWidgets.append(VehicleWeaponChoice(self.col3, "Right upper arm", True, False, self.weaponMultiplier))
                self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Left upper arm", True, False, self.weaponMultiplier))

                self.weaponWidgets[4].pack()
                self.weaponWidgets[5].pack()
                self.weaponWidgets[6].pack()
                self.weaponWidgets[7].pack()
                self.weaponWidgets[2].pack()
                self.weaponWidgets[3].pack()
                self.weaponWidgets[0].pack()
                self.weaponWidgets[1].pack()

        elif self.vehicleSGO.value() == 'app:/Object/Vehicle407_bigbegaruta.sgo':
            self.baseHP = 7500.0
            replaceParamsAndRemoveWeapons(self, ProteusParams)
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Left cannon", True, False, self.weaponMultiplier))
            self.weaponWidgets.append(VehicleWeaponChoice(self.col3, "Right cannon", True, False, self.weaponMultiplier))
            self.weaponWidgets.append(VehicleWeaponChoice(self.col4, "Missiles", True, False, self.weaponMultiplier))
            self.weaponWidgets[0].setValue(['app:/weapon/v_407bigbegaruta_cannon.sgo', [0.0, 0.0]])
            self.weaponWidgets[1].setValue(['app:/weapon/v_407bigbegaruta_cannon.sgo', [0.0, 0.0]])
            self.weaponWidgets[2].setValue(['app:/weapon/v_407bigbegaruta_missile.sgo', [0.0, 0.0]])
            self.weaponWidgets[0].pack()
            self.weaponWidgets[1].pack()
            self.weaponWidgets[2].pack()

        elif self.vehicleSGO.value() == 'app:/Object/v512_keiTruck_bgp.sgo':  # Truck
            self.baseHP = 200.0

        elif self.vehicleSGO.value() == 'app:/Object/v503_bike.sgo' or \
                self.vehicleSGO.value() == 'app:/Object/v503_bike_omegaz.sgo':  # Bike
            self.baseHP = 150.0



    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class SmokeCandleBullet02(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SmokeCandleBullet02"))

    def value(self):
        pass

    def setValue(self):
        pass

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class SolidBullet01(tk.LabelFrame):
    def __init__(self, parent, isSubProjectile):
        tk.LabelFrame.__init__(self, parent, text=getText("SolidBullet01"))
        self.isSubProjectile = isSubProjectile
        self.isBouncy = DropDownWidget(self, "Is bouncy?",
                                       {"Not bouncy": 0, "Bouncy": 1, "Also not bouncy, likely dev mistake?": 2})
        self.enableExtra = CheckBoxWidget(self, "Enable extra options", 0, 1)
        self.enableExtra.input.trace_add("write", self.enableOrDisableExtra)
        self.hitEffectScale = FreeInputWidget(self, "Hit effect scale", float)
        self.unknown = FreeInputWidget(self, "Unknown float", float)

        self.isBouncy.pack()
        self.enableExtra.pack()
        self.enableExtra.pack()
        self.hitEffectScale.pack()
        self.unknown.pack()

        self.enableOrDisableExtra()

    def enableOrDisableExtra(self, *args):
        if self.enableExtra.value() == 0:
            disableInput(self.hitEffectScale)
            disableInput(self.unknown)
        else:
            enableInput(self.hitEffectScale)
            enableInput(self.unknown)

    def value(self):
        if self.enableExtra.value() != 1:
            if self.isBouncy.value() != 0:
                return [self.isBouncy.value()]
            else:
                if self.isSubProjectile:
                    return [0]
                else:
                    return None
        else:
            return [self.isBouncy.value(), self.hitEffectScale.value(), self.unknown.value()]

    def setValue(self, l):
        if l is None:
            self.isBouncy.setValue(0)
            self.enableExtra.setValue(0)
            self.hitEffectScale.setValue(1)
            self.unknown.setValue(0.25)
        elif len(l) > 1:
            self.isBouncy.setValue(l[0])
            self.enableExtra.setValue(1)
            self.hitEffectScale.setValue(l[1])
            self.unknown.setValue(l[2])
        else:
            self.isBouncy.setValue(l[0])
            self.enableExtra.setValue(0)
            self.hitEffectScale.setValue(1)
            self.unknown.setValue(0.25)

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class SolidBullet01Rail(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SolidBullet01Rail"))

    def value(self):
        return None

    def setValue(self, l):
        pass

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class SolidExpBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SolidExpBullet01"))

    def value(self):
        pass

    def setValue(self):
        pass

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class SolidPelletBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SolidPelletBullet01"))
        self.penetrationTime = FreeInputWidget(self, "Penetration duration", int, restrictPositive=True, initialValue=4,
                                               tooltip="How long the bullets in frames the bullets will maintain their penetraion property")
        self.penetrationTime.pack()

    def value(self):
        return [self.penetrationTime.value()]

    def setValue(self, l):
        self.penetrationTime.setValue(l[0])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class SpiderStringBullet02(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SpiderStringBullet02"))
        self.unknown = FreeInputWidget(self, "Unknown float", float, tooltip="0.1 or 0.025, maybe thickness?")
        self.unknown.pack()

    def value(self):
        return [self.unknown.value()]

    def setValue(self, l):
        self.unknown.setValue(l[0])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class SupportUnitBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SupportUnitBullet02"))
        self.buffType = DropDownWidget(self, "Buff type",
                                       {"Health": 0, "Wing diver energy": 1, "Defense": 2, "Power": 3},
                                       tooltip="Other parameters are controlled by parameters.\nDamage = heal amount or stat multiplier\nExplosion radius = buff radius\nAmmo lifetime = buff duration")
        self.offsetFrame = tk.LabelFrame(self, text="Buff stream offset")
        self.offsetX = FreeInputWidget(self.offsetFrame, "X", float)
        self.offsetY = FreeInputWidget(self.offsetFrame, "Y", float)
        self.offsetZ = FreeInputWidget(self.offsetFrame, "Z", float)

        self.buffType.pack()
        self.offsetFrame.pack()
        self.offsetX.pack()
        self.offsetY.pack()
        self.offsetZ.pack()

    def value(self):
        return [self.buffType.value(), [self.offsetX.value(), self.offsetY.value(), self.offsetZ.value()]]

    def setValue(self, l):
        self.buffType.setValue(l[0])
        self.offsetX.setValue(l[1][0])
        self.offsetY.setValue(l[1][1])
        self.offsetZ.setValue(l[1][2])

    def test(self):
        print(self.__class__.__name__)
        testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
        testValues = [eval(key) for key in testDict.keys()]
        for v in testValues:
            self.setValue(v)
            if v != self.value():
                print(v)
                print(self.value())
                raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
        print(f"{self.__class__.__name__} tests successful")


class TargetMarkerBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("TargetMarkerBullet01"))

    def value(self):
        pass

    def setValue(self):
        pass
