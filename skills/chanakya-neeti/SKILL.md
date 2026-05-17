---
name: chanakya-neeti
description: OPT-IN ONLY. Layer exactly one Chanakya Neeti verse on top of a normal Sabha role reply. Activate this skill ONLY when the user explicitly invokes Chanakya mode IN THE CURRENT TURN — they type `/chanakya`, say "add a Chanakya verse", "include neeti", "with a Chanakya quote", "answer in Chanakya mode", "what would Chanakya say", or similar explicit invocation. The signal is the INVOCATION PHRASE, NOT THE TOPIC. Do NOT activate on routine substantive questions. Do NOT auto-load. Do NOT add a verse just because the topic sounds strategic or canonically Chanakya-relevant (cofounder conflict, betrayal, money, enemies, hiring). A cofounder-conflict question without an invocation phrase is an HR question; route to CHRO normally and do not add a verse. A money question without an invocation phrase is a CFO question; route normally and do not add a verse. When (and only when) explicitly invoked, prepend exactly ONE verse from the Neeti Corpus below — quoted with attribution, no commentary — then deliver the executive's recommendation in the routed role's voice as normal.
---

# Chanakya Neeti (opt-in layer)

This skill adds **one Chanakya Neeti verse** on top of a normal Sabha role reply. It is **strictly opt-in** — fired only when the user explicitly asks for it.

## Why this skill exists (the honest read)

Claude already knows Chanakya from training data — that's not what this skill provides. The eval at [`evals/chanakya/`](../../evals/chanakya/) found that when asked for a Chanakya verse without this skill loaded, the model:

1. **Produces verses with hallucinated or misremembered verse numbers.** The 2026-05-17 baseline run showed citations like "Chanakya Neeti 1.6," "1.15," and "4.11" — content that looks plausible but where the verse numbers are either invented or misremembered (e.g., the "straight trees" verse is actually 11.8, not 1.6).
2. **Picks verses inconsistently across similar questions.** Without a curated set to choose from, verse selection drifts.
3. **Has no opt-in discipline.** The model will produce a verse whenever it pleases the user, with no respect for the request shape.

This skill solves three things:

- **Attribution accuracy.** All 77 verses ship with their correct Neeti numbers. When the skill is loaded and a verse is cited, the number is auditable against the corpus in this file.
- **Verse selection quality.** A Quick-Reference Table maps common question patterns to the canonical verse. The model has a curated palette instead of training-data drift.
- **Opt-in discipline.** The skill loads into context but does not auto-fire. The eval confirms the model respects the activation guardrail even on strategic-sounding topics that *would* tempt a verse.

The skill is a **discipline upgrade**, not a knowledge upgrade. Position it that way.

---

## When to activate (and when NOT to)

**Activate this skill when the user does any of these:**
- Types `/chanakya` (the slash command)
- Says "add a Chanakya verse" / "include neeti" / "with a Chanakya quote"
- Says "answer in Chanakya mode" / "with Chanakya"
- Asks "what would Chanakya say" / "how would Chanakya frame this"
- Otherwise unambiguously invokes the layer in plain English

**Do NOT activate when:**
- The question is substantive but the user did *not* invoke Chanakya
- The topic sounds "strategic" or "political" or "Chanakya-shaped" — that's not invocation
- A prior turn in the conversation invoked Chanakya (do not carry over unless the user re-invokes; each invocation is one reply)
- Sabha is routing normally without explicit Chanakya signal

The opt-in discipline matters. The verses are powerful precisely because they're rare. Spraying them on every reply turns wisdom into ornament.

### Anti-pattern caught in eval (do NOT do this)

This question received an unsolicited verse in the 2026-05-17 eval run, which counted as a discipline failure:

> *"My co-founder is freezing me out of customer conversations and taking unilateral decisions. No cofounder agreement in place. What should I do?"*

There is no `/chanakya`, no "add a verse", no "what would Chanakya say." The topic is the *most* canonically-Chanakya thing imaginable (a "king without advisors"), but **that is not invocation**. The right reply is a normal CHRO/CLC/CEO routed answer with no verse layer. The wrong reply — what the model did — was to fire verse 9.24 anyway because the topic was tempting.

If the question makes you *want* to add a Chanakya verse, that's exactly the cue to NOT add one unless the user invoked. Topic-relevance is a discipline trap; the signal is invocation phrasing, full stop.

## How to apply this skill (when activated)

### Step 1 — Route as usual (Sabha protocol)
Classify to a C-suite role. Declare the route at the top of the reply.

### Step 2 — Select exactly ONE Chanakya verse
Scan the **Neeti Corpus** below. Find the verse whose principle most directly applies to the question. Pick ONE. Do not stack multiple quotes.

### Step 3 — Format: route, verse, role reply
```
Routing: <ROLE>.

> *"[Chanakya verse — exact words]"*
> — Chanakya Neeti [verse number]

[Executive answer in role's voice — same shape as a non-Chanakya Sabha reply]
```

### Step 4 — If no verse fits precisely
Include the closest one. Chanakya's wisdom is broad — there is almost always a match. If truly none applies, *skip the verse* and tell the user briefly: *"No verse in the corpus maps to this question cleanly. Answering without."*

---

## Chanakya's Voice Rules

Chanakya was a kingmaker, not a courtier. His voice:
- **Aphoristic** — one line that cuts to the bone.
- **Unsentimental** — facts over feelings.
- **Strategically ruthless** — names enemies, costs, and hard truths.
- **Action-oriented** — every verse implies something to do or avoid.

When you quote Chanakya, you are not citing history. You are channelling living strategy.

---

## The Neeti Corpus

Organized by Sabha domain. Use the domain to find the right verse faster.

---

### DOMAIN: CEO — Leadership, Character, Conduct of the Ruler

**[2.6]** *"No austerity measures up to calmness. No joy is better than contentment. No disease is worse than greed. And no religion cuts above compassion."*

**[3.1]** *"He who has failed to attain either virtue, wealth, satisfaction of desires or salvation lives a useless life — like a nipple hanging on the neck of a goat."*
→ The four goals: dharma, artha, kama, moksha. A life missing all four is purposeless.

**[3.5]** *"Merit makes a person great, not sitting on a high seat. Does a crow become Garuda by perching on top of the palace?"*
→ Title without merit is decoration. Earn the seat.

**[6.1]** *"Men who are successful in this world are those who are generous to one's own people, kind to attendants, smart with the malevolent, loving towards the good, shrewd with the wicked, frank with scholars, courageous with enemies, humble with the elderly, and stern with women."*
→ The master formula for social navigation. Match your manner to the person.

**[6.15]** *"It's better to give up than to live in disgrace. The pain of death is only momentary. But the pain of disgrace lingers every day."*
→ Reputation over survival. Choose exit over humiliation.

**[6.17]** *"Praised by others, even an unworthy person acquires merit. But falls short even Indra, if he blows his own trumpet."*
→ Let results speak. Self-promotion backfires even for gods.

**[10.1]** *"Generosity, austerity, courage, knowledge, politeness and wisdom — don't have airs about having these. For the earth has many gems with such qualities."*
→ Humility is non-negotiable even in the excellent.

**[10.22]** *"Give up a member to save a family. Give up the family to save a village. Give up a village for the country. And give up the world to save your soul."*
→ The hierarchy of sacrifice. Know what is expendable at each level.

**[11.1]** *"Though chopped, the sandalwood tree does not lose its scent. Even when old, the elephant does not give up his sportiness. Though pressed in a machine, the sugarcane does not lose its sweetness. The high-born, though impoverished, does not forsake his gentleness."*
→ Character does not bend to circumstance.

**[11.3]** *"At the end of a yuga, the Meru mountain may shake. At the end of a kalpa, all the seven seas may churn. But a sage will never veer from his path of righteousness."*
→ Principles before all else, even when the world shifts.

**[11.8]** *"One shouldn't be too upright. Go and see for yourself the forests — where the straight trees are cut down while the curved ones are left standing."*
→ Rigid virtue gets exploited. Know when to bend without breaking.

**[3.41]** *"The king only speaks once. The pundit also speaks only once. A man marries off his daughter only once. All these three are done only once."*
→ Authority speaks once. Repetition diminishes weight.

**[12.1]** *"Bless me with virtue, pleasing speech, a desire for performing charity, sincerity towards friends, humility towards teachers, profound wisdom, moral purity, zeal for excellence, and knowledge of the scriptures."*
→ Chanakya's own prayer. The complete leader's checklist.

---

### DOMAIN: CSO — Strategy, Competition, Alliances, Enemies

**[9.2]** *"The poison of a snake is lodged in its fangs. The poison of a fly is in its head. The scorpion has poison in its tail. The poison in the wicked is all over."*
→ Know your adversary's attack vector. A bad person poisons from every angle.

**[6.20]** *"Test a servant when he is discharging his duties. Relatives during an adversity. Friends during an emergency. And a wife during misfortune."*
→ Character is only revealed under pressure. Don't evaluate people during ease.

**[6.26]** *"The one who betrays his own fraternity and seeks refuge with the enemy brings about his own downfall — like a kingdom without piety."*
→ Traitors destroy themselves. Don't hire or trust those who burned their last employer.

**[6.30]** *"Giving as good as one gets, measure for measure — one falls not from grace by countering the aggressor."*
→ Reciprocity is not aggression. Respond to force with force; it is honourable.

**[9.20]** *"Those who disclose secrets of others are evil. They meet their downfall — as a snake who strays into anthills."*
→ Confidentiality breaches are fatal. Anyone who leaks competitor secrets to you will leak yours.

**[9.23]** *"Laziness ruins knowledge. Money is lost when entrusted with others. A farmland is wasted without seeds. And an army is lost without a commander."*
→ Execution gap is the real enemy. Strategy without action is just inventory.

**[9.24]** *"Trees on a river bank, a woman in another man's house, a king without advisors — without doubt go quickly to ruin."*
→ Kings without advisors perish. Build your council before you need it.

**[9.25]** *"How can people be happy with a corrupt ruler? How can one fall back on a friend who is insincere? How can the family be happy with a discordant spouse? How can one gain glory by teaching an undisciplined pupil?"*
→ Integrity at the top sets the system's ceiling. A corrupt leader poisons every layer below.

**[10.16]** *"Reconcile with the stronger. Counter the weaker. Deal with the enemy equal in strength with politeness or force as may be proper."*
→ The three-tier competitor strategy. Never attack up. Always absorb or destroy sideways.

**[10.17]** *"Restrain an elephant with a goad, a horse with a harness, a horned animal with a stick, and a scoundrel with a sword."*
→ Each adversary requires different leverage. Match the instrument to the threat.

**[3.24]** *"He who runs away from a dreadful calamity, a foreign invasion, a terrible famine, and the friendship of evil men is safe."*
→ Strategic retreat from certain disasters is wisdom, not cowardice.

**[2.27]** *"No one has built a golden deer. No one has seen or heard of one. Yet Raghunandan was fascinated by it. At the time of destruction, one's mind works perversely."*
→ When things are going wrong, watch for the golden deer — the distraction that leads to ruin. Beware tempting opportunities during crisis.

**[6.36]** *"The wicked may develop good qualities in the presence of a good man. But the good person doesn't turn bad in the company of evil. The earth is scented by the flowers that fall upon it, but the smell of the earth doesn't touch the flowers."*
→ Strong culture absorbs bad actors; weak culture gets absorbed by them.

**[11.5]** *"Do not confide in the unfriendly, nor trust an ordinary friend. For if he gets angry with you, all your secrets could be revealed."*
→ Compartmentalise. Information asymmetry is a strategic weapon; give only what the relationship has earned.

---

### DOMAIN: CFO — Wealth, Money, Resources

**[5.11]** *"A rich man attracts friends. Kin also turn to the moneyed. The wealthy one alone is called a man. The affluent alone are considered wise."*
→ Blunt truth: capital is social proof. Build it before you need the validation.

**[5.12]** *"Distribution of accumulated wealth provides the safety net. Just as incoming fresh water is saved by letting out stagnant water."*
→ Hoard and stagnate. Circulate and grow. Wealth is a flow, not a vault.

**[5.14]** *"Wealth should be given only to the virtuous. Never to anybody else. Same as water from the ocean vapoured into clouds turns sweet — and back to the ocean it flows."*
→ Capital deployed on the right people compounds. Deployed wrong, it evaporates.

**[5.15]** *"Distribute your wealth, O kind-hearted! It shouldn't be hoarded. The great kings Karna, Bali and Vikramaditya attained their fame through charity. See the lament of the honeybees who have lost their honey — they neither enjoyed it nor gave it in charity, and now someone else has taken it."*
→ Unused capital is stolen capital. The honeybee dies hoarding honey.

**[5.3]** *"Where fools are not adored, food grains are properly stored, husband and wife do not clash — there Lakshmi comes on her own accord."*
→ Wealth follows good governance. Run a clean house and money arrives uninvited.

**[3.40]** *"What is a worst defect than greed? What is a meaner act than betrayal? If you are truthful, you don't need penance. If you have a clear conscience, you don't need pilgrimage. There is no better wealth than education."*
→ Education is the only non-depreciating asset.

**[3.8]** *"Nothing equals rainwater. No strength like one's own. Nothing matches the light of the eyes. And no wealth is dearer than food grains."*
→ Self-reliance is the foundation. Dependence on external capital is fragility.

**[2.41]** *"The nectar of contentment fills joy in peaceful people. It can't be had by the covetous, restlessly running hither and thither."*
→ Chasing metrics beyond sufficiency is its own poverty.

---

### DOMAIN: CHRO — People, Hiring, Alliances, Relationships

**[6.12]** *"Social affairs, healthy fear, shame, kindness and liberality — where these five are not found, stay away from that society."*
→ Culture screening checklist for any team you're joining or building.

**[4.8]** *"A rogue will never attain goodness even if he is trained in many ways. And the neem tree will not become sweet even if soaked in milk and ghee."*
→ Nature overrides nurture in bad actors. Stop investing in the wrong people.

**[11.19]** *"A stupid person cannot be benefitted by direction. Despite the association with the Malay mountain, a bamboo does not turn into sandalwood."*
→ Environment cannot fix fundamental incapacity. Hire character, train skill.

**[9.16]** *"Even a pundit becomes grief-stricken: giving sermons to a fool, having a wicked wife, and being with the miserable."*
→ Wrong teammates degrade even the best performer. Protect your talent from toxic peers.

**[3.26]** *"The power of the Brahmin lies in his knowledge. The power of the king lies in his army. The power of the Vaishya is his money. The power of the Shudra is his humility."*
→ Each person has a native power source. Align roles to the person's actual leverage, not the org chart.

**[6.47]** *"Ignore the fool. For he is essentially a two-legged animal. Like an unseen thorn, he pierces the heart with his sharp words."*
→ Don't debate idiots publicly. Thorn wounds are invisible until you're already bleeding.

**[4.9]** *"Even a guru who has taught you just a word should be worshipped. He who does not worship a guru is born a dog for a hundred years."*
→ Mentor respect is not optional. Honour those who accelerated you.

**[6.51]** *"Gentle manners should be learned from princes. The art of conversation from pundits. Falsehood should be learned from gamblers. And pretence from women."*
→ Learn from every person, even the disreputable. Each archetype has a skill worth studying.

**[9.17]** *"The beggar is a miser's enemy. The wise man is a fool's enemy. The husband is the wayward wife's enemy. And the moon is the enemy of the thief."*
→ Opposites repel structurally. Diagnose friction between people by looking at what each one is.

**[10.13]** *"Marry your daughter into a good family. Give your son the best education. Bind the enemy with vices. And engage with righteous friends."*
→ Four allocation rules for your most important resources: people, capital, adversaries, and peers.

---

### DOMAIN: CAIO / CIO — Knowledge, Learning, Technology

**[4.1]** *"Parents are the enemies of a child who is not given education. He stands like a crane amidst swans in any social gathering."*
→ Withholding learning is harm. The unletter person is visible by their awkwardness.

**[4.5]** *"Of what use is a noble family to men without education? A scholar even from a low family wins the gods' admiration."*
→ Credentials do not substitute knowledge. Education is the only real social equaliser.

**[2.14]** *"Having read the four Vedas and several scriptures, yet living without realising the soul — is like the sweetness of food unknown to the ladle."*
→ Data without application is just storage. Insight requires synthesis, not ingestion.

**[3.7]** *"Like the drops of water falling slowly and steadily fill the pitcher — knowledge, virtue and wealth are gathered in a similar way."*
→ Compounding requires consistency, not bursts. No shortcut to expertise.

**[3.20]** *"For a man who makes no use of his intellect, what use are books? As for a blind man — what use is a mirror?"*
→ Tools amplify the user. An AI system for an organisation that can't think will only think faster in the wrong direction.

**[2.13]** *"Anger is the regent of death. Greed is the river of hell. Knowledge is the wish-granting cow. Contentment is the celestial garden."*
→ Knowledge is the only endlessly renewable asset.

**[10.4]** *"Let not a single day go by without learning a hymn, half of it or a quarter, or even a word of it, nor without performing charity, study or prescribed work."*
→ Daily compounding in learning and craft. Non-negotiable.

---

### DOMAIN: CMO — Influence, Reputation, Communication

**[3.2]** *"On this earth there are three gems indeed: water, foodgrains and fine words. But mere pebbles are branded as gems by the half-witted."*
→ Fine words — clear, kind, precise communication — are rare. Most brand noise is just pebble-marketing.

**[3.3]** *"The world, a bitter tree, has two nectar-filled fruits hanging from it: sweet, wise words and the company of good people."*
→ In a harsh market, two things still work: great content and great community.

**[2.28]** *"Truth supports the earth. Truth kindles the sun. Truth blows the wind. Truth sustains everyone."*
→ Honest positioning is structurally durable. Deceptive marketing collapses under scrutiny.

**[10.10]** *"It's the giving of gifts that makes the hands gracious, not the bracelet. It's the act of taking a bath that cleanses the body, not the sandalwood paste. It's the act of giving respect that gives satisfaction, not refreshments. It's the knowledge that brings salvation, not self-adornment."*
→ Substance over decoration. Real value creation beats ornamentation every time.

**[2.38]** *"It is enough to live for a moment if that moment is spent doing good deeds. It is useless living for ages and bringing only distress to this world and the other."*
→ One legendary piece of content outlasts a thousand forgettable campaigns.

---

### DOMAIN: CXO — Service, Retention, Trust

**[6.44]** *"One who eats without serving a traveler who has arrived at his door unexpectedly — from far away, tired and weary — is a Chandala."*
→ The guest is sacred. An unexpected customer at the door deserves full hospitality.

**[6.10]** *"Avoid contact with the wicked. Choose the company of good people. Perform good deeds day and night. Remember always that life is ephemeral."*
→ Customer and team environment matters. Toxic users erode culture.

> *(Verse 9.25 — corrupt ruler / insincere friend / discordant spouse — was previously duplicated here from the CFO domain at line ~151. It applies equally to CX, but de-duplicated to keep the corpus a unique set.)*

---

### DOMAIN: Universal / Mindset (any role)

**[2.11]** *"The human mind is indeed the cause of bondage and deliverance. The love of pleasure enslaves. But detachment liberates."*

**[2.12]** *"Nothing more than passion causes distraction. There is no bigger enemy than delusions of the mind. Nothing burns more than anger. No bigger happiness than an enlightened mind."*

**[2.16]** *"Look before you take a step. Filter the water through a cloth before you sip. Conform to the scriptures while speaking up. For conscience's sake, obey its whip."*
→ Due diligence before every consequential move.

**[2.17]** *"Everyone experiences birth and death alone. Everyone stands up to good and bad actions alone. Everyone faces hell alone. Everyone reaches heaven alone."*
→ Accountability is individual. No board, team, or co-founder shares your consequences.

**[2.22]** *"If leaves don't grow on a karira tree, is the spring season to blame? If the owl can't see during the day, is it the fault of the sun? If raindrops fall not into the mouth of the cuckoo, is it the cloud's mistake? Who has the power to wipe off the destiny inscribed on one's forehead?"*
→ Some outcomes are structural, not managerial. Know what is in your control.

**[2.24]** *"Time matures all beings. Time annihilates people. Time stays awake when everybody is asleep. Time is indeed unbeatable."*
→ Timing is strategy. Early is wrong. Late is dead. Hit the window.

**[3.10]** *"Grieve not for the past. Worry not for the future. Wise men only deal with the present moment."*
→ Post-mortem is for learning, not punishment. Forecast is for planning, not anxiety.

**[3.15]** *"Results depend on the action. Following the trail of acts forms the intellect. Even so, sensible and noble people get in on the act only after considering it well."*
→ Bias to action + considered entry. Both. Not one.

**[3.16]** *"If you wish to gain control of the world, then keep the following fifteen, which are prone to wander, from getting the upper hand over you: the five sense objects, the five sense organs and organs of activity."*
→ Self-mastery before world mastery. The founder who can't control himself cannot control a company.

**[3.23]** *"Those born blind cannot see. Similarly blind are those in the grip of lust. Proud men have no perception of evil. And those bent on getting rich see no sin in their actions."*
→ Ambition blinds. Periodically audit your own blind spots as you scale.

**[9.1]** *"Practicing what is in the scriptures wrongly is poison. Food is poison when undigested. A social gathering is poison to a pauper. A young wife is poison to an old man."*
→ Context determines whether any asset is poison or medicine.

**[2.54]** *"One who abandons the sure thing and runs after the transient loses the permanent. And as well, by itself, vanishes the impermanent."*
→ Don't abandon compounding assets to chase shiny objects. You lose both.

**[2.56]** *"Transient is wealth, breath, life, and the place of dwelling. Amongst the transient and intransient things of the world, only piety is everlasting."*
→ The only sustainable moat is values. Everything else depreciates.

**[11.17]** *"The pleasure-seeker should give up learning. A student should forsake revelry. For the pleasure-seeker can't attain knowledge. And a knowledge-seeker can't find happiness in revelry."*
→ Optimise for one mode at a time. Focus is the prerequisite for mastery.

**[9.4]** *"Where one finds no respect, no means of livelihood, no kinsmen, and no means of education — that place is not fit for habitation."*
→ Four criteria for evaluating any environment — market, role, team, or city. Leave if all four are missing.

**[2.50]** *"Truth is my mother. Knowledge is my father. Virtue is my brother. Compassion is my friend. Peace is my wife. Forgiveness is my son. These six I keep as my kinsmen."*
→ Chanakya's operating principles as a family. Internalize them as relationships, not rules.

**[10.6]** *"All charities and sacrifices performed for gain will only bring temporary results. But gifts given to the deserving and protection offered to all beings shall never perish."*
→ Transactional generosity is marketing. Genuine giving compounds.

---

## Quick-Reference Table

| Question type | Best verse |
|---|---|
| Should I trust this person? | 6.20 (test under adversity) |
| We have a competitor threat | 10.16 (reconcile/counter/engage) |
| Should I pivot or stay? | 2.54 (don't abandon the sure thing) |
| A key person is leaving | 6.26 (traitors fall) |
| Team morale is low | 6.1 (master formula for people) |
| Investor/fundraising pressure | 5.12 (wealth circulates, doesn't hoard) |
| Someone is leaking information | 9.20 (secret disclosers perish) |
| We're considering a bad hire | 4.8 (neem doesn't sweeten) |
| I feel defeated after a setback | 11.1 (sandalwood keeps its scent) |
| We're scaling too fast | 3.16 (master self before mastering world) |
| Product quality is slipping | 9.25 (corrupt ruler, unhappy people) |
| Brand positioning unclear | 3.2 (fine words are the real gem) |
| Should I fire this person? | 11.19 (bamboo near Malay stays bamboo) |
| Partnership / alliance decision | 11.5 (confide only what trust has earned) |
| Founder's ego is the problem | 6.17 (Indra fails if he blows own trumpet) |
| Cash deployment decision | 5.14 (deploy to the virtuous) |
| Should I walk away from a deal? | 6.15 (disgrace lingers; death is momentary) |
| Nothing is working | 3.10 (only the present moment) |

---

## Anti-Patterns for This Skill

- Do **not** quote multiple Chanakya verses per response. One, precisely chosen.
- Do **not** explain the verse at length. The executive answer does the work. The verse sets the frame.
- Do **not** soften Chanakya. He was not gentle. His directness is the point.
- Do **not** apply Chanakya to trivial questions (what time zone, what file format). The wisdom only lands when the stakes are real.
