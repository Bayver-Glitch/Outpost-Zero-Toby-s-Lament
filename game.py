"""
OUTPOST ZERO - Colony Survival Sim
VERSION 2 - More Features!
"""

import random
import time

# ==================== GAME STATE ====================

class Game:
    def __init__(self):
        self.day = 1
        self.season = "Spring"
        self.weather = "Clear"
        self.temperature = 65
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
    
    def update_weather(self):
        """Update weather based on season"""
        season_temps = {
            "Spring": (45, 70),
            "Summer": (60, 85),
            "Fall": (35, 60),
            "Winter": (10, 35)
        }
        
        low, high = season_temps[self.season]
        self.temperature = random.randint(low, high)
        
        # Weather
        weather_roll = random.randint(1, 100)
        if weather_roll < 60:
            self.weather = "Clear"
        elif weather_roll < 75:
            self.weather = "Cloudy"
        elif weather_roll < 85:
            self.weather = "Rain"
        elif weather_roll < 92:
            self.weather = "Cold"
        elif weather_roll < 97:
            self.weather = "Storm"
        else:
            self.weather = "Fog"
    
    def update_season(self):
        """Advance seasons"""
        day_in_season = (self.day - 1) % 30
        if day_in_season == 0 and self.day > 1:
            seasons = ["Spring", "Summer", "Fall", "Winter"]
            current = seasons.index(self.season)
            self.season = seasons[(current + 1) % 4]

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
        
        # Skills
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
        self.sickness = None
        self.is_alive = True
        
    def __str__(self):
        status = f"{self.name} | HP:{self.health} ST:{self.stamina} HAPP:{self.happiness}"
        if self.injuries:
            status += f" [{', '.join(self.injuries)}]"
        if self.sickness:
            status += f" [{self.sickness}]"
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

def get_skill_bonus(survivor, task_skill):
    """Calculate skill bonus including happiness"""
    skill = survivor.skills[task_skill]
    
    # Happiness modifier
    if survivor.happiness > 70:
        bonus = 15
    elif survivor.happiness > 50:
        bonus = 5
    elif survivor.happiness > 30:
        bonus = -10
    else:
        bonus = -25
    
    # Weather modifier
    weather = game.weather if 'game' in dir() else "Clear"
    if weather == "Rain":
        bonus -= 10
    elif weather == "Storm":
        bonus -= 20
    elif weather == "Cold":
        bonus -= 15
    
    return skill + bonus

def do_scavenge(survivor, game):
    skill = get_skill_bonus(survivor, "Scavenging")
    roll = random.randint(1, 100)
    result = skill + roll
    
    print(f"\n  {survivor.name} goes scavenging...")
    
    if result > 100:
        found = random.sample(["food", "materials", "medicine", "ammo", "scrap", "book"], 3)
        for item in found:
            add_item(item, game, 1)
        print(f"    AMAZING! Found: {', '.join(found)}")
    elif result > 70:
        found = random.sample(["food", "materials", "medicine", "scrap"], 2)
        for item in found:
            add_item(item, game, 1)
        print(f"    Good haul: {', '.join(found)}")
    elif result > 40:
        found = random.choice(["food", "materials", "scrap"])
        add_item(found, game, 1)
        print(f"    Found: {found}")
    else:
        if random.random() < 0.25:
            injury = random.choice(["Cut", "Bruise"])
            survivor.injuries.append(injury)
            survivor.health -= 15
            print(f"    BAD! Got injured: {injury} (-15 HP)")
            survivor.happiness -= 5
        else:
            print(f"    Found nothing.")

def do_hunt(survivor, game):
    skill = get_skill_bonus(survivor, "Hunting")
    roll = random.randint(1, 100)
    result = skill + roll
    
    print(f"\n  {survivor.name} goes hunting...")
    
    if game.weather == "Rain":
        print(f"    Hard to hunt in the rain!")
        result -= 30
    
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
    skill = get_skill_bonus(survivor, "Gathering")
    
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
    skill = get_skill_bonus(survivor, "Farming")
    roll = skill + random.randint(1, 100)
    
    print(f"\n  {survivor.name} works on the farm...")
    
    if "Farm" not in game.buildings and "Greenhouse" not in game.buildings:
        print(f"    No farm! Can't farm.")
        return
    
    # Weather affects farming
    weather_mod = 0
    if game.weather == "Rain":
        weather_mod = 10
    elif game.weather == "Storm":
        weather_mod = -20
    elif game.weather == "Clear":
        weather_mod = 10
    
    roll += weather_mod
    
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
    skill = get_skill_bonus(survivor, "Building")
    
    print(f"\n  {survivor.name} tries to build...")
    
    if game.materials < 10:
        print(f"    Not enough materials! Need 10.")
        return
    
    if skill + random.randint(1, 100) > 50:
        building = random.choice(["Workshop", "Well", "Chicken Coop", "Greenhouse", "Pen", "Smokehouse"])
        if building not in game.buildings:
            game.buildings[building] = 1
            game.materials -= 10
            print(f"    Built {building}!")
            survivor.happiness += 5
        else:
            game.buildings[building] += 1
            game.materials -= 10
            print(f"    Upgraded {building}!")
    else:
        game.materials -= 3
        print(f"    Made some progress. Used 3 materials.")

def do_rest(survivor, game):
    print(f"\n  {survivor.name} rests...")
    
    # Weather affects rest
    if game.weather == "Storm":
        print(f"    Storm kept them awake...")
        heal = random.randint(5, 10)
        stamina = random.randint(10, 20)
    else:
        heal = random.randint(10, 20)
        stamina = random.randint(20, 35)
    
    survivor.health = min(100, survivor.health + heal)
    survivor.stamina = min(100, survivor.stamina + stamina)
    print(f"    +{heal} HP, +{stamina} Stamina")
    
    # Heal injuries
    if survivor.injuries and random.random() < 0.3:
        recovered = survivor.injuries.pop()
        print(f"    Healed: {recovered}")
    
    # Sickness check
    if survivor.sickness:
        if random.random() < 0.3:
            survivor.sickness = None
            print(f"    Recovered from {survivor.sickness}!")
            survivor.sickness = None

def do_cook(survivor, game):
    skill = get_skill_bonus(survivor, "Cooking")
    
    print(f"\n  {survivor.name} cooks...")
    
    if game.food < 5:
        print(f"    Not enough food to cook!")
        return
    
    bonus = skill // 20
    food_made = 4 + bonus
    
    if random.random() < 0.3 + (bonus * 0.1):
        # Special meal!
        game.food -= 3
        game.food += food_made + 3
        print(f"    Made a special meal! +{food_made + 3} food")
        
        # Happiness boost for everyone
        for s in game.survivors:
            s.happiness += 5
            if s.favorite_food == "Meat" or s.favorite_food == "Fish":
                s.happiness += 5
    else:
        game.food -= 3
        game.food += food_made
        print(f"    Cooked: +{food_made} food")

def do_guard(survivor, game):
    skill = get_skill_bonus(survivor, "Combat")
    
    print(f"\n  {survivor.name} stands guard...")
    
    # Weather affects encounters
    encounter_chance = 0.2
    if game.weather == "Fog":
        encounter_chance = 0.35
    elif game.weather == "Storm":
        encounter_chance = 0.1
    
    if random.random() < encounter_chance:
        enemy = random.choice(["wolf", "zombie", "raider", "zombie dog"])
        print(f"    ENEMY! A {enemy} approaches!")
        
        combat_roll = skill + random.randint(1, 100)
        
        if combat_roll > 60:
            print(f"    {survivor.name} defeated the {enemy}!")
            survivor.happiness += 5
            if random.random() < 0.3:
                loot = random.choice(["ammo", "medicine", "food"])
                add_item(loot, game, 1)
                print(f"    Looted: {loot}")
        else:
            damage = random.randint(10, 25)
            survivor.health -= damage
            print(f"    {survivor.name} took {damage} damage!")
            survivor.happiness -= 10
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
    print(f"DAY {game.day} - {game.season} - {game.weather} {game.temperature}F")
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
            if s.sickness:
                print(f"      SICK: {s.sickness}")

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
    global game
    
    print("="*60)
    print("         OUTPOST ZERO")
    print("   Colony Survival Simulator v2.0")
    print("="*60)
    print()
    
    # Create game
    game = Game()
    game.survivors = create_starting_characters()
    
    # Set up some initial relationships
    game.survivors[0].relationships["Sarah"] = 20  # Marcus likes Sarah
    game.survivors[1].relationships["Marcus"] = 15  # Sarah likes Marcus
    
    print("Your group of 4 survivors has settled in an old farmhouse.")
    print("You have the 'Gardening Basics' book.")
    print("Day 1 begins...\n")
    
    # Main game loop
    while not game.game_over:
        # Update weather
        game.update_season()
        game.update_weather()
        
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
            
            # Check death
            if survivor.health <= 0:
                print(f"\n💀 {survivor.name} has died!")
                survivor.is_alive = False
                # Sadness for others
                for s in game.survivors:
                    if s != survivor and s.is_alive:
                        s.happiness -= 15
        
        # Consume food
        alive = len([s for s in game.survivors if s.is_alive and s.health > 0])
        food_needed = alive * 2
        game.food -= food_needed
        print(f"\n\nSurvivors ate {food_needed} food.")
        
        # Random events
        print("\n" + "-"*40)
        print("NIGHT EVENTS")
        print("-"*40)
        
        event_roll = random.randint(1, 100)
        
        if event_roll < 5:
            print("A survivor had a nightmare!")
            victim = random.choice([s for s in game.survivors if s.is_alive and s.health > 0])
            victim.happiness -= 10
        elif event_roll < 10:
            print("Found hidden stashes!")
            game.food += random.randint(3, 8)
        elif event_roll < 15:
            print("Someone got sick!")
            victim = random.choice([s for s in game.survivors if s.is_alive and s.health > 0])
            victim.sickness = random.choice(["Cold", "Flu", "Food Poisoning"])
            victim.health -= 15
            print(f"    {victim.name} has {victim.sickness}!")
        elif event_roll < 20:
            print("Good weather! Everyone rested well.")
            for s in game.survivors:
                if s.is_alive:
                    s.happiness += 5
        elif event_roll < 25:
            print("Two survivors had a chat...")
            s1, s2 = random.sample([s for s in game.survivors if s.is_alive], 2)
            change = random.randint(-5, 15)
            s1.relationships[s2.name] = s1.relationships.get(s2.name, 0) + change
            s2.relationships[s1.name] = s2.relationships.get(s1.name, 0) + change
            print(f"    {s1.name} and {s2.name} got along {'well' if change > 0 else 'poorly'}!")
        
        # Weather effects
        if game.weather == "Storm":
            print("A storm rages outside!")
            for s in game.survivors:
                if s.is_alive and s.job != "Guard":
                    s.happiness -= 5
        elif game.weather == "Fog":
            print("Thick fog surrounds the settlement...")
        
        # Temperature effects
        if game.temperature < 32:
            print("Freezing cold! Need warmth or people will suffer.")
            for s in game.survivors:
                if s.is_alive and s.job == "Guard":
                    s.health -= 5
        elif game.temperature > 85:
            print("Scorching heat!")
            for s in game.survivors:
                if s.is_alive:
                    s.stamina -= 10
        
        # Remove dead
        game.survivors = [s for s in game.survivors if s.is_alive]
        
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
