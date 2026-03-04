# OUTPOST ZERO - Health, Injury & Medical System

## COMBAT & INJURY SYSTEM

### Children in Combat

**Rule:** Children CANNOT be attacked/killed in combat
- If enemy attacks child: Child instantly DOWN (no damage)
- No blood, no death animation
- Child sits/stands crying until picked up by adult
- Pick up = instant revive to full health

### Adults in Combat

**When hit by enemy:**
- Character enters DOWNED state
- Cannot move, attack, or defend
- Lying on ground until:
  1. Revived by ally (medic/first aid)
  2. Bleed out (if not bandaged in time)
  3. Death (if too much damage taken)

### Downed State

| State | Health | Can Act | Can Move | Bleeding |
|-------|---------|---------|----------|----------|
| DOWNED | 0 HP | No | No | Maybe |

**Revival:**
- Medic/First aid character must reach them
- Revival takes 10 seconds
- After revival: 50% max health
- Must be bandaged first if bleeding

**Death:**
- If not revived within 60 seconds: Character DIES
- Permanent death (cannot be brought back)
- Memorial event triggers

---

## BLEEDING SYSTEM

### Bleeding Levels

| Level | Blood Loss/Second | Time to Death | Treatment |
|-------|-------------------|--------------|------------|
| Superficial | 1 HP | 90 sec | Bandage |
| Moderate | 3 HP | 30 sec | Bandage + First Aid |
| Severe | 5 HP | 18 sec | Med Kit + Doctor |
| Arterial | 10 HP | 9 sec | Med Kit + Surgery |

### Bleeding Out

**Immediate Actions:**
1. Apply Bandage (stops bleeding for superficial/moderate)
2. Apply First Aid (stops bleeding + stabilizes)
3. Use Med Kit (stops all bleeding + heals some)
4. Doctor (stops bleeding + prevents infection)

**If bleeding stops:**
- Character is STABILIZED
- Still at 0 HP, needs revival
- After revival: 25-50% max health

**If bleeding continues:**
- Character dies after time limit

---

## MEDICAL FACILITIES

### Tech Level Medical Capabilities

| Tech Level | Facility | Capabilities |
|------------|----------|---------------|
| 1 | None | Bandages, basic first aid |
| 2 | First Aid Station | +25% healing, stitch wounds |
| 3 | Medical Bay | +50% healing, set bones, prevent infection |
| 4 | Clinic | +75% healing, surgery, blood transfusions |
| 5 | Hospital | Full healing, organ transplants, advanced surgery |

### Medical Facility Effects

| Facility | Healing Rate | Bed Bonus | Patient Capacity |
|----------|--------------|-----------|-----------------|
| None (floor) | 0.5 HP/day | -25% recovery | Unlimited |
| Cot | 1 HP/day | 0% recovery | 1 |
| Bunk | 2 HP/day | +10% recovery | 2 |
| Medical Bed | 5 HP/day | +25% recovery | 2 |
| Hospital Bed | 10 HP/day | +50% recovery | 4 |

---

## WOUND TYPES & TREATMENT

### Wound Categories

| Wound | Cause | Treatment | If Untreated |
|-------|-------|-----------|--------------|
| Scrape | Minor combat | Bandage | Heal slowly, -1 stamina |
| Cut | Blade combat | Bandage + First Aid | Heavy bleeding, infection risk |
| Bruise | Any | Rest | -5% work efficiency |
| Sprain | Falling | Bandage + Rest | -15% athletics for 3 days |
| Broken Finger | Hard impact | Splint + Rest | -10% crafting for 7 days |
| Broken Arm | Heavy impact | Cast + Rest | -40% work for 14 days |
| Broken Leg | Heavy impact | Crutches + Bed Rest | -60% movement for 21 days |
| Deep Wound | Powerful attack | Med Kit + Doctor | Heavy bleeding, infection |
| Gunshot | Firearms | Surgery + Med Kit | -50% health, permanent scar |
| Bite | Zombie/Animal | Clean + Doctor + Vaccine | Disease chance |

### Wound Severity Levels

Each wound has Severity 1-5:

| Severity | Health Penalty | Work Penalty | Duration | Recovery |
|----------|----------------|--------------|-----------|----------|
| 1 | -10% | -5% | 3 days | Full |
| 2 | -20% | -10% | 7 days | Full |
| 3 | -30% | -20% | 14 days | May scar |
| 4 | -40% | -30% | 30 days | Permanent effect |
| 5 | -50% | -50% | 60 days | May not recover |

---

## PERMANENT INJURIES

### Permanent Effects (Severity 4-5)

| Injury | Effect | Treatment |
|--------|--------|------------|
| Leg Injury | -30% to -60% movement speed | Rebreak + reset (requires Tech 4+) |
| Arm Injury | -30% to -60% work efficiency | Rebreak + reset |
| Eye Loss | -25% accuracy, -10% perception | Glass eye (Tech 4+) |
| Hearing Loss | -25% perception | Hearing aid (Tech 5) |
| Lung Damage | -20% stamina, -10% work in smoke | None |
| Chronic Pain | -10% all stats in cold/rain | Pain medication |
| Scar | -5% charisma (social) | Plastic surgery (Tech 5) |

### Example: Leg Injury Progression

```
Day 1: Broken leg (Severity 4)
- Cannot walk
- Put in bed, casts on

Day 7: Cast removed, slight improvement
- Can move with crutches (-50% movement)

Day 14: Walking but still limping
- -40% movement

Day 30: Leg healed but wrong
- Permanent -35% movement speed
- Can't run fast anymore
- Can't do heavy labor

Day 60 (with Tech 4+): Optional Surgery
- Rebreak leg
- Reset properly
- 50% chance full recovery
- If fails: could be worse
```

---

## INFECTION & DISEASE

### Infection

**Causes:**
- Dirty wounds
- Contaminated water/food
- Zombie bites
- Dead bodies nearby

### Infection Levels

| Infection | Symptom | Treatment |
|-----------|---------|-----------|
| Minor | -5 HP/day, -10% work | Clean wound, rest |
| Moderate | -10 HP/day, -20% work | Antibiotics |
| Severe | -20 HP/day, -40% work, fever | IV + Doctor |
| Sepsis | -50 HP/day, possible death | Hospital + Surgery |

### Disease

| Disease | Spread | Symptoms | Treatment |
|---------|--------|----------|-----------|
| Cold | Air | -10% work, -5 stamina | Rest, medicine |
| Flu | Contact | -20% work, -15 stamina | Medicine |
| Food Poisoning | Contaminated food | -30% work, vomiting | Medical Bay |
| Pneumonia | Air | -30% work, coughing | Hospital |
| Depression | Trauma | -15 contentment/day | Therapy, medicine |
| PTSD | Combat trauma | -20% work, nightmares | Specialist |

---

## MEDICAL SKILL LEVELS

### Treatment Capabilities

| Medical Skill | Can Treat |
|--------------|-----------|
| 1-10 | Bandages, basic first aid |
| 11-20 | Clean wounds, stitch, set simple bones |
| 21-30 | Moderate wounds, prevent infection |
| 31-40 | Severe wounds, surgery basics |
| 41-50 | Advanced surgery, blood transfusions |
| 51-60 | Organ damage, reconstructive |
| 60+ | Near-miraculous recovery |

### Medicine Tech Requirements

| Medicine | Tech Level | Required Skills |
|----------|------------|-----------------|
| Bandages | 1 | None |
| Antiseptic | 2 | Herbalism + Medicine 20 |
| Antibiotics | 3 | Science 30 |
| Vaccines | 4 | Biology 40, Medicine 40 |
| Surgery Kit | 3 | Medicine 30 |
| Advanced Surgery | 4 | Medicine 50, Biology 50 |
| Mind-Altering Medicine | 4 | Chemistry 40, Medicine 40 |
| Gene Therapy | 5 | Biology 60, Medicine 60 |

---

## TRAITS FROM INJURIES

### Physical Traits (Developed after severe injury)

| Previous Injury | New Trait | Effect |
|----------------|-----------|--------|
| Bad leg | Limp | -10% movement, -5% work |
| Blind in one eye | One-Eyed | -10% ranged accuracy |
| Deaf in one ear | Hard of Hearing | -10% perception |
| Facial scar | Scarred | -5% social, some fear it |
| Lost finger | Missing Digit | -5% crafting |
| Chronic Pain | Painful Memory | -5% in cold/rain |

### Mental Traits (Developed after trauma)

| Event | New Trait | Effect |
|-------|-----------|--------|
| Witnessed death | Traumatized | -10% work in combat |
| Zombie bite survived | Triggered | -15% work near zombies |
| Starvation | Survivors Guilt | -10% contentment when food abundant |
| Lost child | Grief-Stricken | -20% contentment, +10% with children |
| Torture | Broken Will | -20% social, -10% work |
| Betrayed by friend | Trust Issues | -15% relationship gains |

---

## MENTAL HEALTH

### Mental State (0-100)

| State | Effect |
|-------|--------|
| 90-100 | +15% work, +10% learning |
| 70-89 | +5% work, +5% learning |
| 50-69 | Normal |
| 30-49 | -10% work, -10% social |
| 10-29 | -20% work, -20% social, -5% health |
| 0-9 | Depression, may refuse to work |

### Improving Mental Health

| Activity | Effect | Requirements |
|----------|--------|---------------|
| Social Time | +10 mental | Free time, other characters |
| Comfortable Bed | +5 mental | Comfort 50+ |
| Good Meal | +15 mental | Kitchen + cook |
| Therapy | +20 mental | Medicine 30+, 1 hour/day |
| Medication | +25 mental | Tech 4+, pharmacy |
| Hearing Good News | +30 mental | Random event |
| Exercise | +10 mental | Athletics 20+ |

### Mental Health Crises

If mental drops to 0:
- Character has breakdown
- Cannot work
- May self-harm
- May leave settlement
- Requires immediate intervention

---

## MEDICAL EVENT EXAMPLES

### Random Events

| Event | Trigger | Effect |
|-------|---------|--------|
| Epidemic | Poor hygiene | 30% of settlement sick |
| Plague | Zombie nearby | Severe illness spread |
| Contaminated Water | Dirty well | Food poisoning spread |
| Healing Breakthrough | Doctor high skill | Instant full health for one |
| Miracle Cure | Random | Cures all ailments |

### Story Events

**Phyllis's Daughter:**
- Finding daughter triggers emotional event
- If daughter is zombie: -50 mental health for Phyllis
- If daughter is alive: +50 mental health, +25 for whole camp

**Survivor's Guilt:**
- Character saw friend die
- Triggers random breakdown
- Requires therapy or they'll leave

---

## EXAMPLE: RECOVERY SCENARIO

### Marcus Gets Badly Wounded

**Day 47:** Marcus attacked by raiders
- Takes severe wound (severity 4)
- Bleeding heavily
- Companion applies bandage - slows but doesn't stop

**Day 47 (30 seconds later):**
- Medic arrives, applies first aid
- Bleeding stabilizes
- Carried back to camp

**Day 48:**
- Marcus at 0 HP, stabilized
- First aid station bed
- Recovery: 2 HP/day

**Day 52:**
- 10 HP (still critical)
- Can be moved to medical bay

**Day 60:**
- 26 HP (still weak)
- Doctor examines: Permanent damage likely

**Day 75:**
- 45 HP (plateaued)
- Doctor says: "-30% work forever, -15% movement"

**Option 1: Accept Fate**
- Marcus becomes overseer (lighter work)
- Gets "Limp" trait

**Option 2: Surgery (Tech 4 required)**
- Risk: 40% chance death on table
- 30% chance full recovery
- 30% chance worse
