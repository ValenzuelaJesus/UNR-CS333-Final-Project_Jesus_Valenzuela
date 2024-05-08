'''
CS 333.1001 Testing and DevOps
Instructor: Erin Keith
Final Project
Armor.py: Contains the behaviors of the Players armor
'''
class Armor:
    def __init__(self, name, armor_class, armor_rating, speed, stamina_regen, passive):
        self._name = name 
        self._armor_class = armor_class #3 types heavy, light, and medium
        self._armor_rating = armor_rating # determines the damage mitegation of the armor
        self._speed = speed # determines how quickly the player moves 
        self._stamina_regen = stamina_regen #determines how quickly stamina used for spriting is regenerated
        self._passive = passive # Each Armor has a passive that offers a bonus, more gernades, stims, lower recoil, resist explosive
        self.apply_extra_padding()
    # Getters
    def get_name(self):
        return self._name

    def get_armor_class(self):
        return self._armor_class

    def get_armor_rating(self):
        return self._armor_rating

    def get_speed(self):
        return self._speed

    def get_stamina_regen(self):
        return self._stamina_regen

    def get_passive(self):
        return self._passive

    # Setters
    def set_name(self, name):
        self._name = name

    def set_armor_class(self, armor_class):
        self._armor_class = armor_class

    def set_armor_rating(self, armor_rating):
        self._armor_rating = armor_rating

    def set_speed(self, speed):
        self._speed = speed

    def set_stamina_regen(self, stamina_regen):
        self._stamina_regen = stamina_regen

    def set_passive(self, passive):
        self._passive = passive

    def apply_extra_padding(self): # One of the passives increases the armor rating 
        if self._passive == "Extra Padding":
            if self._armor_class == "light":
                self._armor_rating += 43
            elif self._armor_class == "medium":
                self._armor_rating += 50
            elif self._armor_class == "heavy":
                self._armor_rating += 56
    
    def get_passive_description(self):
        descriptions = {
            "Fortified": "Further reduces recoil when crouching or prone by 30%. Provides 50% resistance to explosive damage.",
            "Servo-Assisted": "Increases throwing range by 30%. Provides +50% limb health.",
            "Engineering Kit": "Further reduces recoil when crouching or prone by 30%. Increases initial inventory and holding capacity of grenades by +2.",
            "Med-Kit": "Increases initial inventory and holding capacity of stims by +2. Increases stim effect duration by 2.0s.",
            "Electrical Conduit": "Provides 95% resistance to arc damage.",
            "Scout": "Markers placed on the map will generate radar scans every 2.0s. Reduces range at which enemies can detect the wearer by 30%.",
            "Democracy Protects": "50% chance to not die when taking lethal damage. Prevents all damage from bleeding if chest hemorrhages.",
            "Extra Padding": "Increases armor rating based on armor class."
        }
        return descriptions.get(self._passive, "ERROR: No passive ability description found.")


