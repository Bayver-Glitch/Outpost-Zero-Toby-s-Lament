# OUTPOST ZERO - Design Philosophy & Disease

## DISEASE OUTBREAKS

### How Diseases Spread

**Sources:**
- Contaminated water
- Poor hygiene
- Dead bodies nearby
- Miasma exposure
- Food poisoning
- Zombie bites

### Disease Types

| Disease | Source | Symptoms | Treatment |
|---------|--------|----------|----------|
| Cold | Air | -10% work, coughing | Rest, medicine |
| Flu | Contact | -20% work, fever | Medicine |
| Food Poisoning | Bad food | -30% work, vomiting | Medical Bay |
| Pneumonia | Cold exposure | -30% work, coughing | Hospital |
| Infection | Dirty wounds | -10 HP/day | Antibiotics |
| Dysentery | Dirty water | -20% work, -10 HP | Medicine, clean water |
| Typhoid | Contaminated water | -40% work, -15 HP | Hospital, medicine |
| Plague | Miasma | -50% work, -30 HP | Quarantine, hospital |

### Outbreak Events

```
⚠️ DISEASE OUTBREAK!

Location: Quarters
Cause: Dirty water supply
Affected: 3 characters
Symptoms: Dysentery

CONTAGION RISK: HIGH
- Close quarters = fast spread
- Everyone exposed!

ACTIONS:
[1] Quarantine Affected (stops spread)
[2] Clean Water Source (fix cause)
[3] Treat Everyone (medicine)
[4] Wait it Out (risky)
```

### Medical Response

**Quarantine:**
- Isolate sick characters
- -50% spread chance
- Requires: Separate room/building

**Treatment:**
- Doctor with Medicine skill
- Medicine availability
- Rest (in bed)

**Prevention:**
- Clean water
- Hygiene
- Vaccines (Tech 4+)
- Good food

### Disease Example Scenario

```
DAY 35 - SICKNESS

═══════════════════════════════

[MARIA is sick!]

Symptoms: Fever, coughing, weakness
Diagnosis: Pneumonia
Cause: Cold exposure during blizzard

Condition: Critical (-30% work, -15 HP/day)
Contagion: LOW (not spreading)

Treatment:
- Needs: Medical Bay + Doctor
- Medicine: Antibiotics
- Time: 7 days

[ISOLATE] [TREAT] [LEAVE]
```

---

## D WARF FORTRESS STYLE - YES!

### Why This Works

**Dwarf Fortress Philosophy:**
- ASCII/Text graphics = infinite complexity
- Menus and text descriptions = easy to code
- Deep simulation = emergent storytelling
- Millions of possibilities

**Our Version:**
- Same depth, simpler graphics
- Touch-friendly menus
- Mobile-ready!
- Add graphics LATER if wanted

### What's Required

**No graphics needed:**
- Text descriptions
- Menu systems
- Map (text-based)
- Events (text)

**Later additions:**
- Simple sprites (optional)
- Real-time combat view (optional)
- 3D graphics (optional)

---

## MOBILE-FIRST DESIGN

### Touch Interface Philosophy

**No WASD!**
- All navigation via menus
- Tap to select
- Swipe to scroll
- Long-press for info

### Menu Layout

```
═══════════════════════════
🏠 HOME - Day 47
═══════════════════════════

[👥 POPULATION] [📦 STORAGE]
[🗺️ MAP]        [🔬 RESEARCH]

[⚔️ DEFENSE]    [🏗️ BUILD]

[💬 NEWS]       [⚙️ SETTINGS]

═══════════════════════════
```

### Character Management

```
═══════════════════════════
👥 POPULATION (8)
═══════════════════════════

[TAP TO SELECT]

[1] Marcus - Guard - [IDLE]
[2] Wei - Scavenging - [AWAY]
[3] Maria - Cooking - [KITCHEN]
[4] Lin Mei - Farming - [FARM]
[5] Phyllis - Teaching - [QUARTERS]
[6] Kenji - Scout - [AWAY]
[7] Carlos - Guard - [PATROL]
[8] Park - Medic - [MEDICAL]

[TAP CHARACTER FOR DETAILS]
```

### Job Assignment

```
═══════════════════════════
CHARACTER: Marcus
═══════════════════════════

CURRENT JOB: Guard
ZONE: Gate

CHANGE JOB:
[👨‍🌾 FARMER]
[⛏️ SCAVENGER]
[🛡️ GUARD]
[🔪 COMBAT]
[🍳 COOK]
[⚕️ MEDIC]
[📚 TEACHER]
[🏗️ BUILDER]
[🔧 CRAFTER]

[TAP TO ASSIGN]
```

### Map Screen

```
═══════════════════════════
🗺️ MAP - EXPLORED 15%
═══════════════════════════

    [?] [?] [?] [?]
    
 [?] [🏠] [?] [🌲]
 
   [?] [🌲] [?] [?]
   
 [?] [?] [?] [?]

TAP TO SELECT:
🏠 = Your Camp
🌲 = Forest
? = Unexplored

[SCROLL TO SEE MORE]
```

---

## MISSIONS INSTEAD OF REAL-TIME

### How Missions Work

**Instead of watching characters:**
1. Send character on mission
2. Get summary when they return
3. Random events during
4. Results at end

**Example: Scavenging Mission**

```
═══════════════════════════
📤 SCAVENGING MISSION
═══════════════════════════

SELECT TEAM:
[✓] Wei (Stealth 35)
[ ] Kenji (Stealth 30)
[ ] Marcus (Stealth 15)

DESTINATION:
[🏚️ Abandoned Town] - 1 day travel
[🏪 Store District] - 2 days
[🏥 Hospital] - 3 days (Danger!)

ESTIMATED TIME: 2 days
RISK: Medium

[LAUNCH MISSION]
```

### Mission Progress

```
═══════════════════════════
📤 MISSION IN PROGRESS
═══════════════════════════

Team: Wei
Destination: Abandoned Town
Return: Tomorrow

───────────────────────────────────
[REPORT - Day 1]
"Found a good supply. Going deeper."

[REPORT - Day 2]
"Encountered 2 zombies. Combat avoided.
More loot found!"

[ESTIMATED LOOT]
- Food: 30 lbs
- Scrap: 40
- Medicine: 2
```

### Mission Results

```
═══════════════════════════
✅ MISSION COMPLETE
═══════════════════════════

Team: Wei
Destination: Abandoned Town
Time: 2 days

RESULTS:
✓ Loot Obtained:
  - Food: 30 lbs
  - Scrap: 40
  - Medicine: 2
  - Book: "Farming Basics"

⚠️ Incidents:
- Encountered 2 zombies
- Wei injured (moderate)

CHARACTERS:
- Wei: Returned safely

[COLLECT LOOT] [VIEW DETAILS]
```

---

## OPTIONAL REAL-TIME COMBAT

### How It Works

**Default:** Don't watch combat
- Characters fight off-screen
- Results given after

**Optional:** Watch battle
- Popup window
- Real-time combat view
- Can close anytime
- Works like Pokemon battles

### Combat Popup

```
┌─────────────────────────────────────┐
│     ⚔️ COMBAT - TAP TO CLOSE      │
├─────────────────────────────────────┤
│                                      │
│    💂 Marcus ←→ 🧟 Walker          │
│         vs                          │
│    🐺 Zombie Wolf                   │
│                                      │
│  Marcus HP: ████████░░ 75/100     │
│  Wolf HP:   ██░░░░░░░░ 20/100     │
│                                      │
│  [ATTACK]  [DEFEND]  [ITEM]        │
│                                      │
└─────────────────────────────────────┘
```

### You Choose:

- **Watch:** See fight in real-time
- **Don't watch:** Instant results
- **Always watch:** Preference setting
- **Never watch:** Preference setting

---

## GAME SCREENS

### All Touch-Compatible

| Screen | Function |
|--------|----------|
| Home | Main hub |
| Population | Character list/jobs |
| Storage | Inventory management |
| Map | Explore, set destinations |
| Build | Construction |
| Research | Tech tree |
| Laws | Set rules |
| Bar | Mini-games, chat |
| Combat | Watch (optional) |
| Settings | Preferences |

### Simple Graphics Later

**Phase 1:** Text/Menus (we're here)
**Phase 2:** Simple sprites (optional)
**Phase 3:** Real graphics (if wanted)

**All menus stay the same!**
Just add visuals underneath.

---

## EXAMPLE: PLAY SESSION

```
PLAYER OPENS APP:

═══════════════════════════
🏠 HOPE'S END - Day 47
═══════════════════════════

[⚠️] New Reports

TAP: Reports
───────────────────────────────────

REPORTS:
1. Scavenging team returned
2. Trader arrived
3. Maria is sick!
4. Wei wants to talk

TAP: 3 (Maria sick)
───────────────────────────────────

Maria has pneumonia!
Treatment needed.
[VIEW] [ASSIGN MEDIC] [IGNORE]

TAP: Assign Medic
───────────────────────────────────

Select Medic:
[1] Park Ji-Yoon (Medicine 30)
[ ] Anyone available

TAP: Park
───────────────────────────────────

Park assigned to treat Maria.
Expected recovery: 7 days.

[BACK TO HOME]
```

---

## WHY THIS WORKS

**Mobile Perfect:**
- No complex controls
- Tap-based navigation
- Play in short sessions
- Notifications for important events

**Dwarf Fortress Style:**
- Deep simulation
- Emergent storytelling
- Text-based (simple to code)
- Endless replayability

**Optional Graphics:**
- Add anytime
- Doesn't change gameplay
- Menu system stays same

---

*Text first. Touch always. Graphics when ready.*
