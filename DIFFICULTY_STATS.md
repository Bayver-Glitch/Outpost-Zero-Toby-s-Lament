# OUTPOST ZERO - Difficulty & New Stats System

## DIFFICULTY TRAIT DISTRIBUTION

### Easy Mode

**Trait Distribution:**
- 2 GOOD traits (positive only)
- 1 MINOR BAD trait (low impact)
- Chance of good traits: High

**Minor Bad Traits (Easy):**
- Lazy (work output -10%)
- Forgetful (occasional mistakes)
- Clumsy (occasional accidents)
- Flaky (sometimes unreliable)
- Procrastinator (slight work delay)
- Modest (no real penalty)

**No major flaws, no game-breaking traits.**

---

### Normal Mode

**Trait Distribution:**
- 1 GOOD trait
- 1 BAD trait (any)
- Chance: Standard

**Bad Traits Available:**
- Any from the negative list
- Pessimist, Lazy, Arrogant, Rude, etc.

---

### Hard Mode

**Trait Distribution:**
- 1 GOOD trait (rare)
- 2 BAD traits (common)
- Chance: Low good, high bad

**Often Includes:**
- Pessimist, Lazy, Greedy, Cowardly
- Worse work quality
- Mood contagion worse

---

### Custom / Story Characters

**Manual Spawning:**
- Any trait combination
- For quests, special events
- Designed for storytelling

---

## NEW STATS SYSTEM

### INTELLECT (IQ-like)

**Range:** 50-150 (100 = average)

**Effects:**
- Learning speed for skills
- CAPS on certain skills
- Complex task success rate

**Skill Caps by Intellect:**

| Intellect | Max Skill Achievable |
|-----------|---------------------|
| 50 | 30 (Basic only) |
| 70 | 50 (Intermediate) |
| 90 | 70 (Advanced) |
| 110 | 85 (Expert) |
| 130 | 95 (Master) |
| 150 | 100 (Legendary) |

**Examples:**
- Medical: Requires Intellect 80+
- Science Research: Requires Intellect 90+
- Engineering: Requires Intellect 85+

---

### STAMINA (Endurance)

**Range:** 50-150 (100 = average)

**Effects:**
- How long before needing rest
- Movement speed
- Work duration before tired

**Stamina Effects:**

| Stamina | Work Duration | Movement | Rest Need |
|---------|---------------|----------|------------|
| 50 | 50% | Slow | Needs rest often |
| 100 | 100% | Normal | Normal |
| 150 | 150% | Fast | Rarely needs rest |

**Affected by:**
- Traits (Athletic +20, Lazy -20)
- Injuries (leg injuries = -30)
- Sickness (-20)
- Age (older = -5 per 10 years)

---

### CHARISMA (Charm)

**Range:** 50-150 (100 = average)

**Effects:**
- How likeable character is
- Better first impressions
- Better trade prices
- Easier to recruit
- Persuasion success

**Charisma Effects:**

| Charisma | First Impression | Trade | Recruit Chance |
|----------|------------------|-------|----------------|
| 50 | Disliked | -20% | -30% |
| 100 | Neutral | Normal | Normal |
| 150 | Loved | +20% | +30% |

**Example:**
- Character with Charisma 140 can be rude but still likeable!
- "Yeah he's gruff but you can't help liking him"

---

### HEALTH (HP Max)

**Range:** 50-150 (100 = average)

**Effects:**
- Total HP
- Recovery speed
- Survival chance

**Health Effects:**

| Health | Max HP | Recovery | Survival |
|--------|--------|----------|----------|
| 50 | 50 | Slow | Low |
| 100 | 100 | Normal | Normal |
| 150 | 150 | Fast | High |

**Affected by:**
- Traits (Tough +20, Fragile -20)
- Permanent injuries (-10 to -30)
- Age (-5 per 10 years after 40)

---

## INJURY EFFECTS ON STATS

### Leg Injuries

| Injury | Stamina | Movement | Special |
|--------|---------|----------|---------|
| Sprained Ankle | -10 | -25% | Can't run |
| Broken Leg | -30 | -50% | Needs crutches |
| Gimp Leg | -25 | -30% | Permanent -25% |
| Torn ACL | -20 | -35% | Chronic |

### Arm Injuries

| Injury | Work Quality | Skills Affected |
|--------|--------------|------------------|
| Broken Arm | -50% | All 2-handed |
| Gimp Hand | -25% | Fine motor |
| Lost Finger | -15% | Precision tasks |

### Head Injuries

**Most Serious!**

| Injury | Intellect | Memory | Skills Lost |
|--------|-----------|--------|--------------|
| Concussion | -10 | -20% | None |
| Head Wound | -20 | -30% | May lose 1-5 skill |
| Brain Damage | -40 | -50% | Loses advanced skills |

**Example:**
```
Dr. Smith is attacked!
- Survives but: BRAIN DAMAGE
- Intellect: 120 → 80
- Medical Skill: 90 → 45 (can no longer do advanced medicine!)
- "I... I used to know how to do this..."
```

---

## SKILL-SPECIFIC TRAITS

### FARMING (4 traits)

| Trait | Effect |
|-------|--------|
| Green Thumb | +20 farming quality, +10% speed |
| Farm Hand | +15 farming output, -10% fatigue |
| Botanist | +25 crop yield, can identify plants |
| Harvest King | +30 harvest yield, +luck |

### COOKING (4 traits)

| Trait | Effect |
|-------|--------|
| Chef's Kiss | +20 cooking quality, faster |
| Spice Master | +15 food happiness bonus |
| Preserver | +25 food preservation |
| Baker | +20 bread/dessert quality |

### SCAVENGING (4 traits)

| Trait | Effect |
|-------|--------|
| Scavenger | +20 find chance |
| Looter | +15 rare item chance |
| Quick Hands | +20 speed, less rest |
| Expert Finder | +25 valuable finds |

### HUNTING (4 traits)

| Trait | Effect |
|-------|--------|
| Marksman | +20 accuracy |
| Tracker | +30 track finding |
| Trapper | +25 trap success |
| Beastmaster | +20 animal combat |

### COMBAT (4 traits)

| Trait | Effect |
|-------|--------|
| Warrior | +20 melee damage |
| Fighter | +15 defense |
| Brawler | +10 all combat |
| berserker | +25 damage, -10 defense |

### MEDICAL (4 traits)

| Trait | Effect |
|-------|--------|
| Healer | +25 healing rate |
| Surgeon | +15 surgery success |
| Medic | +20 triage efficiency |
| Herbalist | +20 herbal medicine |

### BUILDING (4 traits)

| Trait | Effect |
|-------|--------|
| Builder | +20 build speed |
| Architect | +15 build quality |
| Craftsman | +10 all crafts |
| Efficient | -15 material use |

### SCIENCE/RESEARCH (4 traits)

| Trait | Effect |
|-------|--------|
| Researcher | +25 research speed |
| Inventor | +15 invention chance |
| Analyzer | +20 success chance |
| Experimenter | +10 breakthrough |

### SOCIAL (4 traits)

| Trait | Effect |
|-------|--------|
| Diplomat | +25 persuasion |
| Negotiator | +20 trade prices |
| Leader | +15 group bonus |
| Orator | +20 speech/charm |

### SCOUTING (4 traits)

| Trait | Effect |
|-------|--------|
| Pathfinder | +20 navigation |
| Observer | +25 spot chance |
| Stealthy | +30 stealth |
| Explorer | +20 new area find |

### FISHING (4 traits)

| Trait | Effect |
|-------|--------|
| Angler | +25 catch rate |
| Fisherman | +15 any fish |
| Patience | +20 wait bonus |
| Net Caster | +20 net catch |

---

## TRAIT AFFECTS NEW STATS

### Intellect Traits

| Trait | Intellect Effect |
|-------|------------------|
| Intelligent | +20 Intellect |
| Wise | +15 Intellect, +learn |
| Curious | +10 Intellect |
| Slow | -20 Intellect |
| Naive | -15 Intellect |
| Forgetful | -10 Intellect |

### Stamina Traits

| Trait | Stamina Effect |
|-------|----------------|
| Athletic | +20 Stamina |
| Enduring | +15 Stamina |
| Energetic | +10 Stamina |
| Lazy | -20 Stamina |
| Tired | -15 Stamina |
| Slow | -10 Stamina |

### Charisma Traits

| Trait | Charisma Effect |
|-------|------------------|
| Charismatic | +25 Charisma |
| Charming | +20 Charisma |
| Witty | +15 Charisma |
| Awkward | -20 Charisma |
| Rude | -15 Charisma |
| Grumpy | -10 Charisma |

### Health Traits

| Trait | Health Effect |
|-------|--------------|
| Tough | +20 Health |
| Healthy | +15 Health |
| Robust | +10 Health |
| Fragile | -20 Health |
| Sickly | -15 Health |
| Weak | -10 Health |

---

## IMPLEMENTATION EXAMPLE

```python
class Survivor:
    def __init__(self):
        # New stats
        self.intellect = random.randint(70, 130)
        self.stamina = random.randint(70, 130)
        self.charisma = random.randint(70, 130)
        self.health_max = random.randint(70, 130)
        
        # Skill-specific traits
        self.skill_traits = {}  # {skill: [trait1, trait2]}
        
    def assign_traits_by_difficulty(difficulty):
        if difficulty == "easy":
            # 2 good + 1 minor bad
        elif difficulty == "normal":
            # 1 good + 1 any bad
        elif difficulty == "hard":
            # 1 good (rare) + 2 bad
```

---

## EXAMPLE CHARACTERS

### Easy Character

```
Name: Sarah
Intellect: 110 (High)
Stamina: 100 (Normal)
Charisma: 130 (Very High!)
Health: 100 (Normal)

Traits:
- Cheerful (mood)
- Compassionate (mood)

Skill Traits:
- Medical: Healer (+25 healing)
- Cooking: Chef's Kiss (+20 quality)

Personality: She's amazing! Great doctor, 
great cook, everyone loves her!

This is an EASY mode character.
```

---

### Hard Character

```
Name: Ryan
Intellect: 65 (Low!)
Stamina: 55 (Very Low!)
Charisma: 45 (Disliked)
Health: 70 (Poor)

Traits:
- Pessimist (mood)
- Lazy (-20 stamina!)
- Arrogant (-charisma)

Skill Traits:
- None! Can't excel at anything!

Personality: He's bad at everything, 
unhappy, tired, and people don't like him.

This is a HARD mode character.
```

---

## DIFFICULTY SETTINGS

### Character Generation by Difficulty

```
EASY:
- Intellect: 80-130
- Stamina: 80-130  
- Charisma: 80-130
- Health: 80-130
- Traits: 2 good + 1 minor bad
- Skill Traits: 1 guaranteed

NORMAL:
- Intellect: 70-130
- Stamina: 70-130
- Charisma: 70-130
- Health: 70-130
- Traits: 1 good + 1 any bad
- Skill Traits: 50% chance

HARD:
- Intellect: 50-120
- Stamina: 50-120
- Charisma: 50-120
- Health: 50-120
- Traits: 1 good (rare) + 2 bad
- Skill Traits: 25% chance
```

---

*Stats make characters. Traits tell their stories.*
