'''
CS 333.1001 Testing and DevOps
Instructor: Erin Keith
Final Project
Player.py: Class to manage the behaviors of the player class. Players may be equipped with a primary, secondary, and strategem weapon. 
They have a backpack slot that can be used for carrying additional ammo or support.
'''
from Weapon import Weapon
from Armor import Armor
from Backpack import Backpack
class Player:
    def __init__(self, primary_weapon, secondary_weapon, strategem, grenades, backpack, armor):
        self.primary_weapon = primary_weapon
        self.secondary_weapon = secondary_weapon
        self.strategem = strategem
        self.grenades = grenades
        self.backpack = backpack
        self.armor = armor
        if self.armor is not None:
            self.check_armor_passive()
    # Getters
    def get_primary_weapon(self):
        return self.primary_weapon

    def get_secondary_weapon(self):
        return self.secondary_weapon

    def get_strategem(self):
        return self.strategem

    def get_grenades(self):
        return self.grenades

    def get_backpack(self):
        return self.backpack

    def get_armor(self):
        return self.armor

    # Setters
    def set_primary_weapon(self, weapon):
        self.primary_weapon = weapon

    def set_secondary_weapon(self, weapon):
        self.secondary_weapon = weapon

    def set_strategem(self, strategem):
        self.strategem = strategem

    def set_grenades(self, grenades):
        self.grenades = grenades

    def set_backpack(self, backpack):
        self.backpack = backpack

    def set_armor(self, armor):
        self.armor = armor
    #One of the armor passives increases the ammount of grenades the player can carry this funciton checks for that passive
    def check_armor_passive(self):
        if self.armor.get_passive() == "Engineering Kit":
            if self.grenades.get_category() == "Grenade":
                new_capacity = self.grenades.get_capacity() + 2
                self.grenades.set_capacity(new_capacity)