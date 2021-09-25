from widgets.EDFWidgets import *

vehicleWeapons = j.loadDataFromJson("./data/sorted vehicle weapons.json")
vehicleWeaponStats = j.loadDataFromJson("./data/vehicle weapon stats.json")
vehicleSGOS = {
    "Tank": {
        "Blacker tank": "app:/Object/v505_tank.sgo",
        "EDF 4 tank": 'app:/Object/v505_tank_edf4.sgo',
        "EDF 5 tank": 'app:/Object/v505_tank_edf5.sgo',
        "Railgun tank": 'app:/Object/Vehicle403_Tank.sgo',
        "EMC tank": 'app:/Object/v510_maser.sgo',
        "Titan tank": "app:/Object/Vehicle404_bigtank.sgo"},
    "Ground Vehicles": {
        "Grape": "app:/Object/Vehicle401_Striker.sgo",
        "Ambulance": 'app:/Object/v507_rescuetank.sgo',
        "Happy Manager Ambulance": 'app:/Object/v507_rescuetank_siawase.sgo',
        "Naegling": 'app:/Object/Vehicle402_Rocket.sgo'},
    "Helicopter": {
        "Helicopter Eros": 'app:/Object/v506_heli.sgo',
        "Helicopter Nereid": 'app:/Object/Vehicle409_heli.sgo',
        "Helicopter Brute": 'app:/Object/Vehicle410_heli.sgo'},
    "Nix": {
        "Blue": 'app:/Object/v504_begaruta_blue.sgo',
        "Red": 'app:/Object/v504_begaruta_red.sgo',
        "Green": 'app:/Object/v504_begaruta.sgo',
        "Grey": 'app:/Object/V504_BEGARUTA_MISSION.sgo',
        # "Green 2": 'app:/Object/V504_BEGARUTA_G_MISSION.sgo',  # No difference
        "White": 'app:/Object/v504_begaruta_white.sgo',
        # "White 2": 'app:/Object/V504_BEGARUTA_DLCHS_MISSION.sgo',  # No difference
        "Yellow": 'app:/Object/V504_BEGARUTA_YELLOW.sgo',
        # "Yellow 2": 'app:/Object/V504_BEGARUTA_FW.sgo',  # No difference
        "Gold": 'app:/Object/v504_begaruta_gold.sgo',
        "Pink Phantasia": "app:/Object/v504_begaruta_pink.sgo"},
    "Balam": {
        "Orange": 'app:/Object/V515_RETROBALAM.sgo',
        "Gold": 'app:/Object/V515_RETROBALAM_GOLD.sgo',
        "Gray": 'app:/Object/V515_RETROBALAM_GREY.sgo',
        "Green": 'app:/Object/V515_RETROBALAM_GREEN.sgo',
        "Ultimate": 'app:/Object/V515_RETROBALAM_ULTI.sgo'
    },
    "Depth Crawler": {
        "Regular": 'app:/Object/VEHICLE502_GROUNDROBO.sgo',
        "Gold": 'app:/Object/VEHICLE502_GROUNDROBOGOLD.sgo'
    },
    "Other": {
        "Kei Truck": 'app:/Object/v512_keiTruck_bgp.sgo',
        "Pickup Truck": 'app:/Object/V513_TRAILERTRUCK01CAB.sgo',
        "Bike": 'app:/Object/v503_bike.sgo',
        "Omega Free Bike": 'app:/Object/v503_bike_omegaz.sgo'},
}


class TankParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Tank movement"), bd=5)
        self.parent = parent
        self.bodyTurning = FreeInputWidget(self, "Body turning speed", float, restrictPositive=True,
                                           initialValue=0.1)
        self.maxSpeed = FreeInputWidget(self, "Max speed", float, restrictPositive=True, initialValue=25.0)
        self.brakes = SliderWidget(self, "Braking power", 0, 1, resolution=0.001, tooltip="1 = instant stop",
                                   initialValue=0.015)
        self.unknown1 = FreeInputWidget(self, "Unknown float", float, initialValue=1.0)
        self.unknown2 = FreeInputWidget(self, "Unknown float", float, initialValue=0.125)
        self.acceleration = FreeInputWidget(self, "Acceleration?", float, restrictPositive=True, initialValue=0.25)

        self.bodyTurning.pack()
        self.maxSpeed.pack()
        self.brakes.pack()
        self.unknown1.pack()
        self.unknown2.pack()
        self.acceleration.pack()

    def value(self):
        return [self.bodyTurning.value(),
                self.maxSpeed.value(),
                self.brakes.value(),
                self.unknown1.value(),
                self.unknown2.value(),
                self.acceleration.value()]

    def setValue(self, l):
        self.bodyTurning.setValue(l[0])
        self.maxSpeed.setValue(l[1])
        self.brakes.setValue(l[2])
        self.unknown1.setValue(l[3])
        self.unknown2.setValue(l[4])
        self.acceleration.setValue(l[5])


class CalibanParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Caliban"))
        self.tankParams = TankParams(self)
        self.healingFrame = tk.LabelFrame(self, text=getText("Healing"))
        self.healingRate = FreeInputWidget(self.healingFrame, "Healing rate", float, initialValue=4.0)
        self.healAmmo = FreeInputWidget(self.healingFrame, "Healing ammo", float, restrictPositive=True,
                                        initialValue=1200.0)
        self.tankParams.pack()
        self.healingFrame.pack()
        self.healingRate.pack()
        self.healAmmo.pack()

    def value(self):
        return [self.tankParams.value(), [self.healingRate.value(), self.healAmmo.value()]]

    def setValue(self, l):
        self.tankParams.setValue(l[0])
        self.healingRate.setValue(l[1][0])
        self.healAmmo.setValue(l[1][1])


class GrapeParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Armored Vehicle Grape"))
        self.parent = parent
        self.bodyTurning = FreeInputWidget(self, "Body turning speed", float, restrictPositive=True,
                                           initialValue=0.75)
        self.maxSpeed = FreeInputWidget(self, "Max speed", float, restrictPositive=True, initialValue=70.0)
        self.brakes = SliderWidget(self, "Braking power", 0, 1, resolution=0.001, tooltip="1 = instant stop",
                                   initialValue=0.015)
        self.unknown1 = FreeInputWidget(self, "Unknown float", float, initialValue=1.0)
        self.unknown2 = FreeInputWidget(self, "Unknown float", float, initialValue=0.075)
        self.acceleration = FreeInputWidget(self, "Acceleration?", float, restrictPositive=True, initialValue=0.5)
        self.unknown3 = FreeInputWidget(self, "Unknown float", float, restrictPositive=True, initialValue=0.25)

        self.bodyTurning.pack()
        self.maxSpeed.pack()
        self.brakes.pack()
        self.unknown1.pack()
        self.unknown2.pack()
        self.acceleration.pack()
        self.unknown3.pack()

    def value(self):
        return [self.bodyTurning.value(),
                self.maxSpeed.value(),
                self.brakes.value(),
                self.unknown1.value(),
                self.unknown2.value(),
                self.acceleration.value(),
                self.unknown3.value()]

    def setValue(self, l):
        self.bodyTurning.setValue(l[0])
        self.maxSpeed.setValue(l[1])
        self.brakes.setValue(l[2])
        self.unknown1.setValue(l[3])
        self.unknown2.setValue(l[4])
        self.acceleration.setValue(l[5])
        self.unknown3.setValue(l[6])


class BikeParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Free Bike"))


class NixParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Nix"))
        
        self.movementFrame = tk.LabelFrame(self, text=getText("Movement"), bd=5)
        self.walkSpeed = FreeInputWidget(self.movementFrame, "Walking speed", float, restrictPositive=True, initialValue=7.5)
        self.walkAcceleration = FreeInputWidget(self.movementFrame, "Walk acceleration", float, restrictPositive=True, initialValue=0.005)
        self.turnSpeed = FreeInputWidget(self.movementFrame, "Turn speed", float, restrictPositive=True, initialValue=35.0)
        self.turnAcceleration = FreeInputWidget(self.movementFrame, "Turn acceleration?", float, restrictPositive=True, initialValue=0.06)
        
        self.jumpFrame = tk.LabelFrame(self, text=getText("Jump"), bd=5)
        self.jumpPower = FreeInputWidget(self.jumpFrame, "Jump power", float, restrictPositive=True, initialValue=10.0)
        self.jumpSpeed = SliderWidget(self.jumpFrame, "Jump startup speed", 0.0, 5.0, resolution=0.01, initialValue=3.0)
        self.unknown1 = FreeInputWidget(self.jumpFrame, "Unknown float", float)
        self.boostTime = FreeInputWidget(self.jumpFrame, "Boost time (frames)", int, restrictPositive=True, initialValue=300)
        self.boostPower = FreeInputWidget(self.jumpFrame, "Boost power", float, restrictPositive=True, initialValue=0.5)
        self.boostDelay = FreeInputWidget(self.jumpFrame, "Boost delay", int, restrictPositive=True, initialValue=80)
        
        self.aimFrame = tk.LabelFrame(self, text=getText("Aiming"), bd=5)
        self.aimMaxSpeed = FreeInputWidget(self.aimFrame, "Aiming max speed", float, initialValue=60.0)
        self.aimAcceleration = SliderWidget(self.aimFrame, "Aiming acceleration", 0, 0.999, resolution=0.001, initialValue=0.05)
        self.aimFriction = SliderWidget(self.aimFrame, "Aim friction", 0, 0.999, resolution=0.001, tooltip="", initialValue=0.1)

        self.unknownStruct = tk.LabelFrame(self, text=getText("Unknown struct"))
        self.unknown2 = FreeInputWidget(self, "Unknown float", float, initialValue=0.019999999552965164)
        self.unknown3 = FreeInputWidget(self, "Unknown float", float, initialValue=0.10000000149011612)

        self.movementFrame.pack()
        self.walkSpeed.pack()
        self.walkAcceleration.pack()
        self.turnSpeed.pack()
        self.turnAcceleration.pack()

        self.jumpFrame.pack()
        self.jumpPower.pack()
        self.jumpSpeed.pack()
        self.unknown1.pack()
        self.boostTime.pack()
        self.boostPower.pack()
        self.boostDelay.pack()

        self.aimFrame.pack()
        self.aimMaxSpeed.pack()
        self.aimAcceleration.pack()
        self.aimFriction.pack()

        self.unknownStruct.pack()
        self.unknown2.pack()
        self.unknown3.pack()

    def value(self):
        return [
            [self.walkSpeed.value(),
             self.walkAcceleration.value(),
             self.turnSpeed.value(),
             self.turnAcceleration.value()],

            [self.jumpPower.value(),
             self.jumpSpeed.value(),
             self.unknown1.value(),
             self.boostTime.value(),
             self.boostPower.value(),
             self.boostDelay.value()],

            [[self.aimMaxSpeed.value(),
             self.aimAcceleration.value(),
             self.aimFriction.value()]],

            [self.unknown2.value(),
             self.unknown3.value()]
            ]

    def setValue(self, l):
        self.walkSpeed.setValue(l[0][0])
        self.walkAcceleration.setValue(l[0][1])
        self.turnSpeed.setValue(l[0][2])
        self.turnAcceleration.setValue(l[0][3])

        self.jumpPower.setValue(l[1][0])
        self.jumpSpeed.setValue(l[1][1])
        self.unknown1.setValue(l[1][2])
        self.boostTime.setValue(l[1][3])
        self.boostPower.setValue(l[1][4])
        self.boostDelay.setValue(l[1][5])

        self.aimMaxSpeed.setValue(l[2][0])
        self.aimAcceleration.setValue(l[2][1])
        self.aimFriction.setValue(l[2][2])

        self.unknown2.setValue(l[3][0])
        self.unknown3.setValue(l[3][1])


class HeliParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Helicopter"))


class CrawlerParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Depth Crawler"))


class VehicleWeaponChoice(tk.LabelFrame):
    def __init__(self, parent, label, includesRecoil, isTurret, damageMultiplierWidget, recoilType=""):
        self.parent = parent
        self.includesRecoil = includesRecoil
        self.isTurret = isTurret
        self.damageMultiplierWidget = damageMultiplierWidget
        self.recoilType = recoilType
        tk.LabelFrame.__init__(self, parent, text=getText(label), bd=5)
        self.weaponChoice = MultiDropDownWidget(self, "Weapon Choice", vehicleWeapons)
        self.statsFrame = tk.LabelFrame(self, text=getText("Weapon stats"))
        self.ammoClass = FreeInputWidget(self.statsFrame, "Ammo class", str)
        self.ammoCount = FreeInputWidget(self.statsFrame, "Ammo", int)
        self.baseDamage = FreeInputWidget(self.statsFrame, "Damage", str)
        self.firingRate = FreeInputWidget(self.statsFrame, "Firing Rate", str)
        self.dps = FreeInputWidget(self.statsFrame, "Damage per second", str, tooltip="May be inaccurate for burst weapons")
        self.totalDamage = FreeInputWidget(self.statsFrame, "Potential damage", str)
        self.explosionRadius = FreeInputWidget(self.statsFrame, "Blast Radius", str)
        self.ammoSpeed = FreeInputWidget(self.statsFrame, "Ammo Speed", str, tooltip="Inaccurate for missiles/rockets")
        self.range = FreeInputWidget(self.statsFrame, "Range", str, tooltip="Inaccurate for missiles/rockets")

        self.weaponChoice.valueLabel.inputVar.trace_add("write", self.updateStats)
        self.damageMultiplierWidget.inputVar.trace_add("write", self.updateStats)

        disableInput(self.ammoClass)
        disableInput(self.ammoCount)
        disableInput(self.baseDamage)
        disableInput(self.firingRate)
        disableInput(self.dps)
        disableInput(self.totalDamage)
        disableInput(self.explosionRadius)
        disableInput(self.ammoSpeed)
        disableInput(self.range)

        self.weaponChoice.pack()
        self.statsFrame.pack()
        self.ammoClass.pack()
        self.ammoCount.pack()
        self.baseDamage.pack()
        self.firingRate.pack()
        self.dps.pack()
        self.totalDamage.pack()
        self.explosionRadius.pack()
        self.ammoSpeed.pack()
        self.range.pack()

        self.lockonType = 0
        self.lockonRange = FreeInputWidget(self, "Lock-on range (meters)", float)
        self.lockonTime = FreeInputWidget(self, "Lock-on time (seconds)", int)
        disableInput(self.lockonRange)
        disableInput(self.lockonTime)

        self.recoilFrame = None

        if includesRecoil:
            self.recoilFrame = tk.LabelFrame(self, text=getText("Recoil"))
            self.pushback = FreeInputWidget(self.recoilFrame, "Firing pushback", float)
            self.recoil = FreeInputWidget(self.recoilFrame, "Vertical recoil", float)
            self.recoilFrame.pack()
            self.pushback.pack()
            self.recoil.pack()

        self.turretControl = None

        if isTurret:
            self.turretControl = tk.LabelFrame(self, text=getText("Turret parameters"))
            self.turretMaxSpeed = FreeInputWidget(self.turretControl, "Turret max speed", float, initialValue=100.0)
            self.turretAcceleration = SliderWidget(self.turretControl, "Turret acceleration", 0, 0.999,
                                                   resolution=0.001, initialValue=0.01)
            self.aimFriction = SliderWidget(self.turretControl, "Aim friction", 0, 0.999, resolution=0.001,
                                            tooltip="", initialValue=0.05)
            self.turretControl.pack()
            self.turretMaxSpeed.pack()
            self.turretAcceleration.pack()
            self.aimFriction.pack()

        self.updateStats()

    def value(self):
        if self.weaponChoice.value() == "none":
            return [0]
        v = [self.weaponChoice.value()]
        if self.includesRecoil:
            if self.recoilType == "":
                v.append([self.pushback.value(), self.recoil.value()])
            else:
                v.append([self.recoilType, [self.pushback.value(), self.recoil.value()]])
        if self.isTurret:
            v.append([self.turretMaxSpeed.value(), self.turretAcceleration.value(), self.aimFriction.value()])
        return v

    def setValue(self, l):
        self.weaponChoice.setValue(l[0])
        if len(l) == 1:
            self.includesRecoil = False
            self.recoilType = ""
            self.isTurret = False
        elif len(l) == 2:
            self.includesRecoil = True
            self.isTurret = False
            if isinstance(l[1][0], str):
                self.recoilType = l[1][0]
                self.pushback.setValue(l[1][1][0])
                self.recoil.setValue(l[1][1][1])
            else:
                self.pushback.setValue(l[1][0])
                self.recoil.setValue(l[1][1])
        elif len(l) == 3:
            self.includesRecoil = True
            self.isTurret = True
            if isinstance(l[1][0], str):
                self.recoilType = l[1][0]
                self.pushback.setValue(l[1][1][0])
                self.recoil.setValue(l[1][1][1])
            else:
                self.pushback.setValue(l[1][0])
                self.recoil.setValue(l[1][1])
            self.turretMaxSpeed.setValue(l[2][0])
            self.turretAcceleration.setValue(l[2][1])
            self.aimFriction.setValue(l[2][2])

    def updateStats(self, *args):
        w = vehicleWeaponStats[self.weaponChoice.value()]
        if self.weaponChoice.value() == "none":
            self.statsFrame.pack_forget()
            if self.recoilFrame is not None:
                self.recoilFrame.pack_forget()
            if self.turretControl is not None:
                self.turretControl.pack_forget()
            self.lockonRange.pack_forget()
            self.lockonTime.pack_forget()
        else:
            self.statsFrame.pack()
            if self.includesRecoil:
                self.recoilFrame.pack()
            if self.isTurret:
                self.turretControl.pack()
        self.ammoClass.setValue(w["AmmoClass"])
        self.ammoCount.setValue(w["AmmoCount"])
        if w["AmmoDamageReduce"][0] == 1.0:
            damageStr = str(w['AmmoDamage'] * self.damageMultiplierWidget.value())
        else:
            damageStr = f"{str(w['AmmoDamage'] * self.damageMultiplierWidget.value())} ~ {round(w['AmmoDamage'] * w['AmmoDamageReduce'][0] * self.damageMultiplierWidget.value(), 2)}"
        if w["AmmoIsPenetration"] == 1:
            damageStr += " [PT]"
        if w['FireCount'] > 1:
            damageStr += f"{(' x ' + str(w['FireCount'])) if w['FireCount'] != 0 else ''}"
        if w["FireBurstCount"] > 1:
            damageStr += f" ({w['FireBurstCount']} {getText('burst')})"
        self.baseDamage.setValue(damageStr)
        self.firingRate.setValue(f"{round((60 / (w['FireInterval'] + 1)), 2)} {getText('shots/s')}")
        dps = str(round(((60 / (w["FireInterval"] + 1 + w["FireBurstCount"] * w["FireBurstInterval"])) * w[
            "AmmoDamage"] * w["FireBurstCount"] * w[
                             "FireCount"] * self.damageMultiplierWidget.value()), 2))
        if w["AmmoDamageReduce"][0] != 1.0:
            dps += " ~ "
            dps += str(round(((60 / (w["FireInterval"] + 1 + w["FireBurstCount"] * w["FireBurstInterval"])) * w[
                "AmmoDamage"] * w[
                                  "FireBurstCount"] * w[
                                  "FireCount"] * w["AmmoDamageReduce"][0] * self.damageMultiplierWidget.value()),
                             2))
        self.dps.setValue(dps)
        self.totalDamage.setValue(w["AmmoDamage"] * w["AmmoCount"] * w["FireCount"])
        self.explosionRadius.setValue(str(w["AmmoExplosion"]) + "m")
        self.ammoSpeed.setValue(str(round((w["AmmoSpeed"] * 60), 2)) + "m/s")
        self.range.setValue(str(round((w["AmmoSpeed"] * w["AmmoAlive"]), 2)) + "m")

        if w["LockonType"] == 1 or w["LockonType"] == 3:
            self.lockonRange.setValue(f"{w['LockonRange']} m")
            self.lockonTime.setValue(f"{round((w['LockonTime'] / 60), 2)} s")
            self.lockonRange.pack()
            self.lockonTime.pack()
        else:
            self.lockonRange.pack_forget()
            self.lockonTime.pack_forget()