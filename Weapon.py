'''
CS 333.1001 Testing and DevOps
Instructor: Erin Keith
Final Project
weapon.py: Keeps track of the weapons the players can use in Helldivers 2.
'''
class Weapon:
    def __init__(self, w_name, w_category, w_subcategory, w_damage, w_capacity, w_mags, w_total_rounds, w_fire_rate, w_dps, w_dmg_per_mag, w_dmg_total, w_armor_penetration):
        self._weapon_name = w_name
        self._category = w_category  # Should be 3 types: primary, secondaries, strategem
        self._subcategory = w_subcategory  # Represents type of weapon, rifle, submachine gun, energy weapon, explosive, etc.
        self._damage = float(w_damage)
        self._capacity = float(w_capacity)
        self._mags = float(w_mags)
        self._total_rounds = float(w_total_rounds)
        self._fire_rate = float(w_fire_rate)
        self._dps = float(w_dps)
        self._dmg_per_mag = float(w_dmg_per_mag)
        self._dmg_total = float(w_dmg_total)
        self._armor_penetration = float(w_armor_penetration) 
        # Penetration scales from 1-9 the higher the better. When damage is dealt to the same armor pen, damage dealt is half, when less than no damage, when above does full damage.

    # Getters
    def get_name(self):
        return self._weapon_name

    def get_category(self):
        return self._category

    
    def get_subcategory(self):
        return self._subcategory

    
    def get_damage(self):
        return self._damage

    
    def get_capacity(self):
        return self._capacity

    
    def get_mags(self):
        return self._mags

    
    def get_total_rounds(self):
        return self._total_rounds

    
    def get_fire_rate(self):
        return self._fire_rate

    
    def get_dps(self):
        return self._dps

    
    def get_dmg_per_mag(self):
        return self._dmg_per_mag

    
    def get_dmg_total(self):
        return self._dmg_total

    
    def get_armor_penetration(self):
        return self._armor_penetration

    # Setters
    def set_name(self, value):
        self._weapon_name = value

    def set_category(self, value):
        self._category = value

    def set_subcategory(self, value):
        self._subcategory = value

    def set_damage(self, value):
        self._damage = float(value)

    def set_capacity(self, value):
        self._capacity = float(value)

    def set_mags(self, value):
        self._mags = float(value)

    def set_total_rounds(self, value):
        self._total_rounds = float(value)

    def set_fire_rate(self, value):
        self._fire_rate = float(value)

    def set_dps(self, value):
        self._dps = float(value)

    def set_dmg_per_mag(self, value):
        self._dmg_per_mag = float(value)

    def set_dmg_total(self, value):
        self._dmg_total = float(value)

    def set_armor_penetration(self, value):
        self._armor_penetration = float(value)

