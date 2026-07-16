# Devin Theriault
# 07/16/2026
# Final Project
# Goblin Killing Game

import random
import time

# Character Classes with their stats
CHARACTER_CLASSES = {
    "warrior": {"health": 150, "min_damage": 12, "max_damage": 18, "hit_chance": 0.80},
    "archer": {"health": 100, "min_damage": 15, "max_damage": 20, "hit_chance": 0.80},
    "rogue": {"health": 80, "min_damage": 18, "max_damage": 25, "hit_chance": 0.90}
}

# Monster Stats
GOBLIN_STATS = {"health": 50, "min_damage": 10, "max_damage": 15, "hit_chance": 0.80}


def create_character():
    """Allow the user to create a character with a name and class."""
    print("\n" + "="*50)
    print("CHARACTER CREATION")
    print("="*50)
    
    # Get character name
    character_name = input("\nEnter your character's name: ").strip()
    
    # Display class options
    print("\nChoose your character class:")
    print("1. Warrior - 150 HP, 12-18 attack damage, 80% hit chance")
    print("2. Archer - 100 HP, 15-20 attack damage, 80% hit chance")
    print("3. Rogue - 80 HP, 18-25 attack damage, 90% hit chance")
    
    # Get class choice
    while True:
        class_choice = input("\nEnter your class choice (1, 2, or 3): ").strip()
        if class_choice == "1":
            character_class = "warrior"
            break
        elif class_choice == "2":
            character_class = "archer"
            break
        elif class_choice == "3":
            character_class = "rogue"
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    # Create character dictionary
    class_stats = CHARACTER_CLASSES[character_class]
    character = {
        "name": character_name,
        "class": character_class,
        "health": class_stats["health"],
        "max_health": class_stats["health"],
        "min_damage": class_stats["min_damage"],
        "max_damage": class_stats["max_damage"],
        "hit_chance": class_stats["hit_chance"],
        "defending": False
    }
    
    print(f"\n✓ {character['name']} the {character['class'].capitalize()} has been created!")
    print(f"  Health: {character['health']} HP")
    time.sleep(1.5)
    
    return character


def create_goblin(goblin_number):
    """Create a goblin enemy."""
    goblin = {
        "name": f"Goblin {goblin_number}",
        "health": GOBLIN_STATS["health"],
        "max_health": GOBLIN_STATS["health"],
        "min_damage": GOBLIN_STATS["min_damage"],
        "max_damage": GOBLIN_STATS["max_damage"],
        "hit_chance": GOBLIN_STATS["hit_chance"]
    }
    return goblin


def display_battle_status(character, monster):
    """Display the current health status of both combatants."""
    print(f"\n{character['name']} (Player): {character['health']}/{character['max_health']} HP")
    print(f"{monster['name']} (Enemy): {monster['health']}/{monster['max_health']} HP")


def player_attack(character, monster):
    """Handle player attack with hit/miss mechanic."""
    if random.random() < character["hit_chance"]:
        # Hit
        damage = random.randint(character["min_damage"], character["max_damage"])
        monster["health"] -= damage
        print(f"\n{character['name']} attacks {monster['name']}!")
        print(f"✓ HIT! Dealt {damage} damage.")
        return True
    else:
        # Miss
        print(f"\n{character['name']} attacks {monster['name']}!")
        print(f"✗ MISS! Attack failed.")
        return False


def player_defend(character):
    """Set the player to defend for this turn."""
    character["defending"] = True
    print(f"\n{character['name']} takes a defensive stance!")
    print(f"⚔ Defense activated - incoming damage will be negated this turn.")


def monster_attack(character, monster):
    """Handle monster attack with hit/miss mechanic."""
    if random.random() < monster["hit_chance"]:
        # Hit
        damage = random.randint(monster["min_damage"], monster["max_damage"])
        
        # Check if player is defending
        if character["defending"]:
            print(f"\n{monster['name']} attacks {character['name']}!")
            print(f"✓ HIT! But {character['name']}'s defense negates all damage!")
            character["defending"] = False
        else:
            character["health"] -= damage
            print(f"\n{monster['name']} attacks {character['name']}!")
            print(f"✓ HIT! Dealt {damage} damage.")
    else:
        # Miss
        print(f"\n{monster['name']} attacks {character['name']}!")
        print(f"✗ MISS! Attack failed.")
        character["defending"] = False


def battle(character, monster):
    """Execute a battle between the character and a monster."""
    print("\n" + "="*50)
    print(f"BATTLE START: {character['name']} vs {monster['name']}")
    print("="*50)
    time.sleep(1)
    
    turn_count = 0
    
    while character["health"] > 0 and monster["health"] > 0:
        turn_count += 1
        print(f"\n--- TURN {turn_count} ---")
        display_battle_status(character, monster)
        
        # Player's turn
        while True:
            action = input(f"\nWhat will {character['name']} do? (attack/defend): ").strip().lower()
            if action == "attack":
                player_attack(character, monster)
                break
            elif action == "defend":
                player_defend(character)
                break
            else:
                print("Invalid action. Please choose 'attack' or 'defend'.")
        
        # Check if monster is defeated
        if monster["health"] <= 0:
            print(f"\n🎉 Victory! {monster['name']} has been defeated!")
            return True
        
        time.sleep(1)
        
        # Monster's turn
        monster_attack(character, monster)
        
        # Check if player is defeated
        if character["health"] <= 0:
            print(f"\n💀 Defeat! {character['name']} has been defeated!")
            return False
        
        time.sleep(1)
    
    return character["health"] > 0


def main():
    """Main function to run the game."""
    print("\n" + "="*50)
    print("WELCOME TO THE GOBLIN KILLING GAME")
    print("="*50)
    
    while True:
        # Create character
        character = create_character()
        
        # Battle three goblins
        goblins_defeated = 0
        game_over = False
        
        for goblin_num in range(1, 4):
            if game_over:
                break
            
            goblin = create_goblin(goblin_num)
            
            print(f"\n{character['name']} encounters {goblin['name']}!")
            time.sleep(1)
            
            # Battle the goblin
            victory = battle(character, goblin)
            
            if victory:
                goblins_defeated += 1
                print(f"\nGoblins defeated: {goblins_defeated}/3")
                time.sleep(2)
            else:
                game_over = True
                # Character died
                print("\n" + "="*50)
                print("GAME OVER")
                print("="*50)
                print(f"Your character {character['name']} died!")
                
                while True:
                    restart_choice = input("\nWould you like to try again? (yes/no): ").strip().lower()
                    if restart_choice == "yes":
                        break
                    elif restart_choice == "no":
                        print("\nThanks for playing! Goodbye.")
                        return
                    else:
                        print("Invalid choice. Please enter 'yes' or 'no'.")
        
        # Check if player won
        if goblins_defeated == 3:
            print("\n" + "="*50)
            print("Congratulations, you are victorious!!!")
            print("="*50)
            print(f"\n{character['name']} has defeated all 3 Goblins!")
            print(f"Final Health: {character['health']}/{character['max_health']} HP")
            
            while True:
                play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
                if play_again == "yes":
                    break
                elif play_again == "no":
                    print("\nThanks for playing! Goodbye.")
                    return
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
