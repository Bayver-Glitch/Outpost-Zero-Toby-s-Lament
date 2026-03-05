"""
OUTPOST ZERO - Colony Survival Sim
VERSION 3.1 - Extended Traits (Positive & Negative)
"""

import random
import time

# ==================== TRAIT DATABASE ====================

# Positive traits: (name, category, effect_description, stat_bonuses)
POSITIVE_TRAITS = {
    # Moral
    "Honesty": ("moral", "Trustworthy", {"relationship_trust": 20}),
    "Integrity": ("moral", "Principled", {"reputation_good": 10}),
    "Kindness": ("moral", "Compassionate", {"nearby_happiness": 5}),
    "Generosity": ("moral", "Giving", {"gift_events": True}),
    "Fairness": ("moral", "Just", {"reputation_order": 10}),
    "Forgiveness": ("moral", "Understanding", {"betrayal_recovery": 1.5}),
    
    # Emotional
    "Optimist": ("emotional", "Hopeful", {"negative_event_mod": -1}),
    "Resilient": ("emotional", "Tough-minded", {"stress_recovery": 1.5}),
    "Joyfulness": ("emotional", "Cheerful", {"daily_happiness": 5}),
    "Empathetic": ("emotional", "Understanding", {"mood_contagion": 1.25}),
    "Compassionate": ("emotional", "Caring", {"heal_events": True}),
    "Calm": ("emotional", "Level-headed", {"stress_from_events": 0.75}),
    
    # Social
    "Loyal": ("social", "Faithful", {"betrayal_chance": 0}),
    "Charismatic": ("social", "Charming", {"new_relationship": 25}),
    "Tactful": ("social", "Diplomatic", {"relationship_damage": 0.5}),
    "Open-Minded": ("social", "Accepting", {"learning_speed": 1.25}),
    "Humble": ("social", "Modest", {"accepts_help": True}),
    "Reliable": ("social", "Dependable", {"task_completion": 1.20}),
    
    # Work Ethic
    "Diligent": ("work", "Hardworking", {"work_output": 1.15}),
    "Disciplined": ("work", "Focused", {"stamina_use": 0.75}),
    "Perseverant": ("work", "Persistent", {"never_gives_up": True}),
    "Creative": ("work", "Innovative", {"special_discovery": 10}),
    "Enthusiastic": ("work", "Passionate", {"interested_work_quality": 1.10}),
    "Resourceful": ("work", "Clever", {"problem_solving": 15}),
    
    # Combat
    "Courageous": ("combat", "Brave", {"combat_damage": 1.20}),
    "Tactical": ("combat", "Strategic", {"combat_advantage": 15}),
    "Stealthy": ("combat", "Sneaky", {"sneak_success": 25}),
    "Protective": ("combat", "Defensive", {"ally_defense": 15}),
    "Vigilant": ("combat", "Alert", {"danger_detection": 25}),
    "Daring": ("combat", "Bold", {"risk_success": 15}),
    
    # Health
    "Tough": ("health", "Hardy", {"damage_taken": 0.75}),
    "Fast Healer": ("health", "Quick Recovery", {"healing_rate": 2.0}),
    "Pain Resistant": ("health", "Stoic", {"pain_effects": 0.5}),
    "Athletic": ("health", "Fit", {"stamina": 1.15}),
    "Healthy": ("health", "Robust", {"illness_chance": 0.5}),
    "Enduring": ("health", "Stamina", {"stamina_cap": 1.20}),
    
    # Intellect
    "Wise": ("intellect", "Judicious", {"learn_from_mistakes": 1.25}),
    "Curious": ("intellect", "Inquisitive", {"exploration_yield": 1.25}),
    "Intelligent": ("intellect", "Smart", {"skill_gain": 1.20}),
    "Adaptable": ("intellect", "Flexible", {"new_situation": 1.25}),
    "Focused": ("intellect", "Concentrated", {"distraction": 0.5}),
    "Knowledgeable": ("intellect", "Learned", {"teaching_efficiency": 1.25}),
    
    # Social Flaws (actually positive)
    "Modest": ("social", "Humble", {"arrogance_check": True}),
}

# Negative traits: (name, category, effect_description, stat_penalties)
NEGATIVE_TRAITS = {
    # Moral
    "Dishonest": ("moral", "Deceptive", {"relationship_trust": -20}),
    "Manipulative": ("moral", "Scheming", {"deception_success": 20}),
    "Cruel": ("moral", "Callous", {"nearby_happiness": -5}),
    "Vindictive": ("moral", "revengeful", {"forgiveness": 0}),
    "Hypocritical": ("moral", "Two-faced", {"trust_decay": 1.5}),
    "Ingrateful": ("moral", "Unthankful", {"gift_happiness": -5}),
    
    # Emotional
    "Pessimist": ("emotional", "Negative", {"negative_event_mod": 1}),
    "Melancholic": ("emotional", "Sad", {"daily_happiness": -3}),
    "Anxious": ("emotional", "Worried", {"stress_from_events": 1.5}),
    "Irritable": ("emotional", "Short-fused", {"mood_contagion": 1.25}),
    "Nervous": ("emotional", "Jumpy", {"calm_check_fail": True}),
    "Moody": ("emotional", "Unpredictable", {"happiness_volatility": 1.5}),
    
    # Social
    "Arrogant": ("social", "Conceited", {"rejects_help": True}),
    "Rude": ("social", "Impolite", {"relationship_damage": 1.25}),
    "Selfish": ("social", "Self-centered", {"share_chance": 0}),
    "Stubborn": ("social", "Obstinate", {"accepts_advice": False}),
    "Cynical": ("social", "Distrustful", {"new_relationship": -15}),
    "Dismissive": ("social", "Dismissive", {"teaching_accept": 0.5}),
    
    # Work Ethic
    "Lazy": ("work", "Idle", {"work_output": 0.75}),
    "Slacker": ("work", "Unreliable", {"task_completion": 0.75}),
    "Procrastinator": ("work", "Delayer", {"work_efficiency": 0.85}),
    "Impulsive": ("work", "Hasty", {"mistake_chance": 1.25}),
    "Careless": ("work", "Negligent", {"accident_chance": 1.5}),
    "Unmotivated": ("work", "Listless", {"voluntary_work": False}),
    
    # Combat
    "Cowardly": ("combat", "Fearful", {"combat_damage": 0.75}),
    "Reckless": ("combat", "Careless", {"self_damage": 1.5}),
    "Aggressive": ("combat", "Hostile", {"friendly_fire": 1.5}),
    "Hesitant": ("combat", "Indecisive", {"missed_attacks": 1.25}),
    "Panicky": ("combat", "Frightened", {"retreat_chance": 1.5}),
    
    # Health
    "Fragile": ("health", "Frail", {"damage_taken": 1.25}),
    "Slow Healer": ("health", "Poor Recovery", {"healing_rate": 0.5}),
    "Sickly": ("health", "Ailing", {"illness_chance": 1.5}),
    "Allergic": ("health", "Reactive", {"allergy_events": True}),
    "Addicted": ("health", "Dependent", {"withdrawal_effects": True}),
    "Claustrophobic": ("health", "Crowd-fearing", {"stress_in_crowds": 1.5}),
    
    # Intellect
    "Naive": ("intellect", "Gullible", {"deception_vulnerability": 1.5}),
    "Forgetful": ("intellect", "Absent-minded", {"skill_decay": 1.25}),
    "Slow": ("intellect", "Dim", {"learning_speed": 0.75}),
    "Obsessed": ("intellect", "Fixated", {"balanced_judgment": False}),
    "Narrow-Minded": ("intellect", "Closed", {"new_idea_acceptance": 0.5}),
    "Confused": ("intellect", "Bewildered", {"decision_quality": 0.75}),
    
    # Other Flaws
    "Envious": ("flaw", "Jealous", {"jealousy_events": True}),
    "Greedy": ("flaw", "Acquisitive", {"hoarding": True}),
    "Jealous": ("flaw", "Resentful", {"happy_nearby_sad": True}),
    "Wrathful": ("flaw", "Angry", {"anger_events": True}),
    "Prideful": ("flaw", "Haughty", {"accepts_criticism": False}),
    "Lustful": ("flaw", "Obsessed", {"romance_distraction": True}),
    "Gluttonous": ("flaw", "Overeater", {"food_consumption": 1.5}),
    "Flaky": ("flaw", "Unreliable", {"commitment_keep": 0.5}),
    "Defensive": ("flaw", "Thin-skinned", {"criticism_effect": 1.5}),
    "Indecisive": ("flaw", "Hesitant", {"decision_time": 1.5}),
    "Apathetic": ("flaw", "Unconcerned", {"event_response": 0.5}),
    "Narcissistic": ("flaw", "Self-absorbed", {"self_focus": True}),
}

ALL_TRAITS = {**POSITIVE_TRAITS, **NEGATIVE_TRAITS}

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
        self.reputation = {"good": 0, "order": 0, "wealth": 0, "danger": 0}
        
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
        
        self.job = "Unassigned"
        
        # Traits
        self.traits = []
        self.trait_names = []  # For display
        self.assign_random_traits()
        
        # Relationships
        self.relationships = {}
        
        self.injuries = []
        self.sickness = None
        self.is_alive = True
        
    def assign_random_traits(self):
        """Assign 2-4 random traits"""
        # 1-2 positive traits
        pos_options = list(POSITIVE_TRAITS.keys())
        self.traits.append(random.choice(pos_options))
        if random.random() < 0.5:
            self.traits.append(random.choice(pos_options))
        
        # 1-2 negative traits  
        neg_options = list(NEGATIVE_TRAITS.keys())
        if random.random() < 0.7:  # 70% chance of at least one flaw
            self.traits.append(random.choice(neg_options))
            if random.random() < 0.4:
                self.traits.append(random.choice(neg_options))
        
        self.trait_names = self.traits.copy()
    
    def get_trait_effects(self, effect_type):
        """Get all trait effects of a certain type"""
        total = 0
        for trait in self.traits:
            if trait in ALL_TRAITS:
                cat, desc, effects = ALL_TRAITS[trait]
                if effect_type in effects:
                    total += effects[effect_type]
        return total
    
    def get_quality_modifier(self):
        mood = self.happiness
        if mood > 70: q = 10
        elif mood > 50: q = 5
        elif mood > 30: q = -5
        elif mood > 10: q = -10
        else: q = -15
        
        # Traits modify quality
        q += self.get_trait_effects("work_output")
        q += self.get_trait_effects("quality_bonus")
        
        # Clamp
        return max(-20, min(20, q))
    
    def get_mood_contagion(self):
        if self.happiness > 70: return 2
        elif self.happiness > 50: return 1
        elif self.happiness > 30: return 0
        elif self.happiness > 10: return -1
        else: return -2
    
    def get_contagion_resistance(self):
        resist = 1.0
        resist += self.get_trait_effects("mood_contagion")
        return max(0.25, min(2.0, resist))
    
    def get_daily_base_change(self):
        change = 0
        change += self.get_trait_effects("daily_happiness")
        return max(-10, min(10, change))
    
    def get_event_modifier(self, event_val):
        mod = self.get_trait_effects("negative_event_mod")
        return event_val + mod
    
    def __str__(self):
        mood = "+" if self.happiness > 60 else "=" if self.happiness > 40 else "-"
        q = self.get_quality_modifier()
        quality = "++" if q > 5 else "+" if q > 0 else "--" if q < -5 else "-" if q < 0 else "="
        return f"{self.name} | HP:{self.health} HAPP:{self.happiness}{mood} Q:{q:+d}{quality}"

# ==================== CREATE CHARACTERS ====================

def create_character(name, age, profession, skills, trait_list, sex="Male"):
    s = Survivor(name, age, sex, profession)
    for skill, level in skills.items():
        s.skills[skill] = level
    s.traits = trait_list
    s.trait_names = trait_list.copy()
    return s

def create_starting_characters():
    # Marcus - generally positive
    marcus = create_character("Marcus", 34, "Leader", 
        {"Scavenging": 35, "Combat": 30, "Building": 25, "Leadership": 30}, 
        ["Optimist", "Diligent", "Courageous", "Arrogant"], "Male")
    marcus.happiness = 65
    
    # Sarah - very positive
    sarah = create_character("Sarah", 28, "Hunter",
        {"Hunting": 45, "Fishing": 35, "Scavenging": 20},
        ["Cheerful", "Compassionate", "Athletic", "Careless"], "Female")
    sarah.happiness = 70
    
    # Ryan - mostly negative
    ryan = create_character("Ryan", 42, "Scavenger",
        {"Scavenging": 50, "Gathering": 35, "Combat": 25},
        ["Pessimist", "Lazy", "Cynical", "Greedy"], "Male")
    ryan.happiness = 25
    
    # Elena - mixed
    elena = create_character("Elena", 24, "Builder",
        {"Building": 40, "Crafting": 35, "Farming": 20},
        ["Creative", "Stubborn", "Energetic", "Moody"], "Female")
    elena.happiness = 50
    
    return [marcus, sarah, ryan, elena]

# ==================== ACTIONS ====================

def get_quality_name(q):
    if q >= 90: return "LEGENDARY"
    elif q >= 70: return "EXCELLENT"
    elif q >= 50: return "Good"
    elif q >= 30: return "Poor"
    else: return "TERRIBLE"

def do_scavenge(survivor, game):
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Scavenging"] + q_mod
    roll = random.randint(1, 100)
    result = skill + roll
    
    print(f"\n  {survivor.name} goes scavenging...")
    
    if result > 100:
        found = random.sample(["food", "materials", "medicine", "ammo", "scrap", "book"], 3)
        for item in found: add_item(item, game, 1)
        print(f"    AMAZING! Found: {', '.join(found)}")
    elif result > 70:
        found = random.sample(["food", "materials", "medicine", "scrap"], 2)
        for item in found: add_item(item, game, 1)
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
            print(f"    BAD! Got {injury} (-15 HP)")
        else:
            print(f"    Found nothing.")

def do_hunt(survivor, game):
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Hunting"] + q_mod
    result = skill + random.randint(1, 100)
    
    print(f"\n  {survivor.name} hunts...")
    if game.weather == "Rain": result -= 30
    
    if result > 80:
        game.food += 15
        print(f"    Big deer! +15 food")
    elif result > 50:
        game.food += 8
        print(f"    Rabbit! +8 food")
    elif result > 30:
        game.food += 4
        print(f"    Small catch. +4 food")
    else:
        print(f"    No luck.")

def do_gather(survivor, game):
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Gathering"] + q_mod
    
    print(f"\n  {survivor.name} gathers...")
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
        print(f"    Nothing.")

def do_farm(survivor, game):
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Farming"] + q_mod
    roll = skill + random.randint(1, 100)
    
    print(f"\n  {survivor.name} farms...")
    if "Farm" not in game.buildings:
        print(f"    No farm!")
        return
    
    roll += 10 if game.weather == "Clear" else -20 if game.weather == "Storm" else 0
    
    if roll > 60:
        food_gain = random.randint(5, 12)
        game.food += food_gain
        print(f"    {get_quality_name(roll)} harvest! +{food_gain} food")
    elif roll > 30:
        game.food += random.randint(2, 5)
        print(f"    Harvest.")
    else:
        print(f"    Poor harvest.")

def do_build(survivor, game):
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Building"] + q_mod
    
    print(f"\n  {survivor.name} builds...")
    if game.materials < 10:
        print(f"    Need 10 materials!")
        return
    
    roll = skill + random.randint(1, 100)
    if roll > 50:
        building = random.choice(["Workshop", "Well", "Greenhouse", "Pen"])
        game.buildings[building] = game.buildings.get(building, 0) + 1
        game.materials -= 10
        print(f"    {get_quality_name(roll)}! Built {building}!")
    else:
        game.materials -= 3
        print(f"    Progress.")

def do_rest(survivor, game):
    print(f"\n  {survivor.name} rests...")
    survivor.health = min(100, survivor.health + random.randint(10, 20))
    survivor.stamina = min(100, survivor.stamina + random.randint(20, 35))
    print(f"    +HP, +Stamina")

def do_cook(survivor, game):
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Cooking"] + q_mod
    
    print(f"\n  {survivor.name} cooks...")
    if game.food < 5:
        print(f"    No food!")
        return
    
    if random.random() < 0.3:
        game.food -= 3
        game.food += 7
        print(f"    Special meal! +7 food")
        for s in game.survivors: s.happiness += 3
    else:
        game.food -= 3
        game.food += 4
        print(f"    +4 food")

def do_guard(survivor, game):
    q_mod = survivor.get_quality_modifier()
    skill = survivor.skills["Combat"] + q_mod
    
    print(f"\n  {survivor.name} guards...")
    if random.random() < 0.2:
        enemy = random.choice(["wolf", "zombie", "raider"])
        print(f"    Enemy! A {enemy} attacks!")
        roll = skill + random.randint(1, 100)
        if roll > 60:
            print(f"    Defeated it!")
            survivor.happiness += 5
        else:
            damage = random.randint(10, 25)
            survivor.health -= damage
            print(f"    Took {damage} damage!")
    else:
        print(f"    Quiet.")

# ==================== HELPERS ====================

def add_item(item, game, amount=1):
    if item == "food": game.food += amount * random.randint(2, 5)
    elif item == "materials": game.materials += amount * random.randint(1, 3)
    elif item == "scrap": game.scrap += amount * random.randint(2, 5)
    elif item == "medicine": game.medicine += amount
    elif item == "ammo": game.ammo += amount * random.randint(1, 3)
    elif item == "book":
        books = ["Hunting Guide", "Fishing Manual", "Carpentry", "First Aid", "Botany"]
        found = random.choice(books)
        if found not in game.books:
            game.books.append(found)
            print(f"    NEW BOOK: {found}!")

def check_game_over(game):
    if game.food <= 0:
        print("\n" + "="*50)
        print("GAME OVER - Starvation!")
        return True
    if not any(s.is_alive for s in game.survivors):
        print("\n" + "="*50)
        print("GAME OVER - Everyone died!")
        return True
    return False

def mood_contagion(game):
    for s in game.survivors:
        if not s.is_alive: continue
        for other in game.survivors:
            if s == other or not other.is_alive: continue
            influence = other.get_mood_contagion()
            resistance = s.get_contagion_resistance()
            if influence != 0:
                s.happiness += int(influence * resistance * 0.5)

def daily_mood_change(game):
    for s in game.survivors:
        if not s.is_alive: continue
        change = s.get_daily_base_change()
        if game.weather == "Rain":
            change += s.get_trait_effects("weather_mood")
        s.happiness += change

def print_status(game):
    print(f"\n{'='*60}")
    print(f"DAY {game.day} - {game.season} - {game.weather} {game.temperature}F")
    print(f"{'='*60}")
    print(f"\nFOOD: {game.food} | WATER: {game.water} | SCRAP: {game.scrap}")
    print(f"MATERIALS: {game.materials} | MEDS: {game.medicine} | AMMO: {game.ammo}")
    print(f"\nBUILDINGS: {', '.join([f'{k}(v{v})' for k,v in game.buildings.items()])}")
    
    print(f"\nSURVIVORS ({len(game.survivors)}):")
    print("-" * 55)
    for s in game.survivors:
        if s.health > 0:
            q = int(s.get_quality_modifier())
            q_str = "++" if q > 5 else "+" if q > 0 else "--" if q < -5 else "-" if q < 0 else ""
            traits = ", ".join(s.traits[:2])
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
        q_mod = int(survivor.get_quality_modifier())
        print(f"  {num}: {job} (Skill:{skill} Q:{q_mod:+d})")
    
    while True:
        choice = input(f"\nTask for {survivor.name} (1-8): ").strip()
        for num, job in jobs:
            if choice == num:
                return job, skill_map[num]
        print("1-8 please.")

# ==================== MAIN ====================

def main():
    print("="*60)
    print("         OUTPOST ZERO v3.1")
    print("   Extended Traits (Positive & Negative)")
    print("="*60)
    print()
    
    game = Game()
    game.survivors = create_starting_characters()
    
    print("4 survivors with mixed traits!")
    print("Watch how traits affect everything...")
    print()
    
    while not game.game_over:
        game.update_season()
        game.update_weather()
        
        print_status(game)
        
        mood_contagion(game)
        daily_mood_change(game)
        
        print("\n" + "-"*40)
        print("ASSIGN TASKS")
        print("-"*40)
        
        for survivor in game.survivors:
            if survivor.health <= 0: continue
            task, skill = get_job_choice(survivor)
            survivor.job = task
            
            if task == "Scavenge": survivor.stamina -= 20; do_scavenge(survivor, game)
            elif task == "Hunt": survivor.stamina -= 25; do_hunt(survivor, game)
            elif task == "Gather": survivor.stamina -= 15; do_gather(survivor, game)
            elif task == "Farm": survivor.stamina -= 15; do_farm(survivor, game)
            elif task == "Build": survivor.stamina -= 20; do_build(survivor, game)
            elif task == "Cook": survivor.stamina -= 10; do_cook(survivor, game)
            elif task == "Rest": do_rest(survivor, game)
            elif task == "Guard": survivor.stamina -= 15; do_guard(survivor, game)
            
            if survivor.health <= 0:
                print(f"\n💀 {survivor.name} died!")
                survivor.is_alive = False
                for s in game.survivors: s.happiness -= 15
        
        alive = len([s for s in game.survivors if s.is_alive and s.health > 0])
        game.food -= alive * 2
        print(f"\n\nAte {alive * 2} food.")
        
        # Night events
        print("\n" + "-"*40)
        print("NIGHT")
        print("-"*40)
        
        roll = random.randint(1, 100)
        if roll < 5: print("Bad dreams...")
        elif roll < 10: game.food += random.randint(2, 6)
        elif roll < 15:
            v = random.choice([s for s in game.survivors if s.is_alive])
            v.sickness = random.choice(["Cold", "Flu"]); v.health -= 10
        
        for s in game.survivors:
            if s.is_alive: s.happiness = max(-100, min(100, s.happiness))
        
        game.survivors = [s for s in game.survivors if s.is_alive]
        game.day += 1
        
        if check_game_over(game):
            game.game_over = True
        
        if not game.game_over:
            if input("\nNext day? (q to quit): ").lower() == 'q':
                break
    
    print(f"\nGame over! Survived {game.day} days!")

if __name__ == "__main__":
    main()
