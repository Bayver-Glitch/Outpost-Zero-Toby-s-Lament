"""
OUTPOST ZERO - Text-Based Prototype
A survival game about building a community through discovery
"""

import random
import time
from datetime import datetime

# ==================== GAME STATE ====================

class Game:
    def __init__(self):
        self.day = 1
        self.food = 12
        self.water = 20
        self.materials = 10
        self.medicine = 2
        self.ammo = 10
        self.books = ["Gardening Basics"]  # Start with one book
        self.discovered_recipes = []
        self.buildings = ["Farmhouse", "Fire Pit"]
        self.survivors = []
        self.game_over = False
        
    def add_survivor(self, survivor):
        self.survivors.append(survivor)

# ==================== CHARACTERS ====================

class Survivor:
    def __init__(self, name, age, sex, profession="Survivor"):
        self.name = name
        self.age = age
        self.sex = sex
        self.profession = profession
        
        # Stats (1-100)
        self.health = 100
        self.stamina = 100
        self.stress = 10
        
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
            "Teaching": random.randint(5, 15),
            "Science": random.randint(5, 15),
        }
        
        # Education (1-6: Illiterate → PhD)
        self.education = random.choice([1, 1, 2, 2, 2, 3])  # Weighted toward basic/grade school
        
        # Personality
        self.mood = random.choice(["Happy", "Content", "Neutral", "Anxious", "Grumpy"])
        self.disposition = random.choice(["Calm", "Joyful", "Aloof", "Grumpy", "Serious"])
        self.traits = random.sample(["Brave", "Curious", "Honest", "Patient", "Lazy", "Cowardly", "Selfish", "Kind"], 2)
        
        # Injuries
        self.injuries = []
        
        # Memory/Relationships (key = survivor name, value = -100 to +100)
        self.relationships = {}
        
        # Stats this character cares about
        self.favorite_food = random.choice(["Meat", "Berries", "Fish", "Vegetables"])
        
    def __str__(self):
        return f"{self.name} ({self.profession})"

# ==================== STARTING CHARACTERS ====================

def create_starting_characters():
    chars = [
        Survivor("Marcus", 34, "Male", "Leader"),
        Survivor("Sarah", 28, "Female", "Hunter"),
        Survivor("Ryan", 42, "Male", "Scavenger"),
        Survivor("Elena", 24, "Female", "Builder"),
    ]
    
    # Customize some stats
    chars[0].skills["Leadership"] = 30
    chars[0].skills["Scavenging"] = 35
    chars[0].education = 3  # Grade school
    
    chars[1].skills["Hunting"] = 45
    chars[1].skills["Fishing"] = 35
    chars[1].traits = ["Patient", "Kind"]
    chars[1].favorite_food = "Fish"
    
    chars[2].skills["Scavenging"] = 50
    chars[2].skills["Combat"] = 30
    chars[2].traits = ["Cautious", "Selfish"]
    chars[2].education = 2
    
    chars[3].skills["Building"] = 40
    chars[3].skills["Crafting"] = 35
    chars[3].traits = ["Curious", "Creative"]
    chars[3].education = 2
    
    return chars

# ==================== ACTIONS ====================

def scavenge(survivor, game):
    """Send survivor to scavenge in the wasteland"""
    skill = survivor.skills["Scavenging"]
    roll = random.randint(1, 100)
    result = skill + roll
    
    print(f"\n{survivor.name} goes scavenging...")
    time.sleep(0.5)
    
    if result > 80:  # Great success
        found = random.sample(["Food", "Food", "Materials", "Medicine", "Book", "Ammo"], 2)
        for item in found:
            add_item(item, game)
        print(f"  GREAT FIND! Found: {', '.join(found)}")
        return True
    elif result > 50:  # Success
        found = random.choice(["Food", "Materials", "Food", "Ammo", "Scrap"])
        add_item(found, game)
        print(f"  Found: {found}")
        return True
    elif result > 30:  # Mixed
        found = random.choice(["Food", "Nothing"])
        if found != "Nothing":
            add_item(found, game)
            print(f"  Found: {found}")
        else:
            print("  Found nothing, but stayed safe.")
        return True
    else:  # Failure
        if random.random() < 0.3:
            injury = random.choice(["Cut", "Bruise", "Sprain"])
            survivor.injuries.append(injury)
            print(f"  BAD LUCK! Got injured: {injury}")
        else:
            print("  Couldn't find anything and barely escaped!")
        return False

def hunt(survivor, game):
    """Send survivor hunting"""
    skill = survivor.skills["Hunting"]
    roll = random.randint(1, 100)
    result = skill + roll
    
    print(f"\n{survivor.name} goes hunting...")
    time.sleep(0.5)
    
    if result > 70:
        game.food += 10
        print(f"  SUCCESS! Caught a deer! (+10 Food)")
    elif result > 40:
        game.food += 5
        print(f"  Got a rabbit. (+5 Food)")
    elif result > 20:
        game.food += 2
        print(f"  Small catch. (+2 Food)")
    else:
        print("  No luck today.")
        if random.random() < 0.2:
            injury = "Sprain"
            survivor.injuries.append(injury)
            print(f"  And got injured: {injury}")

def gather(survivor, game):
    """Send survivor to gather wild plants"""
    skill = survivor.skills["Gathering"]
    roll = random.randint(1, 100)
    result = skill + roll
    
    print(f"\n{survivor.name} goes gathering...")
    time.sleep(0.5)
    
    finds = []
    for _ in range(2):
        roll = skill + random.randint(1, 100)
        if roll > 40:
            finds.append(random.choice(["Berries", "Mushrooms", "Herbs", "Firewood"]))
    
    if finds:
        for item in finds:
            if item == "Food":
                game.food += 2
            elif item == "Berries":
                game.food += 3
            elif item == "Firewood":
                game.materials += 2
            else:
                game.materials += 1
        print(f"  Found: {', '.join(finds)}")
    else:
        print("  Found nothing useful.")

def farm(survivor, game):
    """Send survivor to farm"""
    skill = survivor.skills["Farming"]
    roll = skill + random.randint(1, 100)
    
    print(f"\n{survivor.name} tends the farm...")
    time.sleep(0.5)
    
    if roll > 40:
        food_gain = random.randint(3, 8)
        game.food += food_gain
        print(f"  Harvest! +{food_gain} Food")
    else:
        print("  Crops didn't grow well this time.")

def rest(survivor, game):
    """Rest and recover"""
    print(f"\n{survivor.name} rests and recovers.")
    survivor.stamina = min(100, survivor.stamina + 30)
    survivor.health = min(100, survivor.health + 5)
    if survivor.injuries:
        if random.random() < 0.3:
            removed = survivor.injuries.pop()
            print(f"  Injury healed: {removed}")

def build(survivor, game):
    """Try to build something"""
    skill = survivor.skills["Building"]
    roll = skill + random.randint(1, 100)
    
    print(f"\n{survivor.name} tries to build...")
    time.sleep(0.5)
    
    if game.materials < 5:
        print("  Not enough materials!")
        return
        
    if roll > 50:
        new_building = random.choice(["Greenhouse", "Smokehouse", "Well", "Workshop"])
        game.buildings.append(new_building)
        game.materials -= 5
        print(f"  Built: {new_building}!")
    else:
        game.materials -= 2
        print("  Made some progress, but not finished.")

# ==================== HELPERS ====================

def add_item(item, game):
    if item == "Food":
        game.food += random.randint(2, 5)
    elif item == "Materials":
        game.materials += random.randint(1, 4)
    elif item == "Medicine":
        game.medicine += 1
    elif item == "Ammo":
        game.ammo += random.randint(1, 3)
    elif item == "Book":
        new_books = ["Hunting Guide", "Fishing Manual", "Carpentry Guide", "First Aid", "Botany", "Mechanics"]
        found_book = random.choice(new_books)
        if found_book not in game.books:
            game.books.append(found_book)
            print(f"  NEW BOOK DISCOVERED: {found_book}")
    elif item == "Scrap":
        game.materials += random.randint(2, 6)

def check_game_over(game):
    """Check if game is over"""
    if game.food <= 0:
        print("\n" + "="*50)
        print("GAME OVER - Starvation!")
        print("Your settlement has collapsed.")
        return True
    if game.survivors and all(s.health <= 0 for s in game.survivors):
        print("\n" + "="*50)
        print("GAME OVER - Everyone has perished!")
        return True
    return False

# ==================== MAIN GAME LOOP ====================

def main():
    print("="*60)
    print("         OUTPOST ZERO")
    print("    A Survival Discovery Game")
    print("="*60)
    print()
    
    # Create game
    game = Game()
    game.survivors = create_starting_characters()
    
    print("Your group of survivors has settled in an abandoned farmhouse.")
    print("You have the Gardening book from the car trunk.")
    print()
    print(f"Starting with {len(game.survivors)} survivors:")
    for s in game.survivors:
        print(f"  - {s.name}: {s.profession}")
    print()
    print("Day 1 begins...")
    print()
    
    # Main game loop
    while not game.game_over:
        print("\n" + "="*50)
        print(f"DAY {game.day} - Morning")
        print("="*50)
        
        # Show status
        print(f"\nRESOURCES:")
        print(f"  Food: {game.food} | Water: {game.water} | Materials: {game.materials}")
        print(f"  Medicine: {game.medicine} | Ammo: {game.ammo}")
        print(f"  Buildings: {', '.join(game.buildings)}")
        print(f"  Books: {', '.join(game.books)}")
        
        print(f"\nSURVIVORS:")
        for s in game.survivors:
            injuries = f" ({', '.join(s.injuries)})" if s.injuries else ""
            print(f"  {s.name}: HP {s.health} | ST {s.stamina} | Mood: {s.mood}{injuries}")
        
        # Check starvation
        if game.food <= 0:
            print("\n⚠️ OUT OF FOOD! Someone will die!")
            victim = random.choice(game.survivors)
            victim.health = 0
            print(f"  {victim.name} has perished from starvation!")
        
        # Day phase - assign tasks
        print("\n" + "-"*40)
        print("TASK ASSIGNMENT")
        print("-"*40)
        
        # Simple automatic task assignment for prototype
        task_counts = {"Scavenge": 0, "Hunt": 0, "Gather": 0, "Farm": 0, "Build": 0, "Rest": 0}
        
        # Player chooses (simplified)
        print("\nChoose tasks for each survivor:")
        print("1. Scavenge - Find supplies in wasteland (risky)")
        print("2. Hunt - Hunt wild game (medium risk)")
        print("3. Gather - Collect berries, wood (safe)")
        print("4. Farm - Grow food (slow but steady)")
        print("5. Build - Construct/upgrade (needs materials)")
        print("6. Rest - Recover stamina/health")
        
        # For prototype, auto-assign based on available workers
        assignments = []
        for s in game.survivors:
            if game.food < 15:
                if s.skills["Hunting"] > 20:
                    task = "Hunt"
                else:
                    task = "Gather"
            elif game.materials < 8:
                task = "Gather"
            elif random.random() < 0.5:
                task = random.choice(["Scavenge", "Hunt", "Gather"])
            else:
                task = random.choice(["Farm", "Rest", "Gather"])
            
            task_counts[task] += 1
            assignments.append((s, task))
            print(f"  {s.name}: {task}")
        
        print("\n...the day passes...")
        time.sleep(1)
        
        # Execute tasks
        print("\n" + "-"*40)
        print("DAILY ACTIVITIES")
        print("-"*40)
        
        for survivor, task in assignments:
            if survivor.health <= 0:
                continue
                
            if task == "Scavenge":
                scavenge(survivor, game)
            elif task == "Hunt":
                hunt(survivor, game)
            elif task == "Gather":
                gather(survivor, game)
            elif task == "Farm":
                farm(survivor, game)
            elif task == "Build":
                build(survivor, game)
            elif task == "Rest":
                rest(survivor, game)
        
        # Consume food/water
        food_consumed = len([s for s in game.survivors if s.health > 0]) * 2
        game.food -= food_consumed
        print(f"\nSurvivors ate {food_consumed} food.")
        
        # Night events
        print("\n" + "-"*40)
        print("NIGHT EVENTS")
        print("-"*40)
        
        event_roll = random.randint(1, 100)
        
        if event_roll < 10:
            print("A cold rain fell all night. Everyone is miserable.")
            for s in game.survivors:
                s.mood = "Anxious" if s.mood != "Depressed" else "Sad"
        elif event_roll < 15:
            survivor = random.choice(game.survivors)
            print(f"{survivor.name} had a nightmare about the old world.")
            survivor.stress += 10
        elif event_roll < 20:
            found_food = random.randint(1, 3)
            game.food += found_food
            print(f"In the night, someone found {found_food} food hidden in their pocket!")
        
        # Update day
        game.day += 1
        
        # Check game over
        if check_game_over(game):
            game.game_over = True
        
        # Brief pause
        time.sleep(0.5)

if __name__ == "__main__":
    main()
