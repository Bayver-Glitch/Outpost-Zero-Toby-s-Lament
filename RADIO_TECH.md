# OUTPOST ZERO - Radio & Tech Tree Systems

## RADIO SYSTEM

### Radio Progression

| Tech Level | Radio Type | Range | Features |
|------------|------------|-------|----------|
| 1 | None | - | - |
| 2 | Hand-Crank Radio | 1km | Receive only |
| 3 | Walkie-Talkie | 3km | 2-way short range |
| 4 | Base Station | 10km | Permanent base |
| 5 | Network | 50km | Full communication |

---

### Stage 1: Receiver Only (Tech 2)

**Finding a Radio:**
- Scavengers find working/cranked radios
- Can pick up signals
- No response capability

**What You Hear:**
```
[RADIO STATIC]

"...anyone out there... this is survivor camp...
if you can hear us... we have food..."

"...raiders moving south... avoid highway 9..."

"...military checkpoint at mile marker 45...
friendly..."

"...the mist... it's growing... God help us..."
```

**Random Radio Events:**

| Event | Info Gained |
|-------|-------------|
| Survivor Camp | Location on map, potential trade |
| Raider Warning | Danger zone marked |
| Military Signal | Faction location |
| Distress Call | Rescue opportunity |
| Music/Voices | Morale boost |
| Static Only | Nothing |

---

### Stage 2: Walkie-Talkies (Tech 3)

**Unlocks:**
- Buy from traders
- Find in military locations
- Eventually craft (requires electronics)

**How It Works:**
- Assign radio to scout team (1-3 people)
- Scout can contact base
- Base can contact scout

**Radio Conversation:**

```
SCENARIO: Scout finds injured survivor

[SCOUT (Kenji)]:
"Base, this is Kenji. We found something."

[BASE (Marcus)]:
"Go ahead, Kenji. What do you have?"

[SCOUT]:
"There's a woman here. Badly hurt. Says 
she's from a settlement to the north. 
They're under attack. Wants help."

[BASE]:
"Can you bring her in?"

[SCOUT]:
"She's in no shape to move. Needs a medic.
I've got maybe 2 hours before dark."

[BASE]:
"Understood. Sending Park with the cart.
Stay put, keep her alive."

[SCOUT]:
"Copy that. We'll be at the old gas station.
Kenji out."
```

---

### Stage 3: Base Station (Tech 4)

**Building:**
```
Radio Station:
- Cost: 100 scrap, 30 electronics
- Requires: Tech 4, Workshop
- Staff: 1 (Radio Operator)
- Range: 10km
```

**Features:**
- 24/7 monitoring
- Multiple channels
- Can reach other settlements
- Automated alerts

**Radio Operator Job:**
- Monitors radio constantly
- Records important messages
- Responds to calls
- Can send messages to scouts

---

### Stage 4: Full Network (Tech 5)

**Capabilities:**
- Contact other settlements
- Trade via radio
- Coordinate large operations
- Early warning system
- Map-wide communication

**Late Game Radio Network:**
```
[NETWORK STATUS]
- Connected Stations: 3
- Your Settlement: Hope's End
- Partner: Farm Collective (North)
- Partner: River Community (East)

[INCOMING MESSAGE]
"This is Farm Collective. We have surplus 
seeds. Interested in trade?"

[OUTGOING]
"Hope's End to Collective. Affirmative.
We'll send a team."
```

---

## SCOUT SURPRISES (Pre-Radio)

### Return Events

When scouts return, they bring more than loot:

**Type 1: Survivors**
```
Scout returns with: NEW CHARACTER

Wei: "We found someone on the road. 
She was hiding in a barn."

[Character: Sarah, age 28]
- Health: Injured (needs care)
- Skills: Farming 30, Cooking 25
- Background: Lost her family
- Wants to join: Yes

[ACCEPT] [ASK MORE] [TURN AWAY]
```

**Type 2: Location Discovery**
```
Wei: "Found something interesting. 
Old military outpost. Looks looted, but 
might be more inside."

New Map Marker: Military Outpost
- Distance: 2 days travel
- Danger: HIGH
- Loot: Unknown

[PLAN EXPEDITION] [MARK FOR LATER]
```

**Type 3: Captured Person**
```
Kenji returns: "Found this guy tied up in 
a cabin. Raiders had him. He's pretty 
beat up."

[Character: Tom, age 35]
- Health: Critical
- Has info: Raiders planning attack
- Profession: Former soldier

[RESCUE] [QUESTION FIRST] [LEAVE HIM]
```

**Type 4: Injured Survivor**
```
Park returns with: INJURED CHARACTER

Park: "Found him in a ditch. Wolf attack.
Barely alive."

[Character: Rick, age 22]
- Health: 10/100 (dying!)
- Injury: Wolf bites (infected)
- Needs: Immediate medical

[TREAT NOW] [USE HERBS] [LEAVE]
```

**Type 5: Trade Opportunity**
```
Kenji: "Met a trader on the road. Says 
there's a big market in the old mall. 
Wants to set up regular routes."

Trade Route: Old Mall
- Frequency: Weekly
- Type: Junk Dealer
- Notes: Has rare items

[ESTABLISH ROUTE] [VISIT ONCE]
```

**Type 6: Enemy Scout**
```
Wei: "Spotted a raider scout watching 
our walls. Think they know we're here."

Enemy Scout: Observed position
- Group Size: Unknown
- Intent: Reconnaissance
- Time: Just now

[IGNORE] [HUNT HIM] [SET TRAP]
```

**Type 7: Pet/Animal**
```
Kenji returns carrying: DOG

Kenji: "Found this guy starving in a 
house. No collar. Pretty friendly."

[Dog Stats:]
- Name: Scraps
- Health: 60%
- Training: None
- Can become: Scout dog, Guard dog

[ADOPT] [PUT DOWN] [KEEP IN CAMP]
```

---

## TECH TREE SYSTEM

### How Tech Unlocks Work

**Two-Step Process:**

```
STEP 1: DISCOVER
- Find book, blueprint, or example
- Unlocks knowledge that tech is possible

STEP 2: RESEARCH  
- Use Laboratory to develop
- Takes time and materials
- Requires prerequisites
```

### Example: Building a Forge

```
DISCOVERY:
Scavenger finds: "Blacksmith's Guide" book
Status: "You now know a forge is possible"

RESEARCH (in Laboratory):
Requirements:
- Science: 20+
- Time: 15 days
- Materials: 100 scrap, 50 stone, 20 iron

Researching...
[████████░░░] 70%

COMPLETE!
"Unlocked: Basic Forge"
"Can now build Blacksmithy station"
```

---

### Tech Categories

| Category | Building | Research Location |
|----------|----------|------------------|
| Building | Various | Town Center |
| Crafting | Workshop | Workshop |
| Farming | Farm | Farm |
| Medical | Medical Bay | Laboratory |
| Military | Barracks | Workshop |
| Science | Laboratory | Laboratory |
| Communication | Radio | Laboratory |

---

### TECH LEVEL 1 → 2 (Scrap → Fundamentals)

**Required:**
- Find "Basic Crafts" book OR
- Character with relevant skills teaches

**Unlocks:**
```
[Building]
✓ Wooden Walls (instead of scrap)
✓ Wooden Tower
✓ Smokehouse

[Crafting]
✓ Stone Tools (improved)
✓ Basic Leather

[Farming]
✓ Basic Farming (level 2 crops)
✓ Basic Irrigation

[Other]
✓ Basic Well
```

---

### TECH LEVEL 2 → 3 (Fundamentals → Foundations)

**Required:**
- Find "Intermediate [Skill]" books
- Some require characters with teaching

**Unlocks:**
```
[Building]
✓ Stone Walls
✓ Barn
✓ Workshop
✓ Forge (Blacksmith!)

[Combat]
✓ Crossbow (better than bow)
✓ Basic Armor
✓ Fire weapons (torches, fire arrows)

[Farming]
✓ Raised Garden Beds
✓ Greenhouse (basic)
✓ Fruit Trees

[Medical]
✓ Medical Bay
✓ Antibiotics (if herbs available)

[Other]
✓ Leather Armor
✓ Better Well
```

---

### TECH LEVEL 3 → 4 (Foundations → Industrial)

**Required:**
- Research in Laboratory
- Specific books needed
- Character skills

**Unlocks:**
```
[Building]
✓ Generator
✓ Garage
✓ Medical Bay (advanced)
✓ Workshop II

[Combat]
✓ Flintlock Weapons!
✓ Black Powder
✓ Basic Firearms
✓ Steel Armor

[Farming]
✓ Greenhouse II
✓ Irrigation System
✓ Advanced Animals

[Science]
✓ Radio Station
✓ Basic Research

[Medical]
✓ Clinic
✓ Surgery
✓ Vaccines

[Other]
✓ Electricity (basic)
✓ Radio (walkie-talkie)
```

---

### TECH LEVEL 4 → 5 (Industrial → Modern)

**Required:**
- Extensive research
- Rare books
- High-skill characters
- Lots of resources

**Unlocks:**
```
[Building]
✓ Laboratory
✓ Computer Lab
✓ Modern Housing
✓ Hydroponics Farm
✓ Power Plant

[Combat]
✓ Modern Firearms (rare ammo)
✓ Advanced Armor
✓ Vehicles

[Science]
✓ Full Research Network
✓ Automation
✓ Advanced Medicine

[Communication]
✓ Radio Network
✓ Long-range Communication

[Medical]
✓ Hospital
✓ Gene Therapy
✓ Full Cures
```

---

## RESEARCH EXAMPLES

### Example 1: Radio

```
STEP 1: DISCOVERY
Source: Find "Electronics for Beginners" book
Result: "You now know radios are possible"

STEP 2: PREREQUISITES
- Tech Level 3
- Workshop built
- Character with Science 20+

STEP 3: RESEARCH
Time: 20 days
Materials: 50 scrap, 30 electronics, 20 copper

[Researching Radio Systems...]

STEP 4: COMPLETE
Result: Unlocked Radio Station blueprint
Can now build: Radio Station
```

### Example 2: Hydroponics

```
STEP 1: DISCOVERY
Source: Find "Advanced Agriculture" magazine
Result: "Hydroponic growing is possible"

STEP 2: PREREQUISITES  
- Tech Level 4
- Laboratory built
- Character with Science 40+, Farming 50+

STEP 3: RESEARCH
Time: 45 days
Materials: 200 scrap, 100 steel, 50 electronics,
           50 glass, 20 herbs (for nutrients)

[Researching Hydroponics...]

STEP 4: COMPLETE
Result: Unlocked Hydroponics Farm
```

---

## RESEARCH INTERFACE

```
═══════════════════════════════════
    🔬 RESEARCH - Day 47
═══════════════════════════════════

AVAILABLE RESEARCH:

[1] Radio Station
    Status: Discovered ✓
    Progress: [██████░░░░] 60%
    Time Remaining: 8 days
    Scientist: Wei (Science 35)

[2] Basic Forge
    Status: Ready to Research
    Time: 15 days | Cost: 100 scrap
    [START RESEARCH]

[3] Greenhouse
    Status: Discovered ✓
    Requirements not met (Tech 3 required)
    [VIEW PREREQS]

[4] Advanced Medicine
    Status: Not Discovered
    Hint: Find "Modern Medicine" book
    [SEARCH INFO]

───────────────────────────────────
BOOKS NEEDED:
- Blacksmith Guide (for Forge)
- Radio Basics (for Radio)
- Modern Medicine (for Advanced Med)
```

---

## BOOK DISCOVERY

### Where Books Are Found

| Location | Book Types |
|----------|------------|
| Houses | Living skills, cooking |
| Libraries | All types |
| Schools | Teaching, science |
| Hospitals | Medical |
| Military | Combat, weapons |
| Stores | Trade, crafting |
| Factories | Engineering |

### Rare Books

| Book | Effect | Rarity |
|------|--------|--------|
| Master Blacksmith | +10 forge quality | Very Rare |
| Medical Encyclopedia | All medical +20% | Rare |
| Ancient Farming | Secret crop techniques | Rare |
| Military Tactics | Combat strategies | Rare |
| Survival Guide | All skills +5 | Legendary |

---

## EXAMPLE: COMPLETE TECH JOURNEY

```
DAY 1: Find "Basic Crafts" book in house
- Now know basic building possible

DAY 15: Have resources, research 10 days
- Tech Level 2 unlocked!

DAY 30: Scout finds "Blacksmith Guide"
- Can now research forge

DAY 45: Build workshop, research forge 15 days
- Forge built!

DAY 60: Scout finds "Radio Basics" book
- Can research radio

DAY 80: Tech 3, build lab, research radio
- Radio station day 100!

DAY 150: All Tech 4
- Working on Tech 5

DAY 200: Victory!
```

---

*Discover. Research. Advance.*
