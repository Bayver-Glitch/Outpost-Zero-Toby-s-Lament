# OUTPOST ZERO - Character Systems Design

## FULL CHARACTER STATS

### Basic Information
| Stat | Description | Range |
|------|-------------|-------|
| Name | Character name | String |
| Age | Years old | 5-90 |
| Sex | Biological sex | Male/Female/Other |
| Race | Self-identified | String |
| Height | Feet/inches or cm | 3'0" - 7'0" |
| Weight | Pounds/kg | 50 - 400 lbs |
| Appearance | Physical description | Text |

### Disposition/Personality
| Trait | Description | Range |
|-------|-------------|-------|
| Mood | Current state | Happy, Content, Neutral, Anxious, Sad, Depressed, Angry, Furious |
| Disposition | Base personality | Joyful, Calm, Aloof, Grumpy, Mean, Kind, Serious, Playful |
| Stress | Current stress level | 0-100 |
| Trust | How much they trust the player/leader | 0-100 |
| Loyalty | Commitment to settlement | 0-100 |

### Personality Traits (Select 2-4)
Positive:
- Brave - Not scared of danger
- Compassionate - Cares about others
- Curious - Wants to learn
- Honest - Always tells truth
- Patient - Calm under pressure
- Creative - Good at problem-solving
- Loyal - Stick by friends
- Humble - Doesn't boast

Negative:
- Cowardly - Avoids danger
- Selfish - Puts self first
- Deceitful - Lies when convenient
- Impulsive - Acts without thinking
- Lazy - Avoids work
- Arrogant - Thinks they're better
- Cold - Doesn't show emotion
- Hotheaded - Explosive temper

### Education Level
| Level | Description | Reading Ability |
|-------|-------------|-----------------|
| Illiterate | Cannot read | None |
| Basic | Can read simple words | Basic signs, labels |
| Reading/Writing | Can read/write basic | Children's books, simple notes |
| Grade School | Elementary education | Simple novels, newspapers |
| High School | Secondary education | Novels, technical manuals |
| College | University degree | Academic papers, complex texts |
| Masters/PhD | Advanced degree | Technical/scientific papers |

**Why education matters:**
- Higher education = faster learning
- Can understand complex books
- Can teach others
- Can operate advanced equipment
- Can invent new things

---

## SKILLS SYSTEM

### Skill Categories

#### Survival Skills (Available from start)
| Skill | Description | Scale |
|-------|-------------|-------|
| Scavenging | Finding items in wasteland | 1-100 |
| Hunting | Tracking and killing game | 1-100 |
| Fishing | Catching fish | 1-100 |
| Gathering | Finding wild plants, berries | 1-100 |
| Woodcutting | Chopping trees | 1-100 |
| Athletics | Physical tasks, running | 1-100 |
| Stealth | Avoiding detection | 1-100 |
| Endurance | Physical stamina | 1-100 |

#### Combat Skills (Unlock via discovery)
| Skill | Description | Scale |
|-------|-------------|-------|
| Melee | Hand-to-hand combat | 1-100 |
| Ranged | Guns, bows, thrown weapons | 1-100 |
| Tactics | Strategic combat | 1-100 |
| First Aid | Treat wounds | 1-100 |
| Evasion | Dodging attacks | 1-100 |

#### Production Skills (Unlock via discovery)
| Skill | Description | Scale |
|-------|-------------|-------|
| Farming | Grow crops | 1-100 |
| Cooking | Prepare food | 1-100 |
| Preservation | Smoke, salt, can food | 1-100 |
| Crafting | Make items | 1-100 |
| Blacksmithing | Forge metal items | 1-100 |
| Tailoring | Make clothing | 1-100 |
| Construction | Build structures | 1-100 |
| Mechanical | Repair vehicles | 1-100 |
| Electrical | Wire, generators | 1-100 |

#### Intellectual Skills (Unlock via discovery)
| Skill | Description | Scale |
|-------|-------------|-------|
| Teaching | Train others | 1-100 |
| Medicine | Advanced healing | 1-100 |
| Science | Research, experiments | 1-100 |
| Engineering | Design structures | 1-100 |
| Computing | Program computers | 1-100 |
| Chemistry | Create chemicals | 1-100 |
| Biology | Understand plants/animals | 1-100 |
| Physics | Understand technology | 1-100 |

### Skill Checks
- Roll = Skill + d100
- Difficulty: Easy (30), Medium (50), Hard (70), Expert (90), Legendary (110)
- Success = task completed
- Failure = attempt wasted, may cause injury/event

### Skill Progression
- Using skill = +1 XP per use
- Level up = +5 to skill every 20 XP
- Teaching = 2x XP gain for student

---

## INJURY SYSTEM

### Injury Types
| Injury | Effect | Healing Time | Treatment |
|--------|--------|--------------|-----------|
| Scratch | -5 athletics | 1 day | Bandage |
| Cut | -10 athletics, -5 combat | 3 days | First aid |
| Bruise | -2 all | 1 day | Rest |
| Sprain | -15 athletics | 5 days | Wrap, rest |
| Broken Finger | -10 crafting | 14 days | Splint, rest |
| Broken Arm | -40 crafting/farming, -20 combat | 30 days | Cast, rest |
| Broken Leg | -60 movement, -30 athletics | 45 days | Crutches, bed rest |
| Concussion | -20 all, mood swings | 14 days | Bed rest |
| Burn | -15 appearance, -10 combat | 20 days | Ointment |
| Infection | -5 health/day if untreated | 10 days | Medicine |
| Frostbite | -25 dexterity | Permanent | Amputation/cleaning |

### Injury Effects on Mood
Each injury causes specific mood effects:
- Broken Arm: Irritable, frustrated (Pain constantly)
- Broken Leg: Angry, depressed (Can't move)
- Concussion: Confused, anxious (Head hurts)
- Blindness: Devastated, angry (Permanent)
- Scarring: Self-conscious (If appearance-focused)

### Pain System
- Each injury has a pain value (1-10)
- Pain reduces morale and work efficiency
- Pain medication can reduce pain temporarily
- Some characters have high pain tolerance

---

## MEMORY & RELATIONSHIP SYSTEM

### Memory Types

**Event Memories:**
- Who saved their life
- Who caused their injury
- Who helped them
- Who betrayed them
- First day at settlement
- Major events witnessed

**Relationship Memories:**
- Shared meals
- Worked together
- Arguments
- Gifts given/received
- Lessons taught/learned

### Memory Impact

**Positive Memories (Increase relationship):**
- Saved from danger (+20)
- Given food when hungry (+10)
- Helped with work (+5)
- Taught something (+10)
- Shared story (+5)

**Negative Memories (Decrease relationship):**
- Caused injury (-30)
- Stole food (-20)
- Insulted publicly (-15)
- Ignored during crisis (-25)
- Blamed for mistake (-10)

### Relationship Scores
- -100 to +100
- -100: Mortal enemy
- -50: Dislikes strongly
- -25: Annoyed
- 0: Neutral
- +25: Acquaintance
- +50: Friend
- +75: Close friend
- +100: Best friend/romantic interest

### Family System
- Parents, siblings, children tracked
- Family members start with +25 trust
- Family reunions are major events
- Adoption creates new family bonds

### Example Memory:
> "Day 47: Marcus fell while scavenger run. His arm got caught in a collapsed building. It was Ryan's fault - he pushed Marcus to go faster. Marcus's arm healed crooked. Now Marcus每次看到Ryan都很生气."

---

## AI CHARACTER SYSTEM (Post-MVP)

### Concept
Each NPC has an "inner voice" - their thoughts, feelings, goals. Powered by a small local LLM.

### Character Profiles
Each character has:
- Backstory (50-200 words)
- Personality prompt
- Goals and desires
- Fears
- Secrets
- Speech patterns

### Bar/Recreation Scenes
The town pub becomes a social hub:
- Characters drink, talk, play games
- Player can join conversations
- Characters interact with each other
- Stories emerge from interactions
- Drama, romance, arguments, friendships

### Interaction Types
- **Conversation:** Talk about jobs, rumors, feelings
- **Games:** Cards, darts, bowling, chess
- **Stories:** Character tells tales of before
- **Advice:** Characters offer suggestions
- **Complaints:** Workers voice concerns
- **Celebrations:** Birthdays, holidays, victories

### Technical Implementation
- Small 1-3B parameter model per character
- Runs locally (no cloud)
- Context: Character stats, memories, relationships
- Personality prompts keep characters consistent
- Can be toggled on/off for performance

---

## EXAMPLE CHARACTER SHEET

### MARCUS CHEN
**Basic:**
- Name: Marcus Chen
- Age: 34
- Sex: Male
- Race: Asian American
- Height: 5'10"
- Weight: 175 lbs
- Appearance: Scar across left cheek, calloused hands, tired eyes

**Education:** High School Graduate
- Can read novels, technical manuals
- Can do basic math

**Skills:**
| Skill | Level |
|-------|-------|
| Scavenging | 45 |
| Hunting | 38 |
| Athletics | 42 |
| Melee | 25 |
| First Aid | 15 |
| Cooking | 20 |
| Construction | 12 |
| Teaching | 8 |

**Personality:**
- Disposition: Calm
- Mood: Content
- Stress: 15/100
- Trust: 60/100
- Loyalty: 75/100
- Traits: Patient, Honest, Curious

**Injuries:**
- Healing broken right arm (Day 47, 23 days left)
- Pain level: 4/10
- Mood effect: -10 to mood when working

**Relationships:**
- Ryan Torres: -30 (caused broken arm)
- Sarah Kim: +35 (friend)
- Player: +45 (saved his life once)

**Memory Log:**
- "Day 12: Sarah shared her food with me when I was sick. I'll never forget that."
- "Day 47: Ryan pushed me. I fell. My arm still hurts. I don't trust him anymore."

**Goals:**
- Find his sister (separated during collapse)
- Build a safe home
- Learn to read computers

---

## MORALE SYSTEM

### What Affects Morale?
- Food quality (varied vs. same rations)
- Rest quality (bed vs. floor)
- Safety (safe vs. danger)
- Social (friends vs. lonely)
- Accomplishment (working vs. idle)
- Health (injured vs. healthy)
- Privacy (own room vs. crowded)

### Morale Effects
| Morale | Work Efficiency | Combat | Health |
|--------|----------------|--------|--------|
| 90-100 | +25% | +15% | +10% |
| 70-89 | +10% | +5% | +0% |
| 50-69 | 0% | 0% | -5% |
| 30-49 | -15% | -10% | -10% |
| 0-29 | -30% | -25% | -20% |

---

## CHARACTER CREATION AT GAME START

### Starting 4 Characters (Examples)

1. **The Leader** (Player or NPC)
2. **The Scavenger** - Good at finding things
3. **The Hunter** - Good at providing food
4. **The Builder** - Good at construction

Each has:
- Unique backstory
- 3-4 skills above 20
- 1-2 negative traits
- 1 positive trait
- One secret

---

*This character system allows for deep storytelling, emergent narratives, and eventually AI-powered roleplay.*
