# OUTPOST ZERO - Trading & Economy

## CURRENCY: BARTER SYSTEM

**No money.** This is post-apocalypse. Everyone barters.

### Trade Goods Values

| Item | Base Value | Notes |
|------|------------|-------|
| Food (1 lb) | 1 | Basic unit |
| Scrap Metal | 0.5 | Common |
| Medicine | 10 | High value |
| Ammo | 15 | Very rare |
| Weapons | 20-50 | Depends |
| Armor | 15-40 | Depends |
| Alcohol | 5 | Luxuries |
| Herbs | 8 | Medicine source |
| Books | 10 | Knowledge |
| Fuel | 8 | Tech 3+ |

### Trade Ratios

**In Your Favor:**
- They need food: +50% value
- Winter: +25%
- You have unique item: +25%

**Against You:**
- You need item: -25%
- Plenty of item available: -25%
- Desperate: -50%

---

## TRADING CARAVANS

### Types of Traders

#### 1. Wanderer Trader
```
Appearance: Small cart, 1-2 people
Frequency: Weekly
Inventory: Mixed basics

Buys: Food, scrap, supplies
Sells: Tools, medicine, odds and ends
Risk: Low
```

#### 2. Farming Collective
```
Appearance: Wagon train, 3-5 people
Frequency: Bi-weekly
Inventory: Seeds, tools, food

Buys: Tools, labor
Sells: Seeds, animals, preserved food
Risk: Low
```

#### 3. Raider Negotiators
```
Appearance: Armed group, 5-10 people
Frequency: Monthly
Inventory: Stolen goods, weapons

Buys: Food (desperate), supplies
Sells: Weapons (risky), meds, ammo
Risk: Medium (could attack)
```

#### 4. Chinese Cooperative
```
Appearance: Organized convoy, 5-8 people
Frequency: Monthly
Inventory: Quality goods, medicine

Buys: Labor, food, scrap
Sells: Medicine, tools, electronics
Relationship: Can improve with good deals
Risk: Low
```

#### 5. American Remnant Patrol
```
Appearance: Military vehicle, 3-5 soldiers
Frequency: Random
Inventory: Military supplies, ammo

Buys: Food, tribute
Sells: Weapons (rare!), ammo (rare!)
Risk: Depends on attitude
```

#### 6. Junkyard Scavenger
```
Appearance: Beat-up truck, 1-2 people  
Frequency: Weekly
Inventory: Scrap, junk, rare finds

Buys: Scrap, metals
Sells: Random rare items, electronics
Risk: Low
```

#### 7. Traveling Doctor
```
Appearance: Wagon with medical symbol, 1-2 people
Frequency: Monthly
Inventory: Medicine, herbs, treatment

Buys: Food, shelter
Sells: Medicine, treatment, herbs
Risk: Low
```

---

## TRADER INTERFACE

### When Trader Arrives

```
══════════════════════════════════════
    🚛 WANDERER TRADER - DAY 47
══════════════════════════════════════

[Trader Mike]
"I'm just passing through. Got some goods 
to trade. Fair deals, that's me."

REPUTATION: Neutral

YOUR INVENTORY VALUE: 200
TRADER INVENTORY VALUE: 180

──────────────────────────────────────
    [TRADE]  [TALK]  [ASK NEWS]  [BYE]
──────────────────────────────────────
```

### Trade Screen

```
══════════════════════════════════════
    TRADE WITH MIKE
══════════════════════════════════════

YOUR OFFER:                    HIS OFFER:
[Food x20] ←─────────────→ [Medicine x2]
[Scrap x50]                  [Bandages x5]

Current Ratio: FAIR

[ADD ITEM]              [REMOVE ITEM]

──────────────────────────────────────
    [ACCEPT TRADE]  [COUNTER]  [LEAVE]
──────────────────────────────────────
```

---

## REPUTATION SYSTEM

### Trader Reputation

| Level | Name | Effect |
|-------|------|--------|
| -3 | Hostile | Won't trade, may attack |
| -2 | Untrusted | Overpriced by 25% |
| -1 | Unknown | Standard prices |
| 0 | Neutral | Standard prices |
| +1 | Friendly | 10% discount |
| +2 | Trusted | 20% discount |
| +3 | Honored | 30% discount, first pick |

### Gaining Reputation

| Action | Reputation |
|--------|------------|
| Fair deal | +1 |
| Generous deal (you lose) | +2 |
| Helpful (give info) | +1 |
| Hostile action | -2 |
| Attack/Kill trader | -3 (all traders) |

### Faction Reputation

| Faction | Enemies | Allies |
|---------|---------|--------|
| Wanderers | Raiders | Farming Collective |
| American Remnant | Chinese Cooperative | - |
| Chinese Cooperative | American Remnant | - |
| Raiders | Everyone | - |

---

## TRADER INVENTORY EXAMPLES

### Wanderer Trader Mike

```
[FOOD]
- Canned Beans x10 (value: 10)
- Rice x15 (value: 15)

[TOOLS]
- Hammer x1 (value: 15)
- Nails x50 (value: 10)
- Rope x3 (value: 12)

[MEDICINE]
- Bandages x5 (value: 25)
- Herbs x10 (value: 40)

[WANTED]
- Food (desperately need)
- Scrap metal
- Alcohol
```

### Chinese Cooperative Li Wei

```
[MEDICINE]
- Antibiotics x3 (value: 60)
- Medicine x5 (value: 50)
- Herbs x20 (value: 80)

[TOOLS]
- Tools x5 (value: 75)
- Parts x10 (value: 40)

[Electronics]
- Circuit Boards x3 (value: 30)
- Wire x20 (value: 20)

[WANTED]
- Food
- Labor (will pay in goods)
- Books
- Information
```

---

## RANDOM TRADER EVENTS

### Trader Events

| Event | Trigger | Outcome |
|-------|---------|---------|
| Desperate Trader | Trader low on food | Huge discount |
| Scammer | Random | Price manipulation |
| Trader Ambushed | Random | Help = big reward |
| Trader Robbed | Random | They need help |
| Rare Item | Random | One-time special |
| Bulk Buyer | Has excess | Pay premium |
| Information | Talk | Reveal map/locations |

### Example Events

**Desperate Trader:**
```
Trader: "Please... I haven't eaten in two days.
        I'll give you anything for some food."

[Trader will accept VERY low prices]
```

**Trader Ambushed:**
```
EVENT: Raiders are attacking the trader!

Options:
[1] Help Fight - Risk injury, big reward
[2] Wait and Rob - Get loot, -reputation
[3] Hide - Safe, no reward
```

**Rare Item:**
```
Trader: "Know what I found? This beauty..."

[Shows: Working Generator!]
[Value: 500! Only one available!]
```

---

## SELLING TO TRADERS

### What Traders Buy

| Trader Type | Buys (High) | Buys (Low) |
|-------------|-------------|------------|
| Wanderer | Food | Scrap |
| Farming | Seeds, tools | Anything |
| Raiders | Weapons | Food (desperate) |
| Chinese | Labor, food | Medicine, tools |
| American | Tribute, food | Ammo, weapons |
| Junkyard | Scrap | Random |
| Doctor | Food, shelter | Medicine |

---

## PLAYER AS TRADER

### Eventually...

**When settlement is large enough:**
- Can set up own trade route
- Send character as merchant
- Other settlements will visit YOU
- Become a major player

---

## ECONOMY BALANCE

### Early Game (Camp)
- Scavenging = main source
- Traders = lifelines
- Food = most valuable

### Mid Game (Village)
- Farming begins
- Crafting valuable
- Multiple traders visit

### Late Game (Town)
- Self-sufficient possible
- Trade for luxuries
- Become a trader

---

## EXAMPLE TRADE SCENARIO

```
DAY 47 - WANDERER TRADER ARRIVES

═══════════════════════════════════

TRADER MIKE: "Hey! Good to see some 
live ones. Got any food to trade?"

MARCUS: "We've got some. What've you got?"

MIKE: "Medicine, tools, some good rope.
       Take a look."

───────────────────────────────────

MARCUS: [looks at inventory]
- Bandages x5 (value: 25)
- Herbs x8 (value: 32)
- Hammer (value: 15)
- Rope x2 (value: 8)

WANTS:
- Food x40 (value: 40)

MARCUS: "That's a fair deal."

MIKE: "Pleasure doing business."

───────────────────────────────────

RESULTS:
- Gave: 40 food
- Got: Bandages, Herbs, Hammer
- Reputation: +1 (fair deal)

───────────────────────────────────

[Mike looks around, leans in]

MIKE: "Hey... I heard something interesting.
       Old military base, about a week east.
       Big place. Might be worth checking out.
       But dangerous."

QUEST UNLOCKED: Military Base
```

---

*Trade fairly. Build reputation. Survive.*
