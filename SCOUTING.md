# OUTPOST ZERO - Scouting & Resource Systems

## SCOUTING SYSTEM

### Fog of War

**Default:** Entire map is black (unexplored)
- Scouts reveal areas as they explore
- Revealed areas stay on map (memory)
- New enemies spawn in unrevealed areas
- Player must periodically re-scout for new threats

### Map Tiles

| Tile Type | Symbol | Explored When |
|-----------|--------|---------------|
| Forest | 🌲 | Scout walks through |
| Building | 🏠 | Scout enters |
| Road | 🛤️ | Scout walks on |
| Water | 💧 | Scout reaches |
| Miasma | 💨 | Revealed at edge |
| Enemy Camp | ⚔️ | Scout spots enemies |

### Scout Selection

**UI:**
```
══════════════════════════════
    🗺️ SCOUTING - DAY 47
══════════════════════════════

AVAILABLE SCOUTS:
[1] Kenji (Stealth: 35, Combat: 25)
    Traits: Lucky, Scout
    Equipment: Shortbow, Light Armor

[2] Wei (Stealth: 30, Combat: 30)
    Traits: Quick Learner
    Equipment: Crossbow, Leather

[3] Park Ji-Yoon (Stealth: 20, Combat: 15)
    Traits: Healer
    Equipment: Knife

SELECT SCOUT: [Kenji] [Wei] [Ji-Yoon]

DESTINATION:
[Click on map to select area]
Current target: [Town Ruins - 500m NW]

⏱️ Estimated time: 4 hours
⚠️ Danger Level: MEDIUM
```

### Exploration Actions

| Action | Time | Effect |
|--------|------|--------|
| Walk Through | 1 hr/tile | Reveals terrain |
| Enter Building | 2-4 hrs | Full loot, possible enemies |
| Mark Danger | 10 min | Places warning marker |
| Set Trap | 30 min | If scavenger skill 20+ |

### Building Exploration

**Process:**
1. Scout clicks building on map
2. Enters and searches room by room
3. Loot automatically goes to inventory
4. If inventory full → returns to base

**Building Types:**

| Building | Rooms | Loot Quality | Danger |
|----------|-------|--------------|--------|
| House | 2-4 | Low-Med | Low |
| Store | 3-6 | Med-High | Medium |
| School | 4-8 | Med (books!) | Medium |
| Hospital | 5-10 | High (meds!) | High |
| Warehouse | 4-8 | High | High |
| Military Base | 10+ | Very High | Very High |
| Police Station | 3-6 | High (weapons!) | High |

### Enemy Marking

**When scout spots enemy:**
- Enemy position marked on map
- Enemy type indicated if identifiable
- "⚠️" warning placed
- Number indicates quantity

```
MAP LEGEND:
🏠 = Explored building
🌲 = Forest (explored)
💨 = Miasma edge
⚠️ = DANGER - Wolves spotted (3)
⚠️ = DANGER - Zombies (12)
📍 = Scout current position
```

---

## LOOT TABLES

### What Scouts Find

#### Canned Food (Early Game)
| Item | Slots | Stack | Uses |
|------|-------|-------|------|
| Canned Beans | 2 | 6 | Food (low nutrition) |
| Canned Corn | 2 | 6 | Food |
| Canned Meat | 2 | 4 | Food (protein) |
| Expired Soup | 1 | 4 | Food (may get sick) |

*Note: Most canned food is bad by now. Fresh > canned > expired.*

#### Metals
| Item | Slots | Stack | Breaks Into |
|------|-------|-------|-------------|
| Scrap Metal | 4 | 99 | - |
| Aluminum Cans | 2 | 50 | Aluminum |
| Copper Pipes | 2 | 20 | Copper |
| Copper Wire | 1 | 30 | Copper |
| Steel Pipes | 2 | 15 | Steel |
| Nails/Screws | 1 | 50 | Iron |
| Fuse Box | 2 | 5 | Copper + electronics |

#### Tools
| Item | Slots | Notes |
|------|-------|-------|
| Rusty Hammer | 1 | Fixable |
| Wrench Set | 2 | Useful |
| Screwdriver | 1 | |
| Saw (broken) | 2 | Needs repair |
| Drill (dead batteries) | 2 | Rechargeable? |
| Multimeter | 1 | Electronics |

#### Weapons (Early)
| Item | Slots | Condition | Notes |
|------|-------|-----------|-------|
| Kitchen Knife | 1 | Fair | Common find |
| Baseball Bat | 2 | Good | Solid weapon |
| Hunting Knife | 1 | Fair | |
| Revolver | 1 | Poor | No ammo |
| Shotgun | 2 | Poor | Rare |
| Arrows (Crafting) | 2 | Various | Can reuse |

#### Medicine
| Item | Slots | Stack | Rarity |
|------|-------|-------|--------|
| Bandages | 1 | 10 | Common |
| Antiseptic | 1 | 5 | Uncommon |
| Antibiotics | 1 | 3 | Rare |
| Pain Killers | 1 | 5 | Uncommon |
| Vitamins | 1 | 10 | Common |
| First Aid Kit | 2 | 2 | Rare |

#### Herbs & Plants
| Item | Slots | Stack | Found In |
|------|-------|-------|----------|
| Medicinal Herbs | 2 | 20 | Forests |
| Mints | 2 | 15 | Forests |
| Mushrooms (unknown) | 1 | 10 | Forests |
| Seeds (various) | 1 | 10 | Stores, homes |

#### Books & Knowledge
| Item | Slots | Effect |
|------|-------|--------|
| Magazine | 1 | +1 random skill |
| Skill Book | 2 | +5-10 specific skill |
| Recipe Book | 2 | Unlocks recipe |
| Map | 1 | Reveals area |
| Diary | 1 | Character backstory |

#### Electronics (Tech 3+)
| Item | Slots | Uses |
|------|-------|------|
| Circuit Board | 2 | Crafting |
| Battery | 1 | Power |
| Electric Motor | 2 | Crafting |
| Phone (dead) | 1 |拆解 for parts |
| Computer Parts | 2 | Tech crafting |
| Solar Panel (broken) | 4 | Repair possible |

#### Clothing & Armor
| Item | Slots | Stats |
|------|-------|-------|
| T-Shirt | 1 | +1 comfort |
| Jeans | 2 | +2 armor |
| Winter Jacket | 2 | +3 armor, +cold |
| Leather Jacket | 2 | +4 armor |
| Work Boots | 2 | +foot armor |
| Cap | 1 | +1 comfort |

---

## BREAKING DOWN ITEMS

### Deconstruction (Scrapyard Job)

**Purpose:** Turn found items into base materials

| Input Item | Output | Yield |
|------------|--------|-------|
| Aluminum Cans | Aluminum | 2 per can |
| Copper Pipes | Copper | 3 per pipe |
| Copper Wire | Copper | 1 per 5 coils |
| Steel Pipes | Steel | 3 per pipe |
| Old Electronics | Various | Random metals |
| Circuit Board | Copper, silver | Small |
| Car Parts | Steel, aluminum | Varies |

### Crafting from Raw Materials

```
Base Materials List:
- Iron: Nails, tools, weapons
- Steel: Tools, weapons, armor
- Aluminum: Tools, crafting
- Copper: Wire, electronics
- Wood: Buildings, weapons
- Leather: Armor, belts
- Plastic: Various
```

---

## RESOURCE GATHERING JOBS

### Lumberjack/Woodcutter

**Job:** Chop trees for wood

| Tech Level | Tool | Production | Notes |
|------------|------|------------|-------|
| 1 | Axe | 5 wood/day | Basic |
| 2 | Sharp Axe | 10 wood/day | Better |
| 3 | Iron Axe | 20 wood/day | Good |
| 4 | Chainsaw | 50 wood/day | When fuel available |

**Requirements:**
- Forest tiles nearby
- Axe (any kind)

### Gatherer

**Job:** Forage in forests, fields, near water

| Resource | Chance | Tech Level |
|----------|--------|-------------|
| Herbs | 40% | 1+ |
| Berries | 30% | 1+ |
| Mushrooms | 15% | 1+ |
| Nuts | 20% | 2+ |
| Seeds | 25% | 1+ |
| Honey | 10% | 2+ (bees) |

### Hunter

**Job:** Hunt animals for meat and pelts

| Animal | Meat | Pelt | Difficulty |
|--------|------|------|------------|
| Rabbit | 2 lbs | Small | Easy |
| Deer | 20 lbs | Medium | Medium |
| Bear | 50 lbs | Large | Hard |
| Wolf | 10 lbs | Medium | Medium |

### Fisher

**Job:** Fish in lakes/rivers

| Fish | Weight | Tech Level |
|------|--------|-------------|
| Trout | 2 lbs | 1+ |
| Salmon | 5 lbs | 2+ |
| Catfish | 8 lbs | 2+ |

---

## LATE GAME QUESTION: Gatherers?

**User asked:** "gatherers wont be useful in late game?"

**Answer:** YES and NO!

### Why Gatherers Stay Useful:

1. **Berries/Nuts** - Even late game, wild foraging supplements farming
2. **Herbs** - Some only grow wild (special medicinal plants in Miasma edges)
3. **Honey** - Renewable, valuable
4. **Mushrooms** - Some only wild (even tech 5 can't grow)
5. **Emergency Food** - If crops fail, gatherers = backup

### Late Game Balance:

| Job | Early Game | Mid Game | Late Game |
|-----|------------|----------|-----------|
| Lumberjack | ESSENTIAL | Needed | Less (forests deplete) |
| Gatherer | ESSENTIAL | Supplement | Niche/backup |
| Hunter | IMPORTANT | Supplement | Pets replace hunting |
| Fisher | Nice | Nice | Fish farms! |
| Farmer | - | ESSENTIAL | ESSENTIAL |

### Solution: Multi-Tasking

**Late game characters can have secondary jobs:**
- Farmer: Can also gather when crops done
- Hunter: Can also scout
- Fisher: Can also cook

**Result:** Everyone does a little foraging even late game!

---

## JOB COMBINATIONS

### Example Late Game Characters

```
Name: Marcus
Primary Job: Guard (Combat)
Secondary: Hunter (Weekends)

Name: Maria  
Primary Job: Cook
Secondary: Gatherer (when low on food)

Name: Wei
Primary Job: Blacksmith
Secondary: Lumberjack (when wood low)

Name: Lin Mei
Primary Job: Farmer
Secondary: Gatherer (seasonal)
```

---

## SCOUTING EVENTS

### Random Encounters

| Event | Trigger | Outcome |
|-------|---------|---------|
| Survivor Found | Scout finds lost person | Potential recruit |
| Trap | Failed stealth check | Injury, trap loot |
| Hidden Cache | Random chance | Good loot |
| Ambush | Scout in danger zone | Combat or flee |
| Abandoned Camp | Random | Supplies, possible pet |
| Trader | Scout meets trader on road | Trade opportunity |
| Discovery | Scout finds special location | Quest/mission |

### Exploration Rewards

| Location | Special Loot |
|----------|--------------|
| Library | Books, maps |
| Hospital | Medicine |
| Police Station | Weapons |
| Military Base | Ammo, armor |
| School | Teaching materials |
| Grocery Store | Seeds (rare!) |
| Pet Store | Possible animal! |

---

*Explore. Discover. Survive.*
