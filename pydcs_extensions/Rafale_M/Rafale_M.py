from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from pydcs_extensions.weapon_injector import inject_weapons




class WeaponsRafale_M:
    _3_Mk_82 = {"clsid": "{60CC734F-0AFA-4E2E-82B8-93B941AB11CF}", "name": "3 Mk-82", "weight": 783}
    AASM_250 = {"clsid": "{AASM_250}", "name": "AASM_250", "weight": 250}
    AASM_250_RIGHT = {"clsid": "{AASM_250_RIGHT}", "name": "AASM_250_RIGHT", "weight": 250}
    AASMx3L = {"clsid": "{AASMx3L}", "name": "AASMx3L", "weight": 250}
    AASMx3R = {"clsid": "{AASMx3R}", "name": "AASMx3R", "weight": 250}
    AIM_120B = {"clsid": "{C8E06185-7CD6-4C90-959F-044679E90751}", "name": "AIM-120B", "weight": 157.8}
    AIM_120C = {"clsid": "{40EF17B7-F508-45de-8566-6FFECC0C1AB8}", "name": "AIM-120C", "weight": 161.5}
    AIM_7M = {"clsid": "{8D399DDA-FF81-4F14-904D-099B34FE7918}", "name": "AIM-7M", "weight": 230}
    AIM_9M_Sidewinder_IR_AAM = {"clsid": "{6CEB49FC-DED8-4DED-B053-E1F033FF72D3}", "name": "AIM-9M Sidewinder IR AAM", "weight": 86.64}
    AIM_9P_Sidewinder_IR_AAM = {"clsid": "{9BFD8C90-F7AE-4e90-833B-BFD0CED0E536}", "name": "AIM-9P Sidewinder IR AAM", "weight": 86.18}
    AN_AAQ_28_LITENING = {"clsid": "{A111396E-D3E8-4b9c-8AC9-2432489304D5}", "name": "AN/AAQ-28 LITENING", "weight": 300}
    LAU_10___4_ZUNI_MK_71 = {"clsid": "{F3EFE0AB-E91A-42D8-9CA2-B63C91ED570A}", "name": "LAU-10 - 4 ZUNI MK 71", "weight": 440}
    LAU_115_2_LAU_127_AIM_120C = {"clsid": "LAU-115_2*LAU-127_AIM-120C", "name": "LAU-115 - 2 AIM-120C", "weight": 468}
    LAU_131___7_2_75__rockets_M151__HE_ = {"clsid": "{69926055-0DA8-4530-9F2F-C86B157EA9F6}", "name": "LAU-131 - 7 2.75' rockets M151 (HE)", "weight": 102.3}
    LAU_131x3_HYDRA_70_M151 = {"clsid": "LAU_131x3_HYDRA_70_M151", "name": "LAU-131*3 - 7 2.75' rockets M151 (HE)", "weight": 357.7}
    LAU_61___19_2_75__rockets_MK151_HE = {"clsid": "{FD90A1DC-9147-49FA-BF56-CB83EF0BD32B}", "name": "LAU-61 - 19 2.75' rockets MK151 HE", "weight": 290.59}
    LAU3_HE151 = {"clsid": "LAU3_HE151", "name": "LAU-3 - 19 2.75' rockets MK151 HE", "weight": 234}
    LAU3_HE5 = {"clsid": "LAU3_HE5", "name": "LAU-3 - 19 2.75' rockets MK5 HEAT", "weight": 234}
    LAU3_WP156 = {"clsid": "LAU3_WP156", "name": "LAU-3 - 19 2.75' rockets MK156 WP", "weight": 234}
    MER_2_MK_82 = {"clsid": "{D5D51E24-348C-4702-96AF-97A714E72697}", "name": "MER*2 MK-82", "weight": 200}
    MER_2_MK_83 = {"clsid": "{18617C93-78E7-4359-A8CE-D754103EDF63}", "name": "MER*2 MK-83", "weight": 200}
    METEOR = {"clsid": "{RAFALE_MBDA_METEOR}", "name": "METEOR", "weight": 199}
    MICA_IR = {"clsid": "{0DA03783-61E4-40B2-8FAE-6AEE0A5C5AAE}", "name": "MICA IR", "weight": 110}
    MICA_NG = {"clsid": "{RAFALE_MICA_NG}", "name": "MICA_NG", "weight": 199}
    mk_84 = {"clsid": "{mk_84}", "name": "mk_84", "weight": 1000}
    R_550_Magic_2 = {"clsid": "{FC23864E-3B80-48E3-9C03-4DA8B1D7497B}", "name": "R.550 Magic 2", "weight": 89}
    RAF_RPL711 = {"clsid": "{RAF_RPL711}", "name": "RAF_RPL711", "weight": 820}
    RAF_RPL751 = {"clsid": "{RAF_RPL751}", "name": "RAF_RPL751", "weight": 1450}
    Smokewinder___blue_smk = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E743}", "name": "Smokewinder - blue_smk", "weight": 200}
    Smokewinder___green = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E742}", "name": "Smokewinder - green", "weight": 200}
    Smokewinder___orange = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E746}", "name": "Smokewinder - orange", "weight": 200}
    Smokewinder___red_smk = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E741}", "name": "Smokewinder - red_smk", "weight": 200}
    Smokewinder___white = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E744}", "name": "Smokewinder - white", "weight": 200}
    Smokewinder___yellow = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E745}", "name": "Smokewinder - yellow", "weight": 200}
    Super_530D = {"clsid": "{FD21B13E-57F3-4C2A-9F78-C522D0B5BCE1}", "name": "Super 530D", "weight": 270}
    TALIOS_THALES = {"clsid": "{TALIOS_THALES}", "name": "TALIOS_THALES", "weight": 265}


inject_weapons(WeaponsRafale_M:)


class Rafale_M(PlaneType):
    id = "Rafale_M"
    flyable = True
    height = 5.2
    width = 10.86
    length = 14.36
    fuel_max = 3165
    max_speed = 2376
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Liveries:

        class USSR(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Georgia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Venezuela(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Australia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Israel(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Combined_Joint_Task_Forces_Blue(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Sudan(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Norway(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Romania(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Iran(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Ukraine(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Libya(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Belgium(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Slovakia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Greece(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class UK(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Third_Reich(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Hungary(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Abkhazia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Morocco(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class United_Nations_Peacekeepers(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Switzerland(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class SouthOssetia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Vietnam(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class China(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Yemen(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Kuwait(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Serbia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Oman(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class India(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Egypt(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class TheNetherlands(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Poland(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Syria(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Finland(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Kazakhstan(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Denmark(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Sweden(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Croatia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class CzechRepublic(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class GDR(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Yugoslavia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Bulgaria(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class SouthKorea(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Tunisia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Combined_Joint_Task_Forces_Red(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Lebanon(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Portugal(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Cuba(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Insurgents(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class SaudiArabia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class France(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class USA(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Honduras(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Qatar(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Russia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class United_Arab_Emirates(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Italian_Social_Republi(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Austria(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Bahrain(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Italy(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Chile(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Turkey(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Philippines(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Algeria(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Pakistan(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Malaysia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Indonesia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Iraq(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Germany(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class South_Africa(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Jordan(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Mexico(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class USAFAggressors(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Brazil(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Spain(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Belarus(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Canada(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class NorthKorea(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Ethiopia(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Japan(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

        class Thailand(Enum):
            _01_marine_mat_17f = "01 marine mat 17f"
            _02_marine_12_f = "02 marine 12 f"
            _03_black_derive_11f = "03 black derive 11f"
            _04_11f_tiger_meet = "04 11f tiger meet"
            _05_brazil = "05 brazil"
            _07_marine_tiger_2014 = "07 marine tiger 2014"
            _08_flottile_12_f_90_ans = "08 flottile 12-f.90 ans"
            _09_rafale_export = "09 rafale export"
            _10_india_air_force = "10 india air force"
            _11_11f_tiger_meet_2017 = "11 11f tiger meet 2017"

    class Pylon1:
        Smokewinder___red_smk = (1, Weapons.Smokewinder___red_smk)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue_smk = (1, Weapons.Smokewinder___blue_smk)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        R_550_Magic_2 = (1, Weapons.R_550_Magic_2)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        MICA_IR = (1, Weapons.MICA_IR)

    class Pylon2:
        mk_84 = (2, Weapons.mk_84)
        MER_2_MK_83 = (2, Weapons.MER_2_MK_83)
        MER_2_MK_82 = (2, Weapons.MER_2_MK_82)
        _3_Mk_82 = (2, Weapons._3_Mk_82)
        LAU_131___7_2_75__rockets_M151__HE_ = (2, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU3_HE151 = (2, Weapons.LAU3_HE151)
        LAU3_WP156 = (2, Weapons.LAU3_WP156)
        LAU3_HE5 = (2, Weapons.LAU3_HE5)
        R_550_Magic_2 = (2, Weapons.R_550_Magic_2)
        AIM_7M = (2, Weapons.AIM_7M)
        AIM_120B = (2, Weapons.AIM_120B)
        AIM_120C = (2, Weapons.AIM_120C)
        LAU_115_2_LAU_127_AIM_120C = (2, Weapons.LAU_115_2_LAU_127_AIM_120C)
        Super_530D = (2, Weapons.Super_530D)
        METEOR = (2, Weapons.METEOR)
        AASM_250 = (2, Weapons.AASM_250)
        AASMx3L = (2, Weapons.AASMx3L)
        MICA_NG = (2, Weapons.MICA_NG)

    class Pylon3:
        mk_84 = (3, Weapons.mk_84)
        MER_2_MK_83 = (3, Weapons.MER_2_MK_83)
        MER_2_MK_82 = (3, Weapons.MER_2_MK_82)
        _3_Mk_82 = (3, Weapons._3_Mk_82)
        LAU3_HE151 = (3, Weapons.LAU3_HE151)
        LAU3_WP156 = (3, Weapons.LAU3_WP156)
        LAU_131x3_HYDRA_70_M151 = (3, Weapons.LAU_131x3_HYDRA_70_M151)
        R_550_Magic_2 = (3, Weapons.R_550_Magic_2)
        AIM_7M = (3, Weapons.AIM_7M)
        AIM_120B = (3, Weapons.AIM_120B)
        AIM_120C = (3, Weapons.AIM_120C)
        Super_530D = (3, Weapons.Super_530D)
        RAF_RPL711 = (3, Weapons.RAF_RPL711)
        RAF_RPL751 = (3, Weapons.RAF_RPL751)
        METEOR = (3, Weapons.METEOR)
        MICA_NG = (3, Weapons.MICA_NG)

    class Pylon4:
        R_550_Magic_2 = (4, Weapons.R_550_Magic_2)
        AIM_9M_Sidewinder_IR_AAM = (4, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (4, Weapons.AIM_9P_Sidewinder_IR_AAM)
        LAU3_WP156 = (4, Weapons.LAU3_WP156)
        LAU_10___4_ZUNI_MK_71 = (4, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        MICA_IR = (4, Weapons.MICA_IR)
        MICA_NG = (4, Weapons.MICA_NG)

    class Pylon5:
        mk_84 = (5, Weapons.mk_84)
        RAF_RPL711 = (5, Weapons.RAF_RPL711)
        RAF_RPL751 = (5, Weapons.RAF_RPL751)
        R_550_Magic_2 = (5, Weapons.R_550_Magic_2)
        AIM_7M = (5, Weapons.AIM_7M)
        AIM_120B = (5, Weapons.AIM_120B)
        AIM_120C = (5, Weapons.AIM_120C)
        Super_530D = (5, Weapons.Super_530D)
        METEOR = (5, Weapons.METEOR)
        MICA_NG = (5, Weapons.MICA_NG)

    class Pylon6:
        R_550_Magic_2 = (6, Weapons.R_550_Magic_2)
        AIM_9M_Sidewinder_IR_AAM = (6, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (6, Weapons.AIM_9P_Sidewinder_IR_AAM)
        LAU3_WP156 = (6, Weapons.LAU3_WP156)
        LAU_10___4_ZUNI_MK_71 = (6, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61___19_2_75__rockets_MK151_HE = (6, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        MICA_IR = (6, Weapons.MICA_IR)
        MICA_NG = (6, Weapons.MICA_NG)

    class Pylon7:
        AN_AAQ_28_LITENING = (7, Weapons.AN_AAQ_28_LITENING)
        TALIOS_THALES = (7, Weapons.TALIOS_THALES)

    class Pylon8:
        mk_84 = (8, Weapons.mk_84)
        MER_2_MK_83 = (8, Weapons.MER_2_MK_83)
        MER_2_MK_82 = (8, Weapons.MER_2_MK_82)
        _3_Mk_82 = (8, Weapons._3_Mk_82)
        LAU3_HE151 = (8, Weapons.LAU3_HE151)
        LAU3_WP156 = (8, Weapons.LAU3_WP156)
        LAU_131x3_HYDRA_70_M151 = (8, Weapons.LAU_131x3_HYDRA_70_M151)
        R_550_Magic_2 = (8, Weapons.R_550_Magic_2)
        AIM_7M = (8, Weapons.AIM_7M)
        AIM_120B = (8, Weapons.AIM_120B)
        AIM_120C = (8, Weapons.AIM_120C)
        Super_530D = (8, Weapons.Super_530D)
        RAF_RPL711 = (8, Weapons.RAF_RPL711)
        RAF_RPL751 = (8, Weapons.RAF_RPL751)
        METEOR = (8, Weapons.METEOR)
        MICA_NG = (8, Weapons.MICA_NG)

    class Pylon9:
        METEOR = (9, Weapons.METEOR)
        MICA_NG = (9, Weapons.MICA_NG)
        mk_84 = (9, Weapons.mk_84)
        MER_2_MK_83 = (9, Weapons.MER_2_MK_83)
        MER_2_MK_82 = (9, Weapons.MER_2_MK_82)
        _3_Mk_82 = (9, Weapons._3_Mk_82)
        LAU_131___7_2_75__rockets_M151__HE_ = (9, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU3_HE151 = (9, Weapons.LAU3_HE151)
        LAU3_WP156 = (9, Weapons.LAU3_WP156)
        LAU3_HE5 = (9, Weapons.LAU3_HE5)
        R_550_Magic_2 = (9, Weapons.R_550_Magic_2)
        AIM_7M = (9, Weapons.AIM_7M)
        AIM_120B = (9, Weapons.AIM_120B)
        AIM_120C = (9, Weapons.AIM_120C)
        LAU_115_2_LAU_127_AIM_120C = (9, Weapons.LAU_115_2_LAU_127_AIM_120C)
        Super_530D = (9, Weapons.Super_530D)
        AASM_250_RIGHT = (9, Weapons.AASM_250_RIGHT)
        AASMx3R = (9, Weapons.AASMx3R)

    class Pylon10:
        MICA_IR = (10, Weapons.MICA_IR)
        R_550_Magic_2 = (10, Weapons.R_550_Magic_2)
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red_smk = (10, Weapons.Smokewinder___red_smk)
        Smokewinder___green = (10, Weapons.Smokewinder___green)
        Smokewinder___blue_smk = (10, Weapons.Smokewinder___blue_smk)
        Smokewinder___white = (10, Weapons.Smokewinder___white)
        Smokewinder___yellow = (10, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (10, Weapons.Smokewinder___orange)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike, task.Reconnaissance, task.Intercept]
    task_default = task.CAP


