# OUTPOST ZERO - Mood, Quality & Trait Systems

## CORE CONCEPT: REAL LIFE IS HARD

**Goal:** Not everyone can be happy. Not everyone SHOULD be happy.
- Same conditions = different perspectives
- Mood affects EVERYTHING
- Traits modify everything
- Some people are just miserable - deal with it

---

## MOOD CONTAGION

### How Moods Spread

**Rule:** Characters are affected by others' moods.

```
MOOD NEARBY:

Character in area: PAUL (-20 happiness, miserable)
Nearby characters:
- Marcus (+5, "Paul is bringing everyone down")
- Sarah (-3, "Feeling the negativity")
- Elena (+2, "Doesn't let it affect her")

Result:
- Paul: -20 (baseline)
- Marcus: +5 -3 = +2 (affected but resilient)
- Sarah: +5 -3 = +2 (affected)
- Elena: +5 +2 = +7 (immune to mood contagion)
```

### Mood Transmission

| Person's Mood | Nearby Effect |
|---------------|---------------|
| Very Happy (+80+) | +2 to everyone |
| Happy (+60) | +1 to everyone |
| Neutral | No effect |
| Sad (-40) | -1 to everyone |
| Depressed (-60) | -2 to everyone |
| Miserable (-80) | -3 to everyone |

### Trait Modifiers for Contagion

| Trait | Effect |
|-------|--------|
| Empathic | +50% mood contagion received |
| Stoic | -50% mood contagion received |
| Cheerful | Immune to negative moods |
| Grumpy | -50% positive moods received |
| Optimist | Immune to sadness contagion |

---

## WORK QUALITY SYSTEM

### How Mood Affects Crafting

**Every craft/building/farming = Quality Check**

```
QUALITY CALCULATION:

Base Quality = Skill + Random(1-20)

Mood Modifier:
- Very Happy (+80): +10 quality
- Happy (+60): +5 quality
- Neutral: +0
- Sad (-40): -5 quality
- Depressed (-60): -10 quality

Trait Modifiers:
- Perfectionist: +2 always
- Lazy: -2 always  
- Slacker: -3 always
- Detail Oriented: +3 if not rushed

RESULT: Final Quality Score
```

### Quality Tiers

| Quality | Score | Name | Effect |
|---------|-------|------|--------|
| Legendary | 90+ | Masterwork | +50% stats |
| Excellent | 70-89 | Fine | +25% stats |
| Good | 50-69 | Normal | +0% (baseline) |
| Poor | 30-49 | Subpar | -25% stats |
| Terrible | <30 | Garbage | -50% stats, breaks fast |

### Quality Examples

```
CRAFT: Iron Knife
Skill: 40
Mood: Happy (+60) = +5

Roll: 15 (random)
Base: 55

Traits: Perfectionist (+2)

Final: 57 = GOOD quality!

═══════════════════════════

CRAFT: Iron Knife  
Skill: 40
Mood: Depressed (-60) = -10

Roll: 8 (random)
Base: 38

Traits: Lazy (-2)

Final: 26 = TERRIBLE!

Result:
"Good" knife: 25 damage, lasts 100 uses
"Terrible" knife: 12 damage, breaks after 20 uses
```

---

## TRAIT SYSTEM

### Trait Categories

#### Mood Modifiers

| Trait | Effect |
|-------|--------|
| Optimist | Never takes negative events as hard (-1 from negatives) |
| Pessimist | Takes everything hard (+1 to negatives) |
| Stoic | 50% less mood contagion |
| Empathic | 50% more mood contagion |
| Cheerful | +10 happiness per day naturally |
| Melancholic | -5 happiness per day naturally |
| Grumpy | -2 happiness when around others |
| Bright Side | Sees positives in negatives |

#### Work Modifiers

| Trait | Effect |
|-------|--------|
| Perfectionist | +2 quality always |
| Detail Oriented | +3 quality if not rushed |
| Lazy | -2 quality always |
| Slacker | -3 quality always |
| Hard Worker | +1 quality, +10% stamina use |
| Efficient | -20% time to complete |
| Slow | +20% time to complete |

#### Social Modifiers

| Trait | Effect |
|-------|--------|
| Charismatic | +25% relationship gains |
| Awkward | -25% relationship gains |
| Liar | Can fake relationships |
| Loyal | Never betrays |
| Betrayer | May betray for right price |

#### Health Modifiers

| Trait | Effect |
|-------|--------|
| Tough | -25% damage taken |
| Fragile | +25% damage taken |
| Fast Healer | 2x healing rate |
| Slow Healer | 0.5x healing rate |
| Pain Resistant | -50% pain effects |
| Hypochondriac | Thinks sick when not (-happiness) |

---

## PERSONALITY FROM EXPERIENCE

### How Traits Change

**Traits can be GAINED or LOST based on experiences:**

| Experience | Possible Trait Gain |
|------------|---------------------|
| Survived injury | Brave |
| Lost loved one | Melancholic |
| Betrayed | Suspicious |
| Many arguments | Grumpy |
| Happy childhood | Cheerful |
| Many failures | Pessimist |
| Mastered skill | Perfectionist |
| Always rushed | Slacker |

### Example: Trait Acquisition

```
PAUL - Day 100

Event: Paul loses his 5th friend to death

Result:
- Gained trait: "Melancholic"
- Effect: -5 happiness per day forever

Event: Paul finds medicine for sick child

Result:  
- Gained trait: "Hopeful"
- Effect: -2 from negatives

PAUL NOW:
- Melancholic (-5/day)
- Hopeful (-2 from negatives)
- Net: -7 baseline mood
```

---

## REALITY: NOT EVERYONE CAN BE HAPPY

### The Hard Truth

**In real life:** Some people are just miserable no matter what.

**In game:** We simulate this.

```
EXAMPLE SETTLEMENT - Day 50:

Conditions: 
- Food: Plenty
- Shelter: Good
- Safety: Secure
- Weather: Nice

Character happiness:

Marcus: 85 (Happy!)
"Life is good here. We survived!"

Sarah: 75 (Content)
"Pretty good. Miss my family sometimes."

Elena: 80 (Happy)
"This is better than I expected!"

Ryan: 25 (Miserable)
"Everything is terrible. I hate it here."

WHY RYAN IS MISERABLE:
- Traits: Pessimist, Melancholic
- Lost friend day 30 (-happiness)
- Chronic pain (-happiness)
- Hates rain (-happiness)
- Even when good: finds something wrong

OPTIONS:
1. Deal with it - Ryan is just miserable
2. Therapy - Can improve slowly
3. Kick him out - Some people don't belong
4. Find what triggers him - Fix root cause
```

---

## MOOD EFFECTS SUMMARY

### Daily Happiness Calculation

```
DAILY HAPPINESS CHANGE =

+ Base mood (from traits):
  - Cheerful: +10
  - Melancholic: -5
  - None: 0

+ From events today:
  - Good meal: +5
  - Rain: -3
  - Argument: -10
  - Partner time: +10
  ...etc

+ From mood contagion:
  - Nearby happy: +1
  - Nearby sad: -1

+ From health:
  - Injured: -5
  - Sick: -5
  
+ From work quality:
  - Made good item: +3
  - Made terrible item: -3

FINAL: New happiness for tomorrow
```

### Happiness Thresholds

| Happiness | Mood | Work Quality | Contagion |
|-----------|------|--------------|-----------|
| 80-100 | Ecstatic | +10 | +2 to all |
| 60-79 | Happy | +5 | +1 to all |
| 40-59 | Content | +0 | None |
| 20-39 | Sad | -5 | -1 to all |
| 0-19 | Depressed | -10 | -2 to all |
| <0 | Miserable | -15 | -3 to all |

---

## EXAMPLE: MISERABLE RYAN

```
DAY 47 - RYAN'S DAY

Morning Check:
- Mood: Miserable (-30 happiness)
- Traits: Pessimist (-negatives), Melancholic (-5/day)
- Chronic pain from old injury (-5)

Event: Sunny day!
- Everyone +2 happiness
- Ryan (Pessimist): "It'll rain tomorrow..."
- Ryan gets: +0 (negates!)

Event: Good breakfast!
- Everyone +3 happiness
- Ryan: "Not as good as before."
- Ryan gets: +1 (reduced!)

Work: Scavenge
- Skill: 50
- Mood: Miserable (-15 to quality)
- Result: Makes TERRIBLE knife (-15 damage)
- Ryan: "Even I can't do anything right."

Lunch:
- Sees Marcus laughing with Sarah
- Ryan: "Must be nice to not have problems."
- Marcus/Sarah: -1 each (mood contagion)

Dinner:
- Sits alone
- Ryan: "No one likes me anyway."
- No one sits with him (his attitude drives them off)

Night:
- Dreams about dead friend
- -10 happiness

═══════════════════════════════

DAY START: 25 happiness
DAY END: 20 happiness (-5)

Tomorrow will be worse.
```

---

## KICKING OUT MISERABLE CHARACTERS

### When to Banish

```
IF CHARACTER HAPPINESS < -50 for 14+ DAYS:

WARNING: {Name} is extremely unhappy
- Has been miserable for {X} days
- Affects morale of others
- May cause problems

OPTIONS:
[1] Intervention - Try to help
[2] Assign to easy work - Reduce stress
[3] Therapy - Use medical
[4] Banish - Remove from settlement
[5] Do nothing - Hope improves
```

### After Banishment

```
{name} has been banished!

Reaction:
- Some happy: "Good riddance!"
- Some sad: "That's sad..."
- Family: -20 happiness if family present
- Others: Varies

{name} may return as:
- Raider (if hostile)
- Trader (if neutral)
- Beggar (if lucky)
```

---

## IMPLEMENTATION: QUALITY FUNCTION

```python
def calculate_quality(character, task_skill):
    """Calculate work quality based on mood and traits"""
    
    # Base from skill
    quality = task_skill + random.randint(1, 20)
    
    # Mood modifier
    if character.happiness > 70:
        quality += 10
    elif character.happiness > 50:
        quality += 5
    elif character.happiness > 30:
        quality -= 5
    elif character.happiness > 10:
        quality -= 10
    else:
        quality -= 15
    
    # Traits
    if "Perfectionist" in character.traits:
        quality += 2
    if "Lazy" in character.traits:
        quality -= 2
    if "Slacker" in character.traits:
        quality -= 3
    if "Detail Oriented" in character.traits:
        quality += 3  # If not rushed
    
    return quality
```

---

## THE RESULT

**This creates real emergent stories:**

- "Ryan is miserable no matter what we do"
- "Elena makes amazing weapons because she's happy"
- "Paul's knives are terrible since Maryanne left"
- "Everyone's happier when Sarah is around - she's so cheerful!"
- "We had to banish Greg. He was poisoning the whole camp."

**That's Dwarf Fortress. That's real life.**

---

*Not everyone can be happy. That's okay.*
