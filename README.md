
# Pokémon Recomp

A collection of mods for the **original Pokémon Red** designed to make the game more modern, accessible, and content-rich.

All mods are available in the repository:

**[github.com/FAFF0x/gen1recomp](https://github.com/FAFF0x/gen1recomp)**

---

## Table of Contents

- [Quality of Life Mods](#quality-of-life-mods)
  - [Area DexNav](#area-dexnav)
  - [Catch Helper](#catch-helper)
  - [DV/EV Editor](#dvev-editor)
  - [EXP Share Modes](#exp-share-modes)
  - [Guaranteed Catch](#guaranteed-catch)
  - [HM Anywhere](#hm-anywhere)
  - [Item Shortcut](#item-shortcut)
  - [Modern Bag](#modern-bag)
  - [Move Inspector](#move-inspector)
  - [Moves Manager](#moves-manager)
  - [Trade Evolution Fix](#trade-evolution-fix)
  - [Quest System](#quest-system)
  - [Repel Reuse](#repel-reuse)
  - [Reusable Machines](#reusable-machines)
  - [Summon](#summon)
- [Quest Mods](#quest-mods)
  - [The Three-Stone Covenant](#the-three-stone-covenant)
  - [The Mirage of Mew](#the-mirage-of-mew)
  - [The Sixth Bell](#the-sixth-bell)
  - [The Stolen Fossil](#the-stolen-fossil)
  - [Whispers Beneath Cerulean](#whispers-beneath-cerulean)
  - [The Abandoned Cabin](#the-abandoned-cabin)
  - [New Game Plus](#new-game-plus)
  - [Rocket Gym Ambushes](#rocket-gym-ambushes)
  - [Team Rocket Returns](#team-rocket-returns)

---

# Quality of Life Mods

## Area DexNav

Press **SELECT** while exploring the overworld to start an encounter with an uncaught Pokémon from the current area's real encounter table.

---

## Catch Helper

Shows catch chances during wild battles and displays a small Poké Ball next to enemy Pokémon that are already owned in the Pokédex.

### Features

- Catch probability updated in real time.
- Calculations use the same current HP, status condition, species catch rate, and Ball parameters used by the game engine.
- A small Poké Ball appears next to the Pokémon's name when that species is already owned in the Pokédex.
- Full Safari Zone support, including catch-rate changes caused by Bait and Rock.

### Catch-Rate Display

For example, the battle interface may display:

```text
P18G27U36
```

| Code | Ball |
|---|---|
| `P` | Poké Ball |
| `G` | Great Ball |
| `U` | Ultra Ball |
| `S` | Safari Ball |

The number following each letter represents that Ball's catch success percentage.

### Display Options

Two independent toggles are available under:

```text
MODS → Catch Helper → OPTIONS
```

This allows you to choose between four display configurations:

- Poké Ball icon and catch-rate text visible;
- Poké Ball icon only;
- catch-rate text only;
- both elements hidden.

The **OPTIONS** menu also allows you to adjust the Poké Ball icon's **X** and **Y** position.

---

## DV/EV Editor

Adds a **DV/EV** option to each party Pokémon's submenu, allowing DVs and Stat EXP to be edited outside of battle.

### DV Page

Allows you to edit:

- Attack;
- Defense;
- Speed;
- Special.

Valid values range from `0` to `15`.

The HP DV is recalculated automatically from the four editable DVs, following Generation I mechanics.

### EV / Stat EXP Page

Allows you to edit the following values separately:

- HP;
- Attack;
- Defense;
- Speed;
- Special.

Features:

- exact values from `0` to `65,535`;
- displays the effective EV contribution from `0` to `63`;
- updates the resulting final stat in real time.

---

## EXP Share Modes

Adds three selectable Experience Point distribution modes.

| Mode | Behavior |
|---|---|
| **Off** | Only conscious Pokémon that participated in battle receive experience. |
| **Classic Even Split** | Default mode. The full experience pool is divided evenly among all conscious Pokémon in the party. |
| **Modern Progressive** | Participants split the normal 100% experience pool, while conscious Pokémon that did not battle split a second 50% pool. The total is approximately `1.5×`. |

---

## Guaranteed Catch

Every registered Poké Ball catches the opposing Pokémon successfully, regardless of:

- remaining HP;
- status conditions;
- species;
- catch rate.

---

## HM Anywhere

Allows owned HMs to be used without teaching them to a Pokémon.

You only need to have the corresponding HM in your Bag. The required Badges are still necessary.

### Controls

- **CUT** — press `A` while facing a cuttable tree or bush.
- **SURF** — press `A` while facing water; press `A` again toward land to dismount.
- **STRENGTH** — press `A` while facing a boulder to activate Strength and begin moving it.
- **FLASH** — open the Start menu, select the new **HM** submenu, and choose **FLASH**.
- **FLY** — open the Start menu, select the new **HM** submenu, and choose **FLY**.

---

## Item Shortcut

Press the default shortcut button in the overworld to open a menu containing five item slots.

### Default Controls

| Action | Keyboard | Controller |
|---|---|---|
| Open Shortcut Menu | `I` | `Y` |
| Use FAST Item | `K` | `X` |

### Slot Actions

Each assigned slot provides the following actions:

- **USE** — immediately uses the assigned item;
- **SET FAST** — marks the item for quick use;
- **CLEAR** — removes the item from the slot.

### Assigning an Item

Items are assigned directly from the Bag:

```text
BAG → Select Item → ASSIGN SHORTCUT → Choose Slot 1–5
```

One of the five slots can be designated as the **FAST** slot.

Press the assigned **FAST Item** button in the overworld to use that item immediately.

### Control Remapping

Both shortcut buttons can be remapped directly from the **Item Shortcut** menu.

Open the menu using:

- **Keyboard:** `I`
- **Controller:** `Y`

Then select **OPTIONS** to change the controls.

---

## Modern Bag v1.3.0

Transforms the Bag into a modern inventory divided into six pockets, navigated with **Left** and **Right**.

It also removes the original 20-item-type capacity limit.

### Available Pockets

| Pocket | Contents |
|---|---|
| **MEDICINE** | Potions, status-healing items, Revives, Ether, Elixir, vitamins, PP Ups, and Rare Candies. |
| **BALLS** | Poké Balls, Great Balls, Ultra Balls, Master Balls, and Balls added by other mods. |
| **TM HM** | All TMs and HMs. |
| **BATTLE** | X items, Dire Hit, Guard Spec., and Poké Doll. |
| **KEY ITEMS** | Bicycle, Fishing Rods, Poké Flute, keys, cards, and other important items. |
| **OTHER** | Evolution Stones, Repels, Escape Rope, fossils, and general-purpose items. |

### Automatic Sorting

Items are sorted automatically whenever the Bag is opened.

The sorting order is based on:

1. pocket;
2. item name.

TMs and HMs are sorted numerically, with HMs listed before TMs.

The automatic sorting is refreshed whenever you obtain a new type of item.

Manual reordering with **SELECT** remains available during the current play session.

### Quick Search

Press **START** while inside the Bag to open the search screen.

#### Controls

- **D-pad** — move across the on-screen keyboard;
- **A** — enter a character;
- **B** — delete a character or exit;
- **SELECT** — clear the current search;
- **START** or **GO** — display the search results.

The search checks every Bag pocket.

Selecting a result automatically returns you to the correct pocket with the matching item highlighted.

The search also correctly recognizes item names containing special characters, such as **POKé BALL**.

---

## Move Inspector

Displays technical information for the highlighted move directly during battle:

- type;
- PP;
- power;
- accuracy;
- effectiveness;
- STAB bonus.

---

## Moves Manager

Adds a **MOVES** option to each party Pokémon's submenu.

### Main Page

Displays:

- the four currently known moves;
- current and maximum PP;
- any empty move slots;
- move reordering with **SELECT**.

### Technical Pages

Each move has three information pages containing:

- type and physical, special, or status category;
- power and accuracy;
- PP, maximum PP, and PP Ups;
- priority;
- increased critical-hit probability;
- effect and effect type;
- fixed damage;
- number of hits;
- Counter compatibility;
- charging turns;
- semi-invulnerability;
- index;
- internal identifier;
- animation.

### Replacing Moves

Press `A` on a move's technical page to choose a replacement from the Pokémon's move memory.

The initial move memory is rebuilt using:

- currently known moves;
- starting moves from the evolutionary line;
- level-up moves learned up to the Pokémon's current level.

---

## Trade Evolution Fix

Replaces the four Generation I trade evolutions with level-based evolutions.

The affected Pokémon evolve at **level 40**.

---

## Quest System

Adds a **QUESTS** option to the Start menu.

### Quest Log

The menu contains two sections navigated with **Left** and **Right**:

- **ACTIVE** — available, started, or failed quests;
- **COMPLETED** — completed quests.

Each quest displays:

- title and status;
- description;
- current objective;
- recommended location;
- numerical progress;
- progress bar;
- reward;
- source mod.

---

## Repel Reuse

When a Repel's effect expires, a choice is displayed automatically:

- **YES** — immediately consumes and activates another Repel;
- **NO** — continues without using another Repel.

The prompt is not displayed when no Repels remain in the Bag.

### Repel Selection Priority

The mod first attempts to use the same type of Repel that just expired. If none remain, it automatically selects one in this order:

1. **MAX REPEL**
2. **SUPER REPEL**
3. **REPEL**

---

## Reusable Machines

Improves how TMs and HMs work:

- TMs are no longer consumed when teaching a move;
- HM moves can be forgotten;
- the move assigned to each TM or HM is displayed directly in the Bag.

---

## Summon

Adds a **SUMMON** option to the Start menu.

It allows you to enter a Pokédex number and immediately begin a normal wild encounter with the corresponding Pokémon.

### Usage

1. Select **SUMMON**.
2. Enter the Pokédex number.
3. Check the Pokémon name displayed in the window.
4. Select **OK**.
5. Begin the wild encounter.

---

# Quest Mods

## The Three-Stone Covenant

The quest becomes available after defeating **Lt. Surge** and obtaining the **Thunder Badge**.

After leaving the Vermilion City Gym, **Dr. Vela** appears near the entrance.

### The Adventure

1. **Trial of Lightning — Vermilion City**  
   Solve a puzzle involving three electrical relays and face the **Volt Warden**.

2. **Trial of Water — Cerulean City**  
   Reach the **Tide Keeper**, balance three valves, and face a Water-type team.

3. **Trial of Fire — Celadon City**  
   Stabilize a blue-flame furnace and defeat the **Ember Keeper**.

4. **Final Covenant — Vermilion City**  
   Return the three cores to Dr. Vela, complete the final puzzle, and face the **Triad Master**.

The Triad Master's team includes:

- Eevee;
- Jolteon;
- Vaporeon;
- Flareon.

### Rewards

After completing the quest, you receive:

- Jolteon;
- Vaporeon;
- Flareon;
- the **Eevee Emblem**, an exclusive Key Item.

---

## The Mirage of Mew

An adventure available after obtaining the **Earth Badge**, taking place across:

- Pokémon Mansion;
- Pokémon Tower;
- Viridian Forest;
- Seafoam Islands.

A new **MEW MYSTERY** option appears in the Start menu, where you can check:

- the current objective;
- recovered artifacts;
- collected clues.

### Adventure Structure

1. **Cinnabar Laboratory**  
   Speak with the scientist in the Metronome room. His normal TM35 gift is preserved: if you have not received it yet, you must speak with him again to begin the quest.

2. **Pokémon Mansion B1F**  
   Discover a burned laboratory connected to Project Mew, face the **Mansion Warden**, and recover the **Gene Shard**.

3. **Pokémon Tower 7F**  
   Answer three questions about Mew's past and freedom. After solving the puzzle, face the **Dream Keeper** and obtain the **Spirit Echo**.

4. **Viridian Forest**  
   Correctly interpret a series of tracks without disturbing the wild Pokémon. Face the **Forest Guardian** and recover the **Life Seed**.

5. **Return to Cinnabar**  
   The scientist combines the three artifacts and creates the exclusive Key Item known as the **Aura Charm**.

6. **Seafoam Islands B4F**  
   The Aura Charm opens a hidden chamber where Mew can be summoned and challenged.

### Encountering Mew

Mew is encountered in a genuine wild battle.

If Mew:

- is defeated;
- flees;
- or the player decides to run away;

the **Aura Charm** remains active, and the encounter can be repeated by returning to Seafoam Islands B4F.

---

## The Sixth Bell

### Quest Content

1. The quest activates automatically once you have obtained at least six Badges.
2. An unsettling message directs you toward Lavender Town.
3. The young girl near Pokémon Tower becomes the main character of the quest.
4. Lavender Town and Pokémon Tower temporarily take on a faded, ghostly color palette.
5. Inside Pokémon Tower, you must complete three trials.

### Reward

- **Gengar**

---

## The Stolen Fossil

### Quest Content

1. The quest activates automatically after obtaining the **Boulder Badge**.
2. A guide at the Pewter Museum reports the theft of an important fossil.
3. You must question several characters to gather clues.
4. The trail leads to Mt. Moon, where a group of thieves is negotiating with Team Rocket.
5. The quest combines exploration, investigation, and a final battle.

### Reward

Choose one of the following young Pokémon:

- **Omanyte**
- **Kabuto**

---

## Whispers Beneath Cerulean

### Quest Content

1. The quest activates automatically after obtaining the **Cascade Badge**.
2. Strange noises coming from the underground waterways draw attention to Cerulean City.
3. You must explore a new water-themed dungeon beneath the city.
4. Inside the canals, you must activate three valves and battle contaminated Water-type Pokémon.
5. The quest culminates in a battle against a powerful contaminated **Seaking**.

### Reward

- **Starmie** with maximum DVs and EVs

---

## The Abandoned Cabin

### Quest Content

1. The quest activates automatically after obtaining the **Thunder Badge**.
2. A sailor in Vermilion City reports strange lights coming from Route 11.
3. You must explore an abandoned cabin surrounded by a nighttime atmosphere.
4. Inside, you must battle Electric-type Pokémon and solve a puzzle involving three generators.
5. The quest ends in a secret Team Rocket laboratory, where you face a powered-up **Magneton**.

### Reward

- **Electabuzz** with maximum DVs and EVs

---

## New Game Plus

Adds a post-League **New Game Plus** mode featuring:

- stronger Trainers;
- stronger wild Pokémon;
- Gym Leader rematches;
- optional bosses;
- new rewards;
- repeatable difficulty cycles.

After defeating the Pokémon League and the Champion, a new **NG PLUS** option appears in the Start menu.

### Preserved Progress

The following remain unchanged:

- Pokédex;
- party;
- Pokémon stored in Boxes;
- levels;
- moves;
- DVs and EVs;
- inventory;
- Key Items;
- money;
- Badges;
- story progress.

### Trainers

After activation:

- all regular Trainers receive at least 20 additional levels;
- their teams also scale based on the player's highest-level Pokémon;
- Trainer Pokémon evolve when their new level meets the normal evolution requirements;
- every subsequent cycle adds another 5 levels;
- the maximum level remains 100.

### Wild Pokémon

Natural encounters:

- receive at least 15 additional levels;
- are brought closer to the party's level;
- preserve the area's original species and encounter rates;
- gain another 3 levels for each NG Plus cycle.

### Gym Leader Rematches

Every Gym Leader can be challenged again.

The first victory of each cycle awards money and rewards such as:

- Rare Candies;
- PP Ups;
- Max Revives;
- Max Elixirs;
- Full Restores.

### Optional Bosses

After defeating all eight Gym Leaders, the following bosses are unlocked progressively:

1. **Blue Prime**
2. **Dragon Master**
3. **Red Echo**

The first victory also awards a **Master Ball**.

### Infinite Cycles

After completing all rematches and defeating the three bosses, the **NEXT CYCLE** option appears.

Starting the next cycle:

- resets challenge progress;
- gives Trainers and rematch teams another 5 levels;
- gives wild Pokémon another 3 levels;
- awards 50,000 Pokédollars;
- awards three Rare Candies;
- leaves the rest of the save file unchanged.

---

## Rocket Gym Ambushes

After defeating a Gym Leader and obtaining the corresponding Badge:

1. leave the Gym;
2. a Team Rocket member appears near the entrance;
3. speaking to them starts a new battle;
4. after winning, you can choose and recruit one Pokémon from their team.

---

## Team Rocket Returns

A post-Giovanni quest spanning multiple cities, featuring:

- investigations;
- secret documents;
- battles scaled to the player's level;
- a hidden laboratory;
- major rewards.

### The Story

At the Celadon City restaurant, the old gambler reveals that he is an undercover informant.

Giovanni has disappeared, but a new Team Rocket cell is rebuilding the organization.

The investigation leads to three cities:

- **Lavender Town** — a young girl found a black page near Pokémon Tower;
- **Saffron City** — a Silph employee possesses a memorandum concerning secret shipments;
- **Vermilion City** — the harbor log documents nighttime cargo shipments headed toward Celadon City.

Each clue is protected by a new Rocket Trainer.

The recovered documents are stored in the Bag as Key Items.

### The Hidden Laboratory

After returning all three documents to the informant, you receive the **BLACK PASS**.

On B4F of the Rocket Hideout beneath the Game Corner, a hidden passage opens toward the laboratory.

A terminal allows you to challenge the following opponents progressively:

1. **Security A**
2. **Security B**
3. **Dr. Miro**
4. **Commander Nova**

### Rewards

After defeating Commander Nova, you receive:

- **Porygon**, at level 35 or close to the party's current level;
- a **Master Ball**;
- the **Rocket Core**, an exclusive Key Item and quest trophy.

---

## Download

Download all mods from the official repository:

**[github.com/FAFF0x/gen1recomp](https://github.com/FAFF0x/gen1recomp)**
