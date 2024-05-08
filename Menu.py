'''
CS 333.1001 Testing and DevOps
Instructor: Erin Keith
Final Project
Handle player interaction
'''
from Weapon import Weapon
from Armor import Armor
from EnemyPart import EnemyPart
from Enemy import Enemy
from Backpack import Backpack
from Player import Player
from Game_Objects import *
import random

player = Player(None, None, None, 0, None, None)


def select_armor():
    print("Select Armor:")
    for index, armor in enumerate(armors, start=1):
        print(f"{index}. {armor.get_name()}")

    choice = int(input("Enter the number of the armor you want to select: "))
    selected_armor = armors[choice - 1] 
    player.set_armor(selected_armor)
    print(f"You have selected {selected_armor.get_name()}.")

def select_primary_weapon():
    print("Select a primary weapon:")
    for index, weapon in enumerate(primary_weapons, start=1):
        print(f"{index}. {weapon.get_name()}")
    choice = int(input("Enter the number of the primary weapon you want to select: "))
    selected_primary_weapon = primary_weapons[choice - 1]
    print(f"You have selected {selected_primary_weapon.get_name()}.")
    return selected_primary_weapon

def select_secondary_weapon():
    print("Select a secondary weapon:")
    for index, weapon in enumerate(secondary_weapons, start=1):
        print(f"{index}. {weapon.get_name()}")
    choice = int(input("Enter the number of the secondary weapon you want to select: "))
    selected_secondary_weapon = secondary_weapons[choice - 1]
    print(f"You have selected {selected_secondary_weapon.get_name()}.")
    return selected_secondary_weapon

def select_strategem_weapon():
    print("Select a strategem weapon:")
    for index, weapon in enumerate(strategem_weapons, start=1):
        print(f"{index}. {weapon.get_name()}")
    choice = int(input("Enter the number of the strategem weapon you want to select: "))
    selected_strategem_weapon = strategem_weapons[choice - 1]
    print(f"You have selected {selected_strategem_weapon.get_name()}.")
    return selected_strategem_weapon

def select_weapons():
    selected_primary = select_primary_weapon()
    selected_secondary = select_secondary_weapon()
    selected_strategem = select_strategem_weapon()
    player.set_primary_weapon(selected_primary)
    player.set_secondary_weapon(selected_secondary)
    player.set_strategem(selected_strategem)
    print("Weapons have been selected and equipped.")


def face_enemy():
    # Check if the player has equipped armor and weapons
    if not player.get_armor() or not player.get_primary_weapon() or not player.get_secondary_weapon() or not player.get_strategem():
        print("You have not been fully equipped! No true patriot of DEMOCRACY faces the enemy naked.\n Your treason has been noted!")
        return  # Execute the treasonious scum and replace them with another 

    print("Select an enemy to face:")
    for index, enemy in enumerate(enemies, start=1):
        print(f"{index}. {enemy.get_name()} - Health: {enemy.get_health()}")

    enemy_choice = int(input("Enter the number of the enemy you want to face: "))
    selected_enemy = enemies[enemy_choice - 1]

    # List the weapons for the player to choose from
    print("Choose your weapon:")
    print("1. Primary Weapon")
    print("2. Secondary Weapon")
    print("3. Strategem Weapon")
    weapon_choice = int(input("Enter the number of the weapon you want to use: "))

    # Get the selected weapon based on player's choice
    if weapon_choice == 1:
        selected_weapon = player.get_primary_weapon()
    elif weapon_choice == 2:
        selected_weapon = player.get_secondary_weapon()
    elif weapon_choice == 3:
        selected_weapon = player.get_strategem()
    else:
        print("Invalid weapon choice.")
        return

    # List the enemy parts for the player to choose from
    print("Choose the enemy part to target:")
    for index, part in enumerate(selected_enemy.get_parts(), start=1):
        print(f"{index}. {part.get_name()} - Health: {part.get_health()}")

    part_choice = int(input("Enter the number of the part you want to target: "))
    targeted_part = selected_enemy.get_parts()[part_choice - 1]

    # Simulate damage against the targeted enemy part
    part_health_after_attack = targeted_part.get_health() - selected_weapon.get_damage()
    targeted_part.set_health(part_health_after_attack)

    # Check if the enemy is dead
    enemy_is_dead = any(part.get_health() <= 0 and part.get_owner_dies_on_destruction() for part in selected_enemy.get_parts())

    # Print the result of the attack
    if enemy_is_dead:
        print("The enemies of freedom have been vanquished. You have shown them the power of Liber-Tea.")
    else:
        print("The enemies of Democracy yet lives, and liberty weeps!")    


def randomizer():
    print("Randomizer chosen.")
    # Randomly select one weapon from each category
    selected_primary = random.choice(primary_weapons)
    selected_secondary = random.choice(secondary_weapons)
    selected_strategem = random.choice(strategem_weapons)
    selected_armor = random.choice(armors)  # Randomly select armor

    # Assign the randomly selected weapons and armor to the player
    player.set_primary_weapon(selected_primary)
    player.set_secondary_weapon(selected_secondary)
    player.set_strategem(selected_strategem)
    player.set_armor(selected_armor)

    # Print out the weapons and armor that the player received
    print(f"You have been equipped with the following weapons and armor:")
    print(f"Primary Weapon: {selected_primary.get_name()}")
    print(f"Secondary Weapon: {selected_secondary.get_name()}")
    print(f"Strategem Weapon: {selected_strategem.get_name()}")
    print(f"Armor: {selected_armor.get_name()}")

def exit_program():
    print("Exiting program.")
    exit(0)

def default_case():
    print("Invalid option selected.")

menu_options = {
    1: select_armor,
    2: select_weapons,
    3: face_enemy,
    4: randomizer,
    5: exit_program
}

def menu():
    while True:
        print("\nMenu:")
        print("1. Select Armor")
        print("2. Select Weapons")
        print("3. Face Enemy")
        print("4. Randomizer")
        print("5. Exit Program")
        choice = input("Enter your choice (1-5): ")
        
        # Convert the input to an integer and execute the corresponding function
        action = menu_options.get(int(choice), default_case)
        action()

# Run the menu
menu()
