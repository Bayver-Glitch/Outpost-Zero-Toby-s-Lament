# OUTPOST ZERO - Animals & Pets System

## ANIMAL CATEGORIES

### 1. Companion Pets
| Animal | Size | Happiness | Special |
|--------|------|-----------|---------|
| Dog | Medium | +15 | Loyal, guard, tracking |
| Cat | Small | +10 | Pest control, company |
| Bird | Small | +5 | Singing, pretty |
| Rabbit | Small | +8 | Cuddly |

### 2. Farm Animals
| Animal | Produces | Value | Tech |
|--------|----------|-------|------|
| Chicken | Eggs, meat | Low | 2+ |
| Duck | Eggs, meat | Low | 2+ |
| Pig | Meat | Medium | 2+ |
| Goat | Milk, meat | Medium | 2+ |
| Sheep | Wool, meat | Medium | 3+ |
| Cow | Milk, meat | High | 3+ |
| Horse | Transport | High | 3+ |

### 3. Working Animals
| Animal | Job | Skill |
|--------|-----|-------|
| Horse | Transport, riding | Athletics |
| Ox | Pulling, heavy work | Strength |
| Dog (Guard) | Defense | Combat |
| Dog (Scout) | Tracking | Stealth |
| Cat | Pest control | - |

### 4. Zombie Animals (Miasma)
- ALL animals can become zombies
- Same behaviors as living, but hostile
- Some have resistance (rare!)

---

## PETS SYSTEM

### Getting Pets

**Methods:**
1. Find stray (random event)
2. Rescue from danger
3. Trade for
4. Born in settlement

### Pet Assignment

```
═══════════════════════════
PETS - Day 47
═══════════════════════════

[1] 🐕 SCRAPS (Dog)
    Owner: Kenji
    Bond: Strong
    Training: None
    Jobs: Companion

[2] 🐈 WHISKERS (Cat)
    Owner: Maria
    Bond: Strong
    Training: None
    Jobs: Pest Control

[3] 🐕 BUDDY (Dog) - Available!
    Training: Guard
    Stats: Loyalty 50%
```

### Pet Bonds

**Bond Levels:**
| Level | Effect |
|-------|--------ay | Won't|
| Str stay, may run off |
| Acquaintance | Lives in settlement |
| Friendly | Happy to see owner |
| Bonded | Loyal, follows orders |
| Soul Bond | Die for owner |

### Pet Happiness

```
Pet Effects on Owner:
- Dog (Bonded): +15 happiness, +10 combat if threatened
- Cat (Bonded): +10 happiness, -50% pest issues
- Bird (Bonded): +5 happiness, +5 contentment
```

### Pet Commands

| Command | Dogs | Cats |
|---------|------|------|
| Follow | Yes | Sometimes |
| Stay | Yes | Rarely |
| Guard | Yes | No |
| Fetch | Yes | No |
| Hunt | Yes | Yes |
| Attack | Yes | No |

---

## GUARD ANIMALS

### Training Dogs

```
Guard Dog Training:
- Requires: Animal Training skill 20+
- Time: 30 days
- Materials: Food (lots!)
- Success: 80%
```

### Guard Dog Stats

| Level | Combat | Alertness | Health |
|-------|--------|-----------|--------|
| Puppy | +5 | +10 | 30 |
| Young | +10 | +20 | 50 |
| Adult | +15 | +30 | 80 |
| Veteran | +25 | +40 | 100 |
| Elite | +35 | +50 | 150 |

### Guard Dog Abilities

| Skill | Effect |
|-------|--------|
| Bark | Alerts to danger |
| Bite | Attack enemy |
| Protect | Defend owner |
| Patrol | Help guard zone |

---

## SCOUT ANIMALS

### Tracking Dogs

```
Scout Dog Training:
- Requires: Scout + Animal Training 30+
- Time: 45 days
- Success: 70%
```

### What Scout Dogs Find

| Skill Level | Can Find |
|-------------|----------|
| 20+ | Track enemies |
| 40+ | Find hidden items |
| 60+ | Detect traps |
| 80+ | Find rare resources |

### Scout Dog in Action

```
MISSION REPORT - Day 47

Scout Team: Wei + Scout Dog "Nose"

Day 1:
"Nose picked up a scent. Following..."

Day 2:
"Found survivor camp! 5 people.
Friendly. They want to trade."

Day 3:
"Nose detected trap ahead. Avoided!
Found hidden cache nearby."
```

---

## FARM ANIMALS

### Animal Housing

| Animal | Housing | Space | Tech |
|--------|---------|-------|------|
| Chicken | Coop | 1 tile | 2+ |
| Duck | Coop | 1 tile | 2+ |
| Pig | Pen | 2 tiles | 2+ |
| Goat | Pen | 2 tiles | 2+ |
| Sheep | Field | 4 tiles | 3+ |
| Cow | Barn | 4 tiles | 3+ |
| Horse | Stable | 4 tiles | 3+ |

### Production

```
CHICKEN (Tech 2+)
- Eggs: 1/day
- Meat: 10 lbs (harvest)
- Feed: 1 lb/day

GOAT (Tech 2+)
- Milk: 2 quarts/day
- Meat: 20 lbs (harvest)
- Feed: 3 lbs/day

COW (Tech 3+)
- Milk: 5 quarts/day
- Meat: 50 lbs (harvest)
- Feed: 10 lbs/day

SHEEP (Tech 3+)
- Wool: 1 lb/month (shear)
- Meat: 30 lbs (harvest)
- Feed: 5 lbs/day
```

### Breeding

```
Breeding Animals:
- Need male + female
- Takes 30-60 days
- Produces 1-3 offspring
- Offspring can be raised or sold
```

---

## ZOMBIE ANIMALS

### In the Miasma

**Rule:** Any animal that dies in Miasma becomes zombie

### Zombie Animal Types

| Animal | Zombie HP | Damage | Special |
|--------|-----------|--------|---------|
| Zombie Dog | 60 | Bite + infection | Pack tactics |
| Zombie Cat | 40 | Claw + infection | Silent |
| Zombie Wolf | 80 | Bite + infection | Pack leader |
| Zombie Cow | 150 | Trample | Slow, heavy |
| Zombie Horse | 100 | Kick | Can be ridden (risky!) |
| Zombie Pig | 50 | Bite | Fast |
| Zombie Chicken | 20 | Peck | Swarm! |
| Zombie Bird | 30 | Peck | Fly attacks |

### THE ZOMBIE AARDVARK (JOKE... BUT TERRIFYING)

```
⚠️ MYTH: Zombie Aardvark ⚠️

Rare mutation in Miasma

Stats:
- HP: 70
- Speed: Extremely Fast
- Damage: 40 (digging claws)
- Special: Can burrow through walls!

Appearance:
- Long snout, even longer tongue
- Glowing eyes
- Moves like lightning

Tales from survivors:
"The sounds it makes... like a 
screaming death metal band..."
"IT CAME OUT OF THE FLOOR!"
"I saw one kill a man in 3 seconds"

Encounter warning:
"If you see one: RUN. Do not fight.
Pray you can outrun it."

★★★★★★★★★★★★★★★★★★★★★★★★★★
★★★★★★★★★★★★★★★★★★★★★★★★★★
★★★★★★★★★★★★★★★★★★★★★★★★★★
★★★★★★★★★★★★★★★★★★★★★★★★★★
★★★★★★★★★★★★★★★★★★★★★★★★★★
★                           ★
★    GRRR!!!                ★
★    AARDVARK!              ★
★                           ★
★★★★★★★★★★★★★★★★★★★★★★★★★★
★★★★★★★★★★★★★★★★★★★★★★★★★★
★★★★★★★★★★★★★★★★★★★★★★★★★★
★★★★★★★★★★★★★★★★★★★★★★★★★★
```

---

## ANIMAL RESISTANCE

### Rare Resistance

**Chance:** 5% of animals in Miasma

**Resistant Animals:**
- Don't turn into zombies
- Can survive Miasma exposure
- May develop mutations (positive!)

### Resistant Animal Types

| Animal | Resistance | Mutation |
|--------|-------------|----------|
| Dog | 5% | Enhanced senses |
| Cat | 5% | Night vision |
| Wolf | 5% | Alpha powers |
| Cow | 3% | Larger size |
| Pig | 5% | Immunity |

### Mutation Effects

```
Enhanced Dog:
- Tracking: +50%
- Combat: +25%
- Loyalty: Unbreakable!

Night Vision Cat:
- Can see in Miasma
- Always finds loot
- Never lost

Alpha Wolf:
- Commands other animals
- Can calm zombies
- Extremely valuable
```

---

## PET EVENTS

### Random Events

| Event | Trigger | Result |
|-------|---------|--------|
| Stray Arrives | Random | New pet option |
| Pet Befriends | High bond | Bonus happiness |
| Pet Sick | Random | Treatment needed |
| Pet Dies | Old age/injury | Owner devastated |
| Pet Saves Life | Combat | Deep bond |
| Pet Runs Away | Low bond | Sadness |
| Pet Finds Item | Scout with pet | Bonus loot |
| Pet Pregnant | Male + female | New animal |

### Pet Death

```
═══════════════════════════════════
⚠️ SAD NEWS
═══════════════════════════════════

[Kenji's dog "Scraps" has died]

Kenji: "No... no, buddy...
        You were all I had..."

[Effects:]
- Kenji: -30 happiness
- Kenji: May refuse to work
- Kenji: Depression risk

[OPTIONS:]
[1] Comfort Kenji
[2] Give space
[3] Bury with honor
```

### Pet Saving Owner

```
═══════════════════════════════════
🐕 HEROIC DOG!
═══════════════════════════════════

Combat: Marcus was ambushed by raider!

[介入] SCRAPS attacked raider!
- Distracted enemy
- Marcus recovered
- Raider fled!

Marcus: "That dog... he saved my life.
         Who's a good boy? YOU ARE!"

[Effects:]
- Marcus: +20 happiness
- Scraps: Bond level UP!
- Marcus: Deep bond with dog
```

---

## ANIMAL HAPPINESS

### Animals Need Care

| Need | Effect if Ignored |
|------|-------------------|
| Food | -health, -production |
| Water | -health, -production |
| Space | -happiness, fighting |
| Shelter | -health in weather |

### Animal Happiness Effects

| Animal | Happy | Sad |
|--------|-------|-----|
| Chicken | +egg production | No eggs |
| Cow | +milk production | No milk |
| Dog | +combat, loyalty | May run off |
| Cat | Stays | Goes feral |

---

## COMPLETE ANIMAL LIST

### All Animals in Game

```
COMPANION:
- Dog 🐕
- Cat 🐈
- Bird 🐦
- Rabbit 🐰
- Hamster 🐹

FARM:
- Chicken 🐔
- Duck 🦆
- Turkey 🦃
- Pig 🐖
- Goat 🐐
- Sheep 🐑
- Cow 🐄
- Horse 🐴
- Ox 🐂

EXOTIC (Rare):
- Aardvark 🦡 (JOKE! But terrifying!)
- Anteater
- Armadillo

ZOMBIE VARIANTS:
- All above become zombies in Miasma
- Some have resistance
- Some have mutations
```

---

## EXAMPLE: ANIMAL MANAGEMENT

```
═══════════════════════════════════
🐾 ANIMALS - Day 47
═══════════════════════════════════

PETS (4):
[1] 🐕 Scraps - Kenji - Guard Dog
    HP: 80/80 | Happy
    Training: Guard Lv 3

[2] 🐈 Whiskers - Maria - House Cat
    HP: 25/25 | Happy
    Job: Pest Control

[3] 🐕 Rusty - Available
    Training: Scout Dog (60%)

[4] 🐕 Puppy - Unassigned
    Found: Day 45
    Needs: Owner

───────────────────────────────────

FARM (6):
[1] 🐔 Chicken x5 - Coop
     Eggs: 4/day | Happy

[2] 🐐 Goat x2 - Pen
     Milk: 4/day | Happy

[3] 🐖 Pig x1 - Pen
     Growing | Happy

───────────────────────────────────

ZOMBIE THREAT: 2 zombies detected nearby!
[INCREASE GUARD] [MOVE ANIMALS] [IGNORE]
```

---

## PET/MINIGAMES

### Pet Interaction

```
Tap pet for options:
- Play (+happiness)
- Pet (+bond)
- Train (+skill)
- Send on task
- View stats
```

### Pet Mini-Games

| Game | Pet | Skill |
|------|-----|-------|
| Fetch | Dog | Athletics |
| Chase | Cat | Agility |
| Herding | Dog | Intelligence |
| Tricks | Any | Bond |

---

*Animals bring life - and death - to your settlement.*
