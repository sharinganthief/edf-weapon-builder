from widgets.widgets import *
from widgets.EDFWidgets import *
from PIL import ImageTk, Image
import jsonBuilder as j
from widgets.ammoCustWidgets import *
# from tkscrolledframe import ScrolledFrame


class ClassTab(ScrolledFrame):
    def __init__(self, parent):
        ScrolledFrame.__init__(self, parent)
        self.canvas = self.display_widget(tk.Frame)

        # tk.Frame.__init__(self, parent)
        self.col1 = tk.Frame(self.canvas)
        # self.test = MissileBullet02(self.canvas, False)
        self.ammoCust = SolidBullet01(self.canvas, False)
        # self.test = HomingLaserBullet01(self.canvas)
        # self.test = NapalmBullet01(self.canvas, False)
        # AcidBullet01(self).test()
        self.ammoCust.grid(row=0, column=1, sticky="N")
        # self.testButton = tk.Button(self.col1, text="test", command = lambda:print(self.test.value()))
        # self.test.test()
        # self.test.setValue([[10.0, 20.0], [30.0, 40.0], 20, 2, 'SolidBullet01', 50.0, 60.0, 77.0, 80.0, 90.0, 11, 22, [2.0, 2.0, 2.0, 0.5], [-0.42], 'app:/WEAPON/bullet_grenade.rab', 33, 44, [0, 'e5w_AF_PA-11', 1.0, 1.0, 2.0, 25.0], [0, 'common_damages_explode_S_limited', 1.0, 1.0, 2.0, 25.0]])
        # self.testButton.pack()
        self.classOptions = {
            "Ranger": "Ranger",
            # "Wing Diver": "Wing Diver",
            # "Air Raider": "Air Raider",
            # "Fencer": "Fencer",
            # "Vehicle Weapon": "Vehicle Weapon"
            # getText("AI Weapon (not implemented"): "AI Weapon",
        }
        self.xgsOptions = {
            "Standard Weapon": "Weapon_BasicShoot",
            "Semi Auto Gun": "Weapon_BasicSemiAuto",
            "Homing Weapon": "Weapon_HomingShoot",
            "Thrown Weapon": "Weapon_Throw",
            "Wing Diver Standard Gun": "Weapon_ChargeShoot",
            "Wing Diver Pre-Charge Gun": "Weapon_PreChargeShoot",
            "Fencer Heavy Weapon": "Weapon_HeavyShoot",
            "Fencer Piercer": "Weapon_Swing",
            "Fencer Flashing Spear": "Weapon_PileBanker",
            "Fencer Shield": "Weapon_Shield",
            "Fencer Gatling": "Weapon_Gatling",
            "Fencer Melee": "Weapon_ImpactHammer",
            "Support Marker Gun": "Weapon_MarkerShooter",
            "Guide Laser": "Weapon_LaserMarker",
            "Bomber Call In": "Weapon_RadioContact",
            "Laser Call In": "Weapon_LaserMarkerCallFire",
            "Support Equipment": "Weapon_Accessory",
            "Vehicle Weapon": "Weapon_VehicleShoot",
            "Vehicle Maser(?)": "Weapon_VehicleMaser"

        }
        self.ammoOptions = {
            "SolidBullet01":        "SolidBullet01",
            "None":                 "None",
            "AcidBullet01":         "AcidBullet01",
            "BarrierBullet01":      "BarrierBullet01",
            "BombBullet01":         "BombBullet01",
            "BombBullet02":         "BombBullet02",
            "ClusterBullet01":      "ClusterBullet01",
            # "DecoyBullet01": "DecoyBullet01",
            "FlameBullet02":        "FlameBullet02",
            "GrenadeBullet01":      "GrenadeBullet01",
            "HomingLaserBullet01":  "HomingLaserBullet01",
            "LaserBullet01":        "LaserBullet01",
            "LaserBullet02":        "LaserBullet02",
            "LaserBullet03":        "LaserBullet03",
            "LightningBullet01":    "LightningBullet01",
            "MissileBullet01":      "MissileBullet01",
            "MissileBullet02":      "MissileBullet02",
            "NapalmBullet01":       "NapalmBullet01",
            "NeedleBullet01":       "NeedleBullet01",
            "PileBunkerBullet01":   "PileBunkerBullet01",
            "PlasmaBullet01":       "PlasmaBullet01",
            "PulseBullet01":        "PulseBullet01",
            "RocketBullet01":       "RocketBullet01",
            "SentryGunBullet01":    "SentryGunBullet01",
            "ShieldBashBullet01":   "ShieldBashBullet01",
            "ShockWaveBullet01":    "ShockWaveBullet01",
            "SmokeCandleBullet01":  "SmokeCandleBullet01",
            "SmokeCandleBullet02":  "SmokeCandleBullet02",
            "SolidBullet01Rail":    "SolidBullet01Rail",
            "SolidExpBullet01":     "SolidExpBullet01",
            "SolidPelletBullet01":  "SolidPelletBullet01",
            "SpiderStringBullet02": "SpiderStringBullet02",
            "SupportUnitBullet01":  "SupportUnitBullet01",
            "TargetMarkerBullet01": "TargetMarkerBullet01",
        }
        self.classChoice = DropDownWidget(self.col1, "Class", self.classOptions, tooltip="Class")
        self.xgsChoice = DropDownWidget(self.col1, "Object Class", self.xgsOptions,
                                        tooltip="Determines basic weapon functionality, click for details",
                                        link="https://github.com/KCreator/Earth-Defence-Force-Documentation/wiki/Object-Classes")
        self.AmmoClass = DropDownWidget(self.col1, "AmmoClass", self.ammoOptions,
                                        tooltip="Determines what a weapon shoots, click for details",
                                        link="https://github.com/KCreator/Earth-Defence-Force-Documentation/wiki/AmmoClass-List-(ENG)")
        # self.Description = BigTextWidget(self, "Description")

        self.ammoSize = FreeInputWidget(self.col1, "Ammo size", float, restrictPositive=True, initialValue=1.0)
        self.ammoHitSizeAdjust = FreeInputWidget(self.col1, "Ammo Hit Size Adjust", float, restrictPositive=True, initialValue=1, tooltip="Multiplies(?) the hitbox and surface hit effect")
        self.ammoOwnerMove = SliderWidget(self.col1, "Inherited player momentum", 0, 1, resolution=0.1,
                                          initialValue=0.0,
                                          tooltip="How much of the player's velocity the projectile inherits, 0=none, 1 = all.")
        self.spreadOptions = {
            "Normal (cone)": 0,
            "Erratic horizontal": 1,
            "Uniform horizontal": 2,
            "Erratic vertical": 3,
            "Uniform vertical": 4
        }
        self.fireSpreadType = DropDownWidget(self.col1, "Fire Spread Type", self.spreadOptions)
        self.fireSpreadWidth = SliderWidget(self.col1, "Fire Spread Width", 0, 1, resolution=0.01, initialValue=0.0)
        self.ammoHitImpulseAdjust = FreeInputWidget(self.col1, "Ammo Impulse Adjust", float, restrictPositive=True, tooltip="Affects how much force the bullet imparts on the target.\nRanges naturally from 0.0005 to 2.")
        self.ammoGravityFactor = FreeInputWidget(self.col1, "Ammo Gravity Factor", float, tooltip="How fast the bullet falls, negative values cause it to 'fall' upwards.\nTypically 0 for most guns, 1 for grenades. Plasmafall has the highest gravity at 8")


        self.fireVector = VectorFromAngleWidget(self.col1, "Firing Angle")

        self.updateAmmoCustWidget()

        self.classChoice.pack()
        self.xgsChoice.pack()
        self.AmmoClass.pack()
        self.col1.grid(row=0,column=0, sticky="N")
        self.classChoice.dropDownDisplayed.trace_add("write", self.updateXGSBasedOnClass)
        self.AmmoClass.dropDownDisplayed.trace_add("write", self.updateAmmoCustWidget)
        self.updateXGSBasedOnClass()

        self.ammoSize.pack()
        self.ammoHitSizeAdjust.pack()
        self.ammoOwnerMove.pack()
        self.fireSpreadType.pack()
        self.fireSpreadWidth.pack()
        self.ammoHitImpulseAdjust.pack()
        self.ammoGravityFactor.pack()
        self.fireVector.pack()
        # self.Description.pack()


    def updateAmmoCustWidget(self, *args):
        if self.ammoCust is not None:
            self.ammoCust.grid_forget()
            self.ammoCust.destroy()
            self.ammoCust = None
        self.ammoCust = ammoCustWidgetFromAmmoClass(self.canvas, self.AmmoClass.value(), False)
        if self.ammoCust is not None:
            self.ammoCust.grid(row=0, column=1, sticky="N")
            # self.ammoCust.test()

    def updateXGSBasedOnClass(self, *args):
        if self.classChoice.value() == "Ranger":
            self.xgsOptions = {
                "Standard Weapon": "Weapon_BasicShoot",
                "Semi Auto Gun": "Weapon_BasicSemiAuto",
                "Homing Weapon": "Weapon_HomingShoot",
                # "Thrown Weapon": "Weapon_Throw",
                # "Wing Diver Standard Gun": "Weapon_ChargeShoot",
                # "Wing Diver Pre-Charge Gun": "Weapon_PreChargeShoot",
                # "Fencer Heavy Weapon": "Weapon_HeavyShoot",
                # "Fencer Piercer": "Weapon_Swing",
                # "Fencer Flashing Spear": "Weapon_PileBanker",
                # "Fencer Shield": "Weapon_Shield",
                # "Fencer Gatling": "Weapon_Gatling",
                # "Fencer Melee": "Weapon_ImpactHammer",

                # "Support Marker Gun": "Weapon_MarkerShooter",
                # "Guide Laser": "Weapon_LaserMarker",
                # "Bomber Call In": "Weapon_RadioContact",
                # "Laser Call In": "Weapon_LaserMarkerCallFire",
                # "Support Equipment": "Weapon_Accessory",

                # "Vehicle Weapon": "Weapon_VehicleShoot",
                # "Vehicle Maser(?)": "Weapon_VehicleMaser"
            }
        elif self.classChoice.value() == "Wing Diver":
            self.xgsOptions = {
                "Standard Weapon": "Weapon_BasicShoot",
                "Semi Auto Gun": "Weapon_BasicSemiAuto",
                "Homing Weapon": "Weapon_HomingShoot",
                "Thrown Weapon": "Weapon_Throw",
                "Wing Diver Standard Gun": "Weapon_ChargeShoot",
                "Wing Diver Pre-Charge Gun": "Weapon_PreChargeShoot",
                # "Fencer Heavy Weapon": "Weapon_HeavyShoot",
                # "Fencer Piercer": "Weapon_Swing",
                # "Fencer Flashing Spear": "Weapon_PileBanker",
                # "Fencer Shield": "Weapon_Shield",
                # "Fencer Gatling": "Weapon_Gatling",
                # "Fencer Melee": "Weapon_ImpactHammer",
                "Support Marker Gun": "Weapon_MarkerShooter",
                "Guide Laser": "Weapon_LaserMarker",
                "Bomber Call In": "Weapon_RadioContact",
                "Laser Call In": "Weapon_LaserMarkerCallFire",
                "Support Equipment": "Weapon_Accessory",
                # "Vehicle Weapon": "Weapon_VehicleShoot",
                # "Vehicle Maser(?)": "Weapon_VehicleMaser"
            }
        elif self.classChoice.value() == "Air Raider":
            self.xgsOptions = {
                "Standard Weapon": "Weapon_BasicShoot",
                "Semi Auto Gun": "Weapon_BasicSemiAuto",
                "Homing Weapon": "Weapon_HomingShoot",
                "Thrown Weapon": "Weapon_Throw",
                # "Wing Diver Standard Gun": "Weapon_ChargeShoot",
                # "Wing Diver Pre-Charge Gun": "Weapon_PreChargeShoot",
                # "Fencer Heavy Weapon": "Weapon_HeavyShoot",
                # "Fencer Piercer": "Weapon_Swing",
                # "Fencer Flashing Spear": "Weapon_PileBanker",
                # "Fencer Shield": "Weapon_Shield",
                # "Fencer Gatling": "Weapon_Gatling",
                # "Fencer Melee": "Weapon_ImpactHammer",
                "Support Marker Gun": "Weapon_MarkerShooter",
                "Guide Laser": "Weapon_LaserMarker",
                "Bomber Call In": "Weapon_RadioContact",
                "Laser Call In": "Weapon_LaserMarkerCallFire",
                "Support Equipment": "Weapon_Accessory",
                # "Vehicle Weapon": "Weapon_VehicleShoot",
                # "Vehicle Maser(?)": "Weapon_VehicleMaser"
            }
        elif self.classChoice.value() == "Fencer":
            self.xgsOptions = {
                "Standard Weapon": "Weapon_BasicShoot",
                "Semi Auto Gun": "Weapon_BasicSemiAuto",
                "Homing Weapon": "Weapon_HomingShoot",
                "Thrown Weapon": "Weapon_Throw",
                # "Wing Diver Standard Gun": "Weapon_ChargeShoot",
                # "Wing Diver Pre-Charge Gun": "Weapon_PreChargeShoot",
                "Fencer Heavy Weapon": "Weapon_HeavyShoot",
                "Fencer Piercer": "Weapon_Swing",
                "Fencer Flashing Spear": "Weapon_PileBanker",
                "Fencer Shield": "Weapon_Shield",
                "Fencer Gatling": "Weapon_Gatling",
                "Fencer Melee": "Weapon_ImpactHammer",
                "Support Marker Gun": "Weapon_MarkerShooter",
                "Guide Laser": "Weapon_LaserMarker",
                "Bomber Call In": "Weapon_RadioContact",
                "Laser Call In": "Weapon_LaserMarkerCallFire",
                "Support Equipment": "Weapon_Accessory",
                # "Vehicle Weapon": "Weapon_VehicleShoot",
                # "Vehicle Maser(?)": "Weapon_VehicleMaser"
            }
        elif self.classChoice.value() == "Vehicle Weapon":
            self.xgsOptions = {
                # "Standard Weapon": "Weapon_BasicShoot",
                # "Semi Auto Gun": "Weapon_BasicSemiAuto",
                # "Homing Weapon": "Weapon_HomingShoot",
                # "Thrown Weapon": "Weapon_Throw",
                # "Wing Diver Standard Gun": "Weapon_ChargeShoot",
                # "Wing Diver Pre-Charge Gun": "Weapon_PreChargeShoot",
                # "Fencer Heavy Weapon": "Weapon_HeavyShoot",
                # "Fencer Piercer": "Weapon_Swing",
                # "Fencer Flashing Spear": "Weapon_PileBanker",
                # "Fencer Shield": "Weapon_Shield",
                # "Fencer Gatling": "Weapon_Gatling",
                # "Fencer Melee": "Weapon_ImpactHammer",
                # "Support Marker Gun": "Weapon_MarkerShooter",
                # "Guide Laser": "Weapon_LaserMarker",
                # "Bomber Call In": "Weapon_RadioContact",
                # "Laser Call In": "Weapon_LaserMarkerCallFire",
                # "Support Equipment": "Weapon_Accessory",
                "Vehicle Weapon": "Weapon_VehicleShoot",
                "Vehicle Maser(?)": "Weapon_VehicleMaser"
            }

        self.xgsChoice.replaceOptionMenu(self.xgsOptions, self.updateAmmoClassBasedOnXGS)
        self.updateAmmoClassBasedOnXGS()

    def updateAmmoClassBasedOnXGS(self, *args):
        x = self.xgsChoice.value()
        if x == "Weapon_BasicShoot" or x == "Weapon_BasicSemiAuto" or x == "Weapon_ChargeShoot" or \
            x == "Weapon_PreChargeShoot" or x == "Weapon_HeavyShoot" or x == "Weapon_Swing" or x == "Weapon_PileBanker"\
                or x == "Weapon_VehicleShoot" or x == "Weapon_Gatling":
            self.ammoOptions = {
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
                # "SmokeCandleBullet02 - Not implemented yet": "SmokeCandleBullet02",
                "SolidBullet01Rail": "SolidBullet01Rail",
                # "SolidExpBullet01 - Not implemented yet": "SolidExpBullet01",
                "SolidPelletBullet01": "SolidPelletBullet01",
                "SpiderStringBullet02": "SpiderStringBullet02",
                "SupportUnitBullet01": "SupportUnitBullet01",
                # "TargetMarkerBullet01 - Not implemented yet": "TargetMarkerBullet01",
        }
        elif x == "Weapon_HomingShoot":
            self.ammoOptions = {
                # "SolidBullet01": "SolidBullet01",
                # "None": "None",
                # "AcidBullet01": "AcidBullet01",
                # "BarrierBullet01": "BarrierBullet01",
                # "BombBullet01": "BombBullet01",
                # "BombBullet02": "BombBullet02",
                # "ClusterBullet01": "ClusterBullet01",
                # "DecoyBullet01": "DecoyBullet01",
                # "FlameBullet02": "FlameBullet02",
                # "GrenadeBullet01": "GrenadeBullet01",
                "HomingLaserBullet01": "HomingLaserBullet01",
                # "LaserBullet01": "LaserBullet01",
                # "LaserBullet02": "LaserBullet02",
                # "LaserBullet03": "LaserBullet03",
                # "LightningBullet01": "LightningBullet01",
                "MissileBullet01": "MissileBullet01",
                "MissileBullet02": "MissileBullet02",
                # "NapalmBullet01": "NapalmBullet01",
                # "NeedleBullet01": "NeedleBullet01",
                # "PileBunkerBullet01": "PileBunkerBullet01",
                # "PlasmaBullet01": "PlasmaBullet01",
                # "PulseBullet01": "PulseBullet01",
                # "RocketBullet01": "RocketBullet01",
                # "SentryGunBullet01": "SentryGunBullet01",
                # "ShieldBashBullet01": "ShieldBashBullet01",
                # "ShockWaveBullet01": "ShockWaveBullet01",
                # "SmokeCandleBullet01": "SmokeCandleBullet01",
                # "SmokeCandleBullet02": "SmokeCandleBullet02",
                # "SolidBullet01Rail": "SolidBullet01Rail",
                # "SolidExpBullet01": "SolidExpBullet01",
                # "SolidPelletBullet01": "SolidPelletBullet01",
                # "SpiderStringBullet02": "SpiderStringBullet02",
                # "SupportUnitBullet01": "SupportUnitBullet01",
                # "TargetMarkerBullet01": "TargetMarkerBullet01",
        }
        elif x == "Weapon_Throw":
            self.ammoOptions = {
                "SolidBullet01": "SolidBullet01",
                "None": "None",
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
        elif x == "Weapon_Shield":
            self.ammoOptions = {
                "SolidBullet01": "SolidBullet01",
                "None": "None",
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
        elif x == "Weapon_ImpactHammer":
            self.ammoOptions = {
                "SolidBullet01": "SolidBullet01",
                "None": "None",
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
        elif x == "Weapon_MarkerShooter":
            self.ammoOptions = {
                "TargetMarkerBullet01": "TargetMarkerBullet01"
        }
        elif x == "Weapon_LaserMarker" or x == "Weapon_RadioContact" or \
                x == "Weapon_LaserMarkerCallFire" or x == "Weapon_Accessory":
            self.ammoOptions = {
                "None": ""
        }
        elif x == "Weapon_VehicleMaser":
            self.ammoOptions = {
                "SolidBullet01": "SolidBullet01",
                "None": "None",
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

        self.AmmoClass.replaceOptionMenuNoCmd(self.ammoOptions)


class BasicParamsTab(ScrolledFrame):
    def __init__(self, parent):
        ScrolledFrame.__init__(self, parent)
        self.frame = self.display_widget(tk.Frame)
        self.basicParamsWidget = BasicParamsWidget(self.frame)
        self.basicParamsWidget.pack()

    def getValuesDict(self):
        return self.basicParamsWidget.getValuesDict()


class LockonTab(ScrolledFrame):
    def __init__(self, parent):
        # xgs that can lock on: basicShoot roombas, HomingShoot MissileBullet01/02, HomingLaserBullet01, VehicleShoot MissileBullet01/02 and probably roombas
        ScrolledFrame.__init__(self, parent)
        self.frame = self.display_widget(tk.Frame)
        self.col1 = tk.Frame(self.frame)
        self.col2 = tk.Frame(self.frame)
        self.lockonType = DropDownWidget(self.col1, "Lock-on type", {"No lock-on": 0, "Click to lock": 1, "Passive lock-on": 3})
        self.lockonDistributionType = DropDownWidget(self.col1, "Lock-on Distribution",
                                                     {"Projectile-based": 1, "Burst-based": 0},
                                                     tooltip="Projectile-based: Depends on the number of projectiles fired per shot, each one will home in on an enemy\nBurst-based: Depends on how many projectiles are fired in a burst, each projectile or set of projectiles will attack a different enemy.\nAlso forces reload on fire so the burst count should be equal to the magazine size.")
        self.lockonFireEndToClear = CheckBoxWidget(self.col1, "Maintain lock-on after firing", 1, 0)
        self.lockonTargetType = CheckBoxWidget(self.col1, "Requires guide beacon/laser", 0, 1)
        self.lockonFailedTime = FreeInputWidget(self.col1, "Lock-on failure time", int, restrictPositive=True, tooltip="Time in frames allowed off target before losing any locks in progress")
        self.lockonHoldTime = FreeInputWidget(self.col1, "Lock-on hold time", int, restrictPositive=True, tooltip="Time in frames allowed off target after a successful lock-on has been made before it is lost")
        self.lockonAutoTimeout = CheckBoxWidget(self.col1, "Successful locks reset (WARNING)", 0, 1, tooltip="Tends to crash the game when turned on")
        self.lockonAutoTimeout.label.configure(bg="yellow")
        # self.lockonAutoTimeout = DropDownWidget(self.col1, "Lock-on auto timeout ??", int, {"Normal":0, "Used by Wing Diver/Roombas":1}, tooltip="Not sure entirely")

        self.lockonAngleH = AngleWidget(self.col2, "Lock-on angle (horizontal)")
        self.lockonAngleV = AngleWidget(self.col2, "Lock-on angle (vertical")
        self.lockonTime = StarStructOrFlatWidget(self.col1, "Lock-on Time", "LockOnTime", int, p1=0.9, p2=1.5,
                                                 initialValue=20, restrictPositive=True, inverse=True)
        self.lockonRange = StarStructOrFlatWidget(self.col2, "Lock-on Range", "LockOnRange", float, p1=0.6, p2=0.9,
                                                  initialValue=200, restrictPositive=True)

        self.lockonType.pack()
        self.lockonDistributionType.pack()
        self.lockonFireEndToClear.pack()
        self.lockonTargetType.pack()
        self.lockonFailedTime.pack()
        self.lockonHoldTime.pack()
        self.lockonAutoTimeout.pack()
        self.col1.grid(row=0, column=0, sticky="N")

        self.lockonAngleH.pack()
        self.lockonAngleV.pack()
        self.lockonTime.pack()
        self.lockonRange.pack()
        self.col2.grid(row=0, column=1, sticky="N")

        # self.testB = tk.Button(self, text="test", command=lambda:print(self.getValuesDict()))
        # self.testB.grid(row=0,column=2)

    def getValuesDict(self):
        return {
            "LockonAngle": [self.lockonAngleH.value(), self.lockonAngleV.value()],
            "LockonFailedTime": self.lockonFailedTime.value(),
            "LockonHoldTime": self.lockonHoldTime.value(),
            "LockonRange": self.lockonRange.value(),
            "LockonTargetType": self.lockonType.value(),
            "LockonTime": self.lockonTime.value(),
            "LockOnType": self.lockonType.value(),
            "Lockon_AutoTimeOut": self.lockonAutoTimeout.value(),
            "LockOnDistributionType": self.lockonDistributionType.value(),
            "Lockon_FireEndToClear": self.lockonFireEndToClear.value()
        }


class AppearanceTab(ScrolledFrame):
    def __init__(self, parent):
        ScrolledFrame.__init__(self, parent)
        self.frame = self.display_widget(tk.Frame)
        self.col1 = tk.Frame(self.frame)
        self.col2 = tk.Frame(self.frame)
        self.col3 = tk.Frame(self.frame)
        self.gunModelWidget = GunModelWidget(self.col1)


        self.sightpath = "./data/images/sights/"
        self.sightOptions = {
            "None": "missingSight_animation_model",
            "Ranger rifle": "sight01",
            "Ranger rocket": "sight02",
            "Ranger sniper": "sight05",
            "Ranger special": "sight06",
            "Ranger shotgun": "sight07",
            "W. Diver short range": "sight09",
            "W. Diver long range": "sight10",
            "W. Diver kinetic": "sight11",
            "Air raider crosshair": "sight13",
            "Fencer crosshair": "sight17",
            "Ranger grenade launcher": "sight18",
            "Large square (unused)": "sight15",
            "Circular (unused)": "sight14",
            "Octagonal (unused)": "sight08",
            "2 circles with + (unused)": "sight12"
        }
        self.sightAnimationModel = DropDownWidget(self.col1, "Sight model", self.sightOptions)
        self.sightAnimationModel.dropDownDisplayed.trace_add("write", self.updateSightImg)

        if self.sightAnimationModel.value() == "missingSight_animation_model":
            self.sightImg = ImageTk.PhotoImage(Image.open(f"{self.sightpath}none.png"))
        else:
            self.sightImg = ImageTk.PhotoImage(Image.open(f"{self.sightpath}{self.sightAnimationModel.value()}.png"))
        self.sightImgPanel = ttk.Label(self.col1, image=self.sightImg)


        self.ammoModel = MultiDropDownWidget(self.col2, "Ammo Model", allModels)
        self.ammoColor = ColorWidget(self.col2, "Ammo color")
        self.shellCase = ShellCaseWidget(self.col2)

        self.angleAdjust = AngleWidget(self.col3, "Model angle adjustment")
        self.muzzleFlash = MuzzleFlashWidget(self.col3)

        self.gunModelWidget.RABChoice.valueLabel.inputVar.trace_add("write", self.updateRABDependantValues)


        # self.muzzleFlashCustomParameter = FreeInputWidget(self, "Muzzle flash parameters", str, initialValue="")
        # col1
        self.gunModelWidget.pack()
        self.sightAnimationModel.pack()
        self.sightImgPanel.pack()
        # col2
        self.ammoModel.pack()
        self.ammoColor.pack()
        self.shellCase.pack()
        # col3
        self.angleAdjust.pack()
        self.muzzleFlash.pack()

        # self.gunModelWidget.RABChoice.setValue("app:/Weapon/s_assault_AF14.rab")
        self.col1.grid(row=0,column=0, sticky="N")
        self.col2.grid(row=0,column=1, sticky="N")
        self.col3.grid(row=0, column=2, sticky="N")
        self.updateRABDependantValues()
        self.updateSightImg()


        self.gunModelWidget.classChange("Ranger")


    def updateRABDependantValues(self, *args):
        v = self.gunModelWidget.getModelRelatedInfo()
        self.ammoModel.setValue(v["AmmoModel"])
        # self.ammoColor.setValue(v["AmmoColor"])
        self.shellCase.setValue(v["ShellCase"])
        self.muzzleFlash.muzzleFlashType.setValue(v["MuzzleFlash"])
        if self.muzzleFlash.paramsWidget is not None:
            self.muzzleFlash.paramsWidget.setValue(v["MuzzleFlash_CustomParameter"])
        self.updateSightModel(v["Sight_animation_model"])

    def updateSightModel(self, sightModel, *args):
        if sightModel != "missingSight_animation_model":
            self.sightAnimationModel.setValue(sightModel[0][1][:-4].lower())
        else:
            self.sightAnimationModel.setValue(sightModel)
        self.updateSightImg()

    def updateSightImg(self, *args):
        if self.sightAnimationModel.value() == "missingSight_animation_model":
            self.sightImg = ImageTk.PhotoImage(Image.open(f"{self.sightpath}none.png"))
        else:
            self.sightImg = ImageTk.PhotoImage(Image.open(f"{self.sightpath}{self.sightAnimationModel.value()}.png"))
        self.sightImgPanel.config(image=self.sightImg)
        # print(self.sightAnimationModel.value())


    def getValuesDict(self):
        sight = self.sightAnimationModel.value()
        return {**self.gunModelWidget.getValuesDict(),
                "AmmoModel": self.ammoModel.value(),
                "MuzzleFlash": self.muzzleFlash.muzzleFlashType.value(),
                "MuzzleFlash_CustomParameter": self.muzzleFlash.paramsWidget.value() if self.muzzleFlash.paramsWidget is not None else None,
                "Sight_animation_model": [[f"app:/HUD/{sight}.rab", f"{sight}.mdb"], 0, 0] if sight != "missingSight_animation_model" else None}


class SoundsTab(ScrolledFrame):
    def __init__(self, parent):
        ScrolledFrame.__init__(self, parent)
        self.frame = self.display_widget(tk.Frame)
        self.col3 = tk.Frame(self.frame)
        self.fireSound = SoundWidget(self.frame, "Firing Sound", None)
        self.impactSound = SoundWidget(self.frame, "Impact Sound", None, tooltip="Some ammo types like SolidBullets have an innate impact sound.")
        self.reloadSound = SoundWidget(self.col3, "Fencer reload Sound", None, tooltip="Only used by certain fencer weapons")
        self.shellCaseDischargeSound = SoundWidget(self.col3, "Fencer shell case discharge sound", None, tooltip="Only used by certain fencer weapons.")
        self.ammoEquipFullOptions = {
            "None": None,
            "Ranger Vehicle":        '輸送部隊出撃直後レンジャー',
            "Air Raider Vehicle":    '輸送部隊出撃直後',
            "Phobos":                'フォボス出撃直後',
            "Gunship":               'ホエール出撃直後',
            "Artillery":             '砲兵出撃直後',
            "Combat Bomber":         'カロン出撃直後',
            "Missiles":              'デスピナ出撃直後',
            "Barren Land (Tempest)": 'バレンランド出撃直後',
            "Bulge Laser":           'バルジレーザー出撃直後',
            "Spritefall":            'スプライト出撃直後',
        }
        self.ammoEquipEmptyOptions = {
            "None": None,
            "Ranger Vehicle":        '輸送部隊出撃直後レンジャー',
            "Air Raider Vehicle":    '輸送部隊支援不能',
            "Phobos":                'フォボス支援不能',
            "Gunship":               'ホエール支援不能',
            "Artillery":             '砲兵支援不能',
            "Combat Bomber":         'カロン支援不能',
            "Missiles":              'デスピナ支援不能',
            "Barren Land (Tempest)": 'バレンランド支援不能',
            "Bulge Laser":           'バルジレーザー支援不能',
            "Spritefall":            'スプライト支援不能',
        }
        self.ammoEquipFrame = tk.Frame(self.frame)
        self.ammoEquipFullVoice = DropDownWidget(self.ammoEquipFrame, "When equipped/reloaded",
                                                 self.ammoEquipFullOptions,
                                                 tooltip="Plays sometimes when the weapon is equipped and ammo is full or when it becomes available to use again.")
        self.ammoEquipEmptyVoice = DropDownWidget(self.ammoEquipFrame, "When unavailable voice",
                                                  self.ammoEquipFullOptions,
                                                  tooltip="Plays sometimes when the weapon is equipped and is not available for use.")
        
        self.ammoEquipFullVoice.pack()
        self.ammoEquipEmptyVoice.pack()
        
        self.ammoEquipFrame.grid(row=1, column=0, sticky="N")
        self.fireSound.grid(row=0, column=0, sticky="N")
        self.impactSound.grid(row=0, column=1, sticky="N")
        self.col3.grid(row=0, column=2, sticky="N")
        self.reloadSound.pack()
        self.shellCaseDischargeSound.pack()

    def updateRabDependentValues(self):
        pass

    def getValuesDict(self):
        return {
            "FireSe": self.fireSound.value(),
            "AmmoHitSe": self.impactSound.value(),
            "Ammo_EquipVoice": [self.ammoEquipFullVoice.value(), self.ammoEquipEmptyVoice.value()]
        }


# class StandardWeaponTab(tk.Frame):
#     def __init__(self, parent, width, height, text):
#         tk.Frame.__init__(self, parent, width=width, height=height)
#         self.parent = parent
#         self.label1 = tk.Label(self, text=text)
#         self.label1.pack()

# class AmmoOptionsTab(ScrolledFrame):
#     def __init__(self, parent):
#         ScrolledFrame.__init__(self, parent)
#         self.frame = self.display_widget(tk.Frame)
#         # self.ammoModel = AmmoOptionsWidget(self)
#         # self.ammoModel.grid(row=0, column=0)
#         self.col1 = tk.Frame(self.frame)
#         # self.col2 = tk.Frame(self)
#         self.ammoSize = FreeInputWidget(self.col1, "Ammo size", float, restrictPositive=True, initialValue=0.2)
#         self.ammoHitSizeAdjust = FreeInputWidget(self.col1, "Ammo Hit Size Adjust", float, restrictPositive=True, initialValue=1, tooltip="Multiplies(?) the hitbox and surface hit effect")
#         self.ammoOwnerMove = SliderWidget(self.col1, "Inherited player momentum", 0, 1, resolution=0.1, initialvalue=0.0, tooltip="How much of the player's velocity the projectile inherits, 0=none, 1 = all.")
#         self.spreadOptions = {
#             "Normal (cone)": 0,
#             "Erratic horizontal": 1,
#             "Uniform horizontal": 2,
#             "Erratic vertical": 3,
#             "Uniform vertical": 4
#         }
#         self.fireSpreadType = DropDownWidget(self.col1, "Fire Spread Type", self.spreadOptions)
#         self.fireSpreadWidth = SliderWidget(self.col1, "Fire Spread Width", 0, 1, resolution=0.01, initialvalue=0.0)
#         self.ammoHitImpulseAdjust = FreeInputWidget(self.col1, "Ammo Impulse Adjust", float, restrictPositive=True, tooltip="Affects how much force the bullet imparts on the target.\nRanges naturally from 0.0005 to 2.")
#         self.ammoGravityFactor = FreeInputWidget(self.col1, "Ammo Gravity Factor", float, tooltip="How fast the bullet falls, negative values cause it to 'fall' upwards.\nTypically 0 for most guns, 1 for grenades. Plasmafall has the highest gravity at 8")
#
#
#         self.fireVector = VectorFromAngleWidget(self.col1, "Firing Angle")
#         # self.col2.grid(row=0, column=1)
#         self.col1.grid(row=0, column=0, sticky="N")
#         self.ammoSize.pack()
#         self.ammoHitSizeAdjust.pack()
#         self.ammoOwnerMove.pack()
#         self.fireSpreadType.pack()
#         self.fireSpreadWidth.pack()
#         self.ammoHitImpulseAdjust.pack()
#         self.ammoGravityFactor.pack()
#         self.fireVector.pack()
#
#     def getValuesDict(self):
#         return{
#             "AmmoSize": self.ammoSize.value(),
#             "AmmoHitSizeAdjust": self.ammoHitSizeAdjust.value(),
#             "AmmoHitImpulseAdjust": self.ammoHitImpulseAdjust.value(),
#             "AmmoGravityFactor": self.ammoGravityFactor.value(),
#             "AmmoOwnerMove": self.ammoOwnerMove.value(),
#             "FireSpreadType": self.fireSpreadType.value(),
#             "FireSpreadWidth": self.fireSpreadWidth.value(),
#             "FireVector": [self.fireVector.vectorX.value(), self.fireVector.vectorY.value(), self.fireVector.vectorZ.value()],
#
#         }
