# OUTPOST ZERO - Weather & Environment

## SEASONS

### Season Cycle

| Season | Length | Difficulty | Effect |
|--------|--------|------------|--------|
| Spring | 20 days | Easy | Normal |
| Summer | 25 days | Easy | Bonus crops |
| Fall | 20 days | Medium | Harvest |
| Winter | 30 days | HARD | Survival mode |

### Seasonal Effects

#### Spring
- Crops grow +25%
- Animals active
- Mud (slower movement)
- Beautiful, hopeful

#### Summer
- Crops grow +50%
- Heat (stamina drain)
- Good hunting
- Thunderstorms

#### Fall
- Harvest season
- Food storage time
- Animals preparing
- Beautiful colors

#### Winter
- **CRITICAL:**
  - No crops outside (unless greenhouse)
  - Food shortage common
  - Cold damage (HP drain)
  - Heating fuel needed
  - Ice on water (fishing harder)
- Beautiful snow
- Short days
- Game hardest

---

## WEATHER TYPES

### Clear/Sunny
- Normal operations
- Solar power +25%
- Best for farming

### Cloudy
- Normal
- No penalties

### Rain
- Farming +10%
- Hunting -25% (animals shelter)
- Firewood dries (good for crafting)
- Movement -10%
- Outdoor work -10%

### Heavy Rain
- Flooding possible
- Firewood wet (can't burn)
- Movement -25%
- Outdoor work -50%
- Cellars flood

### Snow
- Movement -25%
- Farming impossible outside
- Hunting +10% (tracks visible)
- Heating needed 2x
- Cold damage if exposed

### Blizzard
- Movement -50%
- Can't go outside safely
- Hunters can still track
- Food consumption 2x (body works harder)
- High cold damage

### Fog
- Visibility reduced (scouting danger!)
- Movement -10%
- Ambush chance +25%
- Miasma harder to see
- Creepy atmosphere

### Thunderstorm
- Can't use electricity (surge)
- Fire dangerous (lightning)
- Move -25%
- Random lightning strikes

---

## TEMPERATURE SYSTEM

### Temperature Scale

| Temp | Effect |
|------|--------|
| Hot (80°F+) | -10% stamina, +water use |
| Warm (65-79°F) | Normal |
| Cool (50-64°F) | Normal |
| Cold (32-49°F) | -1 HP/hour if outside |
| Freezing (0-31°F) | -3 HP/hour, -25% work |
| Bitter (-0°F) | -5 HP/hour, -50% work |

### Cold Effects by Season

```
SPRING: Cold nights only (-1 HP at night)
SUMMER: Normal
FALL: Chilly (-1 HP at night)
WINTER: Always cold (-1 to -5 HP depending)
```

### Warmth Sources

| Source | Warmth | Required |
|--------|--------|----------|
| Fire Pit | 10 | Wood |
| Fireplace | 15 | Wood |
| Heater | 25 | Fuel/Electricity |
| Boiler | 35 | Fuel |
| Central Heat | 50 | Tech 4+ |

### Clothing for Cold

| Clothing | Cold Protection |
|----------|-----------------|
| Summer Clothes | 0 |
| Fall Clothes | +5 |
| Winter Coat | +15 |
| Winter Clothes | +25 |
| Heavy Furs | +40 |

---

## WATER SYSTEM

### Water Sources

| Source | Access | Treatment |
|--------|--------|-----------|
| River | Unlimited | Must purify |
| Lake | Unlimited | Must purify |
| Well | Limited | Must pump |
| Rain | Limited | Filter only |
| Snow | Limited | Melt + filter |

### Water Usage (Per Person/Day)

| Activity | Amount |
|----------|--------|
| Drinking | 1 quart |
| Cooking | 0.5 quart |
| Washing | 1 quart |
| Hygiene | 0.5 quart |
| **Total** | **3 quarts** |

### Getting Water

#### Wells
- Tech Level 1: Hand pump (slow)
- Tech Level 2: Bucket system (faster)
- Tech Level 3: Pump system (fast)
- Tech Level 4: Electric pump (very fast)

#### Rain Collection
- Requires: barrels/containers
- Tech Level 2+: Large collection
- Note: Often contaminated, needs boiling

#### River/Lake
- Requires: transport
- Distance matters (far = more work)
- Always contaminated (Miasma!)

### Water Contamination

| Source | Safe? | Treatment |
|--------|-------|-----------|
| Deep Well | Yes | None needed |
| River (far from Miasma) | Maybe | Boil/filter |
| River (near Miasma) | NO | Must boil 10 min |
| Rain | Maybe | Filter |
| Snow Melt | Yes | None |

### Water as Resource

- Stored in tanks/containers
- Takes inventory space (1 slot = 10 gallons)
- Winter: pipes freeze (Tech 3+ = insulated)
- Used for: drinking, cooking, farming, animals

---

## FISHING SYSTEM

### Fishing Locations

| Location | Fish Type | Difficulty | Tech |
|----------|-----------|------------|------|
| River | Trout | Easy | 1+ |
| Lake | Bass | Medium | 1+ |
| Deep Lake | Salmon | Medium | 2+ |
| Miasma Edge | Strange Fish | Hard | 3+ |

### Fishing Mechanics

```
Job: Fisher

Required: Fishing rod or net
Tech Level 1: Hand line
Tech Level 2: Rod and reel  
Tech Level 3: Net (faster catches)
Tech Level 4: Boat + net
Tech Level 5: Commercial gear
```

### Fishing Yield

| Method | Fish/Day | Skill Bonus |
|--------|----------|-------------|
| Hand Line | 2-5 | +1 per skill |
| Rod/Reel | 5-10 | +2 per skill |
| Net | 10-20 | +3 per skill |
| Boat + Net | 20-40 | +5 per skill |

### Fish Types & Nutrition

| Fish | Weight | Nutrition | Rarity |
|------|--------|-----------|--------|
| Trout | 2 lbs | 15 protein | Common |
| Bass | 3 lbs | 20 protein | Common |
| Salmon | 5 lbs | 30 protein | Uncommon |
| Catfish | 8 lbs | 25 protein | Uncommon |
| Strange Fish | 3 lbs | 10 protein, ??? | Rare (Miasma) |

### Fishing Events

| Event | Chance | Outcome |
|-------|--------|---------|
| Big Catch | 10% | Double yield |
| Nothing | 20% | No catch |
| Old Gear | 5% | Find lost item |
| Miasma Creature | 5% | Combat! (near edge) |
| Rare Fish | 5% | Special recipe |

---

## MIASMA (THE MIST)

### Visual Effect

**Like Silent Hill:**
- Thick fog at edges
- Green/purple tint
- Things move in the mist
- Creepy sounds
- Can't see enemies until close

### Miasma Mechanics

**Expansion:**
- Grows 1 tile/week
- Kills normal plants/animals
- Animals that die in Miasma become zombies

**In the Mist:**
- -50% visibility
- Enemies have +25% attack
- Characters can get lost
- Strange sounds
- Can see "shadows" moving

### Fighting Miasma

| Method | Effectiveness |
|--------|---------------|
| Fire | Kills plants temporarily |
| Salt | Creates barrier (temporary) |
| Herbicide | Kills plants |
| Clearing | Manual removal |
| Walls | Stops expansion |

### Mist Creatures

**Only appear IN Miasma:**
- Lurkers (hide in mist)
- Spitters (shoot from mist)
- Hive Mind (summons)
- Abomination (boss)

### Miasma Edge Warning

```
⚠️ APPROACHING MIASMA EDGE ⚠️

- Visibility: LOW
- Enemy chance: HIGH  
- Do not enter without weapons
- Turn back if mist thickens
```

---

## WEATHER EVENTS

### Random Weather Events

| Event | Season | Effect |
|-------|--------|--------|
| Heat Wave | Summer | +50% water use, -stamina |
| Cold Snap | Any | -10 temp for 3 days |
| Flood | Rain | Lose crops, items |
| Drought | Any | Crops die, water scarce |
| Early Frost | Fall | Harvest ruined |
| Whiteout | Winter | Can't go outside |

### Seasonal Events

**Spring:**
- Flooding
- New growth
- Animals return

**Summer:**
- Thunderstorms
- Heat waves
- Good harvest

**Fall:**
- Harvest festivals
- Prepare for winter
- Animals migrate

**Winter:**
- Starvation risk
- Freezing deaths
- Short days
- Ice fishing

---

## DAY/NIGHT CYCLE

### Time System

| Time | Hours | Activity |
|------|-------|----------|
| Morning | 6am-10am | Work shift 1 |
| Midday | 10am-2pm | Work shift 2 |
| Afternoon | 2pm-6pm | Work shift 3 |
| Evening | 6pm-10pm | Free time, dinner |
| Night | 10pm-6am | Sleep |

### Night Effects

- Visibility -50%
- Stealth +25%
- Most enemies more active
- Guard efficiency +25% (more alert)
- Miasma creatures emerge

### Lighting

| Light Source | Radius | Tech |
|--------------|--------|------|
| Fire | 5m | 1+ |
| Torch | 3m | 1+ |
| Lantern | 8m | 2+ |
| Electric Light | 15m | 4+ |
| Spotlight | 30m | 5+ |

---

## WEATHER UI EXAMPLE

```
═══════════════════════════════════
🌤️ WEATHER: Clear - 65°F
📅 SEASON: Fall - Day 12
───────────────────────────────────
TEMP: 65°F (feels like 65°F)
WIND: Light (5 mph)
HUMIDITY: 45%

FORECAST:
Tomorrow: ☁️ Cloudy - 55°F
2 Days: 🌧️ Rain - 50°F
3 Days: ☀️ Clear - 60°F

───────────────────────────────────
🌡️ HEATING: 0/20 (fire pit needed!)
💧 WATER: 50 gallons (enough)
🌾 FARM: Growing (+25% this season)
```

---

## COLD WEATHER EXAMPLE

```
═══════════════════════════════════
🌨️ WEATHER: Snow - 18°F
📅 SEASON: Winter - Day 7
───────────────────────────────────
TEMP: 18°F (feels like 5°F)
WIND: Medium (15 mph) - WIND CHILL -10°F!
HUMIDITY: 70%

⚠️ WARNING:
- Cold damage: -3 HP/hour outside
- Heating critical!
- Outdoor work -50%
- Only essential tasks

───────────────────────────────────
HEATING STATUS:
🔥 Fire Pit: Burning (40% wood remaining)
❄️ Status: SURVIVABLE

WATER: Frozen at pump!
- Must melt snow
- 1 hour to melt enough for day
```

---

## SEASONAL PREPARATION

### Spring Checklist
- [ ] Repair structures
- [ ] Plant crops
- [ ] Collect water
- [ ] Heal from winter

### Summer Checklist
- [ ] Stockpile food
- [ ] Preserve meat
- [ ] Gather firewood (dry)
- [ ] Trade surplus

### Fall Checklist
- [ ] Harvest everything
- [ ] Prepare preserves
- [ ] Stockpile firewood
- [ ] Fix heating
- [ ] Trade for winter supplies

### Winter Checklist
- [ ] Ration food
- [ ] Stay warm
- [ ] Ice fishing
- [ ] Indoor jobs only
- [ ] Healthcare ready

---

*Weather is not just atmosphere - it's a survival mechanic.*
