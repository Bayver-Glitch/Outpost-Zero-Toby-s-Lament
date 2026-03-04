# OUTPOST ZERO - Enemies & Factions

## ENEMY CATEGORIES

### 1. WILD ANIMALS

| Animal | Behavior | Danger Level | Drops |
|--------|----------|--------------|-------|
| Wolf | Bite, pack tactics | Medium | Wolf pelt, meat |
| Bear | Claw, charge, grab | High | Bear pelt, meat |
| Cougar | Pounce, claw | Medium-High | Pelts |
| Beaver | Chew trees (environmental) | Low | Beaver tail, pelt |
| Cat (feral) | Claw, bite | Low | None |
| Deer | Run away (passive) | None | Meat, pelt |
| Raccoon | Claw, bite | Low | Pelt |
| Snake | Bite (poison!) | Medium | None |

**Behavior Notes:**
- Pack animals (wolves) coordinate attacks
- Predators hunt at night
- Herbivores flee unless cornered
- Beavers chew trees - can crush characters if tree falls

---

### 2. ZOMBIFIED ANIMALS

**Same behaviors as living, but:**
- Don't feel pain
- Don't tire
- Never stop attacking
- Can smell living flesh
- Spawn from dead animals in Miasma zones

| Animal | Behavior | Danger | Special |
|--------|----------|--------|---------|
| Zombie Wolf | Bite, pack | High | Frenzy when smells blood |
| Zombie Bear | Claw, charge | Very High | Doesn't stop |
| Zombie Cat | Claw, ambush | Medium | Silent approach |
| Zombie Beaver | Chew (more aggressive) | Medium | Attacks structures |
| Zombie Bird | Peck, fly attacks | Low | Hard to hit |

---

### 3. ZOMBIFIED HUMANS

**Base zombie type - created from people who die in Miasma zones**

| Action | Description | Damage |
|--------|-------------|--------|
| Hit | Basic punch | 5-10 HP |
| Claw | Rake with fingernails | 10-15 HP, infection risk |
| Bite | Chomp | 15-25 HP, high infection |
| Kick | Stomp | 8-12 HP |
| Throw Object | Pick up rock/stick and hurl | 10-20 HP |
| Grab | Hold in place | Trapped until killed |
| Scream | Alert other zombies | Attracts more |

### Zombie Types

| Type | HP | Speed | Damage | Special |
|------|-----|-------|--------|---------|
| Walker | 50 | Slow | Low | Basic zombie |
| Runner | 30 | Fast | Medium | Swarms |
| Brute | 150 | Slow | High | Tank |
| Crawler | 40 | Low | Medium | Hard to hit |
| Lurker | 45 | Sneaky | Medium | Hides in grass |
| Spitter | 35 | Slow | Ranged (acid) | Ranged attacks |

---

### 4. MUTATIONS (Alien Plant Parasites)

**These are humans/animals that have been PARASITIZED by alien plants**
- They don't "evolve" out of the mist
- They're SENT out by the Miasma
- Rare but extremely dangerous

#### Mutation Types

| Mutation | Source | HP | Speed | Damage | Special |
|----------|--------|-----|-------|--------|---------|
| Hulk | Parasitized human | 300 | Slow | 40 (crush) | Can throw cars |
| Screamer | Parasitized human | 60 | Fast | 15 | Deafening scream, stuns |
| Spitter | Parasitized human | 50 | Slow | 20 (acid) | Ranged acid attack |
| Exploder | Parasitized human/animal | 80 | Medium | 80 (AOE) | Explodes on death, gas damage |
| Bone Archer | Parasitized human | 70 | Medium | 25 (ranged) | Shoots bone spurs like arrows |
| Pouncer | Parasitized cat | 60 | Very Fast | 30 | Jumps from hiding |
| Twisted | Parasitized animal | 200 | Variable | 35 | Random mutations |

#### Rare Mutations (Boss Tier)

| Mutation | HP | Speed | Damage | Special |
|----------|-----|-------|--------|---------|
| Abomination | 500 | Slow | 60 | Massive, multiple attacks |
| Hive Mind | 100 | Slow | 5 | Summons nearby mutations |
| Creeper | 40 | Fast | 50 (poison) | Spits alien seed, grows in wound |

---

### 5. HOSTILE HUMANS

#### Raiders

**Groups that attack settlements for supplies**

| Type | HP | Skills | Equipment | Behavior |
|------|-----|--------|-----------|----------|
| Scavenger | 50 | Scavenging | Knife, club | Sneaky, steals |
| Thug | 80 | Melee | Bat, pipe | Basic fighter |
| Brute | 120 | Strength | Big weapon | Tank |
| Shooter | 60 | Ranged | Pistol (rare) | Uses guns |
| Leader | 100 | Leadership | Various | Buffs others |

**Raider Behavior:**
- Attack storage buildings first
- Will negotiate for food
- May take prisoners (ransom)
- Leave if overwhelmed

#### Bandits

**Smaller scale than raiders**
- Steal food, not attack
- Can be bribed
- Less dangerous

#### Survivors (Desperate)

**Not evil, but will steal to survive**
- May join if offered food/shelter
- Could be recruited
- Random chance to betray

---

### 6. FACTIONS

**Remnants of world governments/organizations**

#### The American Remnant

**Location:** Former military bases, major cities
**Goal:** Restore order, reclaim territory
**Attitude:** Aggressive, sees settlements as resources

| Unit Type | HP | Skills | Equipment |
|-----------|-----|--------|-----------|
| Soldier | 100 | Combat 40 | Rifle (ammo rare), uniform |
| Officer | 120 | Leadership 50 | Pistol, radio |
| Medic | 80 | Medicine 40 | Med kit |
| Engineer | 90 | Engineering 40 | Tools |

**Behavior:**
- May demand tribute
- Will "absorb" settlements
- Fight each other as much as enemies

#### The Chinese Cooperative

**Location:** West coast, former embassies
**Goal:** Preservation, community
**Attitude:** More diplomatic, but firm

**Note from user:** "Your people, probably safer than Americans"

| Unit Type | HP | Skills | Equipment |
|-----------|-----|--------|-----------|
| Guard | 90 | Combat 35 | Spear, crossbow |
| Diplomat | 70 | Persuasion 50 | None |
| Medic | 85 | Medicine 45 | Herbs, basic supplies |
| Engineer | 95 | Mechanics 45 | Tools |

**Behavior:**
- Will trade
- May offer protection for alliance
- Less aggressive than Americans

#### Other Factions

| Faction | Location | Goal | Attitude |
|---------|----------|------|----------|
| The Collective | Urban | Tech preservation | Neutral |
| Farmers Alliance | Rural | Self-sufficiency | Friendly to farmers |
| The Cult | Various | Religious survival | Dangerous, unpredictable |
| Mercenary Guild | Anywhere | Money | Will work for anyone |

---

## MIASMA (ALIEN PLANT ZONE) MECHANICS

### The Mist Boundary

The Miasma is an expanding zone of alien plants and mist:
- Starts at map edges
- Grows slowly over time (1 tile per week)
- Can't build structures inside
- Animals that die in Miasma become zombies

### Miasma Expansion

**Two ways Miasma attacks:**

1. **Direct Growth**
   - Plants grow closer to base
   - Each plant tile = +1 tile Miasma
   - Must destroy plants to stop

2. **Mutation Deployment**
   - Hive mind sends mutations to attack
   - Mutations don't live outside Miasma long
   - Must return or die

### Fighting Miasma

| Method | Effect |
|--------|--------|
| Fire | Kills plants, creates firebreak |
| Herbicide | Kills plants (rare to craft) |
| Salt | Temporary barrier |
| Clearing | Manual plant removal |

---

## COMBAT SCENARIOS

### Scenario: Night Wolf Attack

```
Time: Night
Location: Outside walls

Event: 3 wolves approach camp
- Pack behavior: One distracts, others flank
- If character injured: Wolf smells blood, goes frenzy
- Wolves may drag away downed character
```

### Scenario: Zombie Horde

```
Time: Any
Location: Near Miasma

Event: 15+ zombies detected
- Walkers in front
- Runners on flanks
- Brute in back
- May have lurker hiding in grass
```

### Scenario: Mutation Raid

```
Time: Night (they prefer dark)
Location: Near Miasma edge

Event: 1 Hulk, 2 Bone Archers, 1 Exploder
- Bone archers keep distance, shoot
- Hulk charges front
- Exploder waits, blows up if too close
- Very dangerous - consider walls!
```

### Scenario: Raider Attack

```
Time: Day
Location: Settlement

Event: 8 raiders approach
- Demand food
- If refused: Attack storage first
- May light buildings on fire
- Will take wounded as prisoners
```

### Scenario: Faction "Visit"

```
Time: Day
Location: Settlement

Event: American Remnant patrol (5 soldiers)
- Not attacking... yet
- Demand "tax" in supplies
- Offer "protection" (becomes vassal)
- If refuse: Remembered for next time
```

---

## ENCOUNTER RATES BY DIFFICULTY

| Enemy | Peaceful | Easy | Normal | Hard | Brutal |
|-------|----------|------|--------|------|--------|
| Wild Animals | -50% | Normal | +10% | +25% | +50% |
| Zombies | -50% | -25% | Normal | +25% | +50% |
| Mutations | -75% | -50% | -25% | Normal | +25% |
| Raiders | -50% | Normal | +10% | +25% | +50% |
| Factions | -25% | Normal | Normal | +10% | +25% |

---

## LOOT DROPS

| Enemy | Common | Uncommon | Rare |
|-------|--------|----------|------|
| Wolf | Meat, pelt | - | - |
| Bear | Meat, pelt | Bear bile | - |
| Zombie | Nothing | Ring, watch | Meds, weapons |
| Raider | Food, scrap | Weapons, meds | Ammo |
| Soldier | Ammo, rations | Weapons | Tech |
| Mutation | Nothing | Alien samples | Mutation core |
| Hulk | Nothing | Mutation core | - |

---

*Survive. Build. Thrive. But watch the mist...*
