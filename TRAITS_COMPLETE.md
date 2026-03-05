# OUTPOST ZERO - Character Traits (Complete List)

## COMPREHENSIVE TRAIT SYSTEM

All these traits can be randomly assigned to characters or gained through gameplay.

---

## MORAL TRAITS

| Trait | Definition | Game Effect |
|-------|------------|-------------|
| Honesty | Being truthful and transparent | +20% relationship trust gain |
| Integrity | Adhering to moral principles consistently | +10 reputation Good if leader |
| Kindness | Compassion and consideration | +5 happiness to nearby |
| Generosity | Giving without expecting return | Triggers gift events |
| Forgiveness | Letting go of resentment | -50% mood damage from betrayal |
| Fairness | Treating all equally | +10 Order reputation |

---

## EMOTIONAL TRAITS

| Trait | Definition | Game Effect |
|-------|------------|-------------|
| Optimism | Hopeful attitude | -1 from negative events |
| Pessimist | Expecting negative outcomes | +1 to negative events |
| Resilience | Recovering from difficulties | +50% stress recovery |
| Joyfulness | Cheerful demeanor | +5 daily happiness |
| Empathy | Understanding others' feelings | +25% mood contagion |
| Compassion | Desire to help suffering | Triggers heal events |

---

## SOCIAL TRAITS

| Trait | Definition | Game Effect |
|-------|------------|-------------|
| Loyalty | Faithful to people/groups | Never betrays, +relationship |
| Charisma | Attractive personality | +25% new relationships |
| Tactfulness | Avoiding offense | -50% relationship damage |
| Open-mindedness | Considering new ideas | +25% learning speed |
| Humility | Not overly proud | Accepts criticism well |
| Modesty | Avoiding self-promotion | +10 work quality (humble) |

---

## WORK ETHIC TRAITS

| Trait | Definition | Game Effect |
|-------|------------|-------------|
| Diligence | Persistent effort | +15% work output |
| Self-discipline | Controlling impulses | -25% stamina use |
| Perseverance | Continuing despite obstacles | Never gives up on tasks |
| Reliability | Being dependable | +20% task completion |
| Creativity | Original ideas | +10% chance special discovery |
| Enthusiasm | Excited about activities | +10 work quality when interested |

---

## COMBAT TRAITS

| Trait | Definition | Game Effect |
|-------|------------|-------------|
| Courage | Facing fear | +20% combat damage |
| Bravery | In dangerous situations | Can hold ground longer |
| Stealth | Moving unseen | +25% sneak success |
| Tactics | Strategic thinking | +15% combat advantage |
| Leadership | Inspiring others | +10% nearby ally combat |
| Fragile | Easily hurt | -25% damage resistance |

---

## INTELLECTUAL TRAITS

| Trait | Definition | Game Effect |
|-------|------------|-------------|
| Wisdom | Good judgment | +25% learning from mistakes |
| Curiosity | Desiring knowledge | +25% exploration yield |
| Intelligence | Learning ability | +20% skill gain |
| Expertise | Special knowledge | Can teach specific skill |
| Adaptability | Adjusting to change | +25% new situation success |
| Focus | Concentrated attention | -50% distraction |

---

## HEALTH/FITNESS TRAITS

| Trait | Definition | Game Effect |
|-------|------------|-------------|
| Tough | Resilient to damage | -25% damage taken |
| Fast Healer | Quick recovery | 2x healing rate |
| Pain Resistant | High pain tolerance | -50% pain effects |
| Athletic | Physically capable | +15% stamina |
| Healthy | Rarely sick | -50% illness chance |
| Fragile | Easily injured | +25% damage taken |

---

## PERSONALITY FLAWS (NEGATIVE)

| Trait | Definition | Game Effect |
|-------|------------|-------------|
| Dishonesty | Lying, deception | -20% relationship trust |
| Greed | Excessive desire for stuff | Hoards items |
| Envy | Desiring others' things | -5 happiness near happier |
| Wrath | Intense anger | +25% combat damage, -relationships |
| Sloth | Laziness | -25% work output |
| Pride | Excessive self-importance | Rejects help |
| Lust | Excessive desire | Distracted by romance |
| Gluttony | Overconsumption | Eats 2x food |

---

## MISC TRAITS

| Trait | Definition | Game Effect |
|-------|------------|-------------|
| Lucky | Good fortune | +10% random positive events |
| Unlucky | Bad fortune | +10% random negative events |
| Night Owl | Active at night | +25% night work efficiency |
| Early Bird | Active in morning | +25% morning efficiency |
| Vegetarian | No meat | Cannot eat meat |
| Allergic | Reactions to things | Random debuffs |
| Addicted | Substance dependency | -happiness without substance |
| Claustrophobic | Fear of enclosed | -happiness in small spaces |
| Pyrophobic | Fear of fire | Cannot use fire |

---

## TRAIT COMBINATION EFFECTS

### Powerful Combos

| Combo | Effect |
|-------|--------|
| Optimist + Resilient | Never stays sad long |
| Courage + Combat | Elite warrior |
| Charisma + Generosity | Perfect leader |
| Intelligence + Diligence | Master of any skill |
| Compassion + Medical | Best healer |

### Problematic Combos

| Combo | Effect |
|-------|--------|
| Pessimist + Wrath | Always angry |
| Dishonest + Charisma | Manipulator |
| Lazy + Pride | Won't work, won't improve |
| Envy + Greed | Always dissatisfied |

---

## TRAIT ACQUISITION

### How Traits Are Gained

| Trigger | Possible New Trait |
|---------|-------------------|
| Survive hard battle | Brave |
| Lose friend | Melancholic |
| Betrayed | Suspicious |
| Master skill | Expert |
| Help many | Compassionate |
| Lead successfully | Leadership |
| Many arguments | Grumpy |
| Happy childhood | Cheerful |
| Many failures | Resilient |

### How Traits Can Be Lost

| Trigger | Possible Lost Trait |
|---------|---------------------|
| Betray someone | Loyal |
| Constant failure | Optimist |
| Healed by good med | Fragile |
| Become wealthy | Humble |

---

## IMPLEMENTATION: TRAIT EFFECTS

```python
TRAIT_EFFECTS = {
    # Moral
    "Honesty": {"relationship_trust_bonus": 0.20},
    "Integrity": {"reputation_good": 10},
    "Kindness": {"nearby_happiness": 5},
    "Generosity": {"gift_events": True},
    "Fairness": {"reputation_order": 10},
    
    # Emotional
    "Optimist": {"negative_event_mod": -1},
    "Pessimist": {"negative_event_mod": 1},
    "Resilience": {"stress_recovery": 1.5},
    "Joyfulness": {"daily_happiness": 5},
    "Empathy": {"mood_contagion": 1.25},
    "Compassion": {"heal_events": True},
    
    # Social
    "Loyalty": {"betrayal_chance": 0},
    "Charisma": {"new_relationship_bonus": 0.25},
    "Tactfulness": {"relationship_damage": 0.5},
    "Open-mindedness": {"learning_speed": 1.25},
    "Humility": {"accepts_criticism": True},
    
    # Work
    "Diligence": {"work_output": 1.15},
    "Self-discipline": {"stamina_use": 0.75},
    "Perseverance": {"never_gives_up": True},
    "Reliability": {"task_completion": 1.20},
    "Creativity": {"special_discovery": 0.10},
    "Enthusiasm": {"interested_work_quality": 1.10},
    
    # Combat
    "Courage": {"combat_damage": 1.20},
    "Bravery": {"hold_ground": True},
    "Stealth": {"sneak_success": 1.25},
    "Tactics": {"combat_advantage": 1.15},
    "Leadership": {"ally_combat": 1.10},
    "Fragile": {"damage_taken": 1.25},
    
    # Health
    "Tough": {"damage_taken": 0.75},
    "Fast Healer": {"healing_rate": 2.0},
    "Pain Resistant": {"pain_effects": 0.5},
    "Athletic": {"stamina": 1.15},
    "Healthy": {"illness_chance": 0.5},
    "Fragile": {"damage_taken": 1.25},
    
    # Intellect
    "Wisdom": {"learn_from_mistakes": 1.25},
    "Curiosity": {"exploration_yield": 1.25},
    "Intelligence": {"skill_gain": 1.20},
    "Expert": {"can_teach": True},
    "Adaptability": {"new_situation": 1.25},
    "Focus": {"distraction": 0.5},
}
```

---

## EXAMPLE CHARACTERS WITH TRAITS

```
NAME: Sarah
TRAITS:
- Cheerful (+5 daily happiness)
- Detail Oriented (+3 work quality)
- Loyal (never betrays)
- Fast Healer (2x healing)
- Compassion (helps injured)
- Athletic (+15% stamina)

RESULT:
- Always happy
- Excellent work
- Trusted friend
- Heals fast
- Helps everyone
- Never tires

---

NAME: Ryan  
TRAITS:
- Pessimist (+negative events)
- Grumpy (-happiness near others)
- Lazy (-work output)
- Fragile (+damage taken)
- Envy (-happiness near happy)
- Short-tempered (-relationships)

RESULT:
- Always complains
- Poor work
- Easily hurt
- Resents happy people
- Hard to work with
```

---

*Every trait tells a story.*
