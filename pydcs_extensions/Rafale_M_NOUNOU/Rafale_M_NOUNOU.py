from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from pydcs_extensions.weapon_injector import inject_weapons




class WeaponsRafale_M_NOUNOU:
    MICA_IR = {"clsid": "{0DA03783-61E4-40B2-8FAE-6AEE0A5C5AAE}", "name": "MICA IR", "weight": 110}
    R_550_Magic_2 = {"clsid": "{FC23864E-3B80-48E3-9C03-4DA8B1D7497B}", "name": "R.550 Magic 2", "weight": 89}
    Smoke_Generator___blue_smk_ = {"clsid": "{INV-SMOKE-BLUE}", "name": "Smoke Generator - blue_smk", "weight": 0}
    Smoke_Generator___red_smk_ = {"clsid": "{INV-SMOKE-RED}", "name": "Smoke Generator - red_smk", "weight": 0}
    Smoke_Generator___white_ = {"clsid": "{INV-SMOKE-WHITE}", "name": "Smoke Generator - white", "weight": 0}
    Smokewinder___blue_smk = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E743}", "name": "Smokewinder - blue_smk", "weight": 200}
    Smokewinder___green = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E742}", "name": "Smokewinder - green", "weight": 200}
    Smokewinder___orange = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E746}", "name": "Smokewinder - orange", "weight": 200}


inject_weapons(WeaponsRafale_M_NOUNOU)


class Rafale_M_NOUNOU(PlaneType):
    id = "Rafale_M_NOUNOU"
    group_size_max = 1
    height = 5.28
    width = 10.13
    length = 15.96
    fuel_max = 4500
    max_speed = 2001.996
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1
    tacan = True
    category = "Tankers"  #{8A302789-A55D-4897-B647-66493FA6826F}
    radio_frequency = 127.5

    class Liveries:

        class USSR(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Georgia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Venezuela(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Australia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Israel(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Combined_Joint_Task_Forces_Blue(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Sudan(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Norway(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Romania(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Iran(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Ukraine(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Libya(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Belgium(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Slovakia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Greece(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class UK(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Third_Reich(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Hungary(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Abkhazia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Morocco(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class United_Nations_Peacekeepers(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Switzerland(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class SouthOssetia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Vietnam(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class China(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Yemen(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Kuwait(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Serbia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Oman(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class India(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Egypt(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class TheNetherlands(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Poland(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Syria(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Finland(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Kazakhstan(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Denmark(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Sweden(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Croatia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class CzechRepublic(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class GDR(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Yugoslavia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Bulgaria(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class SouthKorea(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Tunisia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Combined_Joint_Task_Forces_Red(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Lebanon(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Portugal(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Cuba(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Insurgents(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class SaudiArabia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class France(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class USA(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Honduras(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Qatar(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Russia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class United_Arab_Emirates(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Italian_Social_Republi(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Austria(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Bahrain(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Italy(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Chile(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Turkey(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Philippines(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Algeria(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Pakistan(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Malaysia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Indonesia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Iraq(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Germany(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class South_Africa(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Jordan(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Mexico(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class USAFAggressors(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Brazil(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Spain(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Belarus(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Canada(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class NorthKorea(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Ethiopia(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Japan(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

        class Thailand(Enum):
            _01_marine_12_f = "01 marine 12 f"
            _02_rafale_export = "02 rafale export"
            _03_black_derive_11f = "03 black derive 11f"

    class Pylon1:
        MICA_IR = (1, Weapons.MICA_IR)
        R_550_Magic_2 = (1, Weapons.R_550_Magic_2)

    class Pylon10:
        MICA_IR = (10, Weapons.MICA_IR)
        R_550_Magic_2 = (10, Weapons.R_550_Magic_2)

    class Pylon11:
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue_smk = (11, Weapons.Smokewinder___blue_smk)
        Smokewinder___orange = (11, Weapons.Smokewinder___orange)
        Smoke_Generator___red_smk_ = (11, Weapons.Smoke_Generator___red_smk_)
        Smoke_Generator___blue_smk_ = (11, Weapons.Smoke_Generator___blue_smk_)
        Smoke_Generator___white_ = (11, Weapons.Smoke_Generator___white_)

    pylons = {1, 10, 11}

    tasks = [task.Refueling]
    task_default = task.Refueling


