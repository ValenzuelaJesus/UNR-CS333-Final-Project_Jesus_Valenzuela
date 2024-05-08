'''
CS 333.1001 Testing and DevOps
Instructor: Erin Keith
Final Project
lists of armor, enemies, and weapons for the player to select
'''
from Weapon import Weapon
from Armor import Armor
from EnemyPart import EnemyPart
from Enemy import Enemy
from Backpack import Backpack
from Player import Player

#Primary Weapon Instantiation
breaker_sg225 = Weapon("Breaker (SG-225)", "Primary", "Shotgun", 330, 13, 7, 104, 300, 1650, 4290, 34320, 3)
dominator_jar5 = Weapon("Dominator (JAR-5)", "Primary", "Explosive", 275, 15, 6, 105, 250, 1146, 4125, 28875, 6)
scorcher_plas1 = Weapon("Scorcher (PLAS-1)", "Primary", "Energy-Based", 200, 15, 6, 105, 250, 833, 3000, 21000, 6)
sickle_las16 = Weapon("Sickle (LAS-16)", "Primary", "Energy-Based", 55, float('inf'), 3, float('inf'), 750, 688, float('inf'), float('inf'), 3)
breaker_incendiary_sg225ie = Weapon("Breaker Incendiary (SG-225IE)", "Primary", "Shotgun", 240, 25, 6, 175, 300, 1200, 6000, 42000, 3)
defender_smg37 = Weapon("Defender (SMG-37)", "Primary", "Submachine Gun", 70, 45, 8, 405, 520, 607, 3150, 28350, 3)
diligence_r63 = Weapon("Diligence (R-63)", "Primary", "Marksman Rifle", 125, 20, 8, 180, 350, 729, 2500, 22500, 3)
liberator_ar23 = Weapon("Liberator (AR-23)", "Primary", "Assault Rifle", 60, 45, 8, 405, 640, 640, 2700, 24300, 3)
punisher_sg8 = Weapon("Punisher (SG-8)", "Primary", "Shotgun", 405, 16, float('inf'), 76, 80, 540, 6480, 30780, 3)
slugger_sg8s = Weapon("Slugger (SG-8S)", "Primary", "Shotgun", 250, 16, float('inf'), 76, 80, 333, 4000, 19000, 5)
diligence_counter_sniper_63cs = Weapon("Diligence Counter Sniper (63CS)", "Primary", "Marksman Rifle", 140, 15, 6, 105, 350, 817, 2100, 14700, 6)
adjudicator_br14 = Weapon("Adjudicator (BR-14)", "Primary", "Marksman Rifle", 80, 25, 8, 225, 550, 733, 2000, 18000, 6)
blitzer_arc12 = Weapon("Blitzer (ARC-12)", "Primary", "Shotgun", 250, float('inf'), float('inf'), float('inf'), 45, 188, float('inf'), float('inf'), 5)
punisher_plasma_sg8p = Weapon("Punisher Plasma (SG-8P)", "Primary", "Shotgun", 250, 8, 8, 72, 80, 333, 2000, 18000, 5)
breaker_spray_and_pray_sg225sp = Weapon("Breaker Spray&Pray (SG-225SP)", "Primary", "Shotgun", 192, 26, 7, 208, 330, 1056, 4992, 39936, 3)
knight_mp98 = Weapon("Knight (MP-98)", "Primary", "Submachine Gun", 50, 50, 7, 400, 1380, 1150, 2500, 20000, 3)
liberator_penetrator_ar23p = Weapon("Liberator Penetrator (AR-23P)", "Primary", "Assault Rifle", 45, 30, 10, 330, 640, 480, 1350, 14850, 6)
eruptor_r36 = Weapon("Eruptor (R-36)", "Primary", "Explosive", 420, 5, 6, 35, 25, 175, 2100, 14700, 6)
scythe_las5 = Weapon("Scythe (LAS-5)", "Primary", "Energy-Based", 3.5, float('inf'), 4, float('inf'), 6000, 350, float('inf'), float('inf'), 3)
exploding_crossbow_cb9 = Weapon("Exploding Crossbow (CB-9)", "Primary", "Explosive", 420, 5, 8, 45, 50, 350, 2100, 18900, 3)
liberator_concussive_ar23c = Weapon("Liberator Concussive (AR-23C)", "Primary", "Assault Rifle", 65, 30, 10, 330, 320, 347, 1950, 21450, 3)
#Secondary Weapon Instantiation
redeemer_p19 = Weapon("Redeemer (P-19)", "Secondary", "Submachine Gun", 60, 31, 5, 186, 1100, 1100, 1860, 11160, 3)
grenade_pistol_gp31 = Weapon("Grenade Pistol (GP-31)", "Secondary", "Pistol", 600, 1, 8, 9, 20, 200, 600, 5400, 6)
senator_p4 = Weapon("Senator (P-4)", "Secondary", "Revolver", 175, 6, 12, 46, 200, 583, 1050, 8050, 6)
peacemaker_p2 = Weapon("Peacemaker (P-2)", "Secondary", "Pistol", 75, 15, 7, 120, 900, 1125, 1125, 9000, 3)
dagger_las7 = Weapon("Dagger (Las-7)", "Secondary", "Laser Pistol", 2, float('inf'), 3, float('inf'), 6000, 200, float('inf'), float('inf'), 3)
#Grenade Instantiation
g6_frag = Weapon("G-6 Frag", "Grenade", "Standard Grenades", 250, 4, 0, 4, 0, 250, 0, 1000, 3)
g12_high_explosive = Weapon("G-12 High Explosive", "Grenade", "Standard Grenades", 400, 4, 0, 4, 0, 400, 0, 1600, 4)
g10_incendiary = Weapon("G-10 Incendiary", "Grenade", "Standard Grenades", 150, 4, 0, 4, 0, 150, 0, 600, 3)
g16_impact = Weapon("G-16 Impact", "Grenade", "Special Grenade", 400, 4, 0, 4, 0, 400, 0, 1600, 4)
g23_stun = Weapon("G-23 Stun", "Grenade", "Special Grenade", 0, 4, 0, 4, 0, 0, 0, 0, 6)
g3_smoke = Weapon("G-3 Smoke", "Grenade", "Special Grenade", 0, 4, 0, 4, 0, 0, 0, 0, 0)
g123_thermite = Weapon("G-123 Thermite", "Grenade", "Special Grenade", 100, 4, 0, 4, 0, 100, 0, 400, 7)
#Strategem Instantiation
quasar_cannon_las99 = Weapon("Quasar Cannon (LAS-99)", "Strategem", "Launcher", 1000, 1, 0, float('inf'), 4, 100, 1000, float('inf'), 9)
expendable_anti_tank_eat = Weapon("Expendable Anti-Tank (EAT)", "Strategem", "Launcher", 1000, 1, 0, 1, 1, 1000, 1000, 1000, 9)
autocannon_ac8 = Weapon("Autocannon (AC-8)", "Strategem", "Shoulder Cannon", 250, 10, 20, 200, 60, 250, 2500, 50000, 6)
recoilless_rifle_gr8 = Weapon("Recoilless Rifle (GR-8)", "Strategem", "Launcher", 1000, 1, 5, 6, 6, 166.67, 1000, 6000, 9)
grenade_launcher_gl21 = Weapon("Grenade Launcher (GL-21)", "Strategem", "Grenade Launcher", 250, 6, 5, 30, 60, 250, 1250, 7500, 4)
railgun_rs422 = Weapon("Railgun (RS-422)", "Strategem", "Rifle", 400, 1, 20, 20, 20, 400, 400, 800, 5)
anti_materiel_rifle_apw1 = Weapon("Anti-Materiel Rifle (APW-1)", "Strategem", "Rifle", 350, 7, 6, 42, 100, 600, 2100, 14700, 4)
flamethrower_flam40 = Weapon("Flamethrower (FLAM-40)", "Strategem", "Flamethrower", 50, 100, 2, 200, 1000, 250, 5000, 10000, 9)
laser_cannon_las98 = Weapon("Laser Cannon (LAS-98)", "Strategem", "Heavy Machine Gun", 100, float('inf'), 1, float('inf'), 60, 600, float('inf'), float('inf'), 5)
arc_thrower_arc3 = Weapon("Arc Thrower (ARC-3)", "Strategem", "Energy", 330, float('inf'), float('inf'), float('inf'), 20, 30, float('inf'), float('inf'), 6)
machine_gun_mg43 = Weapon("Machine Gun (MG-43)", "Strategem", "Heavy Machine Gun", 65, 200, 2, 400, 600, 65, 13000, 26000, 5)
stalwart_m105 = Weapon("Stalwart (M-105)", "Strategem", "Heavy Machine Gun", 65, 150, 3, 450, 600, 65, 13000, 29250, 3)
airburst_rocket_launcher_rl77 = Weapon("Airburst Rocket Launcher (RL-77)", "Strategem", "Launcher", 500, 1, 8, 8, 6, 88.87, 500, 3000, 3)
spear_faf14 = Weapon("Spear (FAF-14)", "Strategem", "Launcher", 1000, 1, 5, 6, 6, 166.67, 1000, 6000, 9)
heavy_mg_mg206 = Weapon("Heavy MG (MG-206)", "Strategem", "Heavy Machine Gun", 150, 75, 2, 150, 450, 65, 13000, 29250, 3)
#Armor Instantiation
b08_light_gunner_armor = Armor("B-08 Light Gunner Armor", "light", 100, 550, 125, "Extra Padding")
ce07_demolition_specialist_armor = Armor("CE-07 Demolition Specialist Armor", "medium", 64, 536, 118, "Engineering Kit")
ce67_titan_armor = Armor("CE-67 Titan Armor", "heavy", 79, 521, 111, "Engineering Kit")
ce74_breaker_armor = Armor("CE-74 Breaker Armor", "medium", 50, 550, 125, "Engineering Kit")
cm21_trench_paramedic_armor = Armor("CM-21 Trench Paramedic Armor", "medium", 64, 536, 118, "Med-Kit")
ex00_prototype_x_armor = Armor("EX-00 Prototype X Armor", "light", 50, 550, 125, "Electrical Conduit")
fs37_ravager_armor = Armor("FS-37 Ravager Armor", "light", 50, 550, 125, "Fortified")
fs38_eradicator_armor = Armor("FS-38 Eradicator Armor", "light", 50, 550, 125, "Fortified")
sc30_trailblazer_scout_armor = Armor("SC-30 Trailblazer Scout Armor", "light", 50, 550, 125, "Scout")
sc34_infiltrator_armor = Armor("SC-34 Infiltrator Armor", "medium", 70, 530, 115, "Scout")
sc37_legionnaire_armor = Armor("SC-37 Legionnaire Armor", "light", 50, 550, 125, "Servo-Assisted")
b01_tactical_armor = Armor("B-01 Tactical Armor", "heavy", 150, 500, 100, "Extra Padding")
b24_enforcer_armor = Armor("B-24 Enforcer Armor", "heavy", 129, 471, 71, "Fortified")
ce27_ground_breaker_armor = Armor("CE-27 Ground Breaker Armor", "heavy", 100, 500, 100, "Engineering Kit")
ce35_trench_engineer_armor = Armor("CE-35 Trench Engineer Armor", "heavy", 100, 500, 100, "Engineering Kit")
ce81_juggernaut_armor = Armor("CE-81 Juggernaut Armor", "heavy", 100, 500, 100, "Engineering Kit")
cm06_combat_medic = Armor("CM-06 Combat Medic", "medium", 100, 500, 100, "Med-Kit")
cm09_bonesnapper_armor = Armor("CM-09 Bonesnapper Armor", "medium", 100, 500, 100, "Med-Kit")
cm10_clinician_armor = Armor("CM-10 Clinician Armor", "medium", 100, 500, 100, "Engineering Kit")
cm14_physician_armor = Armor("CM-14 Physician Armor", "medium", 100, 500, 100, "Med-Kit")
dp11_champion_of_the_people_armor = Armor("DP-11 Champion of the People Armor", "medium", 100, 500, 100, "Democracy Protects")
dp40_hero_of_the_federation_armor = Armor("DP-40 Hero of the Federation Armor", "medium", 100, 500, 100, "Democracy Protects")
dp53_savior_of_the_free_armor = Armor("DP-53 Savior of the Free Armor", "medium", 100, 500, 100, "Democracy Protects")
ex03_prototype_3_armor = Armor("EX-03 Prototype 3 Armor", "medium", 100, 500, 100, "Electrical Conduit")
ex16_prototype_16_armor = Armor("EX-16 Prototype 16 Armor", "medium", 100, 500, 100, "Electrical Conduit")
fs34_exterminator_armor = Armor("FS-34 Exterminator Armor", "medium", 100, 500, 100, "Fortified")
sa04_combat_technician_armor = Armor("SA-04 Combat Technician Armor", "medium", 100, 500, 100, "Scout")
sa12_servo_assisted_armor = Armor("SA-12 Servo Assisted Armor", "medium", 100, 500, 100, "Servo-Assisted")
sa25_steel_trooper_armor = Armor("SA-25 Steel Trooper Armor", "medium", 100, 500, 100, "Servo-Assisted")
sc15_drone_master_armor = Armor("SC-15 Drone Master Armor", "medium", 100, 500, 100, "Engineering Kit")
tr7_ambassador_of_the_brand_armor = Armor("TR-7 Ambassador of the Brand Armor", "heavy", 150, 500, 100, "Extra Padding")
tr9_cavalier_of_democracy_armor = Armor("TR-9 Cavalier of Democracy Armor", "medium", 100, 500, 100, "Democracy Protects")
tr40_gold_eagle_armor = Armor("TR-40 Gold Eagle Armor", "heavy", 150, 500, 100, "Extra Padding")
tr117_alpha_commander_armor = Armor("TR-117 Alpha Commander Armor", "medium", 100, 500, 100, "Med-Kit")
b27_fortified_commando_armor = Armor("B-27 Fortified Commando Armor", "heavy", 200, 450, 50, "Extra Padding")
cm17_butcher_armor = Armor("CM-17 Butcher Armor", "medium", 150, 450, 50, "Med-Kit")
cw36_winter_warrior_armor = Armor("CW-36 Winter Warrior Armor", "heavy", 200, 450, 50, "Extra Padding")
fs05_marksman_armor = Armor("FS-05 Marksman Armor", "medium", 150, 450, 50, "Fortified")
fs11_executioner_armor = Armor("FS-11 Executioner Armor", "medium", 150, 450, 50, "Fortified")
fs23_battle_master_armor = Armor("FS-23 Battle Master Armor", "medium", 150, 450, 50, "Fortified")
fs55_devastator_armor = Armor("FS-55 Devastator Armor", "medium", 150, 450, 50, "Fortified")
fs61_dreadnought_armor = Armor("FS-61 Dreadnought Armor", "medium", 150, 450, 50, "Servo-Assisted")
sa32_dynamo_armor = Armor("SA-32 Dynamo Armor", "medium", 150, 450, 50, "Servo-Assisted")
tr62_knight_armor = Armor("TR-62 Knight Armor", "heavy", 150, 450, 50, "Servo-Assisted")
# Instantiate Enemy Parts
scavenger_body = EnemyPart("body", 3, 1, 50, True)
spitter_body = EnemyPart("body", 3, 1, 50, True)
pouncers_body = EnemyPart("body", 3, 1, 50, True)
hunters_body = EnemyPart("body", 3, 1, 100, True)
warriors_head = EnemyPart("head", 3, 2, 100, True)
warriors_body = EnemyPart("body", 3, 1, 150, True)
brood_commanders_head = EnemyPart("head", 3, 2, 100, True)
brood_commanders_body = EnemyPart("body", 3, 1, 250, True)
chargers_head = EnemyPart("head", 9, 2, 100, True)
chargers_body = EnemyPart("body", 7, 1, 1000, True)
chargers_leg = EnemyPart("leg", 7, 2, 500, True)
# Istantiate Enemies
scavenger = Enemy("Scavenger", "Termind", "Light", 50, [scavenger_body])
spitter = Enemy("Spitter", "Termind", "Light", 50, [spitter_body])
pouncers = Enemy("Pouncers", "Termind", "Light", 50, [pouncers_body])
hunters = Enemy("Hunters", "Termind", "Light", 100, [hunters_body])
warriors = Enemy("Warriors", "Termind", "Light", 150, [warriors_head, warriors_body])
brood_commanders = Enemy("Brood Commanders", "Termind", "Medium", 250, [brood_commanders_head, brood_commanders_body])
chargers = Enemy("Chargers", "Termind", "Heavy", 1000, [chargers_head, chargers_body, chargers_leg])
# List of primary weapons
primary_weapons = [
breaker_sg225, dominator_jar5, scorcher_plas1, sickle_las16,
breaker_incendiary_sg225ie, defender_smg37, diligence_r63, liberator_ar23,
punisher_sg8, slugger_sg8s, diligence_counter_sniper_63cs, adjudicator_br14,blitzer_arc12, punisher_plasma_sg8p, breaker_spray_and_pray_sg225sp, knight_mp98,
liberator_penetrator_ar23p, eruptor_r36, scythe_las5, exploding_crossbow_cb9,liberator_concussive_ar23c
    ]

# List of secondary weapons
secondary_weapons = [
    redeemer_p19, grenade_pistol_gp31, senator_p4, peacemaker_p2, dagger_las7
]

# List of grenades
grenades = [
    g6_frag, g12_high_explosive, g10_incendiary, g16_impact, g23_stun, g3_smoke, g123_thermite
]

# List of strategem weapons
strategem_weapons = [
    quasar_cannon_las99, expendable_anti_tank_eat, autocannon_ac8, recoilless_rifle_gr8,
    grenade_launcher_gl21, railgun_rs422, anti_materiel_rifle_apw1, flamethrower_flam40,
    laser_cannon_las98, arc_thrower_arc3, machine_gun_mg43, stalwart_m105,
    airburst_rocket_launcher_rl77, spear_faf14, heavy_mg_mg206
]

# List of armors
armors = [
    b08_light_gunner_armor, ce07_demolition_specialist_armor, ce67_titan_armor, ce74_breaker_armor,
    cm21_trench_paramedic_armor, ex00_prototype_x_armor, fs37_ravager_armor, fs38_eradicator_armor,
    sc30_trailblazer_scout_armor, sc34_infiltrator_armor, sc37_legionnaire_armor, b01_tactical_armor,
    b24_enforcer_armor, ce27_ground_breaker_armor, ce35_trench_engineer_armor, ce81_juggernaut_armor,
    cm06_combat_medic, cm09_bonesnapper_armor, cm10_clinician_armor, cm14_physician_armor,
    dp11_champion_of_the_people_armor, dp40_hero_of_the_federation_armor, dp53_savior_of_the_free_armor,
    ex03_prototype_3_armor, ex16_prototype_16_armor, fs34_exterminator_armor, sa04_combat_technician_armor,
    sa12_servo_assisted_armor, sa25_steel_trooper_armor, sc15_drone_master_armor, tr7_ambassador_of_the_brand_armor,
    tr9_cavalier_of_democracy_armor, tr40_gold_eagle_armor, tr117_alpha_commander_armor, b27_fortified_commando_armor,
    cm17_butcher_armor, cw36_winter_warrior_armor, fs05_marksman_armor, fs11_executioner_armor,
    fs23_battle_master_armor, fs55_devastator_armor, fs61_dreadnought_armor, sa32_dynamo_armor, tr62_knight_armor
]

# List of enemies
enemies = [
    scavenger, spitter, pouncers, hunters, warriors, brood_commanders, chargers
]