
# Pokémon Recomp

A collection of mods for the **original Pokémon Red** designed to make the game more modern, accessible, and content-rich.

All mods are available in the repository:

**[github.com/FAFF0x/gen1recomp](https://github.com/FAFF0x/gen1recomp)**

---

## Table of Contents

- [Quality of Life Mods](#quality-of-life-mods)
  - [Advanced Box System](#advanced-box-system)
  - [Area DexNav](#area-dexnav)
  - [Catch Helper](#catch-helper)
  - [DV/EV Editor](#dvev-editor)
  - [EXP Share Modes](#exp-share-modes)
  - [Free Master Ball](#free-master-ball)
  - [Free Rare Candy](#free-rare-candy)
  - [Guaranteed Catch](#guaranteed-catch)
  - [HM Anywhere](#hm-anywhere)
  - [Item Shortcut](#item-shortcut)
  - [Kanto Achievements](#kanto-achievements)
  - [Modern Bag](#modern-bag)
  - [Move Inspector](#move-inspector)
  - [Move Learn Stats](#move-learn-stats)
  - [Moves Manager](#moves-manager)
  - [Nickname Changer](#nickname-changer)
  - [Pokédex Plus](#pokédex-plus)
  - [Trade Evolution Fix](#trade-evolution-fix)
  - [Quest System](#quest-system)
  - [Repel Reuse](#repel-reuse)
  - [Reusable Machines](#reusable-machines)
  - [Summon](#summon)
  - [Universal Free TM Shop](#universal-free-tm-shop)
- [ART Mods](#art-mods)
  - [new_icons](#new_icons)
  - [new_sprites](#new_sprites)
  - [New Item Icons](#new-item-icons)
- [Debugging](#debugging)
  - [Performance Monitor](#performance-monitor)
- [Quest Mods](#quest-mods)
  - [The Three-Stone Covenant](#the-three-stone-covenant)
  - [The Mirage of Mew](#the-mirage-of-mew)
  - [The Sixth Bell](#the-sixth-bell)
  - [The Stolen Fossil](#the-stolen-fossil)
  - [Whispers Beneath Cerulean](#whispers-beneath-cerulean)
  - [The Abandoned Cabin](#the-abandoned-cabin)
  - [The Black Flower](#the-black-flower)
  - [Poachers in the Safari Zone](#poachers-in-the-safari-zone)
  - [Ashes of Cinnabar](#ashes-of-cinnabar)
  - [The Empty Throne](#the-empty-throne)
  - [Echoes Beyond the Fog](#echoes-beyond-the-fog)
  - [Crystal Onix](#crystal-onix)
  - [New Game Plus](#new-game-plus)
  - [Rocket Gym Ambushes](#rocket-gym-ambushes)
  - [Team Rocket Returns](#team-rocket-returns)

---

# Quality of Life Mods

## Advanced Box System

**Current version: v1.0.0**

Expands the original PC Box interface with faster navigation, direct swapping, and improved Box management.

### WITHDRAW

While browsing stored Pokémon:

- press **Left / Right** to switch instantly between **BOX 1 and BOX 12**;
- Box switching remains available even when the current Box is empty;
- you can continue moving between Boxes without returning to the main PC menu.

### DEPOSIT

While viewing the party:

- remain directly in the party list;
- press **Left / Right** to change the destination Box in real time;
- if the selected Box is full, you can immediately move to the next Box without leaving the menu.

### SWAP POKéMON

Adds a dedicated **SWAP POKéMON** option.

To swap Pokémon:

1. select a Pokémon stored in a Box;
2. select a Pokémon in the party;
3. the two Pokémon are exchanged directly.

The swap system also works when:

- the party already contains **6 Pokémon**;
- the party contains only **1 Pokémon**.

Because the total number of party members does not change, the normal party-size restrictions do not prevent the swap.

### Quick SWAP

A direct **SWAP** action is also available inside both:

- **WITHDRAW**
- **DEPOSIT**

This allows Pokémon to be exchanged without returning to the main PC menu.

### RELEASE

The **RELEASE** menu also supports **Left / Right** Box switching, allowing you to move between Boxes without leaving the release screen.

---

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

## Free Master Ball

**Current version: v1.0.0**

Adds the **MASTER BALL** automatically to the **BUY** list of every standard Poké Mart.

### Features

- **MASTER BALL** is available in all normal Poké Marts.
- The purchase price is set to **¥0**.

---

## Free Rare Candy

**Current version: v1.0.0**

Adds **RARE CANDY** to the **BUY** list of every standard Poké Mart.

### Features

- **RARE CANDY** is available in all normal Poké Marts.
- The purchase price is set to **¥0**.

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

## Kanto Achievements

**Current version: v1.0.4**

Adds a complete in-game achievement system with **100 unlockable achievements**.

A new **ACHIEVEMENTS** option is added to the **START** menu.

### Features

- **100 achievements** available to unlock during gameplay;
- three tabs:
  - **ALL** — displays every achievement;
  - **INCOMP** — displays incomplete achievements;
  - **DONE** — displays completed achievements;
- search by achievement name or description;
- category filtering;
- progress tracking;
- completion percentages;
- full achievement details.

---

## Modern Bag

**Current version: v1.5.0**

Transforms the Bag into a modern inventory divided into multiple pockets, navigated with **Left** and **Right**.

It also removes the original 20-item-type capacity limit.

### Available Pockets

| Pocket | Contents |
|---|---|
| **FAVORITES** | Any items marked as favorites. Accessible by pressing **Left** from the Medicine pocket. |
| **MEDICINE** | Potions, status-healing items, Revives, Ether, Elixir, vitamins, PP Ups, and Rare Candies. |
| **BALLS** | Poké Balls, Great Balls, Ultra Balls, Master Balls, and Balls added by other mods. |
| **TM HM** | All TMs and HMs. |
| **BATTLE** | X items, Dire Hit, Guard Spec., and Poké Doll. |
| **KEY ITEMS** | Bicycle, Fishing Rods, Poké Flute, keys, cards, and other important items. |
| **OTHER** | Evolution Stones, Repels, Escape Rope, fossils, and general-purpose items. |

### Favorites

A new **FAVORITES** pocket has been added.

It can be opened by pressing **Left** from the **MEDICINE** pocket.

Any item can be added to Favorites, and favorite items can be used normally directly from this section.

### Item Options

Press **SELECT** on an item to open the **ITEM OPTIONS** menu:

- **ADD FAVORITE** / **REMOVE FAVORITE**
- **PIN TO TOP** / **UNPIN ITEM**
- **MOVE ITEM**
- **CANCEL**

### Pinned Items

Pinned items:

- always remain at the top of their category;
- are not moved by alphabetical sorting;
- preserve the order in which they were pinned;
- remain pinned after closing and reopening the game.

### Indicators

The following indicators may appear next to an item's quantity:

| Indicator | Meaning |
|---|---|
| `F` | Favorite |
| `P` | Pinned to the top |
| `PF` | Favorite and pinned |

Favorite and pinned settings remain saved even when an item's quantity reaches zero.

When the item is obtained again, it automatically returns with the same settings.

### Automatic Sorting

Items are sorted automatically whenever the Bag is opened.

The sorting order is based on:

1. pocket;
2. pinned-item order;
3. item name.

TMs and HMs are sorted numerically, with HMs listed before TMs.

The automatic sorting is refreshed whenever you obtain a new type of item.

Manual reordering remains available through **SELECT → ITEM OPTIONS → MOVE ITEM** during the current play session.

### Quick Search

Press **START** while inside any standard Bag pocket to open the general search screen.

#### Controls

- **D-pad** — move across the on-screen keyboard;
- **A** — enter a character;
- **B** — delete a character or exit;
- **SELECT** — clear the current search;
- **START** or **GO** — display the search results.

The search checks every Bag pocket.

Selecting a result automatically returns you to the correct pocket with the matching item highlighted.

The search also correctly recognizes item names containing special characters, such as **POKé BALL**.

### TM/HM Search, Filters, and Sorting

While inside the **TM HM** pocket, press **START** to open a dedicated panel.

The panel provides the following options:

- **NAME** — search by move name, not only by TM or HM number;
- **TYPE** — filter by move type, including Fire, Water, Grass, Electric, Psychic, and others;
- **CLASS** — filter moves by category:
  - **PHYSICAL**
  - **SPECIAL**
  - **STATUS**
- **SORT** — choose one of the following sorting methods:
  - **Machine Number**
  - **Move Name**
  - **Power High to Low**
  - **Power Low to High**

All filters can be combined.

### TM/HM Move Information

With a TM or HM highlighted, press:

- **Controller:** `Y`
- **Keyboard:** `I`

The information screen displays:

- TM or HM number;
- move name;
- type;
- Physical, Special, or Status class;
- power;
- accuracy;
- PP;
- move effect.

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

## Move Learn Stats

**Current version: v1.0.0**

When a Pokémon already knows four moves and must forget one to learn a new move, the lower panel displays two comparison columns.

### SELECTED

Shows the currently highlighted move that would be forgotten:

- move name;
- **POWER**;
- maximum **PP**.

### LEARNING

Shows the new move the Pokémon is about to learn:

- move name;
- **POWER**;
- maximum **PP**.

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

## Nickname Changer

Adds a new renaming option directly to the standard **POKéMON** menu.

When selecting a Pokémon, the submenu now includes:

```text
STATS → RENAME → SWITCH
```

### Features

- Change a Pokémon's nickname directly from the party menu.
- Nicknames can contain up to **10 characters**.

---

## Pokédex Plus

Pokédex Plus replaces the original Pokédex with a more complete and practical version.

For each Pokémon, it allows you to view general information, base stats, habitats, encounter rates, evolutions, and moves learned by leveling up.

### Features

- Caught Pokémon indicator.
- Automatic scanning of the current party and every PC Box.
- **STATS** tab showing type, base stats, and total base stat value.
- **HABITAT** tab showing areas, encounter methods, levels, and encounter rates.
- Direct access to the area map.
- **EVOLUTION** tab showing the evolution chain and evolution method.
- **LEVEL MOVES** tab showing moves learned by level and their details.
- Quick search by pressing **START**.
- Search Pokémon by name or type.
- Compatibility with Pokémon and encounters added by other mods.

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

## Universal Free TM Shop

**Current version: v1.0.0**

Speaking to the clerk in any Poké Mart opens a new menu with the following options:

- **NORMAL SHOP** — opens the Mart's original item catalog;
- **TM SHOP** — opens a catalog containing every TM from TM01 to TM50;
- **LEAVE** — closes the shop menu.

### TM Shop Features

- TMs are sorted numerically.
- Each entry also displays the move contained in the TM.
- Every TM is sold for `0`.

---

# ART Mods

## new_icons

**Current version: v1.0.2**

Replaces the game's **small Pokémon icons** with a new set of custom icons.

---

## new_sprites

**Current version: v1.0.0**

Replaces the original **Pokémon sprites** with a new set of **modern sprites**.

---

## New Item Icons

Adds a new icon set for items.

### Features

- Includes **88 images** in total.
- **70 sprites** for regular items.
- **18 dedicated sprites** for **TM/HM types**.

---

# Debugging

## Performance Monitor

**Current version: v1.3.0**

A diagnostic tool designed to capture detailed performance data when you encounter lag in a specific area, menu, or battle.

### How to Use

Go to the area, menu, or battle where you notice performance issues and press **F8**.

The monitor records performance data for **10 seconds** and then automatically exports:

```text
performance_report_latest.json
```

It also creates a human-readable version:

```text
performance_report_latest.txt
```

After the test, you can press **F9** at any time to export the latest report again.

### Report Contents

The exported report includes:

- every **frame time** recorded during the 10-second capture;
- real FPS;
- average frame time;
- median frame time;
- **P95** and **P99** frame times;
- **1% low**;
- worst frame;
- number of frames exceeding the **16.67 ms** frame budget;
- number of frames above **18.5 ms**;
- number of frames above **33.3 ms**;
- every individual **slow frame**, including the exact time when it occurred;
- active map and screen at the time of the slow frame;
- the mod consuming the most CPU during that frame;
- second, third, and fourth highest contributors;
- **Deep Lua Profiler** results;
- exact performance hotspot, for example:
  - `main.lua:428`
  - `render.hud`
  - a quest callback
  - other exact Lua hotspots;
- exclusive CPU usage for each mod;
- worst callback for each mod;
- calls per second;
- draw calls generated by each mod;
- canvas switches;
- shader switches;
- Lua RAM usage;
- texture memory usage;
- performance trends sampled every **0.25 seconds**;
- real Logic Steps;
- complete list of loaded mods;
- **exact version of every mod**;
- priority;
- dependencies;
- load order.

### Export Location

Reports are exported to:

```text
AppData\Roaming\pokemon-love2d\performance_reports
```

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

## The Black Flower

The quest becomes available after obtaining the **Rainbow Badge**.

A black flower has begun growing in Celadon City's secret garden, draining energy from the city's Grass-type Pokémon. Erika asks for your help in discovering its origin.

### Gameplay

- Explore a plant-covered maze.
- Navigate areas filled with dangerous spores.
- Discover hidden paths.
- Battle possessed Pokémon.

### Boss

- **Victreebel**

### Reward

- **Vileplume** with maximum DVs and EVs

---

## Poachers in the Safari Zone

The quest becomes available after obtaining the **Soul Badge**.

A group of poachers has illegally entered the Safari Zone to capture rare Pokémon. You must follow their trail without being able to use your party normally.

### Gameplay

- Pursue the poachers through the Safari Zone.
- Use stealth to avoid detection.
- Overcome traps.
- Battle using freed Safari Pokémon.

### Reward

Choose one of the following Pokémon, each with maximum DVs and EVs:

- **Kangaskhan**
- **Tauros**
- **Scyther** or **Pinsir**

---

## Ashes of Cinnabar

The quest becomes available after obtaining the **Volcano Badge**.

Following an eruption in an old laboratory beneath Pokémon Mansion, artificial creatures begin appearing across Cinnabar Island.

### Gameplay

- Explore a burning laboratory.
- Unlock security doors.
- Recover secret documents.
- Complete objectives while an environmental timer is active.

### Boss

- **Ditto**, which repeatedly transforms into members of the player's party

### Reward

- **Arcanine** with maximum DVs and EVs

---

## The Empty Throne

The quest becomes available after obtaining the **Earth Badge**.

After Giovanni's disappearance, a new figure attempts to seize control of the remaining Team Rocket forces beneath Viridian Gym.

### Gameplay

- Explore a final Team Rocket dungeon.
- Battle elite Rocket Trainers.
- Make moral choices.
- Survive multiple consecutive battles.

### Boss

- A new **Rocket Commander** with a full high-level team

### Rewards

- **Porygon** with maximum DVs and EVs
- **Master Ball**

---

## Echoes Beyond the Fog

### Quest Content

The quest becomes available after helping Bill and obtaining the **Soul Badge**.

Bill detects an unknown Pokémon call coming from an abandoned lighthouse beyond the cape.

You travel through the three-level **Cape Signal Observatory** and restore its damaged equipment.

Your objectives include:

- repairing the generator;
- studying the tidal records;
- reproducing the correct **LOW-HIGH-LOW** beacon signal.

The signal opens a hidden route into the three-level **Fogbound Caverns**.

Inside the caverns, you explore:

- flooded ruins;
- ancient relay chambers;
- areas controlled by a **Black Tide scout**.

After recovering the **Mag-Key**, you gain access to the three-level **Black Tide Hideout**.

The hideout contains:

- warehouses;
- laboratories;
- specimen tanks;
- a fortified control room.

You must disable three resonance anchors and stop **Captain Morrow** from capturing the giant Dragonite.

The giant Dragonite answers Bill's beacon because it resembles the call of another member of its species.

After the capture system is destroyed, the giant Dragonite returns freely to the sea.

### Reward

- **Perfect Dragonite**
  - Level 50
  - Maximum DVs
  - Maximum Stat Experience

---

## Crystal Onix

This quest introduces **Crystal Onix** as a completely new Pokédex species, separate from the original Onix.

### Features

- **Crystal Onix** added as a new Pokédex species.
- **Rock / Ice** typing.
- Custom front sprite, back sprite, icon, and overworld sprite.
- A complete quest spanning:
  - **Vermilion City**
  - **Cinnabar Island**
  - **Fuchsia City**
  - **Seafoam Islands B4F**
- New quest items:
  - **Luminous Shard**
  - **Tidal Charm**
- A unique encounter with **Crystal Onix at Level 45**.
- Crystal Onix can either be caught during the encounter or defeated and received later from the sailor.

### Final Reward

- **Crystal Onix**
  - Level 45
  - All DVs set to `15`
  - All Stat Experience values set to `65,535`

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
