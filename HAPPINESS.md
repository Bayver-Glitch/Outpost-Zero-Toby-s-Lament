# OUTPOST ZERO - Happiness & Contentment System

## CORE CONCEPT

Every survivor has a **Contentment Score (0-100)**:
- 0-20: Near breaking point (may leave or cause problems)
- 20-40: Unhappy, grumpy, less productive
- 40-60: Content but not happy
- 60-80: Happy, productive, positive
- 80-100: Ecstatic, boosted stats

**Daily Changes:**
- Base: -1 per day (things always get worse)
- Situational modifiers: +/- per day based on conditions

---

## NEEDS SYSTEM

### 5 Core Needs (Each 0-100):

| Need | Description | Affects | Low Penalty |
|------|-------------|---------|-------------|
| Fullness | Hunger | Productivity, Health | -20 work efficiency |
| Safety | Security | Stress, Health | +10 stress/day |
| Comfort | Physical comfort | Contentment | -10 contentment |
| Social | Connection | Mood, Loyalty | -5 contentment/day |
| Purpose | Meaningful work | Loyalty, Mood | -15 loyalty/month |

### Need Levels Affect:

| Fullness Level | Efficiency |
|----------------|------------|
| 0-20% | -40% work |
| 20-40% | -20% work |
| 40-60% | Normal |
| 60-80% | +10% work |
| 80-100% | +20% work, +5 contentment |

---

## TRAITS SYSTEM

### Trait Categories

#### 1. Environmental Traits (Innate)

| Trait | Effect |
|-------|--------|
| **Afraid of the Dark** | -2 contentment/hour in darkness, -5 if panic |
| **Loves the Dark** | +1 contentment/hour in darkness |
| **Cave Dweller** | +2 contentment in enclosed spaces |
| **Claustrophobic** | -2 contentment in enclosed spaces |
| **Heat Seeker** | +1 contentment near fire/heat |
| **Cold Tolerant** | +1 contentment in cold weather |
| **Cold Intolerant** | -2 contentment in cold weather, -5 if freezing |
| **Storm Chaser** | +1 contentment during storms |
| **Storm Fearing** | -3 contentment during storms |

#### 2. Sleep Traits (Innate)

| Trait | Effect |
|-------|--------|
| **Light Sleeper** | Wakes easily (+25% watch efficiency), -1 contentment if woken |
| **Heavy Sleeper** | Hard to wake, +1 contentment from sleep |
| **Needs Less Sleep** | Functions at 90% with 5 hours, 100% with 6 hours |
| **Needs More Sleep** | Only 80% at 8 hours, 100% at 10 hours |
| **Sleepwalker** | 10% chance of wandering at night (injury risk) |
| **Night Terrors** | -5 contentment if woke others |

#### 3. Social Traits (Innate)

| Trait | Effect |
|-------|--------|
| **People Person** | +1 contentment per friendly interaction |
| **Loner** | -2 contentment when >3 people nearby, +1 when alone |
| **Social Butterfly** | +2 contentment at gatherings |
| **Gossip** | Gains info 25% faster, -2 contentment if excluded |
| **Empath** | +10% teaching effectiveness, takes others' moods harder |
| **Grudge Holder** | -5 to -20 relationship with anyone who wronged them |
| **Forgiving** | Relationships decay 50% slower |

#### 4. Work Traits (Innate)

| Trait | Effect |
|-------|--------|
| **Hard Worker** | +15% work efficiency, +1 contentment when productive |
| **Lazy** | -20% work efficiency, -2 contentment if forced to work hard |
| **Perfectionist** | +10% quality on work, -2 contentment if rushed |
| **Multitasker** | Can do 2 tasks in one day (stamina cost +25%) |
| **Specialist** | +20% efficiency in primary skill, -10% in others |

#### 5. Combat/Trauma Traits (Developed)

| Trait | Trigger | Effect |
|-------|---------|--------|
| **Battle Scared** | Survives violent encounter | -2 contentment in combat |
| **Trigger Happy** | Uses weapon successfully | +1 contentment after combat |
| **Pacifist** | Sees violence | -5 contentment, -10 if involved |
| **Hardened** | Survives 3+ violent events | +2 contentment under threat |
| **Shell Shocked** | Nearly dies in combat | -5 anytime combat occurs |

#### 6. Discovery Traits (Developed)

| Trait | Trigger | Effect |
|-------|---------|--------|
| **Bookworm** | Reads 5+ books | +2 contentment while reading |
| **Curious** | Discovers new thing | +3 contentment for discovery |
| **Tech Hater** | Uses advanced tech | -3 contentment around electricity/computers |
| **Tech Lover** | Around electricity/computers | +2 contentment |
| **Explorer** | In new zone | +2 contentment |

#### 7. Health/Mental Traits (Innate/Developed)

| Trait | Effect |
|-------|--------|
| **Optimist** | -50% stress gain, +1 daily contentment |
| **Pessimist** | +50% stress gain, -1 daily contentment |
| **Stoic** | Immune to mood swings, +2 contentment in crisis |
| **Hypochondriac** | -2 contentment if any health issue |
| **Pain Intolerant** | -3 contentment per injury |
| **Pain Tolerant** | -1 contentment per injury |
| **Lucky** | 10% chance to avoid bad events |
| **Unlucky** | 10% chance bad events are worse |

#### 8. Appearance/Status Traits (Innate)

| Trait | Effect |
|-------|--------|
| **Vain** | -2 contentment if appearance affected |
| **Humble** | +1 contentment regardless of appearance |
| **Status Seeker** | +2 contentment when given authority |
| **Follower** | +1 contentment following others |

---

## TRAIT ACQUISITION

### Innate (Random at Character Creation)
- 1-3 positive traits (30% chance each)
- 1-2 negative traits (40% chance each)

### Developed Over Time (Examples)

**Afraid of the Dark:**
- Trigger: Trapped in darkness for 24+ hours
- Chance: 40%
- Permanent

**Battle Scared:**
- Trigger: Survives combat with <20% health
- Chance: 60%
- Permanent

**Hardened:**
- Trigger: Survives 3+ violent events
- Chance: 70%
- Permanent

**Pacifist:**
- Trigger: Witnessed violent death
- Chance: 30%
- Permanent

**Night Owl:**
- Trigger: Consistently active at night for 30+ days
- Chance: 50%
- Permanent

---

## DAILY CONTENTMENT CALCULATIONS

### Base Changes (Per Day)

```python
def calculate_daily_contentment(survivor):
    change = -1  # Base decay
    
    # Environmental
    if is_dark and "Afraid of the Dark" in traits:
        change -= 2
    if is_dark and "Loves the Dark" in traits:
        change += 1
    if is_cold and "Cold Intolerant" in traits:
        change -= 2
    if is_storming and "Storm Fearing" in traits:
        change -= 3
        
    # Sleep quality
    if slept_well:
        change += 2
    elif slept_poorly:
        change -= 3
        
    # Social
    if had_social_interaction and "People Person" in traits:
        change += 1
    if alone_too_long and "Loner" not in traits:
        change += 1  # Normal people need some company
        
    # Work
    if worked_hard and "Hard Worker" in traits:
        change += 1
    if worked_hard and "Lazy" in traits:
        change -= 2
        
    # Health
    if injured and "Pain Intolerant" in traits:
        change -= 3
        
    return change
```

### Mood Effects on Contentment

| Mood | Contentment Change |
|------|-------------------|
| Happy | +2/day |
| Content | +0/day |
| Anxious | -2/day |
| Sad | -3/day |
| Depressed | -5/day |
| Angry | -4/day |
| Furious | -6/day |

---

## CONTENTMENT EFFICIENCY TABLE

| Contentment | Work Efficiency | Combat | Healing | Learning |
|------------|-----------------|--------|---------|----------|
| 90-100 | +25% | +15% | +25% | +15% |
| 70-89 | +10% | +10% | +10% | +10% |
| 50-69 | 0% | 0% | 0% | 0% |
| 30-49 | -15% | -10% | -15% | -10% |
| 10-29 | -30% | -25% | -30% | -20% |
| 0-9 | -50% | -40% | -50% | -30% |

---

## CHARACTERS HARD TO PLEASE EXAMPLES

### "High Maintenance" Characters (Start with 2-3 negative traits)

**Example: DIANE**
- Age: 32, Former city person
- Traits: Claustrophobic (-2 in buildings), Cold Intolerant (-2 in cold), Hypochondriac (-2 with any injury), Vain (-2 if dirty/rumpled)
- Sleep: Light Sleeper (-1 if woken)
- Base contentment: Starts at 45 (already hard to please)
- **Result:** Needs warm shelter, good bed, constant reassurance. If any comfort issue, contentment drops fast.

### "Easy Going" Characters (Start with 2-3 positive traits)

**Example: MIKE**
- Age: 45, Former homeless veteran
- Traits: Stoic (+2 in crisis), Hardened (+2 under threat), Pain Tolerant (-1 injury effect), Hard Worker (+15% work)
- Sleep: Heavy Sleeper (+1 from sleep)
- Base contentment: Starts at 70
- **Result:** Doesn't complain, works hard, doesn't stress. Good for base operations.

### "Problem Child" (Develops bad traits)

**Example: Your character after a traumatic event**
- Survived being trapped in dark mine for 3 days
- Now has: Afraid of the Dark (-2/hour in dark), Shell Shocked (-5 in combat), Nightmare (-5 if woken)
- Sleeps poorly, anxious in dark, can't handle stress
- **Result:** Needs special accommodation, night shift is impossible

---

## MOOD SYSTEM

### Mood vs Contentment

**Mood** = Short-term emotional state (hours to days)
**Contentment** = Long-term satisfaction (days to weeks)

- Mood can push contentment up or down
- Long-term low contentment creates permanent mood shifts
- Extreme events can instantly change mood

### Mood Transitions

| Current Mood | Days at <30% Contentment | Days at >70% Contentment |
|--------------|-------------------------|-------------------------|
| Happy | → Anxious | → Happy |
| Content | → Anxious | → Happy |
| Neutral | → Sad | → Content |
| Anxious | → Angry | → Content |
| Sad | → Depressed | → Neutral |
| Angry | → Furious | → Anxious |

---

## GROUP EFFECTS

### When Multiple Characters Have Traits

**"People Person"** gives +1 to everyone in social interactions
**"Grudge Holder"** makes other characters nervous around them
**"Optimist"** slightly boosts nearby characters' mood (+0.5)

### Faction Bonuses

| Group Trait | Effect |
|-------------|--------|
| Mostly Happy | +5% work efficiency for all |
| Mostly Sad | -10% work efficiency for all |
| Mixed Relationships | Random events +25% |
| Love Triangle | One character -20% efficiency |
| Best Friends (3+) | +10% efficiency when working together |

---

## EXAMPLE DAY CONTENTMENT CALCULATIONS

### Day 15 - Survivor: MARCUS

**Morning:**
- Woke in warm bed: +1
- Ate good breakfast: +1
- Assigned to farming (not favorite): +0

**Midday:**
- Worked hard in fields: +0 (not "Hard Worker")
- Sunny weather, good day: +0
- Had lunch with Sarah: +1 ("People Person" interaction)

**Evening:**
- Cold night coming, he's "Cold Intolerant": -2
- Has no heater in room: -1 more
- Talked to friend at fire: +1

**Day Total:** +0 (break even)

**But wait!** - His friend Ryan caused his arm to break last week.
- He's "Grudge Holder" toward Ryan: -3 every interaction
- He got -3 from seeing Ryan at dinner

**Final Daily Change:** -3

**Starting Contentment:** 65
**Ending Contentment:** 62

---

## IMPLEMENTATION NOTES

### Priority for MVP
1. Basic contentment (0-100)
2. 5-10 core traits (mix positive/negative)
3. Sleep quality effects
4. Work assignment effects

### Phase 2
- Mood transitions
- Developed traits
- Group dynamics

### Phase 3
- Complex relationships
- Full trait system
- AI-powered conversations (bar scenes)

---

*This system creates characters who feel real - some are nightmares to manage, some are rocks you can count on. The variety is what makes the stories.*
