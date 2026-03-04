# OUTPOST ZERO - Character Backstories & Event System

## FAMILY SYSTEM

### Family Tree (Per Character)

Each character tracks:
- **Parents:** Mother (alive/dead/unknown), Father (alive/dead/unknown)
- **Siblings:** Brother(s), Sister(s) - each with status
- **Children:** Son(s), Daughter(s) - each with status
- **Spouse/Partner:** If applicable
- **Extended:** Cousins, aunts, uncles (optional for complexity)

### Family Status Types
- Alive and with us
- Alive elsewhere (lost in collapse)
- Alive as zombie
- Dead (confirmed)
- Unknown (might be alive)

### Family Events
- **Reunions:** Finding lost family members
- **Deaths:** Learning family died
- **Discovery:** Learning family became zombie

---

## BACKSTORY SYSTEM

### Backstory Categories

#### 1. Childhood
- Where grew up (city/suburb/rural)
- Family wealth (poor/middle/rich)
- Education level (self-taught/parent taught/school)
- Happy/Traumatic

#### 2. Pre-Collapse Life
- Occupation before everything fell
- Key skills from job
- Relationships (married/single/dating)
- Location during collapse

#### 3. The Collapse
- How survived first days/weeks
- Lost anyone close
- Made any major decisions
- What they've been doing since

#### 4. Current State
- How joined settlement
- What they bring (skills, items)
- Goals/aspirations

### Backstory Templates (Random Generation)

**Template A - The Survivor**
```
Background: City person, office job
The Collapse: Was at work when it happened, walked home through chaos
Family: Mother died in initial panic, Father became zombie, killed him
Skills: Management, basic first aid from work training
Joining: Wandered for months, found settlement

Events: May trigger "Family Loss" anniversary events
```

**Template B - The Builder**
```
Background: Construction worker, rural
The Collapse: Was building a cabin when it happened, already had supplies
Family: Wife and two kids with them, all survived
Skills: Construction, woodworking, farming
Joining: Built their own shelter, joined for community

Events: May get "Cabin Fever" type events
```

**Template C - The Healer**
```
Background: Nurse at hospital
The Collapse: Watched hospital become overrun, saved who she could
Family: Brother died helping her escape
Skills: Advanced first aid, herbalism (hobby)
Joining: Healed many along the way, reputation precedes her

Events: Trigger "Need a Healer" rescue scenarios
```

**Template D - The Scavenger**
```
Background: Homeless, lived on streets
The Collapse: Actually BETTER off - knew streets, survived by being invisible
Family: No family to lose
Skills: Scavenging, stealth, street survival
Joining: Found settlement, contributes through scavenging

Events: May trigger "Found long-lost relative" through scavenger contacts
```

**Template E - The Family Man**
```
Background: Family farm, rural
The Collapse: Took in neighbors, created mini-community
Family: Wife, 3 kids, parents all alive
Skills: Farming, hunting, child care
Joining: Group grew too large, sent ahead to find safe place

Events: Strong family bonds affect mood of others
```

---

## EXAMPLE BACKSTORY: "Phyllis"

```
Name: Phyllis Chen
Age: 34

FAMILY:
- Husband: David (deceased - killed by raiders 18 months ago)
- Daughter: Emma (age 15 - KIDNAPPED by raiders 3 years ago)
- Son: Thomas (age 12 - with her, in settlement)
- Mother: Margaret (alive - zombie, killed by Phyllis 2 years ago)
- Father: Robert (unknown - lost during collapse)

EDUCATION:
- High school graduate
- Some college (nursing pre-req)
- Can read/write: Yes (Level 4)

PRE-COLLAPSE:
- Occupation: Elementary school teacher
- Location: Seattle suburbs
- Skills: Teaching, child care, basic first aid (from school training)
- Had no survival skills

THE COLLAPSE:
- Was at school when it happened
- Led 15 kids to safety over 3 days
- Lost 3 children to panic/chaos (never found out what happened)
- Walked 200 miles to rural area

MAJOR EVENTS:
- Year 1: Husband David killed defending camp from raiders
- Year 1: Mother Margaret turned, Phyllis had to put her down
- Year 2: Daughter Emma (13) kidnapped by passing raider group
- Year 3: Son Thomas has nightmares, depends on her heavily

CURRENT:
- Joined settlement 6 months ago
- Works in makeshift school for children
- Very protective of children in camp
- Always watching traders for signs of Emma

TRAITS:
- Afraid of the Dark (developed after being trapped in basement during attack)
- People Person (+1 from social)
- Grudge Holder (-15 toward raiders)
- Night Owl (sleeps lightly)

SKILLS:
- Teaching: 45
- Child Care: 50
- First Aid: 25
- Scavenging: 15
- Farming: 10
```

---

## RANDOM EVENT SYSTEM

### Event Triggers

Events can trigger from:
1. **Time-based:** Day 30, Day 100, anniversaries
2. **Backstory:** Character-specific events
3. **Location:** Where scavenging happens
4. **Random:** Generic events
5. **Chain:** Events that spawn from other events

### Event Types

#### Family Events
| Event | Trigger | Outcome |
|-------|---------|----------|
| Family Reunion | Scavenger in same zone as lost family | Character joy/confusion |
| Death Confirmed | Find proof of death | Grief, mood drop |
| Zombie Relative | Find zombie that IS family | Trauma, must kill |
| Lost Child | Trader with child that looks like them | Investigation opportunity |

**Example - "Phyllis's Daughter":**
```
Event: Trader arrives with young girl (14-16)
Trigger: Settlement at Level 2+, Phyllis in camp
Chance: 15% per trader visit

Details:
- Girl seems familiar
- If player investigates: Find bracelet
- Choice: Confront trader
  - Pay ransom (resources)
  - Fight (combat risk)
  - Let girl choose

Outcomes:
- Success: Emma rescued, massive happiness boost
- Failure: Emma taken, deep trauma for Phyllis
- Neutral: Girl is not Emma
```

#### Weather Events
| Event | Trigger | Outcome |
|-------|---------|----------|
| Storm | Rain/snow | Work efficiency -25% |
| Drought | 5+ days no rain | Crops die, -food |
| Flood | Heavy rain | Loss of supplies, injury risk |
| Extreme Cold | Winter temps | Frostbite, increased heating needs |

#### Scavenging Events
| Event | Trigger | Outcome |
|-------|---------|----------|
| Found Book | Scavenge success | New skill/unlock |
| Survivor Found | Scavenge in moderate+ zone | New recruit possibility |
| Trap | Scavenge failure | Injury, lost items |
| Ambush | Scavenge danger zone | Combat, flee, or die |
| Abandoned Camp | Scavenge anywhere | Resources, possible new character |

#### Relationship Events
| Event | Trigger | Outcome |
|-------|---------|----------|
| New Romance | 2 characters +50+ relationship | Happiness boost |
| Argument | Random low relationship | Mood drops |
| Birthday | Character birthday | Party (happiness boost) |
| Anniversary | Character in camp 1 year | Reflection event |

#### Discovery Events
| Event | Trigger | Outcome |
|-------|---------|----------|
| Ancient Cache | Explore dangerous zone | Rare books/items |
| Research Breakthrough | Scientist in lab | Unlock new tech |
| Strange Signal | Radio operator | Quest/mystery |
| Animal Tamed | Hunter with animal skill | New animal companion |

#### Raid Events
| Event | Trigger | Outcome |
|-------|---------|----------|
| Raider Attack | Random (higher at higher difficulty) | Combat defense |
| Thief | Night time | Lost resources |
| Siege | Large settlement | Multi-day defense |
| Diplomatic Visit | Reputation good | Trade opportunity |

---

## RAID DEFENSE SYSTEM

### Defending Storage

**Storage Building:**
- HP based on construction level
- Contains: Food, Materials, Medicine, Ammo, Fuel
- If breached: Raiders take 30-70% of random resource

**Defense Layers:**

1. **Walls/Gate**
   - HP: Varies by tech level
   - Gate can be breached
   - Can be repaired

2. **Watchtower**
   - Provides early warning (+1 hour to prepare)
   - Guards in tower can defend
   - Night bonus: +25% accuracy

3. **Guards**
   - Assign survivors to patrol
   - Combat skill matters
   - Can be overwhelmed

4. **Traps**
   - Pit traps (slows attackers)
   - Alarm triggers

### Raid Combat

**Wave System:**
- Wave 1: Scout raiders (few)
- Wave 2: Main force (varies)
- Wave 3: Heavy (if main force succeeds)

**Player Choices:**
- Fight (combat, injuries, possible death)
- Negotiate (give resources, lose food but no injuries)
- Flee (lose some supplies, save everyone)

### Raid Outcomes

| Outcome | Effect |
|---------|--------|
| Victory | Reputation +10, loot from raiders |
| Pyrrhic | Won but injuries, -supplies |
| Defeat | Raiders take supplies, possible casualties |
| Negotiated | Lose 20% supplies, no injuries |

---

## FOOD PRODUCTION SYSTEM

### Food Types

#### Protein Sources
| Source | Production | Requires | Tech Level |
|--------|------------|----------|-------------|
| Hunting (deer) | 20 lbs/deer | Hunter + weapon | 1+ |
| Hunting (rabbit) | 2 lbs/rabbit | Hunter | 1+ |
| Fishing | 10 lbs/fish | Fishing skill | 1+ |
| Eggs (chicken) | 1 egg/day | Chicken | 2+ |
| Milk (cow) | 5 quarts/day | Cow | 3+ |
| Cheese | 1 lb/3 quarts milk | Cheese vats | 4+ |

#### Vegetable Sources
| Source | Production | Requires | Tech Level |
|--------|------------|----------|-------------|
| Ground Garden | 5 lbs/day | Farming 20+ | 1+ |
| Raised Beds | 10 lbs/day | Farming 40+ | 2+ |
| Greenhouse | 20 lbs/day | Farming 50+, glass | 3+ |
| Hydroponics | 40 lbs/day | Farming 70+, tech 5 | 5+ |

#### Fruit Sources
| Source | Production | Requires | Tech Level |
|--------|------------|----------|-------------|
| Berry Bushes | 2 lbs/day | Gathering | 1+ |
| Orchard Trees | 10 lbs/day (seasonal) | Farming 30+ | 3+ |
| Greenhouse Fruit | 5 lbs/day | Tech 4+ | 4+ |

### Food Nutrition Requirements

**Daily Requirements (Per Person):**
| Nutrient | Amount | Source |
|----------|--------|--------|
| Calories | 2000 | Meat, grains, fruit |
| Protein | 50g | Meat, eggs, dairy |
| Vitamins | Various | Vegetables, fruit |

**Balanced Meal Bonus:**
- Contains protein + veg + (fruit or grain)
- +10% contentment if balanced
- Deficiencies cause health issues

### Production Examples

**Starting Settlement (Level 1):**
- 1 Hunter (skill 25): 5-15 lbs meat/week
- 1 Gatherer: 10 lbs berries/week  
- 1 Farmer (skill 15): 20 lbs vegetables/week
- Total: ~35-45 lbs food/week
- For 4 people: Need ~56 lbs/week
- **SHORTFALL: -20 lbs/week** → Must scavenge

**Established Settlement (Level 3):**
- 2 Hunters (skill 35): 40 lbs meat/week
- 1 Dairy Cow: 35 quarts milk/week = cheese equivalent
- 3 Farmers (skill 50): 120 lbs vegetables/week
- Berry patches: 30 lbs/week
- **Total: ~225 lbs/week**
- For 20 people: Need ~140 lbs/week
- **SURPLUS: +85 lbs/week** → Surplus for trade

### Skill/Tech Modifiers

**Farmer Skill Modifiers:**
| Skill | Production |
|-------|-----------|
| 1-20 | Base x 0.5 |
| 21-40 | Base x 1.0 |
| 41-60 | Base x 1.5 |
| 61-80 | Base x 2.0 |
| 81-100 | Base x 2.5 |

**Tech Level Modifiers:**
| Tech Level | Soil Quality | Tool Quality | Total Modifier |
|------------|--------------|---------------|-----------------|
| 1 | 0.5 (poor) | 0.5 | x0.25 |
| 2 | 0.7 | 0.7 | x0.5 |
| 3 | 1.0 (normal) | 1.0 | x1.0 |
| 4 | 1.2 | 1.5 | x1.8 |
| 5 | 1.5 | 2.0 | x3.0 |

**Weather Modifiers:**
| Weather | Farming |
|---------|----------|
| Sunny | +25% |
| Cloudy | Normal |
| Rain | +10% |
| Snow | -50% |
| Storm | -75% |

---

## DIFFICULTY LEVELS

### Difficulty Settings

| Difficulty | Resource Find Rate | Crop Yield | Enemy Strength | Trader Frequency |
|------------|-------------------|------------|-----------------|-------------------|
| Peaceful | +50% | +25% | -50% | +50% |
| Easy | Normal | Normal | Normal | Normal |
| Normal | -10% | -10% | +10% | Normal |
| Hard | -25% | -25% | +25% | -25% |
| Brutal | -50% | -50% | +50% | -50% |

### Difficulty Recommendations

- **Peaceful:** Story-focused, don't want stress
- **Easy:** Relaxed gameplay
- **Normal:** Balanced challenge
- **Hard:** For experienced survivors
- **Brutal:** You're going to lose people

---

## EXAMPLE: DIFFICULTY IMPACT

**Scenario:** 4 survivors, Level 2 tech, 1 farmer (skill 30)

| Difficulty | Base Production | Modifiers | Final | People Fed |
|-----------|----------------|-----------|-------|-------------|
| Peaceful | 20 lbs | +25% = 25 | 4 | 4+ |
| Easy | 20 lbs | 0% = 20 | 4 | 4 |
| Normal | 20 lbs | -10% = 18 | 3.6 | 3-4 (struggling) |
| Hard | 20 lbs | -25% = 15 | 3 | 3 (hungry) |
| Brutal | 20 lbs | -50% = 10 | 2 | 2 (starving) |

---

*This creates the survival tension - you're always one bad harvest or raid away from crisis.*
