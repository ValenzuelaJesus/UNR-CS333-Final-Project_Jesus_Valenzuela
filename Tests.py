'''
CS 333.1001 Testing and DevOps
Instructor: Erin Keith
Final Project
tests.py: Unit tests on the classes
'''
import unittest
from Weapon import Weapon
from Armor import Armor
from EnemyPart import EnemyPart
from Enemy import Enemy
from Backpack import Backpack
from Player import Player

class Tests(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon("Liberator(AR-23)", "primary", "rifle", 60, 45, 8, 405, 640, 640, 2700, 24300, 3)
        self.rifle = Weapon("Liberator(AR-23)","primary","rifle",60,45,8,405,640,640,2700,24300,3)
        self.energy_weapon = Weapon("Sickle (LAS-16)", "primary", "energy rifle",55,'inf',3,'inf',750,688,'inf','inf',3)
        self.extrapadding = Armor("B-01 Tactical Armor", "medium", 150, 500, 100, "Extra Padding")
        self.legor = Armor("SC-30 Trailblazer Scout Armor", "light", 50,550,125,"Scout")
        self.enemy_part = EnemyPart("Arm", 10, 1.5, 50, False)
        self.head = EnemyPart("Head", 5, 2.0, 50, True)
        self.leg = EnemyPart("leg", 3, 1.5, 30, False)
        self.enemy = Enemy("Charger", "Terminids", "Medium", 100, [self.head, self.leg])
        self.backpack = Backpack("Jet Pack", "A jet pack with a short cooldown that allows players to jump. Also negates fall damage.", False)
        self.primary = Weapon("Breaker (SG-225)", "Primary", "Shotgun", 330, 13, 7, 104, 300, 1650, 4290, 34320, 3)
        self.secondary = Weapon("Peacemaker (P-2)", "Secondary", "Pistol", 75, 15, 7, 120, 900, 1125, 1125, 9000, 3)
        self.strategem = Weapon("Recoilless Rifle (GR-8)", "Strategem", "Launcher", 5000, 1, 5, 6, 10, 150, 5000, 3000, 9)
        self.grenades = Weapon ("G-16 Impact", "Grenade", "Special Grenade", 400, 4, 0,0,0,400,1600,1600,4)
        self.backpack_2 = Backpack("GR-8 Pack", "A pack carrying 5 additional rockets to reload", True)
        self.armor = Armor("B-27 Fortified Commando Armor", "Heavy", 200, 450, 50, "Extra Padding")
        self.player = Player(self.primary, self.secondary, self.strategem, self.grenades, self.backpack_2, self.armor)



    def test_weapon_constructor(self):
        self.assertEqual(self.rifle.get_name(), "Liberator(AR-23)")
        self.assertEqual(self.rifle.get_category(), "primary")
        self.assertEqual(self.rifle.get_subcategory(), "rifle")
        self.assertEqual(self.rifle.get_damage(), 60)
        self.assertEqual(self.rifle.get_capacity(), 45)
        self.assertEqual(self.rifle.get_mags(), 8)
        self.assertEqual(self.rifle.get_total_rounds(), 405)
        self.assertEqual(self.rifle.get_fire_rate(), 640)
        self.assertEqual(self.rifle.get_dps(), 640)
        self.assertEqual(self.rifle.get_dmg_per_mag(), 2700)
        self.assertEqual(self.rifle.get_dmg_total(), 24300)
        self.assertEqual(self.rifle.get_armor_penetration(), 3)
    
    def test_energy_weapon(self):
        self.assertEqual(self.energy_weapon.get_name(), "Sickle (LAS-16)")
        self.assertEqual(self.energy_weapon.get_category(), "primary")
        self.assertEqual(self.energy_weapon.get_subcategory(), "energy rifle")
        self.assertEqual(self.energy_weapon.get_damage(), 55)
        self.assertEqual(self.energy_weapon.get_capacity(), float('inf'))
        self.assertEqual(self.energy_weapon.get_mags(), 3)
        self.assertEqual(self.energy_weapon.get_total_rounds(), float('inf'))
        self.assertEqual(self.energy_weapon.get_fire_rate(), 750)
        self.assertEqual(self.energy_weapon.get_dmg_per_mag(), float('inf'))
        self.assertEqual(self.energy_weapon.get_dmg_total(), float('inf'))
        self.assertEqual(self.energy_weapon.get_armor_penetration(),3)
    
    # Tests for weapon getters
    def test_weapon_get_name(self):
        self.assertEqual(self.weapon.get_name(), "Liberator(AR-23)")

    def test_weapon_get_category(self):
        self.assertEqual(self.weapon.get_category(), "primary")

    def test_weapon_get_subcategory(self):
        self.assertEqual(self.weapon.get_subcategory(), "rifle")

    def test_weapon_get_damage(self):
        self.assertEqual(self.weapon.get_damage(), 60)

    def test_weapon_get_capacity(self):
        self.assertEqual(self.weapon.get_capacity(), 45)

    def test_weapon_get_mags(self):
        self.assertEqual(self.weapon.get_mags(), 8)

    def test_weapon_get_total_rounds(self):
        self.assertEqual(self.weapon.get_total_rounds(), 405)

    def test_weapon_get_fire_rate(self):
        self.assertEqual(self.weapon.get_fire_rate(), 640)

    def test_weapon_get_dps(self):
        self.assertEqual(self.weapon.get_dps(), 640)

    def test_weapon_get_dmg_per_mag(self):
        self.assertEqual(self.weapon.get_dmg_per_mag(), 2700)

    def test_weapon_get_dmg_total(self):
        self.assertEqual(self.weapon.get_dmg_total(), 24300)

    def test_weapon_get_armor_penetration(self):
        self.assertEqual(self.weapon.get_armor_penetration(), 3)

    # Tests for setters
    def test_weapon_set_name(self):
        self.weapon.set_name("Sniper")
        self.assertEqual(self.weapon.get_name(), "Sniper")

    def test_weapon_set_category(self):
        self.weapon.set_category("Secondary")
        self.assertEqual(self.weapon.get_category(), "Secondary")

    def test_weapon_set_subcategory(self):
        self.weapon.set_subcategory("Marksman")
        self.assertEqual(self.weapon.get_subcategory(), "Marksman")

    def test_weapon_set_damage(self):
        self.weapon.set_damage(50)
        self.assertEqual(self.weapon.get_damage(), 50)

    def test_weapon_set_capacity(self):
        self.weapon.set_capacity(80)
        self.assertEqual(self.weapon.get_capacity(), 80)

    def test_weapon_set_mags(self):
        self.weapon.set_mags(4)
        self.assertEqual(self.weapon.get_mags(), 4)

    def test_weapon_set_total_rounds(self):
        self.weapon.set_total_rounds(320)
        self.assertEqual(self.weapon.get_total_rounds(), 320)

    def test_weapon_set_fire_rate(self):
        self.weapon.set_fire_rate(500)
        self.assertEqual(self.weapon.get_fire_rate(), 500)

    def test_weapon_set_dps(self):
        self.weapon.set_dps(250)
        self.assertEqual(self.weapon.get_dps(), 250)

    def test_weapon_set_dmg_per_mag(self):
        self.weapon.set_dmg_per_mag(2000)
        self.assertEqual(self.weapon.get_dmg_per_mag(), 2000)

    def test_weapon_set_dmg_total(self):
        self.weapon.set_dmg_total(8000)
        self.assertEqual(self.weapon.get_dmg_total(), 8000)

    def test_weapon_set_armor_penetration(self):
        self.weapon.set_armor_penetration(4)
        self.assertEqual(self.weapon.get_armor_penetration(), 4)

    #Tests for Armor Class
    def test_armor_constructor(self):
        self.assertEqual(self.legor.get_name(), "SC-30 Trailblazer Scout Armor")
        self.assertEqual(self.legor.get_armor_class(), "light")
        self.assertEqual(self.legor.get_armor_rating(), 50) 
        self.assertEqual(self.legor.get_speed(), 550)
        self.assertEqual(self.legor.get_stamina_regen(), 125)
        self.assertEqual(self.legor.get_passive(), "Scout")
    
    def test_armor_extrapadding(self):
        self.assertEqual(self.extrapadding.get_armor_rating(), 150+50)

    # Tests for getters
    def test_armor_get_name(self):
        self.assertEqual(self.legor.get_name(), "SC-30 Trailblazer Scout Armor")

    def test_armor_get_armor_class(self):
        self.assertEqual(self.legor.get_armor_class(), "light")

    def test_armor_get_armor_rating(self):
        self.assertEqual(self.legor.get_armor_rating(), 50)  

    def test_armor_get_speed(self):
        self.assertEqual(self.legor.get_speed(), 550)

    def test_armor_get_stamina_regen(self):
        self.assertEqual(self.legor.get_stamina_regen(), 125)

    def test_armor_get_passive(self):
        self.assertEqual(self.legor.get_passive(), "Scout")

    # Tests for setters
    def test_armor_set_name(self):
        self.legor.set_name("test")
        self.assertEqual(self.legor.get_name(), "test")

    def test_armor_set_armor_class(self):
        self.legor.set_armor_class("heavy")
        self.assertEqual(self.legor.get_armor_class(), "heavy")

    def test_armor_set_armor_rating(self):
        self.legor.set_armor_rating(69)
        self.assertEqual(self.legor.get_armor_rating(), 69)

    def test_armor_set_speed(self):
        self.legor.set_speed(100)
        self.assertEqual(self.legor.get_speed(), 100)

    def test_armor_set_stamina_regen(self):
        self.legor.set_stamina_regen(125)
        self.assertEqual(self.legor.get_stamina_regen(), 125)

    def test_armor_set_passive(self):
        self.legor.set_passive("Fortified")
        self.assertEqual(self.legor.get_passive(), "Fortified")

    def test_armor_get_passive_description(self):
        expected_descriptions = {
            "Fortified": "Further reduces recoil when crouching or prone by 30%. Provides 50% resistance to explosive damage.",
            "Servo-Assisted": "Increases throwing range by 30%. Provides +50% limb health.",
            "Engineering Kit": "Further reduces recoil when crouching or prone by 30%. Increases initial inventory and holding capacity of grenades by +2.",
            "Med-Kit": "Increases initial inventory and holding capacity of stims by +2. Increases stim effect duration by 2.0s.",
            "Electrical Conduit": "Provides 95% resistance to arc damage.",
            "Scout": "Markers placed on the map will generate radar scans every 2.0s. Reduces range at which enemies can detect the wearer by 30%.",
            "Democracy Protects": "50% chance to not die when taking lethal damage. Prevents all damage from bleeding if chest hemorrhages.",
            "Extra Padding": "Increases armor rating based on armor class."
        }

        for passive, expected_description in expected_descriptions.items():
            self.legor.set_passive(passive)
            self.assertEqual(self.legor.get_passive_description(), expected_description)

    def test_enemy_part_constructor(self):
        enemy_part = EnemyPart("Arm", 10, 1.5, 50, False)
        self.assertEqual(enemy_part.get_name(), "Arm")
        self.assertEqual(enemy_part.get_armor_value(), 10)
        self.assertEqual(enemy_part.get_damage_multiplier(), 1.5)
        self.assertEqual(enemy_part.get_health(), 50)
        self.assertFalse(enemy_part.get_owner_dies_on_destruction())

    # Tests for Enemy Part getters
    def test_enemy_part_get_name(self):
        self.assertEqual(self.enemy_part.get_name(), "Arm")

    def test_enemy_part_get_armor_value(self):
        self.assertEqual(self.enemy_part.get_armor_value(), 10)

    def test_enemy_part_get_damage_multiplier(self):
        self.assertEqual(self.enemy_part.get_damage_multiplier(), 1.5)

    def test_enemy_part_get_health(self):
        self.assertEqual(self.enemy_part.get_health(), 50)

    def test_enemy_part_get_owner_dies_on_destruction(self):
        self.assertFalse(self.enemy_part.get_owner_dies_on_destruction())

    # Tests for Enemy Part setters
    def test_enemy_part_set_name(self):
        self.enemy_part.set_name("Head")
        self.assertEqual(self.enemy_part.get_name(), "Head")

    def test_enemy_part_set_armor_value(self):
        self.enemy_part.set_armor_value(20)
        self.assertEqual(self.enemy_part.get_armor_value(), 20)

    def test_enemy_part_set_damage_multiplier(self):
        self.enemy_part.set_damage_multiplier(2.0)
        self.assertEqual(self.enemy_part.get_damage_multiplier(), 2.0)

    def test_enemy_part_set_health(self):
        self.enemy_part.set_health(100)
        self.assertEqual(self.enemy_part.get_health(), 100)
    
    def test_enemy_part_set_owner_dies_on_destruction(self):
        self.enemy_part.set_owner_dies_on_destruction(True)
        self.assertTrue(self.enemy_part.get_owner_dies_on_destruction())
    #Enemy Tests
    def test_enemy_enemy_constructor(self):
        self.assertEqual(self.enemy.get_name(), "Charger")
        self.assertEqual(self.enemy.get_faction(), "Terminids")
        self.assertEqual(self.enemy.get_classification(), "Medium")
        self.assertEqual(self.enemy.get_health(), 100)
        self.assertEqual(len(self.enemy.get_parts()), 2)

    def test_enemy_get_name(self):
        self.assertEqual(self.enemy.get_name(), "Charger")

    def test_enemy_get_faction(self):
        self.assertEqual(self.enemy.get_faction(), "Terminids")

    def test_enemy_get_classification(self):
        self.assertEqual(self.enemy.get_classification(), "Medium")

    def test_enemy_get_health(self):
        self.assertEqual(self.enemy.get_health(), 100)

    def test_enemy_get_parts(self):
        self.assertEqual(len(self.enemy.get_parts()), 2)
        self.assertIsInstance(self.enemy.get_parts()[0], EnemyPart)

    # Tests for setters
    def test_enemy_set_name(self):
        self.enemy.set_name("Scavenger")
        self.assertEqual(self.enemy.get_name(), "Scavenger")

    def test_enemy_set_faction(self):
        self.enemy.set_faction("Automaton")
        self.assertEqual(self.enemy.get_faction(), "Automaton")

    def test_enemy_set_classification(self):
        self.enemy.set_classification("Light")
        self.assertEqual(self.enemy.get_classification(), "Light")

    def test_enemy_set_health(self):
        self.enemy.set_health(80)
        self.assertEqual(self.enemy.get_health(), 80)

    def test_enemy_set_parts(self):
        new_parts = [self.leg]  # Setting only one part
        self.enemy.set_parts(new_parts)
        self.assertEqual(len(self.enemy.get_parts()), 1)
        self.assertEqual(self.enemy.get_parts(), new_parts)

    def test_enemy_enemy_check_part_destruction(self): #Integration Tests of Enemy and Enemy part classes
        # 2 cases to test 1 part is a critical part
        self.head.set_health(0)
        self.enemy.check_part_destruction()
        self.assertEqual(self.enemy.get_health(), 0)  # Enemy should be dead

        # Case 2 part is noncritical and enemy can survive loss of the part
        self.head.set_health(50)
        self.enemy.set_health(100)
        # print(self.enemy.get_health())
        # print(self.leg.get_health())
        self.leg.set_health(0)
        self.enemy.check_part_destruction()
        # print(self.enemy.get_health())
        self.assertEqual(self.enemy.get_health(), 100)  

        #Test Backpack 
    def test_backpack_constructor(self):
        backpack = Backpack("Test Pack", "Test Description", False)
        self.assertEqual(backpack.get_name(), "Test Pack")
        self.assertEqual(backpack.get_description(), "Test Description")
        self.assertFalse(backpack.has_ammo())

    def test_backpack_get_name(self):
        self.assertEqual(self.backpack.get_name(), "Jet Pack")

    def test_backpack_get_description(self):
        self.assertEqual(self.backpack.get_description(), "A jet pack with a short cooldown that allows players to jump. Also negates fall damage.")

    def test_backpack_has_ammo(self):
        self.assertFalse(self.backpack.has_ammo())

    def test_backpack_set_name(self):
        self.backpack.set_name("Laser Rover")
        self.assertEqual(self.backpack.get_name(), "Laser Rover")

    def test_backpack_set_description(self):
        new_description = "An rover that lasers Enemies"
        self.backpack.set_description(new_description)
        self.assertEqual(self.backpack.get_description(), new_description)

    def test_backpack_backpack_set_has_ammo(self):
        self.backpack.set_has_ammo(False)
        self.assertFalse(self.backpack.has_ammo())
    
    def test_player_constructor(self):
        primary_weapon = self.primary
        secondary_weapon = self.secondary
        strategem = self.strategem
        grenades = self.grenades
        backpack = self.backpack_2
        armor = self.armor

        player = Player(primary_weapon, secondary_weapon, strategem, grenades, backpack, armor)

        self.assertEqual(player.get_primary_weapon(), primary_weapon)
        self.assertEqual(player.get_secondary_weapon(), secondary_weapon)
        self.assertEqual(player.get_strategem(), strategem)
        self.assertEqual(player.get_grenades(), grenades)
        self.assertEqual(player.get_backpack(), backpack)
        self.assertEqual(player.get_armor(), armor)


    # Tests for getters
    def test_player_get_primary_weapon(self):
        self.assertEqual(self.player.get_primary_weapon(), self.primary)

    def test_player_get_secondary_weapon(self):
        self.assertEqual(self.player.get_secondary_weapon(), self.secondary)

    def test_player_get_strategem(self):
        self.assertEqual(self.player.get_strategem(), self.strategem)

    def test_player_get_grenades(self):
        self.assertEqual(self.player.get_grenades(), self.grenades)

    def test_player_get_backpack(self):
        self.assertEqual(self.player.get_backpack(), self.backpack_2)

    def test_player_get_armor(self):
        self.assertEqual(self.player.get_armor(), self.armor)

    # Tests for setters
    def test_player_set_primary_weapon(self):
        new_primary = Weapon("Test", "Primary", "Test", 80, 10, 2, 20, 800, 800, 1600, 3200, 5)
        self.player.set_primary_weapon(new_primary)
        self.assertEqual(self.player.get_primary_weapon(), new_primary)

    def test_player_set_secondary_weapon(self):
        new_secondary = Weapon("Test", "Secondary", "Test", 50, 8, 2, 16, 300, 400, 3200, 6400, 1)
        self.player.set_secondary_weapon(new_secondary)
        self.assertEqual(self.player.get_secondary_weapon(), new_secondary)

    def test_player_set_strategem(self):
        new_strategem = Weapon("Test", "Strategem", "Test", 50, 8, 2, 16, 300, 400, 3200, 6400, 1)
        self.player.set_strategem(new_strategem)
        self.assertEqual(self.player.get_strategem(), new_strategem)

    def test_player_set_grenades(self):
        new_grenades = 6
        self.player.set_grenades(new_grenades)
        self.assertEqual(self.player.get_grenades(), new_grenades)

    def test_player_set_backpack(self):
        new_backpack = Backpack("Test", "Test", False)
        self.player.set_backpack(new_backpack)
        self.assertEqual(self.player.get_backpack(), new_backpack)

    def test_player_set_armor(self):
        new_armor = Armor("Test", "Heavy", 300, 3, 8, "Fortified")
        self.player.set_armor(new_armor)
        self.assertEqual(self.player.get_armor(), new_armor)

    def test_check_armor_passive_without_engineering_kit(self): #Integration Test between player gernades and armor passive
        # Check if the grenade capacity remains unchanged without the Engineering Kit passive
        initial_capacity =self.player.get_grenades().get_capacity()
        self.player.get_armor().set_passive("Engineering Kit")
        self.player.check_armor_passive()
        new_capacity = self.player.get_grenades().get_capacity()
        self.assertEqual(new_capacity, initial_capacity+2)

    def test_weapon_damage_on_enemy(self): #Integration Test between player and enemy
        self.player_weapon = Weapon("Test", "Primary", "Test", 30, 100, 5, 500, 600, 300, 1500, 7500, 3)
        self.player = Player(self.player_weapon, self.secondary, self.strategem, self.grenades, self.backpack, self.armor)
        self.enemy_part = EnemyPart("Arm", 10, 1.5, 100, False)
        damage_dealt = self.player_weapon.get_damage()
        self.enemy_part.set_health(self.enemy_part.get_health() - damage_dealt)
        damage_dealt = self.weapon.get_damage()
        self.enemy.set_health(self.enemy.get_health() - damage_dealt)
        expected_health = 100 - damage_dealt
        self.assertEqual(self.enemy.get_health(), expected_health)
        self.assertTrue(self.enemy.get_health() > 0)

    def test_weapon_damage_on_enemy_part(self): # Integration Test for testing player and enemy part 
        self.player_weapon = Weapon("Test", "Primary", "Test", 30, 100, 5, 500, 600, 300, 1500, 7500, 3)
        self.player = Player(self.player_weapon, self.secondary, self.strategem, self.grenades, self.backpack, self.armor)
        self.enemy_part = EnemyPart("Arm", 10, 1.5, 100, False)
        damage_dealt = self.player_weapon.get_damage()
        self.enemy_part.set_health(self.enemy_part.get_health() - damage_dealt)
        expected_health = 100 - damage_dealt
        self.assertEqual(self.enemy_part.get_health(), expected_health)
        self.assertTrue(self.enemy_part.get_health() > 0)


if __name__ == '__main__':
    unittest.main()

