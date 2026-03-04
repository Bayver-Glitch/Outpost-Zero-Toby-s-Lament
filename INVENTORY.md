# OUTPOST ZERO - Inventory & Town Systems

## INVENTORY SYSTEM (Diablo 2 Style)

### Grid Layout

**Personal Inventory:** 40 slots (8x5)
**Belt:** 8 slots (horizontal, for potions, ammo)

```
[Slot 1] [Slot 2] [Slot 3] ... [Slot 40]
[ BELT 1 ] [ BELT 2 ] ... [ BELT 8 ]
```

**Item Sizes:**
- Small (1x1): Dagger, ring, ammo
- Medium (1x2): Sword, scroll
- Large (2x2): Armor, big weapons
- Huge (2x3 or 2x4): Two-handed weapons

---

### EQUIPMENT SLOTS

```
          [HEAD]
[GLASSES] [HEAD] [NECKLACE]
[LEFT HAND] [CHEST] [RIGHT HAND]
[LEFT RING] [BELT] [RIGHT RING]
[LEGS]
[FEET]
```

| Slot | Equipment Type |
|------|----------------|
| Head | Helmets, hats |
| Chest | Body armor |
| Legs | Pants, greaves |
| Feet | Boots, shoes |
| Hands | Gloves, gauntlets |
| Left Hand | Weapon OR Shield |
| Right Hand | Weapon |
| Belt | Buckle (stat bonus) |
| Necklace | Amulet |
| Glasses | goggles |
| Ring (x2) | Rings |
| Back | Backpack (inventory space) |

---

### ITEM RARITY & STATS

| Color | Name | Stat Slots | Example |
|-------|------|------------|---------|
| White | Common | 1 | Basic Leather Vest |
| Blue | Uncommon | 2 | Reinforced Vest (+Armor, +Health) |
| Yellow | Rare | 3 | Survivor Vest (+Armor, +Health, +Strength) |
| Orange | Epic | 4 | Veterans Plate |
| Red | Legendary | 5 | Hero's Armor |
| Green | Set | Set bonuses | Complete set = bonus |

### Stat Types

| Stat | Effect |
|------|--------|
| +Health | Max HP |
| +Stamina | Work endurance |
| +Strength | Melee damage |
| +Dexterity | Speed, accuracy |
| +Armor | Damage reduction |
| +Perception | Spotting danger |
| +Charisma | Relationship gains |
| +Healing | Recover faster |
| +Cold Resistance | Cold damage reduction |
| +Fire Resistance | Fire damage reduction |
| +Poison Resistance | Poison damage reduction |

### Item Examples

```
Name: Ragged T-Shirt
Type: Chest Armor
Rarity: White (Common)
Stats: +5 Armor
Size: 2x2

Name: Police Vest
Type: Chest Armor
Rarity: Blue (Uncommon)
Stats: +15 Armor, +10 Health
Size: 2x2

Name: Steel-Reinforced Tactical Vest
Type: Chest Armor
Rarity: Yellow (Rare)
Stats: +25 Armor, +20 Health, +5 Stamina
Size: 2x2

Name: Hero's Plate
Type: Chest Armor
Rarity: Red (Legendary)
Stats: +40 Armor, +30 Health, +15 Strength, +10 Dexterity, +5 All
Size: 2x3

Name: Hunters Set (Green)
- Hunters Cap: +10 Armor, +5 Perception
- Hunters Vest: +20 Armor, +10 Health
- Hunters Boots: +10 Armor, +10 Speed
SET BONUS (2): +10% Damage
SET BONUS (3): +25% Damage, +25% Defense
```

---

### STACKABLE ITEMS

| Item | Slots | Stack Size | Notes |
|------|-------|------------|-------|
| Scrap | 4 | 99 | Building material |
| Ammo (Arrow/Bolt) | 2 | 50 | Archery |
| Ammo (Musket Ball) | 2 | 30 | Flintlock |
| Ammo (Modern) | 1 | 20 | Rare! |
| Herbs | 2 | 25 | Medicine |
| Food | 1 | 10 | Perishable |
| Medicine | 1 | 10 | Med kits |
| Bandages | 1 | 20 | Healing |

---

### SPECIAL ITEMS (Non-Combat)

**Keepakes (Emotional Value):**
```
Item: Wedding Ring (Sarah's)
Type: Ring
Stats: None
Effect: +5 Mental Health for Marcus (her husband)
Description: "Marcus never takes this off. Sometimes he just looks at it."

Item: Photo Album
Type: Key Item
Effect: +10 Mental Health for character
Description: "Old photos of family. Faded but precious."

Item: Grandmothers Necklace
Type: Necklace
Stats: +5 Charisma
Effect: +5 Mental Health for character with "Family" trait
```

**Books (Inventory vs Storage):**
- Skill books go in inventory
- Can be read from inventory
- Reading takes time

---

## BACKPACKS

| Backpack | Slots Added | Weight | Notes |
|----------|-------------|--------|-------|
| None | 0 | - | Base 40 slots |
| Cloth Bag | +5 | Light | Basic |
| School Backpack | +10 | Medium | Common find |
| Hiking Pack | +15 | Medium | Good quality |
| Tactical Vest | +10 | Medium | Adds armor too! |
| Explorer Pack | +20 | Heavy | Large capacity |
| Military Rucksack | +30 | Heavy | Best without vehicle |

---

## TOWN STORAGE

### Storage Building

**Base Storage:** 100 slots
**Upgrades:**
- Shelves: +50 slots
- Crates: +100 slots
- Warehouse: +500 slots

**Organization:**
- General tab: Everything
- Materials tab: Scrap, wood, stone
- Food tab: All food items
- Weapons tab: Weapons only
- Armor tab: Armor only
- Special tab: Keepakes, books

### Food Storage (Requires Kitchen)

- **Perishables:** Spoil over time (reduced with tech)
- **Preserved:** Last longer
- **Max Capacity:** Based on kitchen level

### Profession Buildings

| Building | Function | Required |
|----------|----------|----------|
| Blacksmith | Craft weapons/armor | Forge |
| Workshop | General crafting | Workbench |
| Laboratory | Science/research | Tech 4+ |
| Medical Bay | Healing | First Aid Station+ |
| Kitchen | Cook meals | Level 2+ |

---

## TOWN CENTER (Main Hub)

### Building Interface

```
══════════════════════════════
    🏠 TOWN CENTER - DAY 15
══════════════════════════════

📦 Storage: 45/100 slots
🍞 Food: 120 lbs (enough for 4 days)
⚔️ Defense: Walls HP 150

══════════════════════════════
    👥 CHARACTERS (4)
══════════════════════════════

[1] Marcus   - Farming    - Idle
[2] Phyllis  - Teaching   - Working
[3] Wei      - Scavenging - Idle
[4] Maria    - Cooking    - In Kitchen

══════════════════════════════
    🏗️ BUILD
══════════════════════════════
[Build Wall] [Build Building] [Upgrade]

══════════════════════════════
    ⚖️ LAWS
══════════════════════════════
[View Laws] [Propose Law]

══════════════════════════════
    🎮 RECREATION
══════════════════════════════
[Bar/Inn] [Visit] [Chat]
```

### Assigning Jobs

**Step 1:** Click character from list
**Step 2:** Click "Assign Job" button
**Step 3:** Dropdown shows available jobs:

```
AVAILABLE JOBS:

✓ Farming (Available)
✓ Scavenging (Available)
✓ Hunting (Available)
✓ Guard Duty (Available)
✓ Cooking (Available - requires Kitchen)
✓ Teaching (Available)
✓ Blacksmithing (Requires: Forge)
✓ Medicine (Requires: First Aid Station)
✓ Mechanics (Requires: Workshop)
○ Advanced Medicine (Requires: Clinic - LOCKED)
○ Research (Requires: Laboratory - LOCKED)
```

**Greyed out = not unlocked yet**

---

## LAWS SYSTEM

### Law Categories

| Category | Description |
|----------|-------------|
| Rations | Food distribution rules |
| Labor | Work hours, time off |
| Defense | Guard requirements |
| Trade | Bartering rules |
| Immigration | Who can join |
| Punishment | Crime consequences |
| Religion | Practice allowed |
| Entertainment | What's permitted |

### Law Examples

**Rations Laws:**
| Law | Effect | Tech Level |
|-----|--------|-------------|
| Full Rations | Everyone eats until full | 2+ |
| Limited Rations | Half portions | Any |
| Rationing | One meal per day | Any |
| Priority Feeding | Workers first, children next | Any |

**Labor Laws:**
| Law | Effect | Tech Level |
|-----|--------|-------------|
| 8-Hour Workday | Standard hours | 1+ |
| 10-Hour Workday | More production | Any |
| No Time Off | Maximum work | 1+ |
| Sunday Rest | 1 day off/week | Any |
| Weekly Rest | 2 days off/week | 2+ |

**Time Off Effect:**
- More time off = +10-20% mental health
- Less time off = +10-20% work efficiency, -mental

**Entertainment Laws:**
| Law | Effect | Tech Level |
|-----|--------|-------------|
| No Alcohol | Bar closed | Any |
| Limited Hours | Bar open 6-9pm | 2+ |
| Full Access | Bar always open | 3+ |
| Gambling Allowed | Card games for stakes | 4+ |

### Unlocking Laws

**Tech Level Unlocks:**
- Level 1: Basic laws only
- Level 2: Rationing options, first rest days
- Level 3: Entertainment options
- Level 4: Advanced labor laws
- Level 5: Full rights

**Books Unlock:**
- "Common Sense" - Voting rights
- "The Republic" - Democracy
- "Communist Manifesto" - Collective sharing
- "Atlas Shrugged" - Individual freedom

---

## BAR/INN SYSTEM

### Features

**Atmosphere:**
- Social hub
- Entertainment
- Relationship building
- Mini-games

### Mini-Games

| Game | Players | Skill | Reward |
|------|---------|-------|--------|
| Cards (Various) | 2+ | Luck + Skill | Small items, reputation |
| Dice (Pig) | 2+ | Luck | Small items |
| Arm Wrestling | 2 | Strength | Reputation |
| Storytelling | Group | Charisma | Entertainment |
| Chess | 2 | Strategy | Reputation |

### Effects

- Playing games: +10-20 mental health
- Winning: +5 reputation
- Social bonds increase faster
- Can overhear rumors

---

## CHAT AI SYSTEM

### Concept

A small fast AI that ONLY knows about the game world. Cannot access real internet or discuss real topics.

### Implementation

**Personality Types:**
- Historian (knows old world)
- Optimist (hopeful)
- Realist (pragmatic)
- Joker (humor)
- Elder (wise)

### Usage Examples

```
> Talk to Marcus
"Marcus: Yeah? What do you want?"

> Ask about daughter
"Marcus: Emma... I dream about her every night. 
  Trader came through last week. Said he saw a girl 
  matching her description near the coast..."

> Ask about food
"Marcus: We're running low. Maria says maybe 
  three more days at current rate. The hunters 
  haven't brought back anything in two days."

> Ask about politics
"I don't care about all that government nonsense. 
  We just need to survive. Let's talk about 
  something else."
```

### Chat Rules

- Only game world knowledge
- Won't discuss: Politics, religion, real history
- Will discuss: Personal stories, rumors, advice
- Can trigger story events through conversation
- Characters reveal info over time (trust)

---

## COMPLETE UI LAYOUT

### Main Game Screen

```
┌─────────────────────────────────────────────────────────────┐
│  🏠 OUTPOST ZERO - Day 47          ⚙️  📦  👤            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   [MAP VIEW - Top Down]                                     │
│                                                             │
│   🏠🏠🏠 [Town Area]                                         │
│   🧱🧱🧱🧱 [Walls]                                          │
│   🌾🌾🌾 [Farm]                                            │
│   🌲🌲 [Forest]                                            │
│   💨💨 [Miasma Edge]                                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  📊 STATUS BAR                                              │
│  Day: 47 | Pop: 8 | Food: 120lbs | Scrap: 450 | Mood: 65   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Inventory] [Character] [Build] [Jobs] [Laws] [Bar] [Chat]│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Character Screen

```
┌─────────────────────────────────────────────┐
│  MARCUS CHEN                      LVL 12   │
├─────────────────────────────────────────────┤
│  HP: ████████████░░░░ 75/100               │
│  STA: ██████████████░ 85/100                │
│  MNT: ████████████░░░░ 65/100               │
├─────────────────────────────────────────────┤
│  STR: 25  DEX: 20  PER: 15  CHA: 18         │
│  Skills: Combat 35, Farming 45, Scav 20    │
├─────────────────────────────────────────────┤
│  [EQUIPMENT]                               │
│  Head: [---]    Neck: [---]                 │
│  Chest: Tactical Vest (+15 Armor, +10 HP)   │
│  Hands:[Work Gloves]                        │
│  Legs: [Jeans]    Feet:[Boots]              │
│  Rings:[Wedding Ring ✦] [---]               │
│  Back: [Hiking Pack +10]                    │
│  Weapon: Iron Sword                         │
├─────────────────────────────────────────────┤
│  [INVENTORY]                                │
│  [1][2][3][4][5][6][7][8]                   │
│  [9][📦][📦][ ][ ][ ][ ][ ]                 │
│  (Scrap x47, Blue Potion x3, Key x1)        │
└─────────────────────────────────────────────┘
```

---

*This creates a rich, deep inventory and management experience.*
