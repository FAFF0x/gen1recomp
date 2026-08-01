
# Pokémon Recomp

Una raccolta di mod per **Pokémon Rosso originale** pensate per rendere l’esperienza di gioco più moderna, accessibile e ricca di contenuti.

Tutte le mod sono disponibili nel repository:

**[github.com/FAFF0x/gen1recomp](https://github.com/FAFF0x/gen1recomp)**

---

## Indice

- [Quality of Life Mods](#quality-of-life-mods)
  - [Area DexNav](#area-dexnav)
  - [Catch Helper](#catch-helper)
  - [DV/EV Editor](#dvev-editor)
  - [EXP Share Modes](#exp-share-modes)
  - [Guaranteed Catch](#guaranteed-catch)
  - [HM Anywhere](#hm-anywhere)
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
  - [New Game Plus](#new-game-plus)
  - [Rocket Gym Ambushes](#rocket-gym-ambushes)
  - [Team Rocket Returns](#team-rocket-returns)

---

# Quality of Life Mods

## Area DexNav

Premi **SELECT** mentre esplori il mondo di gioco per avviare un incontro con un Pokémon non ancora catturato presente nella tabella reale degli incontri dell’area corrente.

---

## Catch Helper

Aggiunge informazioni utili durante gli incontri selvatici:

- mostra in tempo reale la probabilità di cattura;
- utilizza gli stessi PS, alterazioni di stato, catch rate e parametri delle Ball usati dal motore di gioco;
- mostra una piccola Poké Ball accanto al nome dei Pokémon già posseduti nel Pokédex;
- supporta la Zona Safari, compresi gli effetti di Esca e Roccia sul catch rate.

### Esempio

```text
P18 G27 U36
```

| Sigla | Ball |
|---|---|
| `P` | Poké Ball |
| `G` | Mega Ball |
| `U` | Ultra Ball |
| `S` | Safari Ball |

Il numero indica la percentuale di successo della cattura.

---

## DV/EV Editor

Aggiunge la voce **DV/EV** al sottomenu di ogni Pokémon della squadra, consentendo di modificare DV e Stat EXP senza entrare in battaglia.

### Pagina DV

Permette di modificare:

- Attacco;
- Difesa;
- Velocità;
- Speciale.

I valori validi vanno da `0` a `15`.

Il DV dei PS viene ricalcolato automaticamente in base ai quattro DV modificabili, come previsto dalle meccaniche della prima generazione.

### Pagina EV / Stat EXP

Permette di modificare separatamente:

- PS;
- Attacco;
- Difesa;
- Velocità;
- Speciale.

Caratteristiche:

- valori esatti da `0` a `65.535`;
- visualizzazione del contributo EV effettivo da `0` a `63`;
- aggiornamento in tempo reale della statistica finale risultante.

---

## EXP Share Modes

Aggiunge tre modalità selezionabili per la distribuzione dei Punti Esperienza.

| Modalità | Funzionamento |
|---|---|
| **Off** | Ricevono esperienza soltanto i Pokémon ancora in vita che hanno partecipato alla lotta. |
| **Classic Even Split** | Modalità predefinita. Il pool completo viene diviso equamente tra tutti i Pokémon in vita della squadra. |
| **Modern Progressive** | I partecipanti dividono il normale pool del 100%; i Pokémon in vita che non hanno combattuto dividono un secondo pool del 50%. Il totale è circa `1,5×`. |

---

## Guaranteed Catch

Ogni Poké Ball registrata cattura sempre il Pokémon avversario, indipendentemente da:

- PS rimanenti;
- alterazioni di stato;
- specie;
- catch rate.

---

## HM Anywhere

Consente di usare le MN possedute senza doverle insegnare a un Pokémon.

È sufficiente avere la relativa MN nello zaino. Le medaglie richieste restano comunque necessarie.

### Comandi

- **CUT** — premi `A` davanti a un albero o a un cespuglio tagliabile.
- **SURF** — premi `A` davanti all’acqua; premi nuovamente `A` verso la terraferma per scendere.
- **STRENGTH** — premi `A` davanti a un masso per attivare Forza e iniziare a spingerlo.
- **FLASH** — apri il menu Start, seleziona il nuovo menu **HM** e scegli **FLASH**.
- **FLY** — apri il menu Start, seleziona il nuovo menu **HM** e scegli **FLY**.

---

## Modern Bag

Trasforma lo zaino in un inventario moderno diviso in sei tasche, navigabili con **Sinistra** e **Destra**.

Rimuove inoltre il limite originale di 20 tipi di oggetti diversi.

### Tasche disponibili

| Tasca | Contenuto |
|---|---|
| **MEDICINE** | Pozioni, cure di stato, Revitalizzanti, Etere, Elisir, vitamine, PP-Su e Caramelle Rare. |
| **BALLS** | Poké Ball, Mega Ball, Ultra Ball, Master Ball e Ball aggiunte da altre mod. |
| **TM HM** | Tutte le MT e le MN. |
| **BATTLE** | Strumenti X, Mirino, Superguardia e Poké Bambola. |
| **KEY ITEMS** | Bicicletta, Canne da pesca, Poké Flauto, chiavi, tessere e altri strumenti importanti. |
| **OTHER** | Pietre evolutive, Repellenti, Fune di Fuga, fossili e strumenti generici. |

---

## Move Inspector

Mostra direttamente durante la lotta le informazioni tecniche della mossa evidenziata:

- tipo;
- PP;
- potenza;
- precisione;
- efficacia;
- bonus STAB.

---

## Moves Manager

Aggiunge la voce **MOVES** al sottomenu di ogni Pokémon della squadra.

### Pagina principale

Mostra:

- le quattro mosse conosciute;
- i PP attuali e massimi;
- eventuali slot vuoti;
- la possibilità di riordinare le mosse premendo **SELECT**.

### Schede tecniche

Ogni mossa dispone di tre pagine informative con:

- tipo e categoria fisica, speciale o di stato;
- potenza e precisione;
- PP, PP massimi e PP Up;
- priorità;
- probabilità di colpo critico aumentata;
- effetto e tipo di effetto;
- danno fisso;
- numero di colpi;
- compatibilità con Counter;
- turni di caricamento;
- semi-invulnerabilità;
- indice;
- identificatore interno;
- animazione.

### Sostituzione delle mosse

Premendo `A` sulla scheda tecnica puoi scegliere una mossa dalla memoria del Pokémon.

La memoria iniziale viene ricostruita usando:

- le mosse attualmente conosciute;
- le mosse iniziali della linea evolutiva;
- le mosse apprese naturalmente entro il livello attuale.

---

## Trade Evolution Fix

Sostituisce le quattro evoluzioni tramite scambio della prima generazione con evoluzioni per livello.

I Pokémon coinvolti si evolvono al **livello 40**.

---

## Quest System

Aggiunge la voce **QUESTS** al menu Start.

### Diario delle missioni

Il menu contiene due sezioni navigabili con **Sinistra** e **Destra**:

- **ATTIVE** — missioni disponibili, iniziate o fallite;
- **COMPLETATE** — missioni concluse.

Per ogni missione vengono mostrati:

- titolo e stato;
- descrizione;
- obiettivo corrente;
- luogo consigliato;
- avanzamento numerico;
- barra grafica;
- ricompensa;
- mod di provenienza.

---

## Repel Reuse

Quando l’effetto di un Repellente termina, viene mostrata automaticamente una scelta:

- **YES** — consuma e attiva immediatamente un altro Repellente;
- **NO** — continua senza Repellente.

La scelta non viene mostrata quando non sono rimasti Repellenti nello zaino.

### Priorità di selezione

La mod prova prima a utilizzare lo stesso tipo di Repellente appena terminato. Se è esaurito, sceglie automaticamente in questo ordine:

1. **MAX REPEL**
2. **SUPER REPEL**
3. **REPEL**

---

## Reusable Machines

Migliora il funzionamento di MT e MN:

- le MT non vengono più consumate quando insegnano una mossa;
- le mosse MN possono essere dimenticate;
- il nome della mossa associata a ogni MT o MN viene mostrato direttamente nello zaino.

---

## Summon

Aggiunge la voce **SUMMON** al menu Start.

Permette di inserire un numero del Pokédex e iniziare immediatamente un normale incontro selvatico con il Pokémon corrispondente.

### Utilizzo

1. Seleziona **SUMMON**.
2. Inserisci il numero del Pokédex.
3. Controlla il nome del Pokémon mostrato nella finestra.
4. Seleziona **OK**.
5. Inizia l’incontro selvatico.

---

# Quest Mods

## The Three-Stone Covenant

La missione diventa disponibile dopo aver sconfitto **Lt. Surge** e ottenuto la **Medaglia Tuono**.

Uscendo dalla Palestra di Aranciopoli, **Dr. Vela** appare vicino all’ingresso.

### L’avventura

1. **Prova del Fulmine — Aranciopoli**  
   Risolvi un enigma con tre relè elettrici e affronta il **Volt Warden**.

2. **Prova dell’Acqua — Celestopoli**  
   Raggiungi il **Tide Keeper**, bilancia tre valvole e affronta una squadra acquatica.

3. **Prova del Fuoco — Azzurropoli**  
   Stabilizza una fornace a fiamma blu e sconfiggi l’**Ember Keeper**.

4. **Patto finale — Aranciopoli**  
   Riporta i tre nuclei a Dr. Vela, completa l’ultimo enigma e affronta il **Triad Master**.

La squadra del Triad Master comprende:

- Eevee;
- Jolteon;
- Vaporeon;
- Flareon.

### Ricompense

Al termine della missione ricevi:

- Jolteon;
- Vaporeon;
- Flareon;
- **Eevee Emblem**, un oggetto chiave esclusivo.

---

## The Mirage of Mew

Un’avventura disponibile dopo la **Medaglia Terra**, ambientata tra:

- Villa Pokémon;
- Torre Pokémon;
- Foresta Smeraldo;
- Isole Spumarine.

Nel menu Start compare la nuova voce **MEW MYSTERY**, dalla quale puoi controllare:

- obiettivo corrente;
- reperti trovati;
- indizi raccolti.

### Struttura dell’avventura

1. **Laboratorio di Cinnabar**  
   Parla con lo scienziato nella stanza di Metronomo. Il normale regalo di TM35 viene preservato: se non l’hai ancora ricevuta, dovrai parlargli nuovamente per iniziare la quest.

2. **Villa Pokémon B1F**  
   Scopri un laboratorio bruciato collegato al Progetto Mew, affronta il **Mansion Warden** e recupera il **Gene Shard**.

3. **Torre Pokémon 7F**  
   Rispondi a tre domande sul passato e sulla libertà di Mew. Dopo l’enigma affronta il **Dream Keeper** e ottieni lo **Spirit Echo**.

4. **Foresta Smeraldo**  
   Interpreta correttamente una serie di tracce senza disturbare i Pokémon selvatici. Affronta il **Forest Guardian** e recupera il **Life Seed**.

5. **Ritorno a Cinnabar**  
   Lo scienziato unisce i tre reperti e crea l’oggetto chiave esclusivo **Aura Charm**.

6. **Isole Spumarine B4F**  
   L’Aura Charm apre una camera nascosta dalla quale puoi chiamare e affrontare Mew.

### Incontro con Mew

Mew viene affrontato in una vera battaglia selvatica.

Se Mew:

- viene sconfitto;
- fugge;
- oppure il giocatore decide di scappare;

l’**Aura Charm** rimane attivo e l’incontro può essere ripetuto tornando alle Isole Spumarine B4F.

---

## New Game Plus

Aggiunge una modalità **New Game Plus** post-Lega con:

- Allenatori più forti;
- Pokémon selvatici potenziati;
- rematch dei Capipalestra;
- boss opzionali;
- nuove ricompense;
- cicli di difficoltà ripetibili.

Dopo aver sconfitto la Lega e il Campione, nel menu Start compare la voce **NG PLUS**.

### Progressi mantenuti

Restano invariati:

- Pokédex;
- squadra;
- Pokémon nei box;
- livelli;
- mosse;
- DV ed EV;
- inventario;
- oggetti chiave;
- denaro;
- medaglie;
- progresso della storia.

### Allenatori

Dopo l’attivazione:

- tutti gli Allenatori normali ricevono almeno 20 livelli aggiuntivi;
- la loro squadra viene adattata anche al livello più alto del giocatore;
- i loro Pokémon evolvono quando il nuovo livello soddisfa le regole evolutive;
- ogni ciclo successivo aggiunge altri 5 livelli;
- il livello massimo resta 100.

### Pokémon selvatici

Gli incontri naturali:

- ricevono almeno 15 livelli aggiuntivi;
- vengono avvicinati al livello della squadra;
- mantengono specie e probabilità originali della zona;
- ottengono altri 3 livelli per ogni ciclo NG Plus.

### Rematch dei Capipalestra

Ogni Capopalestra può essere affrontato nuovamente.

La prima vittoria di ogni ciclo assegna denaro e ricompense, tra cui:

- Caramelle Rare;
- PP-Su;
- Revitalizzanti Max;
- Elisir Max;
- Ripristino Totale.

### Boss opzionali

Dopo aver sconfitto tutti e otto i Capipalestra si sbloccano progressivamente:

1. **Blue Prime**
2. **Dragon Master**
3. **Red Echo**

La prima vittoria assegna anche una **Master Ball**.

### Cicli infiniti

Dopo aver completato tutti i rematch e sconfitto i tre boss compare la voce **NEXT CYCLE**.

Avviando il ciclo successivo:

- i progressi delle sfide vengono azzerati;
- Allenatori e squadre dei rematch guadagnano altri 5 livelli;
- i Pokémon selvatici guadagnano altri 3 livelli;
- ricevi 50.000 Pokédollari;
- ricevi tre Caramelle Rare;
- il resto del salvataggio rimane intatto.

---

## Rocket Gym Ambushes

Dopo aver sconfitto un Capopalestra e ottenuto la relativa medaglia:

1. esci dalla Palestra;
2. un membro del Team Rocket appare vicino all’ingresso;
3. parlandogli inizia una nuova lotta;
4. dopo la vittoria puoi scegliere e reclutare uno dei Pokémon della sua squadra.

---

## Team Rocket Returns

Una missione post-Giovanni ambientata in più città, con:

- indagini;
- documenti segreti;
- lotte adattate al livello del giocatore;
- un laboratorio nascosto;
- ricompense importanti.

### La storia

Nel ristorante di Azzurropoli, il vecchio giocatore d’azzardo rivela di essere un informatore sotto copertura.

Giovanni è scomparso, ma una nuova cellula del Team Rocket sta ricostruendo l’organizzazione.

L’indagine conduce in tre città:

- **Lavandonia** — una bambina ha trovato una pagina nera vicino alla Torre Pokémon;
- **Zafferanopoli** — una dipendente della Silph possiede un memorandum sulle spedizioni segrete;
- **Aranciopoli** — il registro del porto documenta alcuni carichi notturni diretti ad Azzurropoli.

Ogni indizio è protetto da un nuovo Allenatore Rocket.

I documenti recuperati vengono conservati nello zaino come oggetti chiave.

### Il laboratorio clandestino

Dopo aver riportato i tre documenti all’informatore, ricevi il **BLACK PASS**.

Al piano B4F del Rifugio Rocket, sotto il Game Corner, si apre un passaggio nascosto verso il laboratorio.

Un terminale permette di affrontare progressivamente:

1. **Security A**
2. **Security B**
3. **Dr. Miro**
4. **Commander Nova**

### Ricompense

Dopo aver sconfitto Commander Nova ricevi:

- **Porygon**, al livello 35 o vicino al livello attuale della squadra;
- **Master Ball**;
- **Rocket Core**, un oggetto chiave esclusivo e trofeo della missione.

---

## Download

Scarica tutte le mod dal repository ufficiale:

**[github.com/FAFF0x/gen1recomp](https://github.com/FAFF0x/gen1recomp)**
