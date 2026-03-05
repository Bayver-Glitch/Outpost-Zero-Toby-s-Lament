"""
OUTPOST ZERO - Colony Survival Sim
VERSION 4.0 - Tools, Professions, New Stats
"""

import random

# ==================== DIFFICULTY ====================

DIFFICULTY = "normal"  # easy, normal, hard

# ==================== TRAITS ====================

POSITIVE_TRAITS = {
    # Moral
    "Honest": {"category": "moral", "effect": {"relationship_trust": 20}},
    "Generous": {"category": "moral", "effect": {"gift_events": True}},
    "Kind": {"category": "moral", "effect": {"nearby_happiness": 5}},
    "Fair": {"category": "moral", "effect": {"reputation_order": 10}},
    "Loyal": {"category": "moral", "effect": {"betrayal_chance": 0}},
    # Emotional
    "Optimist": {"category": "emotional", "effect": {"negative_event_mod": -1}},
    "Cheerful": {"category": "emotional", "effect": {"daily_happiness": 5}},
    "Calm": {"category": "emotional", "effect": {"stress_from_events": 0.75}},
    "Empathetic": {"category": "emotional", "effect": {"mood_contagion": 1.25}},
    "Resilient": {"category": "emotional", "effect": {"stress_recovery": 1.5}},
    # Social
    "Charismatic": {"category": "social", "effect": {"new_relationship": 25}},
    "Tactful": {"category": "social", "effect": {"relationship_damage": 0.5}},
    "Reliable": {"category": "social", "effect": {"task_completion": 1.20}},
    "Humble": {"category": "social", "effect": {"accepts_help": True}},
    # Work
    "Diligent": {"category": "work", "effect": {"work_output": 1.15}},
    "Disciplined": {"category": "work", "effect": {"stamina_use": 0.75}},
    "Perseverant": {"category": "work", "effect": {"never_gives_up": True}},
    "Creative": {"category": "work", "effect": {"special_discovery": 10}},
    "Enthusiastic": {"category": "work", "effect": {"interested_work_quality": 1.10}},
    # Combat
    "Courageous": {"category": "combat", "effect": {"combat_damage": 1.20}},
    "Tactical": {"category": "combat", "effect": {"combat_advantage": 15}},
    "Stealthy": {"category": "combat", "effect": {"sneak_success": 25}},
    "Protective": {"category": "combat", "effect": {"ally_defense": 15}},
    "Vigilant": {"category": "combat", "effect": {"danger_detection": 25}},
    # Health
    "Tough": {"category": "health", "effect": {"damage_taken": 0.75}},
    "Fast Healer": {"category": "health", "effect": {"healing_rate": 2.0}},
    "Pain Resistant": {"category": "health", "effect": {"pain_effects": 0.5}},
    "Athletic": {"category": "health", "effect": {"stamina": 1.15}},
    "Healthy": {"category": "health", "effect": {"illness_chance": 0.5}},
}

NEGATIVE_TRAITS = {
    # Moral
    "Dishonest": {"category": "moral", "effect": {"relationship_trust": -20}},
    "Selfish": {"category": "moral", "effect": {"share_chance": 0}},
    "Cruel": {"category": "moral", "effect": {"nearby_happiness": -5}},
    "Vindictive": {"category": "moral", "effect": {"forgiveness": 0}},
    # Emotional
    "Pessimist": {"category": "emotional", "effect": {"negative_event_mod": 1}},
    "Melancholic": {"category": "emotional", "effect": {"daily_happiness": -3}},
    "Anxious": {"category": "emotional", "effect": {"stress_from_events": 1.5}},
    "Moody": {"category": "emotional", "effect": {"happiness_volatility": 1.5}},
    "Irritable": {"category": "emotional", "effect": {"mood_contagion": 1.25}},
    # Social
    "Arrogant": {"category": "social", "effect": {"rejects_help": True}},
    "Rude": {"category": "social", "effect": {"relationship_damage": 1.25}},
    "Selfish": {"category": "social", "effect": {"share_chance": 0}},
    "Cynical": {"category": "social", "effect": {"new_relationship": -15}},
    "Stubborn": {"category": "social", "effect": {"accepts_advice": False}},
    # Work
    "Lazy": {"category": "work", "effect": {"work_output": 0.75}},
    "Slacker": {"category": "work", "effect": {"task_completion": 0.75}},
    "Procrastinator": {"category": "work", "effect": {"work_efficiency": 0.85}},
    "Careless": {"category": "work", "effect": {"accident_chance": 1.5}},
    "Unmotivated": {"category": "work", "effect": {"voluntary_work": False}},
    # Combat
    "Cowardly": {"category": "combat", "effect": {"combat_damage": 0.75}},
    "Reckless": {"category": "combat", "effect": {"self_damage": 1.5}},
    "Aggressive": {"category": "combat", "effect": {"friendly_fire": 1.5}},
    # Health
    "Fragile": {"category": "health", "effect": {"damage_taken": 1.25}},
    "Sickly": {"category": "health", "effect": {"illness_chance": 1.5}},
    "Slow Healer": {"category": "health", "effect": {"healing_rate": 0.5}},
    # Intellect
    "Naive": {"category": "intellect", "effect": {"deception_vulnerability": 1.5}},
    "Forgetful": {"category": "intellect", "effect": {"skill_decay": 1.25}},
    "Slow": {"category": "intellect", "effect": {"learning_speed": 0.75}},
}

# Skill-specific traits
SKILL_TRAITS = {
    "Farming": ["Green Thumb", "Farm Hand", "Botanist", "Harvest King"],
    "Cooking": ["Chef's Kiss", "Spice Master", "Preserver", "Baker"],
    "Scavenging": ["Scavenger", "Looter", "Quick Hands", "Expert Finder"],
    "Hunting": ["Marksman", "Tracker", "Trapper", "Beastmaster"],
    "Combat": ["Warrior", "Fighter", "Brawler", "Berserker"],
    "Medical": ["Healer", "Surgeon", "Medic", "Herbalist"],
    "Building": ["Builder", "Architect", "Craftsman", "Efficient"],
    "Fishing": ["Angler", "Fisherman", "Patient", "Net Caster"],
    "Gathering": ["Forager", "Gatherer", "Herbalist", "Hunter"],
}

# ==================== TOOLS ====================

TOOLS = {
    "tier_1": {
        "Basic Hoe": {"skill": "Farming", "bonus": 15},
        "Basic Rake": {"skill": "Farming", "bonus": 15},
        "Hand Axe": {"skill": "Woodcutting", "bonus": 15},
        "Pickaxe": {"skill": "Mining", "bonus": 20},
        "Shovel": {"skill": "Digging", "bonus": 15},
        "Hammer": {"skill": "Building", "bonus": 15},
        "Saw": {"skill": "Carpentry", "bonus": 20},
        "Knife": {"skill": "Skinning", "bonus": 15},
    },
    "tier_2": {
        "Quality Hoe": {"skill": "Farming", "bonus": 30},
        "Quality Axe": {"skill": "Woodcutting", "bonus": 30},
        "Crosscut Saw": {"skill": "Carpentry", "bonus": 35},
        "Anvil": {"skill": "Blacksmithing", "bonus": 40},
        "Forge Hammer": {"skill": "Blacksmithing", "bonus": 35},
    },
    "tier_3": {
        "Medical Kit": {"skill": "Medical", "bonus": 35},
        "Surgical Kit": {"skill": "Medical", "bonus": 50},
    },
}

# ==================== BUILDINGS: TECH 1 ====================

TECH_1_BUILDINGS = {
    # Shelter
    "Lean-to": {"cost": {"scrap": 5, "wood": 10}, "comfort": 2},
    "Scrap Hut": {"cost": {"scrap": 10, "wood": 5}, "comfort": 5},
    "Shared Quarters": {"cost": {"scrap": 10, "wood": 15, "cloth": 2}, "comfort": 5, "capacity": 4},
    # Food
    "Basic Garden": {"cost": {"wood": 5}, "produces": "food"},
    "Smokehouse": {"cost": {"scrap": 5, "wood": 15, "stone": 5}, "produces": "preserve"},
    "Root Cellar": {"cost": {"wood": 10}, "produces": "storage_food"},
    "Basic Kitchen": {"cost": {"scrap": 10, "wood": 10}, "produces": "cooking"},
    "Outdoor Fire Pit": {"cost": {"stone": 5, "wood": 5}, "produces": "cooking"},
    # Water
    "Rain Barrel": {"cost": {"scrap": 3}, "produces": "water"},
    "Dirty Well": {"cost": {"stone": 10}, "produces": "water"},
    "Boiling Station": {"cost": {"stone": 5}, "produces": "water_purify"},
    "Water Storage": {"cost": {"scrap": 5}, "produces": "water_storage"},
    # Defense
    "Scrap Wall": {"cost": {"scrap": 10}, "hp": 20},
    "Wooden Picket": {"cost": {"wood": 10}, "hp": 15},
    "Scrap Gate": {"cost": {"scrap": 15, "wood": 5}, "hp": 15},
    "Makeshift Tower": {"cost": {"scrap": 15, "wood": 10}, "hp": 25, "bonus": "spotting"},
    # Storage
    "Scrap Storage": {"cost": {"scrap": 10}, "slots": 20},
    "Wooden Crate": {"cost": {"wood": 8}, "slots": 10},
    # Workshop
    "Basic Workbench": {"cost": {"scrap": 5, "wood": 10}, "produces": "crafting"},
    # Medical
    "First Aid Corner": {"cost": {"wood": 5}, "produces": "healing"},
    "Sick Bay": {"cost": {"scrap": 5, "wood": 10, "cloth": 3}, "produces": "healing"},
    # Animals
    "Open Pen": {"cost": {"wood": 15}, "produces": "animals"},
    # Recreation
    "Fire Circle": {"cost": {"stone": 10}, "produces": "morale"},
}

# ==================== GAME STATE ====================

class Game:
    def __init__(self):
        self.day = 1
        self.season = "Spring"
        self.weather = "Clear"
        self.temperature = 65
        
        # Resources
        self.food = 30
        self.water = 20
        self.scrap = 30
        self.wood = 20
        self.stone = 10
        self.cloth = 5
        self.medicine = 2
        self.ammo = 5
        self.books = ["Gardening Basics"]
        
        # Tools inventory
        self.tools = ["Hand Axe", "Knife"]  # Starting tools
        
        # Buildings
        self.buildings = {
            "Lean-to": 1,
            "Scrap Hut": 1,
            "Shared Quarters": 1,
            "Basic Garden": 1,
            "Outdoor Fire Pit": 1,
            "Scrap Storage": 1,
            "Scrap Wall": 2,
            "Scrap Gate": 1,
        }
        
        self.survivors = []
        self.game_over = False
        self.population_cap = 10
    
    def update_weather(self):
        temps = {"Spring": (45, 70), "Summer": (60, 85), "Fall": (35, 60), "Winter": (10, 35)}
        self.temperature = random.randint(*temps[self.season])
        self.weather = random.choices(
            ["Clear", "Cloudy", "Rain", "Cold", "Storm", "Fog"],
            weights=[50, 15, 10, 8, 4, 3]
        )[0]
    
    def update_season(self):
        if (self.day - 1) % 30 == 0 and self.day > 1:
            seasons = ["Spring", "Summer", "Fall", "Winter"]
            self.season = seasons[(seasons.index(self.season) + 1) % 4]

# ==================== SURVIVOR ====================

class Survivor:
    def __init__(self, name, profession, age=30):
        self.name = name
        self.age = age
        self.profession = profession
        
        # New Stats (50-150)
        if DIFFICULTY == "easy":
            self.intellect = random.randint(80, 130)
            self.stamina = random.randint(80, 130)
            self.charisma = random.randint(80, 130)
            self.health_max = random.randint(80, 130)
        elif DIFFICULTY == "hard":
            self.intellect = random.randint(50, 120)
            self.stamina = random.randint(50, 120)
            self.charisma = random.randint(50, 120)
            self.health_max = random.randint(50, 120)
        else:
            self.intellect = random.randint(70, 130)
            self.stamina = random.randint(70, 130)
            self.charisma = random.randint(70, 130)
            self.health_max = random.randint(70, 130)
        
        self.health = self.health_max
        self.happiness = 50
        
        # Skills
        self.skills = self.get_profession_skills(profession)
        
        # Traits
        self.traits = []
        self.skill_traits = []  # Skill-specific traits
        self.assign_traits()
        
        # Job
        self.job = "Unassigned"
        
        # Status
        self.injuries = []
        self.sickness = None
        self.is_alive = True
    
    def get_profession_skills(self, profession):
        base = {
            "Scavenger": {"Scavenging": 30, "Gathering": 20, "Combat": 15},
            "Hunter": {"Hunting": 35, "Tracking": 25, "Combat": 20},
            "Farmer": {"Farming": 30, "Gathering": 15, "Building": 10},
            "Builder": {"Building": 35, "Carpentry": 25, "Crafting": 15},
            "Blacksmith": {"Blacksmithing": 30, "Crafting": 20, "Building": 15},
            "Cook": {"Cooking": 35, "Preserving": 20, "Farming": 10},
            "Doctor": {"Medical": 35, "First Aid": 25, "Herbalism": 15},
            "Gatherer": {"Gathering": 35, "Herbalism": 25, "Farming": 15},
            "Guard": {"Combat": 35, "Vigilance": 25, "First Aid": 10},
            "Carpenter": {"Carpentry": 35, "Building": 25, "Crafting": 15},
        }
        skills = base.get(profession, {"General": 20})
        # Add some randomness
        for s in skills:
            skills[s] += random.randint(-5, 10)
        return skills
    
    def assign_traits(self):
        # Get available traits based on difficulty
        pos_options = list(POSITIVE_TRAITS.keys())
        neg_options = list(NEGATIVE_TRAITS.keys())
        
        if DIFFICULTY == "easy":
            # 2 good + 1 minor bad
            self.traits = random.sample(pos_options, 2)
            minor_bad = ["Lazy", "Forgetful", "Clumsy", "Flaky", "Modest"]
            self.traits.append(random.choice(minor_bad))
        elif DIFFICULTY == "hard":
            # 1 good + 2 bad
            self.traits = [random.choice(pos_options)]
            self.traits.extend(random.sample(neg_options, 2))
        else:
            # Normal: 1 good + 1 bad
            self.traits = [random.choice(pos_options), random.choice(neg_options)]
        
        # Skill-specific trait (50% chance normal, 75% easy, 25% hard)
        chance = {"easy": 0.75, "normal": 0.50, "hard": 0.25}[DIFFICULTY]
        if random.random() < chance:
            prof = self.profession
            if prof in SKILL_TRAITS:
                self.skill_traits = [random.choice(SKILL_TRAITS[prof])]
    
    def get_trait_effect(self, effect_name):
        total = 0
        for trait in self.traits:
            if trait in POSITIVE_TRAITS:
                e = POSITIVE_TRAITS[trait]["effect"]
                if effect_name in e:
                    total += e[effect_name]
            if trait in NEGATIVE_TRAITS:
                e = NEGATIVE_TRAITS[trait]["effect"]
                if effect_name in e:
                    total += e[effect_name]
        return total
    
    def get_quality_modifier(self):
        mood = self.happiness
        if mood > 70: q = 10
        elif mood > 50: q = 5
        elif mood > 30: q = -5
        elif mood > 10: q = -10
        else: q = -15
        q += self.get_trait_effect("work_output")
        return max(-20, min(20, q))
    
    def get_daily_happiness_change(self):
        change = 0
        change += self.get_trait_effect("daily_happiness")
        return max(-10, min(10, change))
    
    def __str__(self):
        mood = "+" if self.happiness > 60 else "=" if self.happiness > 40 else "-"
        q = self.get_quality_modifier()
        q_str = "++" if q > 5 else "+" if q > 0 else "--" if q < -5 else "-" if q < 0 else ""
        traits = ", ".join(self.traits[:2])
        return f"{self.name}: {self.profession} | HP:{self.health} HAPP:{self.happiness}{mood} Q:{q:+d}{q_str}"

# ==================== CREATE SURVIVORS ====================

def create_starting_survivors():
    survivors = [
        Survivor("Marcus", "Builder", 34),
        Survivor("Sarah", "Hunter", 28),
        Survivor("Ryan", "Scavenger", 42),
        Survivor("Elena", "Farmer", 24),
        Survivor("Carlos", "Blacksmith", 38),
        Survivor("Maria", "Cook", 35),
    ]
    
    # Give some starting happiness
    for s in survivors:
        s.happiness = random.randint(45, 70)
    
    return survivors

# ==================== ACTIONS ====================

def do_scavenge(survivor, game):
    tool_bonus = 0
    for tool in game.tools:
        if tool in TOOLS.get("tier_1", {}):
            if TOOLS["tier_1"][tool]["skill"] == "Scavenging":
                tool_bonus += TOOLS["tier_1"][tool]["bonus"]
    
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills.get("Scavenging", 10) + q_mod + tool_bonus
    roll = random.randint(1, 100)
    result = skill + roll
    
    print(f"\n  {survivor.name} scavenges...")
    
    if result > 100:
        found = random.sample(["food", "wood", "scrap", "stone", "cloth", "medicine"], 3)
        for item in found:
            add_item(item, game, 1)
        print(f"    AMAZING! Found: {', '.join(found)}")
    elif result > 70:
        found = random.sample(["food", "wood", "scrap", "stone"], 2)
        for item in found: add_item(item, game, 1)
        print(f"    Good: {', '.join(found)}")
    elif result > 40:
        add_item(random.choice(["food", "wood", "scrap"]), game, 1)
        print(f"    Found something.")
    else:
        print(f"    Nothing.")

def do_hunt(survivor, game):
    tool_bonus = 0
    for tool in game.tools:
        if tool in TOOLS.get("tier_1", {}):
            if TOOLS["tier_1"][tool]["skill"] == "Hunting":
                tool_bonus += TOOLS["tier_1"][tool]["bonus"]
    
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills.get("Hunting", 10) + q_mod + tool_bonus
    result = skill + random.randint(1, 100)
    
    print(f"\n  {survivor.name} hunts...")
    if game.weather == "Rain": result -= 30
    
    if result > 80: game.food += 15; print(f"    Big deer! +15 food")
    elif result > 50: game.food += 8; print(f"    Rabbit! +8 food")
    elif result > 30: game.food += 4; print(f"    Small catch.")
    else: print(f"    No luck.")

def do_farm(survivor, game):
    tool_bonus = 0
    for tool in game.tools:
        if tool in TOOLS.get("tier_1", {}):
            if TOOLS["tier_1"][tool]["skill"] == "Farming":
                tool_bonus += TOOLS["tier_1"][tool]["bonus"]
    
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills.get("Farming", 10) + q_mod + tool_bonus
    result = skill + random.randint(1, 100)
    
    print(f"\n  {survivor.name} farms...")
    
    if "Basic Garden" not in game.buildings:
        print(f"    No garden! Need to build one.")
        return
    
    if result > 60:
        game.food += random.randint(5, 12)
        print(f"    Good harvest!")
    elif result > 30:
        game.food += random.randint(2, 5)
        print(f"    Harvest.")
    else:
        print(f"    Poor harvest.")

def do_build(survivor, game):
    tool_bonus = 0
    for tool in game.tools:
        if tool in TOOLS.get("tier_1", {}):
            if TOOLS["tier_1"][tool]["skill"] == "Building":
                tool_bonus += TOOLS["tier_1"][tool]["bonus"]
    
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills.get("Building", 10) + q_mod + tool_bonus
    
    print(f"\n  {survivor.name} builds...")
    
    # List available buildings
    available = [b for b in TECH_1_BUILDINGS if b not in game.buildings]
    if not available:
        print(f"    All buildings built!")
        return
    
    # Try to build
    result = skill + random.randint(1, 100)
    if result > 50 and game.scrap >= 5 and game.wood >= 5:
        building = random.choice(available[:5])
        cost = TECH_1_BUILDINGS[building]["cost"]
        
        can_afford = True
        for res, amt in cost.items():
            if res == "scrap" and game.scrap < amt: can_afford = False
            elif res == "wood" and game.wood < amt: can_afford = False
            elif res == "stone" and game.stone < amt: can_afford = False
            elif res == "cloth" and game.cloth < amt: can_afford = False
        
        if can_afford:
            for res, amt in cost.items():
                if res == "scrap": game.scrap -= amt
                elif res == "wood": game.wood -= amt
                elif res == "stone": game.stone -= amt
                elif res == "cloth": game.cloth -= amt
            
            game.buildings[building] = game.buildings.get(building, 0) + 1
            print(f"    Built {building}!")
        else:
            print(f"    Can't afford {building}!")
    else:
        print(f"    Made progress.")

def do_cook(survivor, game):
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills.get("Cooking", 10) + q_mod
    
    print(f"\n  {survivor.name} cooks...")
    
    if game.food < 5:
        print(f"    No food!")
        return
    
    if random.random() < 0.3:
        game.food += 4
        print(f"    Good meal!")
        for s in game.survivors: s.happiness += 3
    else:
        game.food += 3
        print(f"    Cooked.")

def do_gather(survivor, game):
    tool_bonus = 0
    skill = survivor.skills.get("Gathering", 10) + survivor.get_quality_modifier() + tool_bonus
    result = skill + random.randint(1, 100)
    
    print(f"\n  {survivor.name} gathers...")
    
    finds = []
    for _ in range(3):
        if result + random.randint(1, 50) > 40:
            finds.append(random.choice(["berries", "wood", "herbs", "mushrooms"]))
    
    if finds:
        for item in finds:
            if item in ["berries", "mushrooms"]: game.food += 2
            elif item == "wood": game.wood += 3
            elif item == "herbs": game.medicine += 1
        print(f"    Found: {', '.join(finds)}")
    else:
        print(f"    Nothing.")

def do_rest(survivor, game):
    print(f"\n  {survivor.name} rests...")
    heal = min(20, (100 - survivor.health))
    survivor.health += heal
    survivor.happiness += 5
    print(f"    +{heal} HP, +5 happiness")

def do_guard(survivor, game):
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills.get("Combat", 10) + q_mod
    
    print(f"\n  {survivor.name} guards...")
    
    if random.random() < 0.2:
        print(f"    Enemy!")
        if skill + random.randint(1, 100) > 60:
            print(f"    Defeated!")
            survivor.happiness += 5
        else:
            damage = random.randint(10, 20)
            survivor.health -= damage
            print(f"    Took {damage} damage!")
    else:
        print(f"    Quiet.")

def do_craft(survivor, game):
    """Craft tools"""
    print(f"\n  {survivor.name} crafts...")
    
    # Check for workbench
    if "Basic Workbench" not in game.buildings:
        print(f"    Need workbench!")
        return
    
    # Can craft basic tools if have materials
    if game.scrap >= 5:
        tool = random.choice(["Knife", "Hammer", "Saw"])
        game.scrap -= 5
        game.tools.append(tool)
        print(f"    Crafted {tool}!")
    else:
        print(f"    Need 5 scrap!")

# ==================== HELPERS ====================

def add_item(item, game, amount):
    if item == "food": game.food += amount * random.randint(2, 4)
    elif item == "wood": game.wood += amount * random.randint(2, 4)
    elif item == "scrap": game.scrap += amount * random.randint(2, 4)
    elif item == "stone": game.stone += amount * random.randint(1, 3)
    elif item == "cloth": game.cloth += amount
    elif item == "medicine": game.medicine += amount

def mood_contagion(survivors):
    for s in survivors:
        for other in survivors:
            if s != other and other.is_alive:
                if other.happiness > 70: s.happiness += 1
                elif other.happiness < 30: s.happiness -= 1

# ==================== MAIN ====================

def main():
    print("="*60)
    print("         OUTPOST ZERO v4.0")
    print("   Tools, Professions, New Stats")
    print(f"   Difficulty: {DIFFICULTY.upper()}")
    print("="*60)
    
    game = Game()
    game.survivors = create_starting_survivors()
    
    print("\n6 survivors with professions!")
    print("Tools and stats now matter!")
    print()
    
    while not game.game_over:
        game.update_season()
        game.update_weather()
        
        # Status
        print(f"\n{'='*50}")
        print(f"DAY {game.day} - {game.season} - {game.weather} {game.temperature}F")
        print(f"{'='*50}")
        print(f"FOOD: {game.food} | WATER: {game.water}")
        print(f"WOOD: {game.wood} | STONE: {game.stone} | SCRAP: {game.scrap}")
        print(f"TOOLS: {', '.join(game.tools)}")
        
        print(f"\nBUILDINGS: {', '.join([f'{k}(v{v})' for k,v in game.buildings.items()])}")
        
        print(f"\nSURVIVORS ({len(game.survivors)}):")
        for s in game.survivors:
            if s.is_alive:
                print(f"  {s}")
        
        # Mood contagion
        mood_contagion(game.survivors)
        
        # Assign jobs
        print("\n" + "-"*40)
        print("ASSIGN TASKS")
        print("-"*40)
        
        jobs = [("1", "Scavenge"), ("2", "Hunt"), ("3", "Farm"), ("4", "Build"),
                ("5", "Gather"), ("6", "Cook"), ("7", "Rest"), ("8", "Guard"), ("9", "Craft Tools")]
        
        for survivor in game.survivors:
            if survivor.health <= 0: continue
            
            print(f"\n{survivor.name} ({survivor.profession}):")
            print(f"  Stats: INT:{survivor.intellect} STA:{survivor.stamina} CHA:{survivor.charisma} HP:{survivor.health_max}")
            
            for num, job in jobs:
                print(f"  {num}: {job}")
            
            while True:
                choice = input(f"Task (1-9): ").strip()
                if choice in [n for n, _ in jobs]:
                    survivor.job = jobs[int(choice)-1][1]
                    break
            
            # Do task
            if survivor.job == "Scavenge": do_scavenge(survivor, game)
            elif survivor.job == "Hunt": do_hunt(survivor, game)
            elif survivor.job == "Farm": do_farm(survivor, game)
            elif survivor.job == "Build": do_build(survivor, game)
            elif survivor.job == "Gather": do_gather(survivor, game)
            elif survivor.job == "Cook": do_cook(survivor, game)
            elif survivor.job == "Rest": do_rest(survivor, game)
            elif survivor.job == "Guard": do_guard(survivor, game)
            elif survivor.job == "Craft Tools": do_craft(survivor, game)
            
            if survivor.health <= 0:
                print(f"\n💀 {survivor.name} died!")
                survivor.is_alive = False
        
        # Eat
        alive = len([s for s in game.survivors if s.is_alive])
        game.food -= alive * 2
        print(f"\n\nAte {alive * 2} food.")
        
        # Daily happiness
        for s in game.survivors:
            if s.is_alive:
                s.happiness += s.get_daily_happiness_change()
                s.happiness = max(-100, min(100, s.happiness))
        
        # Night events
        print("\n--- Night ---")
        if random.random() < 0.1:
            print("Good night.")
        
        game.survivors = [s for s in game.survivors if s.is_alive]
        game.day += 1
        
        if game.food <= 0:
            print("\nSTARVATION!")
            game.game_over = True
        
        if not game.game_over:
            if input("\nNext? ").lower() == 'q':
                break
    
    print(f"\nSurvived {game.day} days!")

if __name__ == "__main__":
    main()
