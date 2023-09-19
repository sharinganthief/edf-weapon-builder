from widgets.EDFWidgets import *
from widgets.vehicleSummon import *
import math
from py_linq import Enumerable

# e = j.loadDataFromJson("./data/alleasy.json")
# u = d.uniqueDataByKey("AmmoClass", ["Ammo_CustomParameter"], e)
ammoCust = j.loadDataFromJson("./data/ammoCust.json")

def flatten(S):
    # https://stackoverflow.com/questions/12472338/flattening-a-list-recursively?lq=1
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

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

def testAmmoCust(ammoClass):
    print(ammoClass.__class__.__name__)
    testDict = ammoCust[ammoClass.__class__.__name__]["Ammo_CustomParameter"]
    testValues = [eval(key) for key in testDict.keys()]
    for v in testValues:
        # if ammoClass.__class__.__name__ == "SmokeCandleBullet02":
        #     print(v)
        ammoClass.setValue(v)
        if isinstance(v, list):
            flatV = flatten(v)
            flatACV = flatten(ammoClass.value())
            for i in range(len(flatV)):
                if isinstance(flatV[i], float):
                    if math.fabs(flatV[i] - flatACV[i]) > 0.000001:
                        print(v)
                        print(ammoClass.value())
                        raise ValueError(f"actual\n{ammoClass.value()}\n!=expected\n{v}")
                elif isinstance(flatV[i], str):
                    if flatV[i].lower() != flatACV[i].lower():
                        print(v)
                        print(ammoClass.value())
                        raise ValueError(f"actual\n{ammoClass.value()}\n!=expected\n{v}")
                elif flatV[i] != flatACV[i]:
                    print(f"{flatV[i]} != {flatACV[i]}")
                    # print(v)
                    # print(ammoClass.value())
                    raise ValueError(f"actual\n{ammoClass.value()}\n!=expected\n{v}")
        else:
            if v != ammoClass.value():
                print(v)
                print(ammoClass.value())
                raise ValueError(f"actual\n{ammoClass.value()}\n!=expected\n{v}")

        # if isinstance(v, float):
        #     if math.fabs(v - ammoClass.value()) > 0.000001:
        #         print(v)
        #         print(ammoClass.value())
        #         raise ValueError(f"actual\n{ammoClass.value()}\n!=expected\n{v}")
        # elif v != ammoClass.value():
        #     print(v)
        #     print(ammoClass.value())
        #     raise ValueError(f"actual\n{ammoClass.value()}\n!=expected\n{v}")
    print(f"{ammoClass.__class__.__name__} tests successful")

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
    # "SentryGunBullet01": "SentryGunBullet01",
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
stickingSounds = {
    "None": 0,
    "C4 stick A": '武器Ｃ系爆弾接地Ａ',
    "C4 stick B": '武器Ｃ系爆弾接地Ｂ',
    "C4 stick C": '武器Ｃ系爆弾接地Ｃ',
    "Limpet small": '武器リモート爆弾小着弾',
    "Limpet big": '武器リモート爆弾大着弾',
    "Limpet flechette": '武器フレシェット着弾',
    "Assault beetle": 'むしむしボンバー張り付き',
    "Roomba": 'ルン爆弾ＧＯ',
    "Roomba heavy": 'ルン爆弾ＧＯ重い'
}
armingSounds = {
    "None": 0,
    "Bomb armed": '武器起動可能'
}
detectionSounds = {
    "None": 0,
    "Enemy detected": '敵探知'
}
bounceSounds = {
    "None": 0,
    "Assault beetle bounce": 'むしむしボンバー跳ねる',
    "Roomba bounce": 'ルン爆弾反射',
    "Roomba heavy bounce": 'ルン爆弾反射重い'
}
class AcidBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("AcidBullet01"))
        self.v1 = None
        self.v1Input = FreeInputWidget(self, "Unknown float", float, tooltip="-0.03 or -0.004", initialValue=-0.004)
        self.v1Input.pack()

    def value(self):
        return [self.v1]

    def setValue(self, v):
        self.v1 = v[0]
        self.v1Input.setValue(self.v1)
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
        self.v1.setValue(get_value_from_dict_or_val(l,float,0))
        self.v2.setValue(get_value_from_dict_or_val(l,float,1))
        self.v3.setValue(get_value_from_dict_or_val(l,float,2))
        self.v4.setValue(get_value_from_dict_or_val(l,float,3,0))
        self.v5.setValue(get_value_from_dict_or_val(l,float,3,1))
        self.v6.setValue(get_value_from_dict_or_val(l,float,3,2))
        self.v7.setValue(get_value_from_dict_or_val(l,float,4,0))
        self.v8.setValue(get_value_from_dict_or_val(l,float,4,1))
        self.v9.setValue(get_value_from_dict_or_val(l,float,4,2))
class BombBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("BombBullet01"))
        self.bombOptions = {
            "C4/Mine": 0,
            "Patroller": 1,
            "Assault beetle": 2,
            "Roomba bomb (Requires lock-on)": 3
        }
        self.explosionOptions = {
            "Standard": 0,
            "Splendor": 1,
            "Sniper": 2
        }
        self.bombType = DropDownWidget(self, "Bomb type", self.bombOptions)
        # self.isDetector = CheckBoxWidget(self, "Is detector", 0, 1)
        self.isDetector = DropDownWidget(self, "Detector type", {"None": 0, "Angle detector (splendor only)": 1, "Proximity detector": 2})
        self.bounceFactor = FreeInputWidget(self, "Bounce factor", float, initialValue=0.0)
        self.primerDelay = FreeInputWidget(self, "Priming delay", int, restrictPositive=True,
                                           tooltip="In frames. Usually 0 for limpet, 30 for detectors")
        self.detonationInterval = FreeInputWidget(self, "Detonation interval", int, tooltip="Time between manually triggered bomb explosions")

        self.LEDFrame = tk.LabelFrame(self, text=getText("LED Position"))
        self.LEDX = FreeInputWidget(self.LEDFrame, "X", float, initialValue=0.0)
        self.LEDY = FreeInputWidget(self.LEDFrame, "Y", float, initialValue=0.5)
        self.LEDZ = FreeInputWidget(self.LEDFrame, "Z", float, initialValue=0.0)

        self.explosionType = DropDownWidget(self, "Explosion type", self.explosionOptions)
        self.explosionType.dropDownDisplayed.trace_add("write", self.enableOrDisableSplendor)

        self.splendorFrame = tk.LabelFrame(self, text=getText("Splendor configuration"))
        # self.hSpread = SliderWidget(self.splendorFrame, "Horizontal spread", 0, 1)
        # self.vSpread = SliderWidget(self.splendorFrame, "Vertical spread", 0, 1)
        self.hSpread = AngleWidget(self.splendorFrame, "Horizontal spread")
        self.vSpread = AngleWidget(self.splendorFrame, "Vertical spread")
        self.vAngle = AngleWidget(self.splendorFrame, "Vertical angle")

        self.flechetteCount = FreeInputWidget(self.splendorFrame, "Flechette count", int, restrictPositive=True, initialValue=40)
        self.flechetteLifetime = FreeInputWidget(self.splendorFrame, "Flechette lifetime", int, restrictPositive=True, initialValue=120)
        self.flechetteSpeed = FreeInputWidget(self.splendorFrame, "Flechette speed", float, restrictPositive=True, initialValue=2.0)
        self.flechetteSize = FreeInputWidget(self.splendorFrame, "Flechette size", float, restrictPositive=True,
                                             initialValue=0.5)
        # self.unknown3 = FreeInputWidget(self.splendorFrame, "Unknown int", int, tooltip="Always 1?", initialValue=1)
        self.ammoCust = SolidBullet01(self.splendorFrame, True)

        self.stickSound = DropDownWidget(self, "Contact sound", stickingSounds)
        self.armingSound = DropDownWidget(self, "Arming sound", armingSounds)
        self.detectionSound = DropDownWidget(self, "Detection sound", detectionSounds)
        self.bounceSound = DropDownWidget(self, "Bounce sound", bounceSounds)

        self.bombType.pack()
        self.isDetector.pack()
        self.bounceFactor.pack()
        self.primerDelay.pack()
        self.detonationInterval.pack()
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
        # self.unknown3.pack()
        self.ammoCust.pack()
        self.stickSound.pack()
        self.armingSound.pack()
        self.detectionSound.pack()
        self.bounceSound.pack()

        self.enableOrDisableSplendor()

    def value(self):
        v = [self.bombType.value(), self.isDetector.value(), self.bounceFactor.value(), self.primerDelay.value(),
             self.detonationInterval.value(),
             [self.LEDX.value(), self.LEDY.value(), self.LEDZ.value()],
             self.explosionType.value()]
        if self.explosionType.value() == 1:
            v.append([[self.hSpread.value(),
                       self.vSpread.value(),
                       self.vAngle.value()],
                      self.flechetteCount.value(),
                      self.flechetteLifetime.value(),
                      self.flechetteSpeed.value(),
                      self.flechetteSize.value(), self.ammoCust.value()])
        else:
            v.append(None)

        v.append([self.stickSound.value(),
                  self.armingSound.value(),
                  self.detectionSound.value(),
                  self.bounceSound.value()])
        return v

    def setValue(self, l):
        self.bombType.setValue(get_value_from_dict_or_val(l,float,0))
        self.isDetector.setValue(get_value_from_dict_or_val(l,float,1))
        self.bounceFactor.setValue(get_value_from_dict_or_val(l,float,2))
        self.primerDelay.setValue(get_value_from_dict_or_val(l,float,3))
        self.detonationInterval.setValue(get_value_from_dict_or_val(l,float,4))
        self.LEDX.setValue(get_value_from_dict_or_val(l,float,5,0))
        self.LEDY.setValue(get_value_from_dict_or_val(l,float,5,1))
        self.LEDZ.setValue(get_value_from_dict_or_val(l,float,5,2))
        self.explosionType.setValue(get_value_from_dict_or_val(l,float,6))
        if l[6] == 1:
            self.hSpread.setValue(l[7][0][0])
            self.vSpread.setValue(l[7][0][1])
            self.vAngle.setValue(l[7][0][2])
            self.flechetteCount.setValue(get_value_from_dict_or_val(l,float,7,1))
            self.flechetteLifetime.setValue(get_value_from_dict_or_val(l,float,7,2))
            self.flechetteSpeed.setValue(get_value_from_dict_or_val(l,float,7,3))
            self.flechetteSize.setValue(get_value_from_dict_or_val(l,float,7,4))
            self.ammoCust.setValue(get_value_from_dict_or_val(l,float,7,5))
            self.enableSplendor()
        else:
            self.disableSplendor()
        self.stickSound.setValue(get_value_from_dict_or_val(l,float,8,0))
        self.armingSound.setValue(get_value_from_dict_or_val(l,float,8,1))
        self.detectionSound.setValue(get_value_from_dict_or_val(l,float,8,2))
        self.bounceSound.setValue(get_value_from_dict_or_val(l,float,8,3))

    def enableOrDisableSplendor(self, *args):
        if self.explosionType.value() == 1:
            self.enableSplendor()
        else:
            self.disableSplendor()

    def enableSplendor(self):
        self.splendorFrame.pack()
        enableInput(self.hSpread.input)
        enableInput(self.vSpread.input)
        enableInput(self.vAngle.input)
        enableInput(self.flechetteCount)
        enableInput(self.flechetteLifetime)
        enableInput(self.flechetteSpeed)
        enableInput(self.flechetteSize)
        # enableInput(self.unknown3)

    def disableSplendor(self):
        self.splendorFrame.pack_forget()
        disableInput(self.hSpread.input)
        disableInput(self.vSpread.input)
        disableInput(self.vAngle.input)
        disableInput(self.flechetteCount)
        disableInput(self.flechetteLifetime)
        disableInput(self.flechetteSpeed)
        disableInput(self.flechetteSize)
        # disableInput(self.unknown3)
class BombBullet02(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("BombBullet01"))
        self.bombOptions = {
            "C4/Mine": 0,
            "Patroller": 1,
            "Assault beetle": 2,
            "Roomba bomb (Requires lock-on)": 3
        }
        self.explosionOptions = {
            "Standard": 0,
            "Splendor": 1,
            "Sniper": 2
        }
        self.bombType = DropDownWidget(self, "Bomb type", self.bombOptions)
        # self.isDetector = CheckBoxWidget(self, "Is detector", 0, 1)
        self.isDetector = DropDownWidget(self, "Detector type", {"None": 0, "Angle detector (splendor only)": 1, "Proximity detector": 2})
        self.bounceFactor = FreeInputWidget(self, "Bounce factor", float, initialValue=0.0)
        self.primerDelay = FreeInputWidget(self, "Priming delay", int, restrictPositive=True,
                                           tooltip="In frames. Usually 0 for limpet, 30 for detectors")
        self.detonationInterval = FreeInputWidget(self, "Detonation interval", int, tooltip="Time between manually triggered bomb explosions")

        self.LEDFrame = tk.LabelFrame(self, text=getText("LED Position"))
        self.LEDX = FreeInputWidget(self.LEDFrame, "X", float, initialValue=0.0)
        self.LEDY = FreeInputWidget(self.LEDFrame, "Y", float, initialValue=0.5)
        self.LEDZ = FreeInputWidget(self.LEDFrame, "Z", float, initialValue=0.0)

        self.explosionType = DropDownWidget(self, "Explosion type", self.explosionOptions)
        self.explosionType.dropDownDisplayed.trace_add("write", self.enableOrDisableSplendor)

        self.splendorFrame = tk.LabelFrame(self, text=getText("Splendor configuration"))
        # self.hSpread = SliderWidget(self.splendorFrame, "Horizontal spread", 0, 1)
        # self.vSpread = SliderWidget(self.splendorFrame, "Vertical spread", 0, 1)
        self.hSpread = AngleWidget(self.splendorFrame, "Horizontal spread")
        self.vSpread = AngleWidget(self.splendorFrame, "Vertical spread")
        self.vAngle = AngleWidget(self.splendorFrame, "Vertical angle")

        self.flechetteCount = FreeInputWidget(self.splendorFrame, "Flechette count", int, restrictPositive=True, initialValue=40)
        self.flechetteLifetime = FreeInputWidget(self.splendorFrame, "Flechette lifetime", int, restrictPositive=True, initialValue=120)
        self.flechetteSpeed = FreeInputWidget(self.splendorFrame, "Flechette speed", float, restrictPositive=True, initialValue=2.0)
        self.flechetteSize = FreeInputWidget(self.splendorFrame, "Flechette size", float, restrictPositive=True,
                                             initialValue=0.5)
        # self.unknown3 = FreeInputWidget(self.splendorFrame, "Unknown int", int, tooltip="Always 1?", initialValue=1)
        self.ammoCust = SolidBullet01(self.splendorFrame, True)

        self.stickSound = DropDownWidget(self, "Contact sound", stickingSounds)
        self.armingSound = DropDownWidget(self, "Arming sound", armingSounds)
        self.detectionSound = DropDownWidget(self, "Detection sound", detectionSounds)
        self.bounceSound = DropDownWidget(self, "Bounce sound", bounceSounds)

        self.bombType.pack()
        self.isDetector.pack()
        self.bounceFactor.pack()
        self.primerDelay.pack()
        self.detonationInterval.pack()
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
        # self.unknown3.pack()
        self.ammoCust.pack()
        self.stickSound.pack()
        self.armingSound.pack()
        self.detectionSound.pack()
        self.bounceSound.pack()

        self.enableOrDisableSplendor()

    def value(self):
        v = [self.bombType.value(), self.isDetector.value(), self.bounceFactor.value(), self.primerDelay.value(),
             self.detonationInterval.value(),
             [self.LEDX.value(), self.LEDY.value(), self.LEDZ.value()],
             self.explosionType.value()]
        if self.explosionType.value() == 1:
            v.append([[self.hSpread.value(),
                       self.vSpread.value(),
                       self.vAngle.value()],
                      self.flechetteCount.value(),
                      self.flechetteLifetime.value(),
                      self.flechetteSpeed.value(),
                      self.flechetteSize.value(), self.ammoCust.value()])
        else:
            v.append(None)

        v.append([self.stickSound.value(),
                  self.armingSound.value(),
                  self.detectionSound.value(),
                  self.bounceSound.value()])
        return v

    def setValue(self, l):
        self.bombType.setValue(get_value_from_dict_or_val(l,float,0))
        self.isDetector.setValue(get_value_from_dict_or_val(l,float,1))
        self.bounceFactor.setValue(get_value_from_dict_or_val(l,float,2))
        self.primerDelay.setValue(get_value_from_dict_or_val(l,float,3))
        self.detonationInterval.setValue(get_value_from_dict_or_val(l,float,4))
        self.LEDX.setValue(get_value_from_dict_or_val(l,float,5,0))
        self.LEDY.setValue(get_value_from_dict_or_val(l,float,5,1))
        self.LEDZ.setValue(get_value_from_dict_or_val(l,float,5,2))
        self.explosionType.setValue(get_value_from_dict_or_val(l,float,6))
        if l[6] == 1:
            self.hSpread.setValue(l[7][0][0])
            self.vSpread.setValue(l[7][0][1])
            self.vAngle.setValue(l[7][0][2])
            self.flechetteCount.setValue(get_value_from_dict_or_val(l,float,7,1))
            self.flechetteLifetime.setValue(get_value_from_dict_or_val(l,float,7,2))
            self.flechetteSpeed.setValue(get_value_from_dict_or_val(l,float,7,3))
            self.flechetteSize.setValue(get_value_from_dict_or_val(l,float,7,4))
            self.ammoCust.setValue(get_value_from_dict_or_val(l,float,7,5))
            self.enableSplendor()
        else:
            self.disableSplendor()
        self.stickSound.setValue(get_value_from_dict_or_val(l,float,8,0))
        self.armingSound.setValue(get_value_from_dict_or_val(l,float,8,1))
        self.detectionSound.setValue(get_value_from_dict_or_val(l,float,8,2))
        self.bounceSound.setValue(get_value_from_dict_or_val(l,float,8,3))

    def enableOrDisableSplendor(self, *args):
        if self.explosionType.value() == 1:
            self.enableSplendor()
        else:
            self.disableSplendor()

    def enableSplendor(self):
        self.splendorFrame.pack()
        enableInput(self.hSpread.input)
        enableInput(self.vSpread.input)
        enableInput(self.vAngle.input)
        enableInput(self.flechetteCount)
        enableInput(self.flechetteLifetime)
        enableInput(self.flechetteSpeed)
        enableInput(self.flechetteSize)
        # enableInput(self.unknown3)

    def disableSplendor(self):
        self.splendorFrame.pack_forget()
        disableInput(self.hSpread.input)
        disableInput(self.vSpread.input)
        disableInput(self.vAngle.input)
        disableInput(self.flechetteCount)
        disableInput(self.flechetteLifetime)
        disableInput(self.flechetteSpeed)
        disableInput(self.flechetteSize)
        # disableInput(self.unknown3)
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
        self.momentumConservation.setValue(get_value_from_dict_or_val(l,float,0))
        self.projectileSpread.setValue(get_value_from_dict_or_val(l,float,1))
        self.projectileAccuracy.setValue(get_value_from_dict_or_val(l,float,2))
        self.projectileDirection.setValue(get_value_from_dict_or_val(l,float,3))
        if l[4] != 0:
            self.homingEnabled.setValue(get_value_from_dict_or_val(l,float,4,0))
            self.homingLockRadius.setValue(get_value_from_dict_or_val(l,float,4,1))
        else:
            self.homingEnabled.setValue(0)
            self.homingLockRadius.setValue(0)
        self.subProjectileWidget.setValue(get_value_from_dict_or_val(l,float,5))
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
        # self.sound3 = SoundWidget(self.col2, "Other sound?", returnNoneOr0=0)
        # self.sound4 = SoundWidget(self.col2, "Other Other sound?", returnNoneOr0=0)

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
        # self.sound3.pack()
        # self.sound4.pack()

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
        if type(l) is dict and 'value' in l:
            temp = l['value']
            l = temp
        self.unknown1.setValue(get_value_from_dict_or_val(l, float, 0, 0))
        self.unknown2.setValue(get_value_from_dict_or_val(l, float, 0, 1))
        self.unknown3.setValue(get_value_from_dict_or_val(l, float, 1, 0))
        self.unknown4.setValue(get_value_from_dict_or_val(l, float, 1, 1))
        self.projectileCount.setValue(get_value_from_dict_or_val(l,float,2))
        self.projectileInterval.setValue(get_value_from_dict_or_val(l,float,3))
        self.ammoClass.setValue(get_value_from_dict_or_val(l,str,4))
        self.ammoSpeed.setValue(get_value_from_dict_or_val(l,float,5))
        self.ammoGravity.setValue(get_value_from_dict_or_val(l,float,6))
        self.ammoScale.setValue(get_value_from_dict_or_val(l,float,7))
        self.unknown5.setValue(get_value_from_dict_or_val(l,float,8))
        self.explosionRadius.setValue(get_value_from_dict_or_val(l,float,9))
        self.ammoLifetime.setValue(get_value_from_dict_or_val(l,float,10))
        self.unknown6.setValue(get_value_from_dict_or_val(l,float,11))
        self.ammoColor.setValue(l[12])
        self.customParamWidget.setValue(l[13])
        self.ammoModel.setValue(l[14])
        self.unknown7.setValue(get_value_from_dict_or_val(l,float,15))
        self.unknown8.setValue(get_value_from_dict_or_val(l,float,16))
        self.sound1.setValue(l[17])
        self.sound2.setValue(l[18])
        # self.sound3.setValue(l[19])
        # self.sound4.setValue(l[20])

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
        self.alphaChange = SliderWidget(self.colorFrame, "Alpha change", -1, 0, resolution=0.01, initialValue=0)

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
        self.flameType.setValue(get_value_from_dict_or_val(l,float,0))
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,1))
        self.unknown2.setValue(get_value_from_dict_or_val(l,float,2))
        self.unknown3.setValue(get_value_from_dict_or_val(l,float,3))
        self.redChange.setValue(get_value_from_dict_or_val(l,float,4,0))
        self.blueChange.setValue(get_value_from_dict_or_val(l,float,4,1))
        self.greenChange.setValue(get_value_from_dict_or_val(l,float,4,2))
        self.alphaChange.setValue(get_value_from_dict_or_val(l,float,4,3))
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
        self.detonationType.setValue(get_value_from_dict_or_val(l,float,0))
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,1))
        self.unknown2.setValue(get_value_from_dict_or_val(l,float,2))
        self.bounceDampening.setValue(get_value_from_dict_or_val(l,float,3))
        self.smokeTrailNoise.setValue(get_value_from_dict_or_val(l,float,4))
        self.smokeTrailLifetime.setValue(get_value_from_dict_or_val(l,float,5))
        if len(l) > 6:
            self.fuseVariation.setValue(get_value_from_dict_or_val(l,float,6))
        else:
            self.fuseVariation.setValue(0)
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
        self.fireDirection.setValue(get_value_from_dict_or_val(l, int, 0))
        self.unknown2.setValue(get_value_from_dict_or_val(l, int, 1))
        self.trailLength.setValue(get_value_from_dict_or_val(l, int, 2))
        self.homingFactor.setValue(get_value_from_dict_or_val(l, float, 3))
        self.homingFactor2.setValue(get_value_from_dict_or_val(l, float, 4))
        self.speedScale.setValue(get_value_from_dict_or_val(l, float, 5))
        self.homingDelay.setValue(get_value_from_dict_or_val(l, int, 6))
        self.unknown6.setValue(get_value_from_dict_or_val(l, int, 7))
        self.unknown7.setValue(get_value_from_dict_or_val(l, float, 8))
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
        self.flareColor.setValue(get_value_from_dict_or_val(l,list,0))
        self.flareLightColor.setValue(get_value_from_dict_or_val(l,list,1))
        self.flareScale.setValue(get_value_from_dict_or_val(l,float,2))
        self.flareLightScale.setValue(get_value_from_dict_or_val(l,float,3))
        self.flareLife.setValue(get_value_from_dict_or_val(l,float,4))
        self.numLasers.setValue(get_value_from_dict_or_val(l,float,5))
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,6))
        self.unknown2.setValue(get_value_from_dict_or_val(l,float,7))
        self.laserSpreadSpeed.setValue(get_value_from_dict_or_val(l,float,8))
        self.laserSpeed.setValue(get_value_from_dict_or_val(l,float,9))
        self.laserSegments.setValue(get_value_from_dict_or_val(l,float,10))
        if len(l) > 11:
            self.unknown3.setValue(get_value_from_dict_or_val(l,float,11))
        else:
            self.unknown3.setValue(0)
class LaserBullet02(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("LaserBullet02"))
        self.laserType = DropDownWidget(self, "Laser type", {"Simple laser": 0, "Pulse laser": 1, "Genocide gun": 2})
        self.laserType.pack()

    def value(self):
        return [self.laserType.value()]

    def setValue(self, v):
        self.laserType.setValue(v[0])
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
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,0))
        self.unknown2.setValue(get_value_from_dict_or_val(l,float,1))
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
        self.initialNoise.setValue(get_value_from_dict_or_val(l,float,0))
        self.randomVelocity.setValue(get_value_from_dict_or_val(l,float,1))
        self.curveNoise.setValue(get_value_from_dict_or_val(l,float,2))
        self.bounceFactor.setValue(get_value_from_dict_or_val(l,float,3))
        self.boltModifier.setValue(get_value_from_dict_or_val(l,float,4))
        if len(l) > 5:
            self.optional1.setValue(get_value_from_dict_or_val(l,float,5))
        else:
            self.optional1.setValue(0)
        if len(l) > 6:
            self.optional2.setValue(get_value_from_dict_or_val(l,float,6))
        else:
            self.optional2.setValue(0)
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
        self.missileOption.setValue(get_value_from_dict_or_val(l,float,0))
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,1))
        self.unknown2.setValue(get_value_from_dict_or_val(l,float,2))
        self.unknown3.setValue(get_value_from_dict_or_val(l,float,3,0))
        self.unknown4.setValue(get_value_from_dict_or_val(l,float,3,1))
        self.unknown5.setValue(get_value_from_dict_or_val(l,float,3,2))
        self.accelerationRate.setValue(get_value_from_dict_or_val(l,float,4))
        self.turnRate.setValue(get_value_from_dict_or_val(l,float,5))
        self.topSpeed.setValue(get_value_from_dict_or_val(l,float,6))
        self.unknown6.setValue(get_value_from_dict_or_val(l,float,7,0))
        self.unknown7.setValue(get_value_from_dict_or_val(l,float,7,1))
        self.homingDelay.setValue(get_value_from_dict_or_val(l,float,8))
        self.unknown8.setValue(get_value_from_dict_or_val(l,float,9))
        if l[10] is not None:
            self.enableStruct.setValue(True)
            self.unknown9.setValue(get_value_from_dict_or_val(l,float,10,0))
            self.unknown10.setValue(get_value_from_dict_or_val(l,float,10,1))
            self.enableOrDisableStruct3()
        else:
            self.enableStruct.setValue(False)
            self.enableOrDisableStruct3()

        self.ignitionSound.setValue(get_value_from_dict_or_val(l,float,11))
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
        self.missileOption.setValue(get_value_from_dict_or_val(l,float,0))
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,1))
        self.unknown2.setValue(get_value_from_dict_or_val(l,float,2))
        self.unknown3.setValue(get_value_from_dict_or_val(l,float,3,0))
        self.unknown4.setValue(get_value_from_dict_or_val(l,float,3,1))
        self.unknown5.setValue(get_value_from_dict_or_val(l,float,3,2))
        self.accelerationRate.setValue(get_value_from_dict_or_val(l,float,4))
        self.turnRate.setValue(get_value_from_dict_or_val(l,float,5))
        self.topSpeed.setValue(get_value_from_dict_or_val(l,float,6))
        self.unknown6.setValue(get_value_from_dict_or_val(l,float,7,0))
        self.unknown7.setValue(get_value_from_dict_or_val(l,float,7,1))
        self.homingDelay.setValue(get_value_from_dict_or_val(l,float,8))
        self.unknown8.setValue(get_value_from_dict_or_val(l,float,9))
        if l[10] is not None:
            self.enableStruct.setValue(True)
            self.unknown9.setValue(get_value_from_dict_or_val(l,float,10,0))
            self.unknown10.setValue(get_value_from_dict_or_val(l,float,10,1))
            self.enableOrDisableStruct3()
        else:
            self.enableStruct.setValue(False)
            self.enableOrDisableStruct3()

        self.ignitionSound.setValue(get_value_from_dict_or_val(l,float,11))
        if l[12][0] == 0:
            self.struct4Choice.setValue(get_value_from_dict_or_val(l,float,12,0))
            self.struct4Type0Float1.setValue(get_value_from_dict_or_val(l,float,12,1))
            self.struct4Type0Float2.setValue(get_value_from_dict_or_val(l,float,12,2))
        elif l[12][0] == 1:
            self.struct4Choice.setValue(get_value_from_dict_or_val(l,float,12,0))
            self.struct4Type1Int.setValue(get_value_from_dict_or_val(l,float,12,1))
        self.struct5Int.setValue(get_value_from_dict_or_val(l,float,13,0))
        self.struct5Float1.setValue(get_value_from_dict_or_val(l,float,13,1))
        self.projectileSpread.setValue(get_value_from_dict_or_val(l,float,13,2))
        self.struct6Int.setValue(get_value_from_dict_or_val(l,float,14,0))
        self.struct6Float.setValue(get_value_from_dict_or_val(l,float,14,1))
        self.subProjectile.setValue(get_value_from_dict_or_val(l,float,15))
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
        sub_data = self.subProjectile.value()
        emitter_data = self.emitterSound.value()

        return [
            self.unknown1.value(),
            [self.hSpread.value(),
             self.vSpread.value()],
            self.trailNoise.value(),
            self.subProjectileSize.value(),
            sub_data,
            emitter_data]

    def setValue(self, l):
        self.unknown1.setValue(get_value_from_dict_or_val(l, float, 0))
        self.hSpread.setValue(get_value_from_dict_or_val(l, float, 1, 0))
        self.vSpread.setValue(get_value_from_dict_or_val(l, float, 1, 1))
        self.trailNoise.setValue(get_value_from_dict_or_val(l, float, 2))
        self.subProjectileSize.setValue(get_value_from_dict_or_val(l, float, 3))
        self.subProjectile.setValue(l[4])
        self.emitterSound.setValue(l[5])
class NeedleBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("NeedleBullet01"))
        self.unknown = FreeInputWidget(self, "Unknown int", int, tooltip="Always 1")
        self.unknown.pack()

    def value(self):
        return [self.unknown.value()]

    def setValue(self, l):
        self.unknown.setValue(get_value_from_dict_or_val(l,float,0))
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
        self.hitSound.setValue(get_value_from_dict_or_val(l,float,0))
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
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,0))
        self.unknown2.setValue(get_value_from_dict_or_val(l,float,1))
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
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,0))
        self.unknown2.setValue(get_value_from_dict_or_val(l,float,1,0))
        self.unknown3.setValue(get_value_from_dict_or_val(l,float,1,1))
        self.unknown4.setValue(get_value_from_dict_or_val(l,float,1,2))
        self.unknown5.setValue(get_value_from_dict_or_val(l,float,1,3))
        self.unknown6.setValue(get_value_from_dict_or_val(l,float,2,0))
        self.unknown7.setValue(get_value_from_dict_or_val(l,float,2,1))
        self.unknown8.setValue(get_value_from_dict_or_val(l,float,2,2))
        self.unknown9.setValue(get_value_from_dict_or_val(l,float,2,3))
        self.unknown10.setValue(get_value_from_dict_or_val(l,float,3))
        self.unknown11.setValue(get_value_from_dict_or_val(l,float,4))
        self.unknown12.setValue(get_value_from_dict_or_val(l,float,5))
        self.unknown13.setValue(get_value_from_dict_or_val(l,float,6))
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
        self.rocketType.setValue(get_value_from_dict_or_val(l,float,0))
        self.smokeTrailLifetime.setValue(get_value_from_dict_or_val(l,float,1))
        self.ignitionDelay.setValue(get_value_from_dict_or_val(l,float,2))
        self.smokeTrailDrift.setValue(get_value_from_dict_or_val(l,float,3))
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
        self.friendlyFire.setValue(get_value_from_dict_or_val(l,float,0))
        # self.unknown1.setValue(get_value_from_dict_or_val(l,float,1))
        # self.unknown2.setValue(get_value_from_dict_or_val(l,float,2))
        self.unknown3.setValue(get_value_from_dict_or_val(l,float,3))
        self.searchRange.setValue(get_value_from_dict_or_val(l,float,4))
        self.turnSpeed.setValue(get_value_from_dict_or_val(l,float,5))
        self.unknown4.setValue(get_value_from_dict_or_val(l,float,6))
        # self.firingBone.setValue(get_value_from_dict_or_val(l,float,7))
        self.offsetX.setValue(get_value_from_dict_or_val(l,float,8,0))
        self.offsetY.setValue(get_value_from_dict_or_val(l,float,8,1))
        self.offsetZ.setValue(get_value_from_dict_or_val(l,float,8,2))
        self.ammoClass.setValue(get_value_from_dict_or_val(l,float,9))
        self.ammoCount.setValue(get_value_from_dict_or_val(l,float,10))
        self.fireInterval.setValue(get_value_from_dict_or_val(l,float,11))
        self.ammoLifetime.setValue(get_value_from_dict_or_val(l,float,12))
        self.ammoSpeed.setValue(get_value_from_dict_or_val(l,float,13))
        if isinstance(l[14], list):
            self.ammoVisualMultiplier.setValue(get_value_from_dict_or_val(l,float,14,0))
            self.ammoHitboxMultiplier.setValue(get_value_from_dict_or_val(l,float,14,1))
        else:
            self.ammoVisualMultiplier.setValue(get_value_from_dict_or_val(l,float,14))
            self.ammoHitboxMultiplier.setValue(get_value_from_dict_or_val(l,float,14))
        self.ammoCustWidget.setValue(get_value_from_dict_or_val(l,float,15))
        self.firingSound.setValue(get_value_from_dict_or_val(l,float,16))
        self.muzzleFlash.muzzleFlashType.setValue(get_value_from_dict_or_val(l,float,17))
        if l[17] != "":
            self.muzzleFlash.paramsWidget.setValue(get_value_from_dict_or_val(l,float,18))
        # else:
        #     self.muzzleFlash.paramsWidget
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
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,0))
        self.unknown2.setValue(get_value_from_dict_or_val(l,float,1))
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
            self.shockwaveType.setValue(l[0] if isinstance(l[0], int) else int(l[0]['value']))
            self.unknown.setValue(l[1] if isinstance(l[1], int) else int(l[1]['value']))
        else:
            self.shockwaveType.setValue(None)
class SmokeCandleBullet02(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SmokeCandleBullet02"))
        self.col1 = tk.Frame(self)
        self.col2 = tk.Frame(self)
        self.unknown1 = FreeInputWidget(self.col1, "Unknown float", float, initialValue=0.05000000074505806,
                                        tooltip="Always 0.05000000074505806?")
        self.smokeLifetime = FreeInputWidget(self.col1, "Smoke lifetime/size", int, initialValue=180,
                                             restrictPositive=True)
        self.summonDelay = FreeInputWidget(self.col1, "Summon delay", int, initialValue=120, restrictPositive=True)
        self.summonType = FreeInputWidget(self.col1, "Summon type", int, initialValue=0, tooltip="Always 0?")
        self.airSupportParams = AirSupportParams(self.col2)
        self.firingVoice = SoundWidget(self.col1, "Sound", "")
        self.voice2 = SoundWidget(self.col1, "Sound", "")
        self.endingVoice = SoundWidget(self.col1, "Sound", "")

        self.col1.grid(row=0, column=0, sticky="N")
        self.col2.grid(row=0, column=1, sticky="N")

        self.unknown1.pack()
        self.smokeLifetime.pack()
        self.summonDelay.pack()
        self.summonType.pack()
        self.airSupportParams.pack()
        self.firingVoice.pack()
        self.voice2.pack()
        self.endingVoice.pack()

    def value(self):
        return [
            self.unknown1.value(),
            self.smokeLifetime.value(),
            self.summonDelay.value(),
            self.summonType.value(),
            self.airSupportParams.value(),
            [self.firingVoice.value(),
             self.voice2.value(),
             self.endingVoice.value()]
        ]

    def setValue(self, l):
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,0))
        self.smokeLifetime.setValue(get_value_from_dict_or_val(l,float,1))
        self.summonDelay.setValue(get_value_from_dict_or_val(l,float,2))
        self.summonType.setValue(get_value_from_dict_or_val(l,float,3))
        self.airSupportParams.setValue(get_value_from_dict_or_val(l,float,4))
        self.firingVoice.setValue(get_value_from_dict_or_val(l,float,5,0))
        self.voice2.setValue(get_value_from_dict_or_val(l,float,5,1))
        self.endingVoice.setValue(get_value_from_dict_or_val(l,float,5,2))
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
            if type(l) is dict and 'value' in l:
                val = l['value']
            else:
                val = l
            self.isBouncy.setValue(get_value_from_dict_or_val(val,float,0))
            self.enableExtra.setValue(1)
            self.hitEffectScale.setValue(get_value_from_dict_or_val(val,float,1, default_val=1))
            self.unknown.setValue(get_value_from_dict_or_val(val,float,2, default_val=0.25))
        else:
            self.isBouncy.setValue(get_value_from_dict_or_val(l,float,0))
            self.enableExtra.setValue(0)
            self.hitEffectScale.setValue(1)
            self.unknown.setValue(0.25)
class SolidBullet01Rail(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SolidBullet01Rail"))

    def value(self):
        return None

    def setValue(self, l):
        pass
class SolidExpBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SolidExpBullet01"))
        self.fuseOptions = {"Standard 1-second": 0,
                            "Custom fuse": 1,
                            "Sequential detonation": 2}
        self.fuseType = DropDownWidget(self, "Fuse type", self.fuseOptions, command=self.updateWidgets)
        self.fuse = FreeInputWidget(self, "Fuse delay", int, restrictPositive=True, initialValue=120)
        self.minFuse = FreeInputWidget(self, "Minimum fuse delay", int, restrictPositive=True, initialValue=60)
        self.maxFuse = FreeInputWidget(self, "Maximum fuse delay", int, restrictPositive=True, initialValue=120)
        self.explosionFlare = FreeInputWidget(self, "Explosion flare intensity", float, restrictPositive=True,
                                              initialValue=10.0)

        self.fuseType.pack()

    def updateWidgets(self, *args):
        if self.fuseType.value() == 0:
            self.fuse.pack_forget()
            self.minFuse.pack_forget()
            self.maxFuse.pack_forget()
            self.explosionFlare.pack_forget()
        if self.fuseType.value() == 1:
            self.fuse.pack()
            self.minFuse.pack_forget()
            self.maxFuse.pack_forget()
            self.explosionFlare.pack_forget()
        if self.fuseType.value() == 2:
            self.fuse.pack_forget()
            self.minFuse.pack()
            self.maxFuse.pack()
            self.explosionFlare.pack()

    def value(self):
        if self.fuseType.value() == 0:
            return None
        elif self.fuseType.value() == 1:
            return [self.fuse.value()]
        elif self.fuseType.value() == 2:
            return [[self.minFuse.value(), self.maxFuse.value()], self.explosionFlare.value()]

    def setValue(self, l):
        if l is None:
            self.fuseType.setValue(0)
        elif len(l) == 1:
            self.fuseType.setValue(1)
        elif len(l) == 2:
            self.fuseType.setValue(2)
        else:
            raise ValueError(f"SolidExpBullet01 setvalue error, given list of unexpected length or not a list {l}")
        self.updateWidgets()
class SolidPelletBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SolidPelletBullet01"))
        self.penetrationTime = FreeInputWidget(self, "Penetration duration", int, restrictPositive=True, initialValue=4,
                                               tooltip="How long the bullets in frames the bullets will maintain their penetraion property")
        self.penetrationTime.pack()

    def value(self):
        return [self.penetrationTime.value()]

    def setValue(self, l):
        self.penetrationTime.setValue(get_value_from_dict_or_val(l,float,0))
class SpiderStringBullet02(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("SpiderStringBullet02"))
        self.unknown = FreeInputWidget(self, "Unknown float", float, tooltip="0.1 or 0.025, maybe thickness?")
        self.unknown.pack()

    def value(self):
        return [self.unknown.value()]

    def setValue(self, l):
        self.unknown.setValue(get_value_from_dict_or_val(l,float,0))
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
        self.buffType.setValue(get_value_from_dict_or_val(l,float,0))
        self.offsetX.setValue(get_value_from_dict_or_val(l,float,1,0))
        self.offsetY.setValue(get_value_from_dict_or_val(l,float,1,1))
        self.offsetZ.setValue(get_value_from_dict_or_val(l,float,1,2))
class TargetMarkerBullet01(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("TargetMarkerBullet01"))

    def value(self):
        pass

    def setValue(self):
        pass
class LaserCallin(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Laser Call-in"))
        self.col1 = tk.Frame(self)
        self.col2 = tk.Frame(self)

        self.delay = FreeInputWidget(self.col1, "Call-in delay", int, restrictPositive=True, initialValue=60)
        self.trackingEnabled = CheckBoxWidget(self.col1, "Follows guide beam", 0, 1,
                                              tooltip="Whether the laser/missile continues to follow the guide beam after the initial launch.\nOff for spritefalls, on for bulge lasers/missiles")
        self.trackingSpeed = SliderWidget(self.col1, "Beam tracking speed", 0, 5, resolution=0.01, initialValue=1.0)
        self.trackingPrecision = SliderWidget(self.col1, "Beam tracking precision", 0, 1, resolution=0.01,
                                              initialValue=0.05,
                                              tooltip="How well the target is tracked, low values can cause lasers to swing back and forth before stopping on the target")
        self.laserOptions = {"Normal laser": 0,
                             "Missile": 1,
                             "Genocide gun": 2}
        self.laserStyle = DropDownWidget(self.col1, "Laser type", self.laserOptions, tooltip="")
        self.airSupport = AirSupportParams(self.col2)

        self.col1.grid(row=0, column=0, sticky="N")
        self.col2.grid(row=0, column=1, sticky="N")
        self.delay.pack()
        self.trackingEnabled.pack()
        self.trackingSpeed.pack()
        self.trackingPrecision.pack()
        self.laserOptions.pack()
        self.laserStyle.pack()
        self.airSupport.pack()

    def value(self):
        pass

    def setValue(self, l):
        pass
class AirSupportParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="Air support")
        self.col1 = tk.Frame(self)
        self.col2 = tk.Frame(self)
        self.col3 = tk.Frame(self)
        self.col4 = tk.Frame(self)
        self.attackAngle = AngleWidget(self.col1, "Vertical attack angle", minimum=0, maximum=90)  # 0, 0
        self.angleVariation = AngleWidget(self.col1, "Horizontal angle variation", minimum=0, maximum=360)  # 0, 1
        self.projectileHeight = FreeInputWidget(self.col1, "Projectile starting height", float, restrictPositive=True, initialValue=1000.0)  # 1, 0
        self.horizontalOffset = FreeInputWidget(self.col1, "Projectile horizontal offset", float)  # 1, 1
        self.shotCount = FreeInputWidget(self.col1, "Shot count", int, restrictPositive=True, initialValue=1)  # 2
        self.shotInterval = FreeInputWidget(self.col1, "Shot interval", int, restrictPositive=True, initialValue=5)  # 3
        self.ammoClass = DropDownWidget(self.col1, "Ammo class", subProjectileAmmoOptions)  # 4
        self.ammoSpeed = FreeInputWidget(self.col1, "Ammo speed (m/frame)", float, restrictPositive=True, initialValue=20)  # 5
        self.unknown1 = FreeInputWidget(self.col1, "Unknown float", float)  # 6
        self.ammoSize = FreeInputWidget(self.col1, "Ammo size", float, restrictPositive=True, initialValue=5.0)  # 7
        self.ammoHitSize = FreeInputWidget(self.col1, "Ammo hit size adjustment", float, restrictPositive=True, initialValue=1.0)  # 8
        self.unknown2 = FreeInputWidget(self.col1, "Unknown float", float, tooltip="Some sort of angle adjustment? Doesn't seem to be in radians")  # 9

        self.ammoLifetime = FreeInputWidget(self.col1, "Ammo lifetime", int, restrictPositive=True, initialValue=600)  # 10
        self.ammoIsPenetrate = CheckBoxWidget(self.col1, "Penetrating ammo", 0, 1)  # 11
        self.ammoColor = ColorWidget(self.col1, "Ammo color")  # 12
        self.ammoCust = ammoCustWidgetFromAmmoClass(self.col3, self.ammoClass.value(), True)  # 13
        self.ammoModel = MultiDropDownWidget(self.col2, "Ammo model", allModels)  # 14
        self.delay = FreeInputWidget(self.col1, "Firing delay", int, restrictPositive=True, initialValue=0)  # 15
        # self.missileSound = CheckBoxWidget(self.col2, "Emits rocket sound")  # 16
        self.firingSound = SoundWidget(self.col2, "Firing sound", None)  # 17
        self.impactSound = SoundWidget(self.col2, "Impact sound", None)  # 18

        self.col1.grid(row=0, column=0, sticky="N")
        self.col2.grid(row=0, column=1, sticky="N")
        self.col3.grid(row=0, column=2, sticky="N")
        self.col4.grid(row=0, column=3, sticky="N")

        self.attackAngle.pack()
        self.angleVariation.pack()
        self.projectileHeight.pack()
        self.horizontalOffset.pack()
        self.shotCount.pack()
        self.shotInterval.pack()
        self.ammoClass.pack()
        self.ammoSpeed.pack()
        self.unknown1.pack()
        self.ammoSize.pack()
        self.ammoHitSize.pack()
        self.unknown2.pack()
        self.ammoLifetime.pack()
        self.ammoIsPenetrate.pack()
        self.ammoColor.pack()
        self.ammoCust.pack()
        self.ammoModel.pack()
        self.delay.pack()
        # self..pack(
        self.firingSound.pack()
        self.impactSound.pack()
        self.ammoClass.dropDownDisplayed.trace_add("write", self.updateDependingOnAmmoClass)

    def updateDependingOnAmmoClass(self, *args):
        ac = self.ammoClass.value()
        self.ammoCust.pack_forget()
        self.ammoCust.destroy()
        self.ammoCust = ammoCustWidgetFromAmmoClass(self.col3, ac, True)
        self.ammoCust.pack()
        if ac in bulletsWithModels:
            self.ammoModel.enableInput()
            if ac == "SmokeCandleBullet01":
                self.ammoModel.setValue("app:/WEAPON/e_throw_marker01.rab")
                self.ammoModel.disableInput()
        else:
            self.ammoModel.disableInput()

    def value(self):
        v = [
            [self.attackAngle.value(), self.angleVariation.value()],
            [self.projectileHeight.value(), self.horizontalOffset.value()],
            self.shotCount.value(),
            self.shotInterval.value(),
            self.ammoClass.value(),
            self.ammoSpeed.value(),
            self.unknown1.value(),
            self.ammoSize.value(),
            self.ammoHitSize.value(),
            self.unknown2.value(),
            self.ammoLifetime.value(),
            self.ammoIsPenetrate.value(),
            self.ammoColor.value(),
            self.ammoCust.value(),
            self.ammoModel.value() if self.ammoClass.value() in bulletsWithModels else 0,
            self.delay.value(),
            1 if self.ammoClass.value() in ["MissileBullet01", "MissileBullet02"] else 0,
            self.firingSound.value(),
            self.impactSound.value()
        ]
        return v


    def setValue(self, l):
        self.attackAngle.setValue(get_value_from_dict_or_val(l,float,0,0))
        self.angleVariation.setValue(get_value_from_dict_or_val(l,float,0,1))
        self.projectileHeight.setValue(get_value_from_dict_or_val(l,float,1,0))
        self.horizontalOffset.setValue(get_value_from_dict_or_val(l,float,1,1))
        self.shotCount.setValue(get_value_from_dict_or_val(l,float,2))
        self.shotInterval.setValue(get_value_from_dict_or_val(l,float,3))
        self.ammoClass.setValue(get_value_from_dict_or_val(l,float,4))
        self.ammoSpeed.setValue(get_value_from_dict_or_val(l,float,5))
        self.unknown1.setValue(get_value_from_dict_or_val(l,float,6))
        self.ammoSize.setValue(get_value_from_dict_or_val(l,float,7))
        self.ammoHitSize.setValue(get_value_from_dict_or_val(l,float,8))
        self.unknown2.setValue(get_value_from_dict_or_val(l,float,9))
        self.ammoLifetime.setValue(get_value_from_dict_or_val(l,float,10))
        self.ammoIsPenetrate.setValue(get_value_from_dict_or_val(l,float,11))
        self.ammoColor.setValue(get_value_from_dict_or_val(l,float,12))
        self.ammoCust.setValue(get_value_from_dict_or_val(l,float,13))
        self.ammoModel.setValue(get_value_from_dict_or_val(l,float,14))
        self.delay.setValue(get_value_from_dict_or_val(l,float,15))
        # 1 if self.ammoClass.setValue(l[])
        self.firingSound.setValue(get_value_from_dict_or_val(l,float,17))
        self.impactSound.setValue(get_value_from_dict_or_val(l,float,18))
