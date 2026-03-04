"""
OUTPOST ZERO - Playable Prototype
A survival colony sim - BUILD AND PLAY
"""

import random
import time
import os
import sys

# ==================== GAME STATE ====================

class Game:
    def __init__(self):
        self.day = 1
        self.food = 30
        self.water = 30
        self.materials = 15
        self.medicine = 3
        self.ammo = 5
        self.scrap = 20
        self.books = ["Gardening Basics"]
        self.buildings = {"Farmhouse": 1, "Fire Pit": 1, "Storage": 1}
        self.survivors = []
        self.game_over = False
        self.tech_level = 1
        self.population_cap = 10
        
    def add_survivor(self, survivor):
        if len(self.survivors) < self.population_cap:
            self.survivors.append(survivor)
            return True
        return False

# ==================== CHARACTERS ====================

class Survivor:
    def __init__(self, name, age, sex, profession="Survivor"):
        self.name = name
        self.age = age
        self.sex = sex
        self.profession = profession
        
        # Stats
        self.health = 100
        self.stamina = 100
        self.happiness = 50  # 0-100
        
        # Skills (1-100)
        self.skills = {
            "Scavenging": random.randint(10, 25),
            "Hunting": random.randint(10, 25),
            "Farming": random.randint(10, 25),
            "Gathering": random.randint(10, 25),
            "Building": random.randint(10, 25),
            "Cooking": random.randint(10, 25),
            "Fishing": random.randint(10, 25),
            "Combat": random.randint(10, 25),
            "Medical": random.randint(5, 15),
            "Crafting": random.randint(10, 25),
        }
        
        # Job
        self.job = "Unassigned"
        
        # Personality
        self.traits = []
        self.favorite_food = random.choice(["Meat", "Berries", "Fish", "Vegetables", "Anything"])
        
        # Relationships (name -> -100 to +100)
        self.relationships = {}
        
        # Status
        self.injuries = []
        self.is_alive = True
        
    def __str__(self):
        status = f"{self.name} | HP:{self.health} ST:{self.stamina} HAPP:{self.happiness}"
        if self.injuries:
            status += f" [{', '.join(self.injuries)}]"
        return status

# ==================== CREATE CHARACTERS ====================

def create_character(name, age, profession, skills, traits, food, sex="Male"):
    s = Survivor(name, age, sex, profession)
    for skill, level in skills.items():
        s.skills[skill] = level
    s.traits = traits
    s.favorite_food = food
    return s

def create_starting_characters():
    # Marcus - leader
    marcus = create_character("Marcus", 34, "Leader", 
        {"Scavenging": 35, "Combat": 30, "Building": 25}, 
        ["Brave", "Protective"], "Meat", "Male")
    marcus.happiness = 60
    
    # Sarah - hunter
    sarah = create_character("Sarah", 28, "Hunter",
        {"Hunting": 45, "Fishing": 35, "Scavenging": 20},
        ["Patient", "Kind"], "Fish", "Female")
    sarah.happiness = 55
    
    # Ryan - scavenger
    ryan = create_character("Ryan", 42, "Scavenger",
        {"Scavenging": 50, "Gathering": 35, "Combat": 25},
        ["Cautious", "Selfish"], "Anything", "Male")
    ryan.happiness = 45
    
    # Elena - builder
    elena = create_character("Elena", 24, "Builder",
        {"Building": 40, "Crafting": 35, "Farming": 20},
        ["Creative", "Curious"], "Vegetables", "Female")
    elena.happiness = 50
    
    return [marcus, sarah, ryan, elena]

# ==================== ACTIONS ====================

def do_scavenge(survivor, game):
    """Scavenge in dangerous areas"""
    skill = survivor.skills["Scavenging"]
    roll = random.randint(1, 100)
    result = skill + roll
    
    print(f"\n  {survivor.name} goes scavenging...")
    
    if result > 100:  # Amazing
        found = random.sample(["food", "materials", "medicine", "ammo", "scrap", "book"], 3)
        for item in found:
            add_item(item, game, 1)
        print(f"    AMAZING! Found: {', '.join(found)}")
    elif result > 70:  # Good
        found = random.sample(["food", "materials", "medicine", "scrap"], 2)
        for item in found:
            add_item(item, game, 1)
        print(f"    Good haul: {', '.join(found)}")
    elif result > 40:  # OK
        found = random.choice(["food", "materials", "scrap"])
        add_item(found, game, 1)
        print(f"    Found: {found}")
    else:  # Bad
        if random.random() < 0.25:
            injury = random.choice(["Cut", "Bruise"])
            survivor.injuries.append(injury)
            survivor.health -= 15
            print(f"    BAD! Got injured: {injury} (-15 HP)")
        else:
            print(f"    Found nothing.")

def do_hunt(survivor, game):
    """Hunt for food"""
    skill = survivor.skills["Hunting"]
    roll = random.randint(1, 100)
    result = skill + roll
    
    print(f"\n  {survivor.name} goes hunting...")
    
    if result > 80:
        game.food += 15
        print(f"    SUCCESS! Big deer! +15 food")
    elif result > 50:
        game.food += 8
        print(f"    Got a rabbit. +8 food")
    elif result > 30:
        game.food += 4
        print(f"    Small catch. +4 food")
    else:
        print(f"    No luck today.")
        if random.random() < 0.15:
            survivor.health -= 10
            print(f"    Wolf attack! -10 HP")

def do_gather(survivor, game):
    """Gather berries, wood, herbs"""
    skill = survivor.skills["Gathering"]
    roll = random.randint(1, 100)
    
    print(f"\n  {survivor.name} goes gathering...")
    
    finds = []
    for _ in range(3):
        if skill + random.randint(1, 100) > 40:
            finds.append(random.choice(["berries", "firewood", "herbs", "mushrooms"]))
    
    if finds:
        for item in finds:
            if item == "berries":
                game.food += 2
            elif item == "firewood":
                game.materials += 2
            elif item == "herbs":
                game.medicine += 1
            else:
                game.food += 1
        print(f"    Found: {', '.join(finds)}")
    else:
        print(f"    Found nothing useful.")

def do_farm(survivor, game):
    """Farm crops"""
    skill = survivor.skills["Farming"]
    roll = skill + random.randint(1, 100)
    
    print(f"\n  {survivor.name} works on the farm...")
    
    if "Farm" not in game.buildings:
        print(f"    No farm! Can't farm.")
        return
    
    if roll > 60:
        food_gain = random.randint(5, 12)
        game.food += food_gain
        print(f"    Great harvest! +{food_gain} food")
    elif roll > 30:
        food_gain = random.randint(2, 5)
        game.food += food_gain
        print(f"    Harvest: +{food_gain} food")
    else:
        print(f"    Poor harvest this time.")

def do_build(survivor, game):
    """Build something"""
    skill = survivor.skills["Building"]
    
    print(f"\n  {survivor.name} tries to build...")
    
    if game.materials < 10:
        print(f"    Not enough materials! Need 10.")
        return
    
    if skill + random.randint(1, 100) > 50:
        building = random.choice(["Workshop", "Well", "Chicken Coop", "Greenhouse", "Pen"])
        if building not in game.buildings:
            game.buildings[building] = 1
            game.materials -= 10
            print(f"    Built {building}!")
        else:
            game.buildings[building] += 1
            game.materials -= 10
            print(f"    Upgraded {building}!")
    else:
        game.materials -= 3
        print(f"    Made some progress. Used 3 materials.")

def do_rest(survivor, game):
    """Rest and recover"""
    print(f"\n  {survivor.name} rests...")
    heal = random.randint(10, 20)
    stamina = random.randint(20, 35)
    survivor.health = min(100, survivor.health + heal)
    survivor.stamina = min(100, survivor.stamina + stamina)
    print(f"    +{heal} HP, +{stamina} Stamina")
    
    # Heal injuries
    if survivor.injuries and random.random() < 0.3:
        recovered = survivor.injuries.pop()
        print(f"    Healed: {recovered}")

def do_cook(survivor, game):
    """Cook food (requires Kitchen)"""
    print(f"\n  {survivor.name} cooks...")
    
    if game.food < 5:
        print(f"    Not enough food to cook!")
        return
    
    # Better food with cooking skill
    bonus = survivor.skills["Cooking"] // 20
    food_made = 4 + bonus
    
    if random.random() < 0.3:
        # Special meal!
        game.food -= 3
        game.food += food_made + 3
        print(f"    Made a special meal! +{food_made + 3} food (better)")
        # Happiness boost
        for s in game.survivors:
            if s.favorite_food in ["Meat", "Fish"]:
                s.happiness += 5
    else:
        game.food -= 3
        game.food += food_made
        print(f"    Cooked: +{food_made} food")

def do_guard(survivor, game):
    """Guard the settlement"""
    print(f"\n  {survivor.name} stands guard...")
    
    # Random enemy encounter
    if random.random() < 0.2:
        enemy = random.choice(["wolf", "zombie", "raider"])
        print(f"    ENEMY! A {enemy} approaches!")
        
        combat_roll = survivor.skills["Combat"] + random.randint(1, 100)
        
        if combat_roll > 60:
            print(f"    {survivor.name} defeated the {enemy}!")
            if random.random() < 0.3:
                loot = random.choice(["ammo", "medicine", "food"])
                add_item(loot, game, 1)
                print(f"    Looted: {loot}")
        else:
            damage = random.randint(10, 25)
            survivor.health -= damage
            print(f"    {survivor.name} took {damage} damage!")
            if random.random() < 0.2:
                survivor.injuries.append("Wound")
    else:
        print(f"    Quiet night. All clear.")

# ==================== HELPERS ====================

def add_item(item, game, amount=1):
    if item == "food":
        game.food += amount * random.randint(2, 5)
    elif item == "materials":
        game.materials += amount * random.randint(1, 3)
    elif item == "scrap":
        game.scrap += amount * random.randint(2, 5)
    elif item == "medicine":
        game.medicine += amount
    elif item == "ammo":
        game.ammo += amount * random.randint(1, 3)
    elif item == "book":
        books = ["Hunting Guide", "Fishing Manual", "Carpentry", "First Aid", "Botany", "Mechanics"]
        found = random.choice(books)
        if found not in game.books:
            game.books.append(found)
            print(f"    NEW BOOK: {found}!")

def check_game_over(game):
    if game.food <= 0:
        print("\n" + "="*50)
        print("GAME OVER - Starvation!")
        print("Your settlement has collapsed.")
        return True
    alive = [s for s in game.survivors if s.is_alive and s.health > 0]
    if not alive:
        print("\n" + "="*50)
        print("GAME OVER")
        print("Everyone has perished!")
        return True
    return False

def print_status(game):
    print(f"\n{'='*50}")
    print(f"DAY {game.day} - {game.survivors[0].profession}'s Settlement")
    print(f"{'='*50}")
    print(f"\nRESOURCES:")
    print(f"  Food: {game.food}  Water: {game.water}  Scrap: {game.scrap}")
    print(f"  Materials: {game.materials}  Medicine: {game.medicine}  Ammo: {game.ammo}")
    print(f"  Tech Level: {game.tech_level}")
    print(f"\nBUILDINGS: {', '.join([f'{k}(v{v})' for k,v in game.buildings.items()])}")
    print(f"\nBOOKS: {', '.join(game.books) if game.books else 'None'}")
    
    print(f"\nSURVIVORS ({len(game.survivors)}/{game.population_cap}):")
    for s in game.survivors:
        if s.health > 0:
            mood = "+" if s.happiness > 60 else "=" if s.happiness > 40 else "-"
            print(f"  {mood} {s.name}: {s.job} | HP:{s.health} ST:{s.stamina} HAPP:{s.happiness}")
            if s.injuries:
                print(f"      INJURIES: {', '.join(s.injuries)}")

def get_job_choice(survivor):
    jobs = [
        ("1", "Scavenge"),
        ("2", "Hunt"),
        ("3", "Gather"),
        ("4", "Farm"),
        ("5", "Build"),
        ("6", "Cook"),
        ("7", "Rest"),
        ("8", "Guard"),
    ]
    
    skill_map = {
        "1": "Scavenging", "2": "Hunting", "3": "Gathering",
        "4": "Farming", "5": "Building", "6": "Cooking",
        "7": "Rest", "8": "Combat"
    }
    
    print(f"\n{survivor.name}'s skills:")
    for num, job in jobs:
        skill_level = survivor.skills.get(skill_map[num], 10)
        print(f"  {num}: {job} ({skill_level})")
    
    while True:
        choice = input(f"\nChoose task for {survivor.name} (1-8): ").strip()
        for num, job in jobs:
            if choice == num:
                return job, skill_map[num]
        print("Invalid choice. 1-8 please.")

# ==================== MAIN GAME ====================

def main():
    print("="*60)
    print("         OUTPOST ZERO")
    print("   A Colony Survival Simulator")
    print("="*60)
    print()
    
    # Create game
    game = Game()
    game.survivors = create_starting_characters()
    
    print("Your group of 4 survivors has settled in an old farmhouse.")
    print("You have the 'Gardening Basics' book.")
    print("Day 1 begins...\n")
    
    # Main game loop
    while not game.game_over:
        print_status(game)
        
        # Check starvation
        if game.food < len(game.survivors) * 2:
            print(f"\n⚠️ LOW FOOD! {len(game.survivors) * 2} needed per day!")
        
        # Player assigns tasks
        print("\n" + "-"*40)
        print("ASSIGN TASKS")
        print("-"*40)
        
        for survivor in game.survivors:
            if survivor.health <= 0:
                continue
            
            task, skill = get_job_choice(survivor)
            survivor.job = task
            
            # Execute task
            if task == "Scavenge":
                survivor.stamina -= 20
                do_scavenge(survivor, game)
            elif task == "Hunt":
                survivor.stamina -= 25
                do_hunt(survivor, game)
            elif task == "Gather":
                survivor.stamina -= 15
                do_gather(survivor, game)
            elif task == "Farm":
                survivor.stamina -= 15
                do_farm(survivor, game)
            elif task == "Build":
                survivor.stamina -= 20
                do_build(survivor, game)
            elif task == "Cook":
                survivor.stamina -= 10
                do_cook(survivor, game)
            elif task == "Rest":
                do_rest(survivor, game)
            elif task == "Guard":
                survivor.stamina -= 15
                do_guard(survivor, game)
        
        # Consume food
        food_needed = len([s for s in game.survivors if s.health > 0]) * 2
        game.food -= food_needed
        print(f"\n\nSurvivors ate {food_needed} food.")
        
        # Random events
        print("\n" + "-"*40)
        print("NIGHT EVENTS")
        print("-"*40)
        
        event_roll = random.randint(1, 100)
        
        if event_roll < 5:
            print("A survivor had a nightmare!")
            victim = random.choice([s for s in game.survivors if s.health > 0])
            victim.happiness -= 10
        elif event_roll < 10:
            print("Found hidden stashes!")
            game.food += random.randint(3, 8)
        elif event_roll < 15:
            print("Someone got sick!")
            victim = random.choice([s for s in game.survivors if s.health > 0])
            victim.health -= 15
            if random.random() < 0.3:
                victim.injuries.append("Sick")
        elif event_roll < 20:
            print("Good weather! Everyone rested well.")
            for s in game.survivors:
                s.happiness += 5
        
        # Remove dead
        game.survivors = [s for s in game.survivors if s.health > 0]
        
        # Advance day
        game.day += 1
        
        # Check game over
        if check_game_over(game):
            game.game_over = True
        
        # Continue?
        if not game.game_over:
            cont = input("\nPress Enter for next day (q to quit): ")
            if cont.lower() == 'q':
                print("\nYou abandoned the settlement. Goodbye!")
                break
    
    print("\n" + "="*50)
    print(f"GAME OVER - You survived {game.day} days!")
    print("="*50)

if __name__ == "__main__":
    main()
