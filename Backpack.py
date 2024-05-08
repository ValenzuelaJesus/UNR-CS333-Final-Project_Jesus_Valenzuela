'''
CS 333.1001 Testing and DevOps
Instructor: Erin Keith
Final Project
Backpack.py: In helldivers 2 players can wear backpack which function as support objects, or ammo packs for weapons
Example a jetpack allows player to scale verticle distance
The autocannon strategem has an ammo backpack slot that contains ammo used to reload the weapon
'''
class Backpack:
    def __init__(self, name, description, has_ammo):
        self._name = name
        self._description = description
        self._has_ammo = has_ammo

    # Getters
    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def has_ammo(self):
        return self._has_ammo

    # Setters
    def set_name(self, value):
        self._name = value

    def set_description(self, value):
        self._description = value

    def set_has_ammo(self, value):
        self._has_ammo = value