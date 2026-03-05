"""
OUTPOST ZERO - Colony Survival Sim
VERSION 3.0 - Mood, Quality, Traits & Events
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
        season_temps = {"Spring": (45, 70), "Summer": (60, 85), "Fall": (35, 60), "Winter": (10, 35)}
        low, high = season_temps[self.season]
        self.temperature = random.randint(low, high)
        
        roll = random.randint(1, 100)
        if roll < 60: self.weather = "Clear"
        elif roll < 75: self.weather = "Cloudy"
        elif roll < 85: self.weather = "Rain"
        elif roll < 92: self.weather = "Cold"
        elif roll < 97: self.weather = "Storm"
        else: self.weather = "Fog"
    
    def update_season(self):
        day_in_season = (self.day - 1) % 30
        if day_in_season == 0 and self.day > 1:
            seasons = ["Spring", "Summer", "Fall", "Winter"]
            self.season = seasons[(seasons.index(self.season) + 1) % 4]

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
        self.happiness = 50
        self.base_happiness = 50  # Inherent mood
        
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
        
        # Traits (personality affects everything!)
        self.traits = []
        self.gain_random_traits()
        
        # Relationships
        self.relationships = {}
        
        # Status
        self.injuries = []
        self.sickness = None
        self.is_alive = True
        self.quality_modifier = 0  # From mood
        
    def gain_random_traits(self):
        """Give character some random traits"""
        mood_traits = ["Optimist", "Pessimist", "Stoic", "Cheerful", "Grumpy", "Melancholic"]
        work_traits = ["Perfectionist", "Lazy", "Slacker", "Detail Oriented", "Hard Worker"]
        social_traits = ["Charismatic", "Awkward", "Loyal"]
        health_traits = ["Tough", "Fragile", "Fast Healer", "Pain Resistant"]
        
        # 1-2 mood traits
        self.traits = random.sample(mood_traits, min(1, len(mood_traits)))
        
        # 1 work trait
        self.traits.append(random.choice(work_traits))
        
        # 1 social trait
        self.traits.append(random.choice(social_traits))
        
        # Sometimes a health trait
        if random.random() < 0.3:
            self.traits.append(random.choice(health_traits))
    
    def get_quality_modifier(self):
        """Calculate work quality based on mood + traits"""
        mood = self.happiness
        
        # Mood affects quality
        if mood > 70: q = 10
        elif mood > 50: q = 5
        elif mood > 30: q = -5
        elif mood > 10: q = -10
        else: q = -15
        
        # Traits modify quality
        if "Perfectionist" in self.traits: q += 2
        if "Lazy" in self.traits: q -= 2
        if "Slacker" in self.traits: q -= 3
        if "Detail Oriented" in self.traits: q += 3
        if "Hard Worker" in self.traits: q += 1
        
        self.quality_modifier = q
        return q
    
    def get_mood_contagion(self):
        """How this character affects others"""
        if self.happiness > 70: return 2
        elif self.happiness > 50: return 1
        elif self.happiness > 30: return 0
        elif self.happiness > 10: return -1
        else: return -2
    
    def get_contagion_resistance(self):
        """How resistant to others' moods"""
        if "Stoic" in self.traits: return 0.5
        if "Cheerful" in self.traits: return 0  # Immune to bad
        if "Empathic" in self.traits: return 1.5
        return 1.0
    
    def get_daily_base_change(self):
        """Daily mood change from inherent traits"""
        change = 0
        if "Cheerful" in self.traits: change += 3
        if "Melancholic" in self.traits: change -= 3
        if "Optimist" in self.traits: change += 1
        if "Pessimist" in self.traits: change -= 1
        return change
    
    def get_event_modifier(self, event_val):
        """Modify how much events affect this character"""
        if "Optimist" in self.traits and event_val < 0:
            return event_val + 1  # Less negative
        if "Pessimist" in self.traits and event_val < 0:
            return event_val - 1  # More negative
        if "Bright Side" in self.traits and event_val < 0:
            return event_val + 1
        return event_val
    
    def __str__(self):
        mood = "+" if self.happiness > 60 else "=" if self.happiness > 40 else "-"
        q = self.get_quality_modifier()
        quality = "++" if q > 5 else "+" if q > 0 else "--" if q < -5 else "-" if q < 0 else "="
        return f"{self.name} | HP:{self.health} HAPP:{self.happiness}{mood} Q:{q}{quality}"

# ==================== CREATE CHARACTERS ====================

def create_character(name, age, profession, skills, traits, sex="Male"):
    s = Survivor(name, age, sex, profession)
    for skill, level in skills.items():
        s.skills[skill] = level
    s.traits = traits
    return s

def create_starting_characters():
    # Marcus - leader - generally optimistic
    marcus = create_character("Marcus", 34, "Leader", 
        {"Scavenging": 35, "Combat": 30, "Building": 25, "Leadership": 30}, 
        ["Optimist", "Hard Worker", "Loyal", "Tough"], "Male")
    marcus.happiness = 65
    marcus.base_happiness = 60
    
    # Sarah - hunter - cheerful
    sarah = create_character("Sarah", 28, "Hunter",
        {"Hunting": 45, "Fishing": 35, "Scavenging": 20},
        ["Cheerful", "Detail Oriented", "Loyal", "Pain Resistant"], "Female")
    sarah.happiness = 60
    sarah.base_happiness = 65
    
    # Ryan - pessimistic, grumpy
    ryan = create_character("Ryan", 42, "Scavenger",
        {"Scavenging": 50, "Gathering": 35, "Combat": 25},
        ["Pessimist", "Grumpy", "Slacker", "Fragile"], "Male")
    ryan.happiness = 35
    ryan.base_happiness = 30
    
    # Elena - creative, optimistic
    elena = create_character("Elena", 24, "Builder",
        {"Building": 40, "Crafting": 35, "Farming": 20},
        ["Optimist", "Perfectionist", "Charismatic", "Fast Healer"], "Female")
    elena.happiness = 55
    elena.base_happiness = 55
    
    return [marcus, sarah, ryan, elena]

# ==================== QUALITY CRAFTING ====================

def get_quality_name(quality_score):
    if quality_score >= 90: return "LEGENDARY"
    elif quality_score >= 70: return "EXCELLENT"
    elif quality_score >= 50: return "Good"
    elif quality_score >= 30: return "Poor"
    else: return "TERRIBLE"

def get_quality_bonus(quality_score):
    if quality_score >= 90: return 0.5  # +50%
    elif quality_score >= 70: return 0.25  # +25%
    elif quality_score >= 50: return 0
    elif quality_score >= 30: return -0.25  # -25%
    else: return -0.5  # -50%

# ==================== ACTIONS ====================

def do_scavenge(survivor, game):
    quality_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Scavenging"] + quality_mod
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
            survivor.happiness -= 5
            print(f"    BAD! Got injured: {injury} (-15 HP)")
        else:
            print(f"    Found nothing.")

def do_hunt(survivor, game):
    quality_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Hunting"] + quality_mod
    roll = random.randint(1, 100)
    result = skill + roll
    
    print(f"\n  {survivor.name} goes hunting...")
    
    if game.weather == "Rain": result -= 30
    
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

def do_gather(survivor, game):
    quality_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Gathering"] + quality_mod
    
    print(f"\n  {survivor.name} goes gathering...")
    
    finds = []
    for _ in range(3):
        if skill + random.randint(1, 100) > 40:
            finds.append(random.choice(["berries", "firewood", "herbs", "mushrooms"]))
    
    if finds:
        for item in finds:
            if item == "berries": game.food += 2
            elif item == "firewood": game.materials += 2
            elif item == "herbs": game.medicine += 1
            else: game.food += 1
        print(f"    Found: {', '.join(finds)}")
    else:
        print(f"    Found nothing useful.")

def do_farm(survivor, game):
    quality_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Farming"] + quality_mod
    roll = skill + random.randint(1, 100)
    
    print(f"\n  {survivor.name} works on the farm...")
    
    if "Farm" not in game.buildings and "Greenhouse" not in game.buildings:
        print(f"    No farm! Can't farm.")
        return
    
    weather_mod = 10 if game.weather == "Rain" else 10 if game.weather == "Clear" else -20 if game.weather == "Storm" else 0
    roll += weather_mod
    
    if roll > 60:
        food_gain = random.randint(5, 12)
        game.food += food_gain
        quality_name = get_quality_name(roll)
        print(f"    {quality_name} harvest! +{food_gain} food")
    elif roll > 30:
        food_gain = random.randint(2, 5)
        game.food += food_gain
        print(f"    Harvest: +{food_gain} food")
    else:
        print(f"    Poor harvest this time.")

def do_build(survivor, game):
    quality_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Building"] + quality_mod
    
    print(f"\n  {survivor.name} tries to build...")
    
    if game.materials < 10:
        print(f"    Not enough materials! Need 10.")
        return
    
    roll = skill + random.randint(1, 100)
    
    if roll > 50:
        building = random.choice(["Workshop", "Well", "Chicken Coop", "Greenhouse", "Pen", "Smokehouse"])
        if building not in game.buildings:
            game.buildings[building] = 1
            game.materials -= 10
            quality_name = get_quality_name(roll)
            print(f"    {quality_name}! Built {building}!")
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
    
    heal = random.randint(10, 20)
    stamina = random.randint(20, 35)
    survivor.health = min(100, survivor.health + heal)
    survivor.stamina = min(100, survivor.stamina + stamina)
    print(f"    +{heal} HP, +{stamina} Stamina")
    
    if survivor.injuries and random.random() < 0.3:
        recovered = survivor.injuries.pop()
        print(f"    Healed: {recovered}")

def do_cook(survivor, game):
    quality_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Cooking"] + quality_mod
    
    print(f"\n  {survivor.name} cooks...")
    
    if game.food < 5:
        print(f"    Not enough food to cook!")
        return
    
    bonus = skill // 20
    food_made = 4 + bonus
    
    roll = random.random()
    if roll < 0.3 + (bonus * 0.1):
        game.food -= 3
        game.food += food_made + 3
        quality_name = get_quality_name(skill + random.randint(1, 20))
        print(f"    {quality_name} meal! +{food_made + 3} food")
        
        # Good meal boosts everyone!
        for s in game.survivors:
            s.happiness += 3
            print(f"    Everyone feels better!")
    else:
        game.food -= 3
        game.food += food_made
        print(f"    Cooked: +{food_made} food")

def do_guard(survivor, game):
    quality_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Combat"] + quality_mod
    
    print(f"\n  {survivor.name} stands guard...")
    
    encounter = 0.2
    if game.weather == "Fog": encounter = 0.35
    elif game.weather == "Storm": encounter = 0.1
    
    if random.random() < encounter:
        enemy = random.choice(["wolf", "zombie", "raider", "zombie dog"])
        print(f"    ENEMY! A {enemy} approaches!")
        
        roll = skill + random.randint(1, 100)
        
        if roll > 60:
            print(f"    {survivor.name} defeated the {enemy}!")
            survivor.happiness += 5
            if random.random() < 0.3:
                loot = random.choice(["ammo", "medicine", "food"])
                add_item(loot, game, 1)
                print(f"    Looted: {loot}")
        else:
            damage = random.randint(10, 25)
            survivor.health -= damage
            survivor.happiness -= 10
            print(f"    {survivor.name} took {damage} damage!")
    else:
        print(f"    Quiet night. All clear.")

# ==================== HELPERS ====================

def add_item(item, game, amount=1):
    if item == "food": game.food += amount * random.randint(2, 5)
    elif item == "materials": game.materials += amount * random.randint(1, 3)
    elif item == "scrap": game.scrap += amount * random.randint(2, 5)
    elif item == "medicine": game.medicine += amount
    elif item == "ammo": game.ammo += amount * random.randint(1, 3)
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
        print("GAME OVER - Everyone has perished!")
        return True
    return False

def mood_contagion(game):
    """Spread moods between characters"""
    for s in game.survivors:
        if not s.is_alive: continue
        for other in game.survivors:
            if s == other or not other.is_alive: continue
            
            # Get other's influence
            influence = other.get_mood_contagion()
            resistance = s.get_contagion_resistance()
            
            if influence != 0:
                s.happiness += int(influence * resistance * 0.5)

def daily_mood_natural_change(game):
    """Apply daily mood changes from traits"""
    for s in game.survivors:
        if not s.is_alive: continue
        
        # Base change from traits
        change = s.get_daily_base_change()
        
        # Weather effects based on traits
        if game.weather == "Rain":
            if "Pessimist" in s.traits: change -= 2
            elif "Optimist" in s.traits: change += 0  # Doesn't affect them much
        elif game.weather == "Clear":
            if "Optimist" in s.traits: change += 2
        
        s.happiness += change

def print_status(game):
    print(f"\n{'='*60}")
    print(f"DAY {game.day} - {game.season} - {game.weather} {game.temperature}F")
    print(f"{'='*60}")
    print(f"\nRESOURCES:")
    print(f"  Food: {game.food}  Water: {game.water}  Scrap: {game.scrap}")
    print(f"  Materials: {game.materials}  Medicine: {game.medicine}  Ammo: {game.ammo}")
    
    print(f"\nBUILDINGS: {', '.join([f'{k}(v{v})' for k,v in game.buildings.items()])}")
    print(f"BOOKS: {', '.join(game.books) if game.books else 'None'}")
    
    print(f"\nSURVIVORS ({len(game.survivors)}/{game.population_cap}):")
    print("-" * 50)
    for s in game.survivors:
        if s.health > 0:
            q = s.get_quality_modifier()
            q_str = "++" if q > 5 else "+" if q > 0 else "--" if q < -5 else "-" if q < 0 else ""
            traits = ", ".join(s.traits[:2])  # Show first 2 traits
            print(f"  {s.name}: {s.job} | HP:{s.health} HAPP:{s.happiness} Q:{q:+d}{q_str}")
            print(f"    Traits: {traits}")

def get_job_choice(survivor):
    jobs = [("1", "Scavenge"), ("2", "Hunt"), ("3", "Gather"), ("4", "Farm"),
            ("5", "Build"), ("6", "Cook"), ("7", "Rest"), ("8", "Guard")]
    skill_map = {"1": "Scavenging", "2": "Hunting", "3": "Gathering", "4": "Farming",
                 "5": "Building", "6": "Cooking", "7": "Rest", "8": "Combat"}
    
    print(f"\n{survivor.name}'s skills:")
    for num, job in jobs:
        skill = survivor.skills.get(skill_map[num], 10)
        q_mod = survivor.get_quality_modifier()
        print(f"  {num}: {job} (Skill:{skill} Quality:{q_mod:+d})")
    
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
    print("         OUTPOST ZERO v3.0")
    print("   Mood, Quality & Traits System")
    print("="*60)
    print()
    
    game = Game()
    game.survivors = create_starting_characters()
    
    print("Your group of 4 survivors has settled.")
    print("Each has unique traits affecting work quality!")
    print("Watch the Q: marker - that's work quality!")
    print()
    
    while not game.game_over:
        game.update_season()
        game.update_weather()
        
        print_status(game)
        
        # Mood contagion from previous day
        mood_contagion(game)
        
        # Daily natural mood change
        daily_mood_natural_change(game)
        
        if game.food < len(game.survivors) * 2:
            print(f"\n⚠️ LOW FOOD! Need {len(game.survivors) * 2} per day!")
        
        print("\n" + "-"*40)
        print("ASSIGN TASKS")
        print("-"*40)
        
        for survivor in game.survivors:
            if survivor.health <= 0: continue
            
            task, skill = get_job_choice(survivor)
            survivor.job = task
            
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
            
            if survivor.health <= 0:
                print(f"\n💀 {survivor.name} has died!")
                survivor.is_alive = False
                for s in game.survivors:
                    if s != survivor and s.is_alive:
                        s.happiness -= 15
        
        # Eat
        alive = len([s for s in game.survivors if s.is_alive and s.health > 0])
        food_needed = alive * 2
        game.food -= food_needed
        print(f"\n\nSurvivors ate {food_needed} food.")
        
        # Night events
        print("\n" + "-"*40)
        print("NIGHT EVENTS")
        print("-"*40)
        
        roll = random.randint(1, 100)
        
        if roll < 5:
            print("A survivor had a nightmare!")
            v = random.choice([s for s in game.survivors if s.is_alive])
            v.happiness -= 10
        elif roll < 10:
            print("Found hidden stashes!")
            game.food += random.randint(3, 8)
        elif roll < 15:
            print("Someone got sick!")
            v = random.choice([s for s in game.survivors if s.is_alive])
            v.sickness = random.choice(["Cold", "Flu"])
            v.health -= 15
        elif roll < 20:
            print("Good weather! Everyone rested well.")
            for s in game.survivors:
                if s.is_alive: s.happiness += 5
        
        # Weather effects
        if game.weather == "Storm":
            print("A storm rages!")
            for s in game.survivors:
                if s.is_alive: s.happiness -= 5
        if game.temperature < 32:
            print("Freezing! Need warmth!")
            for s in game.survivors:
                if s.is_alive and s.job == "Guard":
                    s.health -= 5
        
        # Clamp happiness
        for s in game.survivors:
            if s.is_alive:
                s.happiness = max(-100, min(100, s.happiness))
        
        # Remove dead
        game.survivors = [s for s in game.survivors if s.is_alive]
        
        game.day += 1
        
        if check_game_over(game):
            game.game_over = True
        
        if not game.game_over:
            cont = input("\nPress Enter for next day (q to quit): ")
            if cont.lower() == 'q':
                print("\nGoodbye!")
                break
    
    print("\n" + "="*50)
    print(f"GAME OVER - Survived {game.day} days!")
    print("="*50)

if __name__ == "__main__":
    main()
