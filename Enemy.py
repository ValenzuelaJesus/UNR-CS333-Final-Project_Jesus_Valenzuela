'''
CS 333.1001 Testing and DevOps
Instructor: Erin Keith
Final Project
Enemy.py: Enemy class handles the behaviors of the enemies
Enemies belong to a faction which means they will not face multiple factions at once.
Enemies have a name and classification
Enemies have parts that can take seperate damage. 
'''
from EnemyPart import EnemyPart
class Enemy:
    def __init__(self, name, faction, classification, health, parts):
        self.name = name # Example Scavanger, Charger, Bile Titan for 
        self.faction = faction # Currently 2 factions in game more coming. Terminids and Automaton
        self.classification = classification #3 types lights have a high spawn, mediums moderate spawn rate, heavy low spawn rate.
        self.health = health #total health of the enemy when it hits zero the enemy is eleminated
        self.parts = parts  # Array of EnemyParts head, arms, legs, bile sacks, heat vents, 
    
        # Getters
    def get_name(self):
        return self.name

    def get_faction(self):
        return self.faction

    def get_classification(self):
        return self.classification

    def get_health(self):
        return self.health

    def get_parts(self):
        return self.parts

    # Setters
    def set_name(self, value):
        self.name = value

    def set_faction(self, value):
        self.faction = value

    def set_classification(self, value):
        self.classification = value

    def set_health(self, value):
        self.health = value

    def set_parts(self, value):
        self.parts = value
    #Function to check if a part has been destroyed and if the part is critical to the enemy the enemy health is set to zero example
    #An enemy can lose an arm but cannot lose head without dying
    def check_part_destruction(self): 
        for part in self.parts:
            if part.get_health() <= 0:
                if part.get_owner_dies_on_destruction():
                    self.set_health(0)
                    break  
                else:
                    self.set_health(self.get_health() - part.get_health())