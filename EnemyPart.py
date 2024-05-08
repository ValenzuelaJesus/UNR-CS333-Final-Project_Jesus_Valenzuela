'''
CS 333.1001 Testing and DevOps
Instructor: Erin Keith
Final Project
EnemyPart.py: a component of the enemy class. Handles the behavior of individual components of enemies.
For example will track the health of enemy legs, arms, weakpoints, and heads/
'''
class EnemyPart:
    def __init__(self, name, armor_value, damage_multiplier, health, owner_dies_on_destruction):
        self._name = name #Name, for example The bile titan has a weakspot on the forehead
        self._armor_value = armor_value # Scales from 1-9 corresponds with weapon penetration and 
        self._damage_multiplier = damage_multiplier # Some weakpoints take additional damage when struck 
        self._health = health #some components can be destroyed individually without being fatal to the owner 
        self._owner_dies_on_destruction = owner_dies_on_destruction # Some components when destroyed are fatal to the owner

    # Getters
    def get_name(self):
        return self._name

    def get_armor_value(self):
        return self._armor_value

    def get_damage_multiplier(self):
        return self._damage_multiplier

    def get_health(self):
        return self._health

    def get_owner_dies_on_destruction(self):
        return self._owner_dies_on_destruction

    # Setters
    def set_name(self, name):
        self._name = name

    def set_armor_value(self, armor_value):
        self._armor_value = armor_value

    def set_damage_multiplier(self, damage_multiplier):
        self._damage_multiplier = damage_multiplier

    def set_health(self, health):
        self._health = health

    def set_owner_dies_on_destruction(self, owner_dies_on_destruction):
        self._owner_dies_on_destruction = owner_dies_on_destruction