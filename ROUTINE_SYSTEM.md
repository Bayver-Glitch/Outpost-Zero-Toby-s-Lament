# OUTPOST ZERO - Daily Routine & Event System

## CORE CONCEPT

**Characters run on AUTOPILOT for routine tasks.**
- Player assigns WORK
- Game simulates everything else
- Events happen DURING routine actions
- Tiny moments build to BIG stories

---

## TIME SYSTEM

### Time Blocks

| Time | Activity | Player Control |
|------|----------|----------------|
| 5:00 | Wake up | No |
| 5:30 | Hygiene | No |
| 6:00 | Breakfast | No |
| 6:30 | Personal time | No |
| 7:00 | WORK START | YES - player assigns |
| 12:00 | Lunch | No |
| 13:00 | WORK | YES - player assigns |
| 17:00 | Work end | No |
| 18:00 | Dinner | No |
| 19:00 | Free time | No |
| 21:00 | Sleep | No |

---

## MORNING WELLNESS CHECK

### What Happens at Wake Up

```
TIME: 5:00 - {Character} wakes up

=== WELLNESS CHECK ===

1. SICKNESS CHECK
   - Is sick?
   - Did sickness improve/worsen?
   - Heal check (Medical skill helps)

2. INJURY CHECK  
   - Healing progress?
   - Chronic pain?
   - Mobility affected?

3. HAPPINESS CHECK
   - Current happiness: 45
   - Last night's sleep quality
   - Dreams (random event!)

4. RELATIONSHIP MEMORY
   - Remember yesterday's interactions
   - Mood adjusted based on experiences
```

### Morning Event Examples

```
EVENT: Paul wakes up
"Paul groans as he gets out of bed. 
His leg still hurts from last week."

Result: -2 happiness (chronic pain)
        Movement speed -25%

---

EVENT: Sarah wakes up  
"Sarah feels great! She dreamed 
about her family yesterday."

Result: +5 happiness
        +10% work today

---

EVENT: Marcus wakes up
"Marcus hears birds singing. 
Beautiful morning!"

Result: +2 happiness (weather nice)
```

---

## ACTION EVENTS

### Every Action Has Potential Events

**Rule:** When character moves from A to B, check for events.

### Travel Events Table

| Event Type | Chance | Examples |
|------------|--------|----------|
| Accident | 5% | Stub toe, slip, trip |
| Encounter | 10% | Meet someone |
| Discovery | 3% | Find item |
| Weather effect | 15% | Cold, rain, nice |
| Memory | 5% | Think about something |

### Event Examples

```
ACTION: Paul walks to dresser

1. Base travel:
   - Paul walks to dresser
   - No event (70% chance)

2. Accident (5%):
   "Paul stubs his toe on the bed frame!
   'OW! Stupid leg...'"
   - -2 happiness
   - May need healer if bad

3. Memory (5%):
   "Paul remembers Maryanne from yesterday.
   He smiles slightly."
   - +3 happiness

---

ACTION: Sarah walks to kitchen

1. Encounter (10%):
   "Sarah passes Marcus in the hallway.
   Marcus: 'Morning, Sarah!'
   Sarah smiles."
   - Sarah: +2 happiness
   - Marcus: +1 happiness
   - Relationship +1

2. Weather (15%):
   "It's raining outside. Sarah 
   hates the rain."
   - -3 happiness

---

ACTION: Elena walks to work

1. Child (if kids present):
   "Little Tommy runs past, 
   almost trips Elena."
   - +2 happiness (likes kids)
   - Or -5 (doesn't like kids)
```

---

## INTERACTION EVENTS

### Character Meetings

When characters pass each other or work together:

```
MEETING: Paul passes Sarah in hallway

Paul has crush on Sarah (+20 attraction):
   "Sarah! Oh... hi. Good morning!"
   - Paul: +5 happiness
   - Paul: +1 relationship

Sarah dislikes Paul (-10 relationship):
   "Ugh, it's THAT guy..."
   - Sarah: -2 happiness
   - Sarah: -1 relationship

Neutral meeting:
   "Morning."
   "Morning."
   - No effect
```

### Work Together Events

```
TASK: Paul and Sarah both on Build

WORK EVENT: They work together

Good combination:
   "Paul and Sarah work well together.
   Sarah: 'Nice work on that joint!'
   Paul: 'Thanks...'"
   - Both: +3 happiness
   - Relationship +3

Bad combination:
   "Sarah keeps getting in Paul's way.
   'Watch it!' she snaps."
   - Paul: -3 happiness
   - Sarah: -2 happiness
   - Relationship -2
```

---

## DAILY ROUTINE SLOTS

### Routine Categories

| Category | Activities | Required |
|----------|------------|----------|
| Work | Job tasks | Player assigns |
| Sleep | Bed/sleeping | Building |
| Food | Eat meals | Kitchen/food |
| Hygiene | Wash, dress | Water |
| Religion | Pray, worship | Shrine/church |
| Family | Care for kids | Children present |
| Romance | Dates, time with partner | Partner present |
| Leisure | Hobbies, games, fishing | Time + materials |
| Social | Talk, visit friends | Other people |
| Medical | Get treatment | Medic + medicine |

### Filling the Schedule

```
PAUL'S DAILY SCHEDULE:

5:00 - Wake up (automatic)
5:30 - Hygiene: Paul goes to wash up
       → Event: No event
6:00 - Breakfast: Paul goes to kitchen
       → Event: Maryanne is there! +10 happiness!
6:30 - Personal: Paul gets dressed
       → Event: Outfit: Work clothes
7:00 - WORK: Assigned by player (Build)
       → Event: See below
12:00 - Lunch: Paul goes to kitchen
       → Event: Good meal! +3 happiness
13:00 - WORK: Assigned by player
       → Event: See below  
18:00 - Dinner: Paul goes to kitchen
       → Event: Sits near Maryanne +5 happiness
19:00 - Free time: Paul... 
       → [Check available: No kids, has partner]
       → Paul visits Maryanne!
21:00 - Sleep: Paul goes to quarters
```

---

## HAPPINESS FROM ROUTINES

### Sources of Daily Happiness

| Source | Amount | Conditions |
|--------|--------|------------|
| Good sleep | +5 | Comfortable bed |
| Bad sleep | -5 | No bed/cold |
| Good breakfast | +3 | Cook available |
| Good dinner | +5 | Cook available |
| Weather nice | +2 | Sunny, mild |
| Weather bad | -3 | Rain, cold |
| Partner time | +10 | Romance present |
| Family time | +8 | Kids present |
| Friend chat | +5 | Friends nearby |
| Alone time | +3 | Introverts |
| Hobbies | +5 | Has materials |
| Religion | +5 | Prayed |
| Health good | +2 | Not sick/injured |

### Sources of Daily Unhappiness

| Source | Amount | Conditions |
|--------|--------|------------|
| Hungry | -10 | No food |
| Sick | -5 | Illness |
| Injured | -5 | Injuries |
| Pain | -3 | Chronic pain |
| Rain | -3 | Bad weather |
| Cold | -5 | Freezing |
| Alone | -5 | Extrovert needs people |
| No work | -5 | Bored |
| Argument | -10 | Negative interaction |

---

## RELATIONSHIP MEMORY

### How Relationships Work

**Every interaction is remembered!**

```
RELATIONSHIP TRACKING:

Paul → Sarah:
- Day 1: +5 (said hi)
- Day 2: +10 (worked together well)
- Day 3: +15 (she complimented him)
- Day 5: +2 (just said hi)
- Day 7: -5 (she snapped at him)
- Day 8: 0 (avoided him)
- Total: +27 (Friend level)
```

### Relationship Levels

| Score | Level | Behavior |
|-------|-------|----------|
| -50+ | Enemy | Avoid, gossip |
| -20 | Dislike | Cold, rude |
| 0 | Neutral | Basic politeness |
| +20 | Acquaintance | Friendly |
| +40 | Friend | Supportive |
| +60 | Close | Best friends |
| +80 | Soul Mate | Everything shared |

### How Relationships Affect Interactions

```
Paul (Friend +27) meets Sarah:
   "Hey Sarah! How's it going?"
   +1 relationship

Paul (Enemy -30) meets Sarah:
   "...*grunt*..." 
   "So rude..."
   -2 happiness each
```

---

## PERSONALITY FROM EXPERIENCE

### How Events Shape Personality

**Traits can CHANGE based on experiences:**

| Experience | Trait Change |
|------------|--------------|
| Survived pain | +Brave |
| Lost loved one | +Melancholic |
| Betrayed | +Suspicious |
| Many arguments | +Grumpy |
| Happy childhood | +Cheerful |
| Too many losses | +Depressed |

### Long-term Mood

```
CHARACTER MOOD TRACKING:

Paul - Last 7 days:
- Day 41: -5 (argument)
- Day 42: +10 (Maryanne talked)
- Day 43: -15 (injury)
- Day 44: +5 (good sleep)
- Day 45: -5 (rain)
- Day 46: +10 (Maryanne smiled)
- Day 47: +3 (normal day)

Mood Trend: Slightly happy
Overall disposition: Mixed

If trend is negative for 14+ days:
   → Character may develop depression
   → May need therapy
   → May leave settlement
```

---

## IMPLEMENTATION: EVENT FLOW

### Game Loop - Each Character's Turn

```
FOR EACH CHARACTER:
   
   1. MORNING CHECK
      - Wellness (sick/injured?)
      - Happiness adjustment from sleep
      
   2. SCHEDULE: WAKE → HYGIENE
      - Event check: Accident? Memory?
      
   3. SCHEDULE: HYGIENE → BREAKFAST
      - Event check: Weather? Encounter?
      
   4. SCHEDULE: BREAKFAST → WORK
      - Event: Who is there?
      - Food quality check
      
   5. WORK (Player assigned)
      - Work events
      - Co-worker interactions
      
   6. LUNCH → WORK → DINNER
      - Similar checks
      
   7. FREE TIME
      - Available activities check
      - Partner? Family? Friends? Hobbies?
      
   8. SLEEP
      - Sleep quality
      - Dreams (random!)
      - Prepare for next day
```

---

## EXAMPLE: PAUL'S DAY (Detailed)

```
DAY 47 - PAUL'S DAY

═══════════════════════════════════

5:00 - PAUL WAKES UP
"Wellness Check:"
- Health: 85% (leg injury healing)
- Sickness: None
- Happiness: 35 (was 40 yesterday)
- Leg hurts (-2 from chronic pain)

5:30 - HYGIENE
Action: Walk to wash area (10 meters)
Event Check: 
- Roll: 85 (no event)
Result: Clean, ready

6:00 - BREAKFAST
Action: Walk to kitchen
Event: Passes Sarah in hallway!
"Maryanne isn't here... but Sarah nods."
Result: +1 happiness
        Relationship: Paul→Sarah +1

Kitchen Event:
"Good breakfast today! (Cook skill high)"
Result: +5 happiness

6:30 - DRESS
Action: Walk to room, get work clothes
Event: Finds old photo of Maryanne
"Still keeps this..."
Result: +2 happiness (memory)

7:00 - WORK: BUILD
Assigned: Build new Workshop
Event: Works with Elena
Working together:
"Elena: 'Nice hammer work!'
Paul: 'Thanks...'"
Result: +3 happiness
        Paul→Elena +2

12:00 - LUNCH
Action: Walk to kitchen
Event: Rain today!
"I hate the rain..."
Result: -3 happiness

Lunch: Basic meal
Result: +2 happiness

13:00 - WORK
Action: Continue building
Event: Hammer slips, hits hand
"Ow! Dammit!"
Result: -2 happiness
        Minor injury? (check)

18:00 - DINNER
Action: Walk to kitchen
Event: MARYANNE IS THERE!
"Maryanne: 'Sit with us, Paul!'"
Result: +15 happiness!!!
        +5 from good meal
        +10 from Maryanne

19:00 - FREE TIME
Options: 
- Visit Maryanne (+10)
- Read book (+3)
- Sit alone (-2)

Choice: Visit Maryanne!
Event: They talk for an hour
"Maryanne: 'You're sweet, Paul.'"
Result: +10 happiness
        Relationship +5

21:00 - SLEEP
Action: Walk to quarters
Event: Passes rainy window
"Another day..."
Result: -1 happiness

Sleep quality: Good (has bed)
Result: +5 tomorrow

═══════════════════════════════════

DAY 47 TOTALS:
Starting happiness: 40
Ending happiness: 71 (+31!)

Biggest gains:
+15 (Maryanne at dinner)
+10 (Free time with Maryanne)
+5 (Good meals)

Biggest losses:
-3 (Rain)
-2 (Minor accident)
-2 (Chronic pain)

TOMORROW:
Happiness starts at 71!
```

---

## THE RESULT: EMERGENT STORIES

### What This Creates

**Instead of:**
- "Paul is sad because -10 happiness"

**We get:**
- "Paul stubbed his toe, it started raining, but then Maryanne talked to him at dinner and he's SO happy today"

**This generates stories like:**
- "Remember when Paul finally told Maryanne he liked her?"
- "Ryan hasn't been the same since his accident"
- "Marcus and Elena are always arguing lately"
- "The whole camp is happier when the weather is good"

**This is Dwarf Fortress magic!**

---

*Every action is a story opportunity.*
