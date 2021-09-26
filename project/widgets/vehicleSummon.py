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
    "Proteus":{
        "Proteus": 'app:/Object/Vehicle407_bigbegaruta.sgo'
    },
    "Barga": {
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
        vp = self.vehicleParams.value()
        if self.vehicleSGO.value() in vehicleSGOS["Tank"].values():
            v[4][3].append(vp)
            v[4][3].append([w.value() for w in self.weaponWidgets])
        elif self.vehicleSGO.value() == "app:/Object/Vehicle401_Striker.sgo":  # Grape
            v[4][3].append(vp)
            v[4][3].append([w.value() for w in self.weaponWidgets])
        elif self.vehicleSGO.value() == 'app:/Object/v507_rescuetank.sgo' or \
                self.vehicleSGO.value() == 'app:/Object/v507_rescuetank_siawase.sgo':  # Caliban
            v[4][3].append(vp[0])
            v[4][3].append(vp[1])
            v[4][3].append(['app:/weapon/v_507_RescueUnit01.sgo'])
        elif self.vehicleSGO.value() == 'app:/Object/Vehicle402_Rocket.sgo':  # Naegling
            v[4][3].append(vp)
            v[4][3].append([w.value() for w in self.weaponWidgets])
        elif self.vehicleSGO.value() in ['app:/Object/v506_heli.sgo', 'app:/Object/Vehicle410_heli.sgo']:  # Eros, Brute
            v[4][3].append(vp[0])
            v[4][3].append(vp[1])
            v[4][3].append([w.value() for w in self.weaponWidgets])
        elif self.vehicleSGO.value() == 'app:/Object/Vehicle409_heli.sgo':  # Nereid
            v[4][3].append(vp[0])
            v[4][3].append(vp[1])
            v[4][3].append([w.value() for w in self.weaponWidgets])
            v[4][3].append(vp[2])
        elif self.vehicleSGO.value() in vehicleSGOS["Nix"].values():  # Nix
            v[4][3].append(vp[0])
            v[4][3].append(vp[1])
            v[4][3].append(vp[2])
            v[4][3].append([w.value() for w in self.weaponWidgets])
            v[4][3].append(vp[3])
        elif self.vehicleSGO.value() == 'app:/Object/Vehicle407_bigbegaruta.sgo':
            v[4][3].append(vp[0])
            v[4][3].append(vp[1])
            v[4][3].append(vp[2])
            v[4][3].append([w.value() for w in self.weaponWidgets])
            v[4][3].append(vp[3])
        elif self.vehicleSGO.value() in vehicleSGOS["Depth Crawler"].values():
            v[4][3].append(vp[0])
            v[4][3].append([w.value() for w in self.weaponWidgets])
            v[4][3].append(vp[1])
        elif self.vehicleSGO.value() == 'app:/Object/v512_keiTruck_bgp.sgo':  # Truck
            pass
        elif self.vehicleSGO.value() == 'app:/Object/v503_bike.sgo' or \
                self.vehicleSGO.value() == 'app:/Object/v503_bike_omegaz.sgo':  # Bike
            pass
        elif self.vehicleSGO.value() in vehicleSGOS["Barga"].values():
            v[4][3].append(None)
            v[4][3].append([0, 0])

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
            replaceParamsAndRemoveWeapons(self, HeliParams)
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Left gun", True, False, self.weaponMultiplier))
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Right gun", True, False, self.weaponMultiplier))
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Missile pod", True, False, self.weaponMultiplier))
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Fuel", False, False, self.weaponMultiplier))
            self.weaponWidgets[0].pack()
            self.weaponWidgets[1].pack()
            self.weaponWidgets[2].pack()
            self.weaponWidgets[0].setValue(['app:/weapon/v_506heli_gatling01_l.sgo', [0.0, 0.0]])
            self.weaponWidgets[1].setValue(['app:/weapon/v_506heli_gatling01_r.sgo', [0.0, 0.0]])
            self.weaponWidgets[2].setValue(['app:/weapon/v_506heli_missile01.sgo', [0.0, 0.0]])
            self.weaponWidgets[3].setValue(['app:/weapon/v_fuel01.sgo'])

        elif self.vehicleSGO.value() == 'app:/Object/Vehicle409_heli.sgo':  # Nereid
            self.baseHP = 300.0
            replaceParamsAndRemoveWeapons(self, NereidParams)
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Auto-acquisition cannon", True, False, self.weaponMultiplier))
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Missile pod", True, False, self.weaponMultiplier))
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Fuel", False, False, self.weaponMultiplier))
            self.weaponWidgets[0].pack()
            self.weaponWidgets[1].pack()
            self.weaponWidgets[0].setValue(['app:/weapon/v_409heli_gatling01.sgo', [0.0, 0.0]])
            self.weaponWidgets[1].setValue(['app:/weapon/v_409heli_missile01.sgo', [0.0, 0.0]])
            self.weaponWidgets[2].setValue(['app:/weapon/v_fuel01.sgo'])


        elif self.vehicleSGO.value() == 'app:/Object/Vehicle410_heli.sgo':  # Brute
            self.baseHP = 1800.0
            replaceParamsAndRemoveWeapons(self, HeliParams)
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Side guns", True, True, self.weaponMultiplier, recoilType="AimRecoil"))
            self.weaponWidgets.append(VehicleWeaponChoice(self.col2, "Fuel", False, False, self.weaponMultiplier))
            self.weaponWidgets[0].pack()
            self.weaponWidgets[0].setValue(['app:/weapon/v_410heli_gatling01.sgo', ['AimRecoil', [0.0, 0.0]], [90.0, 0.009999999776482582, 0.019999999552965164]])
            self.weaponWidgets[1].setValue(['app:/weapon/v_fuel01.sgo'])

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
        elif self.vehicleSGO.value() in vehicleSGOS["Depth Crawler"].values():
            self.baseHP = 1000.0
            if not isinstance(self.vehicleParams, CrawlerParams):
                replaceParamsAndRemoveWeapons(self, CrawlerParams)
                self.weaponWidgets.append(
                    VehicleWeaponChoice(self.col2, "Gatling", False, False, self.weaponMultiplier))
                self.weaponWidgets.append(
                    VehicleWeaponChoice(self.col2, "Left gun", False, False, self.weaponMultiplier))
                self.weaponWidgets.append(
                    VehicleWeaponChoice(self.col2, "Right gun", False, False, self.weaponMultiplier))
                self.weaponWidgets[0].setValue(['app:/weapon/v_502_groundrobo_gatling.sgo'])
                self.weaponWidgets[1].setValue(['app:/weapon/v_502_groundrobo_missile01_l.sgo'])
                self.weaponWidgets[2].setValue(['app:/weapon/v_502_groundrobo_missile01_r.sgo'])
                self.weaponWidgets[0].pack()
                self.weaponWidgets[1].pack()
                self.weaponWidgets[2].pack()
        elif self.vehicleSGO.value() in vehicleSGOS["Barga"].values():
            self.baseHP = 50000.0
            replaceParamsAndRemoveWeapons(self, BargaParams)
                

    # def test(self):
    #     print(self.__class__.__name__)
    #     testDict = ammoCust[self.__class__.__name__]["Ammo_CustomParameter"]
    #     testValues = [eval(key) for key in testDict.keys()]
    #     for v in testValues:
    #         self.setValue(v)
    #         if v != self.value():
    #             print(v)
    #             print(self.value())
    #             raise ValueError(f"actual\n{self.value()}\n!=expected\n{v}")
    #     print(f"{self.__class__.__name__} tests successful")


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
        self.jumpSpeed = SliderWidget(self.jumpFrame, "Jump animation speed factor", 0.0, 5.0, resolution=0.01, initialValue=3.0)
        self.verticalBoostPower = FreeInputWidget(self.jumpFrame, "Vertical boost power?", float, restrictPositive=True, initialValue=45.0)
        self.boostTime = FreeInputWidget(self.jumpFrame, "Boost time (frames)", int, restrictPositive=True, initialValue=300)
        self.horizontalBoostPower = FreeInputWidget(self.jumpFrame, "Horizontal boost power?", float, restrictPositive=True, initialValue=0.5)
        self.boostDelay = FreeInputWidget(self.jumpFrame, "Boost delay", int, restrictPositive=True, initialValue=80)
        
        self.aimFrame = tk.LabelFrame(self, text=getText("Aiming"), bd=5)
        self.aimMaxSpeed = FreeInputWidget(self.aimFrame, "Aiming max speed", float, initialValue=60.0)
        self.aimAcceleration = SliderWidget(self.aimFrame, "Aiming acceleration", 0, 0.999, resolution=0.001, initialValue=0.05)
        self.aimFriction = SliderWidget(self.aimFrame, "Aim friction", 0, 0.999, resolution=0.001, tooltip="", initialValue=0.1)

        self.unknownStruct = tk.LabelFrame(self, text=getText("Unknown struct"))
        self.unknown2 = FreeInputWidget(self.unknownStruct, "Unknown float", float, initialValue=0.019999999552965164)
        self.unknown3 = FreeInputWidget(self.unknownStruct, "Unknown float", float, initialValue=0.10000000149011612)

        self.movementFrame.pack()
        self.walkSpeed.pack()
        self.walkAcceleration.pack()
        self.turnSpeed.pack()
        self.turnAcceleration.pack()

        self.jumpFrame.pack()
        self.jumpPower.pack()
        self.jumpSpeed.pack()
        self.verticalBoostPower.pack()
        self.boostTime.pack()
        self.horizontalBoostPower.pack()
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
             self.verticalBoostPower.value(),
             self.boostTime.value(),
             self.horizontalBoostPower.value(),
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
        self.verticalBoostPower.setValue(l[1][2])
        self.boostTime.setValue(l[1][3])
        self.horizontalBoostPower.setValue(l[1][4])
        self.boostDelay.setValue(l[1][5])

        self.aimMaxSpeed.setValue(l[2][0])
        self.aimAcceleration.setValue(l[2][1])
        self.aimFriction.setValue(l[2][2])

        self.unknown2.setValue(l[3][0])
        self.unknown3.setValue(l[3][1])


class BargaParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Barga"))

    def value(self):
        return [None, [0, 0]]

    def setValue(self):
        pass


class ProteusParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Proteus"))
        self.col1 = tk.Frame(self)
        self.col2 = tk.Frame(self)
        self.movementFrame = tk.LabelFrame(self.col1, text=getText("Movement"), bd=5)
        self.walkSpeed = FreeInputWidget(self.movementFrame, "Walking speed", float, restrictPositive=True, initialValue=12.0)
        self.walkAcceleration = FreeInputWidget(self.movementFrame, "Walk acceleration", float, restrictPositive=True, initialValue=0.005)
        self.turnSpeed = FreeInputWidget(self.movementFrame, "Turn speed", float, restrictPositive=True, initialValue=20.0)
        self.turnAcceleration = FreeInputWidget(self.movementFrame, "Turn acceleration?", float, restrictPositive=True, initialValue=0.007)

        self.jumpFrame = tk.LabelFrame(self.col1, text=getText("Jump"), bd=5)
        self.jumpPower = FreeInputWidget(self.jumpFrame, "Jump power", float, restrictPositive=True, initialValue=10.0)
        self.jumpSpeed = SliderWidget(self.jumpFrame, "Jump animation speed factor", 0.0, 5.0, resolution=0.01, initialValue=3.0)
        self.verticalBoostPower = FreeInputWidget(self.jumpFrame, "Vertical boost power?", float, restrictPositive=True, initialValue=25.0, tooltip="Seemingly no effect on Proteus, as it has no boosters")
        self.boostTime = FreeInputWidget(self.jumpFrame, "Boost time (frames)", int, restrictPositive=True, initialValue=0, tooltip="Seemingly no effect on Proteus, as it has no boosters")
        self.horizontalBoostPower = FreeInputWidget(self.jumpFrame, "Horizontal boost power?", float, restrictPositive=True, initialValue=0.0, tooltip="Seemingly no effect on Proteus, as it has no boosters")
        self.boostDelay = FreeInputWidget(self.jumpFrame, "Boost delay", int, restrictPositive=True, initialValue=0, tooltip="Seemingly no effect on Proteus, as it has no boosters")

        self.torsoFrame = tk.LabelFrame(self.col2, text=getText("Torso control"), bd=5)
        self.torsoMaxSpeed = FreeInputWidget(self.torsoFrame, "Aiming max speed", float, initialValue=60.0)
        self.torsoAcceleration = SliderWidget(self.torsoFrame, "Aiming acceleration", 0, 0.999, resolution=0.001, initialValue=0.05)
        self.torsoFriction = SliderWidget(self.torsoFrame, "Aim friction", 0, 0.999, resolution=0.001, tooltip="How easily aiming comes to a stop", initialValue=0.1)

        self.leftCannonFrame = tk.LabelFrame(self.col2, text=getText("Left cannon control"), bd=5)
        self.leftCannonMaxSpeed = FreeInputWidget(self.leftCannonFrame, "Aiming max speed", float, initialValue=60.0)
        self.leftCannonAcceleration = SliderWidget(self.leftCannonFrame, "Aiming acceleration", 0, 0.999, resolution=0.001, initialValue=0.05)
        self.leftCannonFriction = SliderWidget(self.leftCannonFrame, "Aim friction", 0, 0.999, resolution=0.001, tooltip="How easily aiming comes to a stop", initialValue=0.1)

        self.rightCannonFrame = tk.LabelFrame(self.col2, text=getText("Right cannon control"), bd=5)
        self.rightCannonMaxSpeed = FreeInputWidget(self.rightCannonFrame, "Aiming max speed", float, initialValue=60.0)
        self.rightCannonAcceleration = SliderWidget(self.rightCannonFrame, "Aiming acceleration", 0, 0.999, resolution=0.001, initialValue=0.05)
        self.rightCannonFriction = SliderWidget(self.rightCannonFrame, "Aim friction", 0, 0.999, resolution=0.001, tooltip="How easily aiming comes to a stop", initialValue=0.1)

        self.missileFrame = tk.LabelFrame(self.col2, text=getText("Aiming"), bd=5)
        self.missileMaxSpeed = FreeInputWidget(self.missileFrame, "Aiming max speed", float, initialValue=60.0)
        self.missileAcceleration = SliderWidget(self.missileFrame, "Aiming acceleration", 0, 0.999, resolution=0.001, initialValue=0.05)
        self.missileFriction = SliderWidget(self.missileFrame, "Aim friction", 0, 0.999, resolution=0.001, tooltip="How easily aiming comes to a stop", initialValue=0.1)

        self.unknownStruct = tk.LabelFrame(self.col1, text=getText("Unknown struct"))
        self.unknown2 = FreeInputWidget(self.unknownStruct, "Unknown float", float, initialValue=0.019999999552965164)
        self.unknown3 = FreeInputWidget(self.unknownStruct, "Unknown float", float, initialValue=0.10000000149011612)


        self.col1.grid(row=0, column=0, sticky="N")
        self.col2.grid(row=0, column=1, sticky="N")
        self.movementFrame.pack()
        self.walkSpeed.pack()
        self.walkAcceleration.pack()
        self.turnSpeed.pack()
        self.turnAcceleration.pack()
        self.jumpFrame.pack()
        self.jumpPower.pack()
        self.jumpSpeed.pack()
        # self.verticalBoostPower.pack()
        # self.boostTime.pack()
        # self.horizontalBoostPower.pack()
        # self.boostDelay.pack()
        self.torsoFrame.pack()
        self.torsoMaxSpeed.pack()
        self.torsoAcceleration.pack()
        self.torsoFriction.pack()
        self.leftCannonFrame.pack()
        self.leftCannonMaxSpeed.pack()
        self.leftCannonAcceleration.pack()
        self.leftCannonFriction.pack()
        self.rightCannonFrame.pack()
        self.rightCannonMaxSpeed.pack()
        self.rightCannonAcceleration.pack()
        self.rightCannonFriction.pack()
        self.missileFrame.pack()
        self.missileMaxSpeed.pack()
        self.missileAcceleration.pack()
        self.missileFriction.pack()
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
                 self.verticalBoostPower.value(),
                 self.boostTime.value(),
                 self.horizontalBoostPower.value(),
                 self.boostDelay.value()],

                [[self.torsoMaxSpeed.value(),
                 self.torsoAcceleration.value(),
                 self.torsoFriction.value()],

                [self.leftCannonMaxSpeed.value(),
                 self.leftCannonAcceleration.value(),
                 self.leftCannonFriction.value()],

                [self.rightCannonMaxSpeed.value(),
                 self.rightCannonAcceleration.value(),
                 self.rightCannonFriction.value()],

                [self.missileMaxSpeed.value(),
                 self.missileAcceleration.value(),
                 self.missileFriction.value()]],

                [self.unknown2.value(),
                 self.unknown3.value()],
        ]

    def setValue(self, l):
        self.walkSpeed.setValue(l[0][0])
        self.walkAcceleration.setValue(l[0][1])
        self.turnSpeed.setValue(l[0][2])
        self.turnAcceleration.setValue(l[0][3])

        self.jumpPower.setValue(l[1][0])
        self.jumpSpeed.setValue(l[1][1])
        self.verticalBoostPower.setValue(l[1][2])
        self.boostTime.setValue(l[1][3])
        self.horizontalBoostPower.setValue(l[1][4])
        self.boostDelay.setValue(l[1][5])

        self.torsoMaxSpeed.setValue(l[2][0][0])
        self.torsoAcceleration.setValue(l[2][0][1])
        self.torsoFriction.setValue(l[2][0][2])

        self.leftCannonMaxSpeed.setValue(l[2][1][0])
        self.leftCannonAcceleration.setValue(l[2][1][1])
        self.leftCannonFriction.setValue(l[2][1][2])

        self.rightCannonMaxSpeed.setValue(l[2][2][0])
        self.rightCannonAcceleration.setValue(l[2][2][1])
        self.rightCannonFriction.setValue(l[2][2][2])

        self.missileMaxSpeed.setValue(l[2][3][0])
        self.missileAcceleration.setValue(l[2][3][1])
        self.missileFriction.setValue(l[2][3][2])

        self.unknown2.setValue(l[3][0])
        self.unknown3.setValue(l[3][1])


class HeliParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Helicopter"))
        self.horizontalSpeed = FreeInputWidget(self, "Horizontal max speed", float, restrictPositive=True, initialValue=40.0)
        self.horizontalAccel = FreeInputWidget(self, "Horizontal acceleration", float, restrictPositive=True, initialValue=0.001)
        self.turnSpeed = FreeInputWidget(self, "Max turn speed", float, restrictPositive=True, initialValue=10.0)
        self.turnAccel = FreeInputWidget(self, "Turn acceleration", float, restrictPositive=True, initialValue=0.002)
        self.lift = FreeInputWidget(self, "Vertical lift", float, restrictPositive=True, initialValue=2)
        self.tiltAngle = FreeInputWidget(self, "Max tilt angle", float, restrictPositive=True, initialValue=40.0, tooltip="Degrees?")
        self.tiltAccel = FreeInputWidget(self, "Tilt acceleration", float, restrictPositive=True, initialValue=0.006)

        self.fuel = FreeInputWidget(self, "Fuel", float, restrictPositive=True, initialValue=40000.0)
        self.fuelConsumption = FreeInputWidget(self, "Fuel consumption rate?", float, restrictPositive=True, initialValue=0.2)

        self.horizontalSpeed.pack()
        self.horizontalAccel.pack()
        self.turnSpeed.pack()
        self.turnAccel.pack()
        self.tiltAngle.pack()
        self.tiltAccel.pack()
        self.fuel.pack()
        self.fuelConsumption.pack()

    def value(self):
        return [
            [self.horizontalSpeed.value(),
             self.horizontalAccel.value(),
             self.turnSpeed.value(),
             self.turnAccel.value(),
             self.lift.value(),
             self.tiltAngle.value(),
             self.tiltAccel.value()],
            [self.fuel.value(),
             self.fuelConsumption.value()]
        ]

    def setValue(self, l):
        self.horizontalSpeed.setValue(l[0][0])
        self.horizontalAccel.setValue(l[0][1])
        self.turnSpeed.setValue(l[0][2])
        self.turnAccel.setValue(l[0][3])
        self.lift.setValue(l[0][4])
        self.tiltAngle.setValue(l[0][5])
        self.tiltAccel.setValue(l[0][6])
        self.fuel.setValue(l[1][0])
        self.fuelConsumption.setValue(l[1][1])


class NereidParams(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.heliParams = HeliParams(self)
        self.heliParams.pack()
        self.searchRange = FreeInputWidget(self, "Turret search range", float, restrictPositive=True, initialValue=200.0)
        self.trackingSpeed = FreeInputWidget(self, "Turret turning speed", float, restrictPositive=True, initialValue=0.2)
        self.searchRange.pack()
        self.trackingSpeed.pack()

    def value(self):
        return [
            self.heliParams.value()[0],
            self.heliParams.value()[1],
            [self.searchRange.value(), self.trackingSpeed.value()]
        ]

    def setValue(self, l):
        self.heliParams.setValue([l[0], l[1]])
        self.searchRange.setValue(l[2][0])
        self.trackingSpeed.setValue(l[2][1])


class CrawlerParams(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text=getText("Depth Crawler"), bd=5)
        self.walkSpeed = FreeInputWidget(self, "Walk speed", float, restrictPositive=True, initialValue=10)
        self.turnSpeed = SliderWidget(self, "Turn speed", 0, 0.2, initialValue=0.075, resolution=0.01)
        self.jumpAnimationSpeed = FreeInputWidget(self, "Jump animation speed multiplier", float, restrictPositive=True, initialValue=2.0)
        self.forwardJumpPower = FreeInputWidget(self, "Forward jump power", float, restrictPositive=True, initialValue=15.0)
        self.verticalJumpPower = FreeInputWidget(self, "Vertical jump power", float, restrictPositive=True, initialValue=15.0)
        self.unknown = FreeInputWidget(self, "Unknown int", int, tooltip="Always 0?")
        self.dodgeSpeed = FreeInputWidget(self, "Dodge speed multiplier", float, restrictPositive=True, initialValue=1.25)

        self.light1 = tk.LabelFrame(self, text=getText("Left headlight"), bd=5)
        self.light1Angle = AngleWidget(self.light1, "Light size", minimum=0, maximum=120)
        self.light1Range = FreeInputWidget(self.light1, "Light range", float, restrictPositive=True, initialValue=200.0)
        self.light1Color = ColorWidget(self.light1, "Light color", hasAlpha=False)

        self.light2 = tk.LabelFrame(self, text=getText("Right headlight"), bd=5)
        self.light2Angle = AngleWidget(self.light2, "Light size", minimum=0, maximum=120)
        self.light2Range = FreeInputWidget(self.light2, "Light range", float, restrictPositive=True, initialValue=200.0)
        self.light2Color = ColorWidget(self.light2, "Light color", hasAlpha=False)


        self.walkSpeed.pack()
        self.turnSpeed.pack()
        self.jumpAnimationSpeed.pack()
        self.forwardJumpPower.pack()
        self.verticalJumpPower.pack()
        self.unknown.pack()
        self.dodgeSpeed.pack()

        self.light1.pack()
        self.light1Angle.pack()
        self.light1Range.pack()
        self.light1Color.pack()
        self.light2.pack()
        self.light2Angle.pack()
        self.light2Range.pack()
        self.light2Color.pack()


    def value(self):
        return [
            [self.walkSpeed.value(),
             self.turnSpeed.value(),
             self.jumpAnimationSpeed.value(),
             self.forwardJumpPower.value(),
             self.verticalJumpPower.value(),
             self.unknown.value(),
             self.dodgeSpeed.value()],
            [['ライト１',
             self.light1Angle.value(),
             self.light1Range.value(),
             self.light1Color.value()],

             ['ライト２',
              self.light2Angle.value(),
              self.light2Range.value(),
              self.light2Color.value()]]

        ]


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