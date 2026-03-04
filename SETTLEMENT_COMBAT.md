# OUTPOST ZERO - Settlement & Combat Systems

## SETTLEMENT GROWTH

### Stages

| Stage | Population | Buildings | Description |
|-------|------------|-----------|-------------|
| Camp | 1-10 | Basic | Temporary shelter, lean-tos |
| Village | 11-30 | Standard | Permanent structures |
| Small Town | 31-60 | Advanced | Special buildings, walls |
| Fortified Town | 61-100 | Extensive | Full defense, industry |
| Community | 100+ | Maximum | Self-sustaining |

### Stage Unlocks

| Stage | Unlocks |
|-------|---------|
| Camp | Lean-to, fire pit, storage |
| Village | Homes, basic walls, workshop |
| Small Town | Family homes, tower, advanced buildings |
| Fortified Town | Multiple walls, barracks, guild halls |
| Community | Everything |

### Name Progression

- **Camp:** Player names (e.g., "Hope's End", "New Beginnings")
- **Village:** Keep name or rename
- **Town:** Same
- **Community:** Same

---

## TURN-BASED COMBAT SYSTEM

### Basic Rules

**Action Economy:**
- Each combatant gets **1 action per turn**
- **Move + Attack** = still 1 action (combined)
- **Use Item** = full turn action
- **Use Ability** = full turn action

**Turn Order:**
- Based on Speed/DEX
- Characters go before enemies usually
- Scouts go first

### Combat Interface

```
══════════════════════════════════
    ⚔️ COMBAT - DAY 47
══════════════════════════════════
    
    [MAP: Farm Area]
         🧟 🧟
    💂 Marcus ←→ 🧟 (Runner)
         👤 Maria
    
    ═══════════════════════════════
    TURN: 3/10
    
    MARCUS HP: 85/100 | STA: 60/100
    
    Actions:
    [1] Attack    [2] Move
    [3] Defend    [4] Item
    [5] Ability  [6] Wait
    
    Target: [Runner] - 15 HP
══════════════════════════════════
```

### Action Types

| Action | Description | Effect |
|--------|-------------|--------|
| Attack | Melee/ranged attack | Deal damage |
| Move | Move to new position | Change location |
| Defend | -50% damage taken | Skip attack |
| Item | Use potion/bandage | Heal/buff |
| Ability | Use special skill | Varies |
| Wait | Skip action | +10% next attack |

### Combat Example

```
MARCUS'S TURN (Action 1/1):
> Attack Runner (Iron Sword)
- Hit! 25 damage
- Runner takes 15 HP damage (RUNNER HP: 0/30)
- Runner eliminated!

> Marcus can still MOVE this turn
> Moves to Maria's position

NEXT: Maria's turn...
```

---

## COMBAT TRAITS

### Offense Traits

| Trait | Effect | Trigger |
|-------|--------|---------|
| Warrior | +25% melee damage | Always |
| Berserker | +30% crit chance | Below 50% HP |
| Assassin | +50% damage from sneak | Ambush only |
| Marksman | +25% ranged damage | Always |
| Wildcard | 20% chance for extra attack | Random per hit |
| Cleave | Hit all adjacent enemies | On kill |

### Defense Traits

| Trait | Effect | Trigger |
|-------|--------|---------|
| Unstoppable | +30% HP, +20% armor | Always |
| Shield Bearer | +40% shield block | Always |
| Iron Will | Immune to fear/stun | Always |
| Evasion | 15% dodge chance | Always |
| Regeneration | +1 HP/turn | In combat |
| Medic | +25% healing items | Using items |

### Utility Traits

| Trait | Effect |
|-------|--------|
| Scout | +2 movement range |
| Tracker | Can see hidden enemies |
| Intimidator | -10% enemy damage |
| Leader | +10% nearby ally damage |
| Healer | Can revive at 0 HP once per battle |

### Job-Specific Combat

| Job | Combat Bonus |
|-----|--------------|
| Guard | +15% defense, +weapon skill |
| Scout | +25% movement, +stealth |
| Hunter | +20% ranged, +tracking |
| Militia | +10% all combat |
| Farmer | +10% defense (defend home) |

---

## GUARD SYSTEM

### How Guards Work

**Assignment:**
1. Select character
2. Assign to "Guard" job
3. Define patrol zone (click on map)

**Patrol Zone:**
- Circular area (configurable radius: 10m, 20m, 30m)
- Guard wanders casually within circle
- Visual indicator shows zone

**Aggro Radius:**
- When GUARDING, aggro = ENTIRE circle
- Enemy enters ANY part of circle → Guard reacts
- Guard moves to intercept

### Guard Behaviors

| Setting | Behavior |
|---------|----------|
| Patrol | Wander within zone |
| Stand | Stay in one spot |
| Scout | Move to zone edges |
| Respond | Only if directly threatened |

### Guard Positions

```
        [Tower]
          
    💂 💂     💂
    
  💂     [GATE]     💂
    
    💂 💂     💂
    
        [Storage]
```

**Example:**
- Guard at gate: Intercepts anyone entering
- Guard at storage: Defends food/supplies
- Guard on wall: Long-range attack
- Guard patrol: Random movement catches flankers

### Guard Commands

| Command | Effect |
|---------|--------|
| Attack on Sight | Kill anything entering zone |
| Challenge | Approach and demand password |
| Hold Position | Don't move, only attack if engaged |
| Retreat | Fall back if overwhelmed |

---

## TOWN BELL SYSTEM

### Ringing the Bell

**Trigger:** Press bell or press hotkey (B)

**Effect:**
- All NON-COMBATANTS rush to Town Hall
- Town Hall becomes fortress
- Fighters stay at positions

### Evacuation Priority

```
BELL RINGS! (RAID WARNING!)

> Maria (Cook) → Running to Town Hall
> Phyllis (Teacher) → Gathering children
> Thomas (Child) → Running to Town Hall
> Emma (Child) → Running to Town Hall

> Marcus (Guard) → Holding position
> Wei (Guard) → Holding position
> Carlos (Militia) → Moving to gate
```

### Town Hall (Fort Mode)

| Stat | Value |
|------|-------|
| HP | 500 |
| Capacity | 20 people |
| Defense Bonus | +25% for inside |
| Supply Cache | Extra med kits inside |

### After Combat

- Bell rings again (or automatic)
- Non-combatants return to jobs
- Guards return to patrol
- Injured go to medical

---

## HOUSING SYSTEM

### Quarters (Start)

**Description:** Shared sleeping area
- Everyone sleeps in one building
- Privacy: None
- Comfort: 10

### Barracks (Upgrade)

**Description:** Separate sleeping for men/women
- Groups of bunks
- Privacy: Minimal
- Comfort: 20

### Family Homes (Late Game)

**Description:** Private home for families
- 1-2 bedroom depending on family
- Privacy: Full
- Comfort: 40-60

### Home Customization

| Upgrade | Comfort | Effect |
|---------|---------|--------|
| Blanket | +5 | Warmer |
| Mattress | +10 | Better sleep |
| Furniture | +15 | Personal space |
| Decorations | +10 | Mental health |
| Garden | +10 | Food + beauty |

### Family Home Example

```
╔══════════════════════════════════╗
║  CHEN FAMILY HOME                 ║
║  Residents: Wei, Lin Mei, Emma     ║
╠══════════════════════════════════╣
║  Room 1: Bedroom (Double Bed)      ║
║  Room 2: Small Bedroom (Single)     ║
║  Kitchen: Basic                    ║
║  Storage: 10 slots                 ║
║  Comfort: 45                      ║
╚══════════════════════════════════╝
```

---

## FIGHTING STRUCTURE

### Everyone Can Fight

**Rule:** Any teenager or adult can fight
- No exceptions
- Weapons distributed from storage

### Combat Readiness

| Character Type | Combat Skill | Equipment |
|----------------|--------------|-----------|
| Guard | High | Best available |
| Scout | Medium-High | Light armor, ranged |
| Militia | Medium | Basic weapons |
| Worker | Low | Whatever available |
| Child | Cannot fight | Evacuate! |
| Elder | Low | Defend in place only |

### Battle Flow

```
1. ENEMY DETECTED
   - Guard spots enemy
   - Bell rings OR guard engages

2. INITIAL RESPONSE
   - Guards engage
   - Scouts flanking
   - Militia assembling

3. COMBAT
   - Turn-based fighting
   - Use abilities
   - Watch HP/stamina

4. VICTORY/DEFEAT
   - Victory: Loot enemies, tend wounded
   - Defeat: Retreat to Town Hall
   - Mixed: Assess losses

5. AFTERMATH
   - Heal wounded
   - Repair defenses
   - Return to jobs
```

---

## EXAMPLE BATTLE SCENARIO

### Setup: Night Raid

```
TIME: Night
SCENE: 6 raiders approaching gate

DEFENDERS:
- Marcus (Guard, Warrior trait) - Gate
- Wei (Guard) - Wall
- Carlos (Militia) - Storage
- Maria (Worker, can fight) - With children

NON-COMBATANTS:
- Phyllis - Town Hall (children)
- Lin Mei - Town Hall (cooking)
- Kids - Town Hall
```

### Combat Begins

```
ROUND 1:
- Marcus: Attack raider #1 (25 dmg) - Kill!
- Marcus: Move to raider #2
- Wei: Attack raider on wall (20 dmg)
- Carlos: Move to assist Marcus
- Raiders: #3 attacks Marcus (10 dmg)
```

```
ROUND 2:
- Marcus: Attack #3 (25 dmg) - Kill!
- Marcus: Defend (taking cover)
- Wei: Attack #4 (15 dmg) - Wounds
- Carlos: Attack #4 (15 dmg) - Kill!
- Raiders: #5 throws rock at Wei (8 dmg)
```

```
ROUND 3:
- Marcus: Attack #5 (25 dmg) - Kill!
- Wei: Attack #6 (20 dmg)
- Carlos: Attack #6 (20 dmg)
- Raider #6: Surrenders! "Please! I give up!"
```

### Victory!

```
RESULTS:
- Raiders killed: 5
- Raider captured: 1
- Marcus HP: 75/100 (injured)
- Wei HP: 90/100 (minor wound)
- Carlos HP: 100/100
- Town Hall: Safe, no casualties

LOOT:
- 20 scrap
- 2 knives
- 15 food
- 1 medicine
```

---

## SETTLEMENT STATUS EXAMPLE

```
═══════════════════════════════
🏠 HOPE'S END - VILLAGE
Day: 47 | Population: 8/30
═══════════════════════════════

📦 Storage: 65/100 | 🍞 Food: 120lbs

DEFENSE:
🧱 Walls: HP 150/150
💂 Guards: 2 (Marcus, Wei)
🗼 Tower: 1 (Maria, when needed)
🔔 Bell: Ready

JOBS:
💂 Guard: 2 | 🌾 Farmer: 1
🧱 Builder: 1 | 🔪 Scavenger: 1
🍳 Cook: 1 | 🏫 Teacher: 1

HOUSING:
🛏️ Quarters: 4 (Comfort: 10)
🏠 Family Homes: 0 (Unlock: 30 pop)

LAWS:
- 8-Hour Workday
- Full Rations
- Bar Open

NEXT VILLAGE: 3 more survivors
```

---

*Defense in depth. Everyone fights. Survive together.*
