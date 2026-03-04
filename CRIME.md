# OUTPOST ZERO - Crime & Justice System

## CRIMES

### Crime Categories

| Crime | Severity | Description |
|-------|----------|-------------|
| Theft | Minor | Stealing food/items |
| Assault | Medium | Fighting, hurting someone |
| Spying | Medium-High | Sharing info with enemies |
| Smuggling | Medium | Bringing banned items |
| Kidnapping | High | Taking person against will |
| Murder | Extreme | Killing a settler |
| Treason | Extreme | Betraying settlement |

### Crime Examples

```
THEFT:
- Stealing food from storage
- Taking others' items
- Looting during chaos

ASSAULT:
- Fighting another settler
- Attacking without reason
- Verbal threats (maybe)

SPYING:
- Sharing location with raiders
- Trading secrets for goods
- Working for factions

SMUGGLING:
- Bringing in banned items
- Hiding items from trade
- Hoarding for personal use

KIDNAPPING:
- Taking a child
- Taking someone as leverage
- Selling to raiders

MURDER:
- Killing another settler
- Killing during raid but not self-defense
- Poisoning

TREASON:
- Leading enemies to settlement
- Sabotaging defenses
- abandoning post during attack
```

---

## PUNISHMENT SYSTEM

### Options

| Punishment | Severity | Time | Effect |
|------------|----------|------|--------|
| Warning | Minor | - | -10 relationship |
| Fine | Minor | - | Lose items/reputation |
| Community Service | Medium | 1-7 days | Work without pay |
| Jail | Medium-High | 7-30 days | Locked up |
| Banishment | High | Permanent | Kick out |
| Execution | Extreme | Death | Murder them |

### Sentencing Guidelines

```
THEFT (First offense):
- Warning
- Fine (return item + penalty)
- Community service

THEFT (Repeat):
- Jail (7-14 days)
- Banishment (3rd offense)

ASSAULT:
- Community service (minor)
- Jail (serious injury)
- Banishment (maiming)

MURDER:
- Jail (30+ days)
- Banishment
- Execution (if brutal)

TREASON:
- Jail (30 days)
- Execution
```

---

## JAIL SYSTEM

### Building

```
JAIL (Tech Level 3+):

Capacity: 4 cells
Requirements: 50 scrap, 20 iron bars

Cell Features:
- Bed
- Bucket
- No windows

Upgrades:
- More cells (10 total)
- Solitary (for dangerous)
- Interrogation room
```

### Jail Routine

```
IN JAIL - Day 47

Wake: 7:00
- Locked in cell

Work: 8:00-12:00
- Break rocks (community service)
- OR Sit in cell (jail only)

Lunch: 12:00
- Bread and water

Work: 13:00-17:00
- Break rocks OR Cell

Dinner: 18:00
- Bread and water

Sleep: 21:00

Daily: -5 contentment (jail)
```

### Time in Jail

| Crime | Typical Time |
|-------|--------------|
| Theft | 3-7 days |
| Assault | 7-14 days |
| Spying | 14-30 days |
| Smuggling | 7-14 days |
| Kidnapping | 30+ days |
| Murder | 30+ or execution |
| Treason | Execution |

---

## BANISHMENT

### Process

```
BANISHMENT:

"Your crimes are unforgivable.
You are hereby banished from [TOWN].
Take only what you carry. Leave now."

Items confiscated:
- All weapons
- Half food
- Radio (if any)

Banished character:
- Leaves settlement
- Can be encountered later
- May become raider!
```

### After Banishment

**Options for Banished:**
- Wander alone
- Join raiders
- Join other factions
- Die in wilderness

**Can Return?**
- Only if pardoned
- Many years later
- Never for murder

---

## EXECUTION

### Methods

| Method | Description | Tech |
|--------|-------------|------|
| Firing Squad | Quick | Any |
| Gallows | Hanging | 2+ |
| Beheading | Quick | 2+ |
| Guillotine | Efficient | 3+ |
| Gas Chamber | Painless | 4+ |

### Execution Process

```
═══════════════════════════════════
⚖️ EXECUTION - Day 47
═══════════════════════════════════

CRIME: Murder (killed Marcus)
Criminal: Tom Wilson

METHOD: Firing Squad

WITNESSES: Required (all settlement)

PLAYER CHOICE:
[1] Proceed with execution
[2] Pardon (controversial!)
[3] Commute to banishment
```

---

## PUBLIC OPINION

### How Settlers React

**Reaction depends on:**
- Crime severity
- Victim relationship
- Punishment fairness

### Opinion Matrix

```
PUNISHMENT: Theft (1 week jail)

REACTIONS:
- Victim's friends: Not harsh enough!
- Criminal's friends: Too harsh!
- Law-abiding: Fair
- Everyone: Depends on mood

RESULT:
- Some contentment: +2
- Some contentment: -3
- Average: Fair enough
```

### Public Reaction Examples

```
CASE 1: Theft - Community Service
───────────────────────────────────
Marcus: "A week breaking rocks? Seems fair."

Maria: "At least they didn't kill him.
        That's what raiders do."

Wei: "The punishment fits the crime."


CASE 2: Murder - Execution
───────────────────────────────────
Maria: "Good. He deserved it."

Kenji: "That's... a lot. Can't look away."

Phyllis: "We just killed someone..."


CASE 3: Theft - Banishment  
───────────────────────────────────
Marcus: "Too harsh! He was hungry!"

Carlos: "We should have given him work."

Wei: "Now he's probably dead. 
       That's on us."
```

---

## CRIME PREVENTION

### Measures

| Measure | Effect |
|---------|--------|
| Visible guards | -20% crime |
| Storage locks | -30% theft |
| Curfew | -15% night crime |
| Community | -10% crime |
| High contentment | -20% crime |

---

## EXAMPLE TRIAL

```
═══════════════════════════════════
⚖️ TRIAL - Day 52
═══════════════════════════════════

CHARGES: Theft (3rd offense), Assault

CRIMINAL: Kenji

EVIDENCE:
- Stole food from storage (3rd time)
- Punched Marcus during argument

VICTIM STATEMENT:
Marcus: "He hit me! Then stole food!
         I've had enough!"

CRIMINAL STATEMENT:
Kenji: "I was hungry! No one was 
        feeding me! I had to!"

WITNESSES:
- Maria saw the fight
- Wei saw him steal

───────────────────────────────────

PUNISHMENT OPTIONS:

[1] Execute (Extreme)
    - All: Shocked!
    - Marcus: "That's too much..."
    - Kenji: [terrified]

[2] Banish (High)
    - Marcus: "Good."
    - Maria: "Please... no..."

[3] Jail 30 days (Medium-High)
    - Marcus: "Fine."
    - Maria: "At least alive..."

[4] Community Service 14 days (Medium)
    - Marcus: "Not enough."
    - Maria: "Fair."

[5] Warning + Fine (Light)
    - Marcus: "You're kidding."

PLAYER CHOOSES: [3] Jail 30 days

───────────────────────────────────

AFTERMATH:
Kenji: -50 contentment
Marcus: +5 (justice served)
Maria: +2 (fair)
Others: Varies
```

---

## CONSEQUENCES OF PUNISHMENTS

### Jail Consequences

| Factor | Effect |
|--------|--------|
| Time in jail | Character gains: "Jailbird" trait |
| During | -30% work efficiency |
| After | -10 work forever? |
| Other prisoners | May bond or fight |

### Banishment Consequences

| Factor | Effect |
|--------|--------|
| Banished | Becomes enemy? |
| If | May return as raider |
| Later | Could attack former home |
| Could | Spread rumors about settlement |

### Execution Consequences

| Factor | Effect |
|--------|--------|
| Victim's family | +50 grief! |
| Killer's family | May seek revenge |
| Community | Some approve, some horrified |
| Religious | May cause conflict |
| Murderer's friends | -30 relationship |

---

## FORGIVENESS

### Pardon System

**Requirements:**
- Time served (half or more)
- Good behavior in jail
- Victim forgives
- Community agrees

**Pardon Effects:**
- Can return to settlement
- Reduced penalty
- Some relationships repair

### Redemption Arc

```
JAIL - Day 90

Kenji (in jail 30+ days):
"I've changed. I understand now.
I was desperate. I shouldn't have 
stolen. I shouldn't have fought."

VISIT FROM MARCUS:
Marcus: "You really seem different."

KENJI: "I want to make amends. 
        Give me a chance."

PARDON OPTIONS:
[1] Release to community service
[2] Release on parole
[3] Keep in jail
[4] Banish anyway
```

---

## ANARCHY MODE (OPTIONAL)

### No Laws

**Optional Game Mode:**
- No courts
- No jail
- Vigilante justice
- Factions handle own

### In Anarchy:

```
OPTION: Let victims decide

Attacked Kenji:
- Marcus: "Eye for an eye!"
- Maryanne: "No! Violence isn't 
             the answer!"

PLAYER CHOICE:
[1] Let Marcus hurt Kenji
[2] Intervene
[3] Jail (requires building)
```

---

## PRISONER INTERACTIONS

### Speaking to Prisoners

```
TAP PRISONER: Kenji

───────────────────────────────

KENJI (Cell 2):
Crime: Theft (3rd), Assault
Days left: 22

Status:
- Health: 80%
- Contentment: 10%
- Mood: Depressed

───────────────────────────────

[ASK ABOUT CRIME]
[ASK ABOUT FEELINGS]
[OFFER FORGIVENESS]
[RELEASE EARLY]
[LEAVE]

───────────────────────────────────

[ASK ABOUT FEELINGS]

Kenji: "I messed up. I know.
        Everyone hates me now.
        I hate me too.
        
        Is... is Marcus okay?"

[OPTIONS]
[Comfort him] [Remind of crime] [Leave]
```

---

## EXAMPLE: MURDER TRIAL

```
═══════════════════════════════════
⚖️ MURDER TRIAL - Day 60
═══════════════════════════════════

CHARGES: Murder in the first degree

CRIMINAL: Sarah (formerly trusted)

CRIME:
- Poisoned Tom's food
- Tom died slowly and painfully
- Motive: Tom killed her husband

EVIDENCE:
- Poison found in her room
- Witnesses heard threats
- She confessed

VICTIM'S FAMILY:
Son: "She killed my father!
      EXECUTE HER!"

SON'S WISHES:
- Wants death
- Nothing less acceptable

───────────────────────────────────

OPTIONS:

[1] Execute
    - Son: Happy (+50)
    - Community: Mixed
    - Sarah's friends: Horrified
    - Precedent: Murder = death

[2] Life in Jail
    - Son: Angry (-30)
    - Community: Acceptable
    - Sarah: Grateful

[3] Banish
    - Son: Furious (-50)
    - Community: Divided
    - Sarah: Alive...

[4] Let Family Decide
    - Son: Chooses execution
    - Community: Respects

PLAYER CHOOSES: [1] Execute

───────────────────────────────────

AFTERMATH:
- Son: +50 relationship (thanks you)
- Sarah's friends: -30 each
- Community: Some relieved
- Some horrified
- Everyone questions: Was justice served?
```

---

## CRIMES BY CHARACTER

### Who Commits Crimes

| Character Type | Common Crimes |
|----------------|--------------|
| Hungry/Desperate | Theft |
| Angry | Assault |
| Greedy | Smuggling |
| Betrayed | Spying |
| Evil | Murder, kidnapping |
| Crazy | Random |

---

*Justice is complicated in the apocalypse.*
