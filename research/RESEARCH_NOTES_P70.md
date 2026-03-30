# P70 — Gallows come Diagrammi di Percorso Procedurale

**Sessione**: 90 — 30 marzo 2026
**Stato**: APERTA FORTE
**Rilevanza paper**: Alta — modifica l'interpretazione fondamentale della funzione dei gallows

---

## Ipotesi centrale

Le gallows del Manoscritto Voynich **non codificano classi farmacologiche arbitrarie**. Sono **diagrammi iconici** del percorso che la materia compie attraverso uno spazio di stati fisici a due dimensioni rappresentato dalla rosetta 3×3 (f85r).

Il glifo *è* la sequenza di trasformazioni — il **nome procedurale della ricetta**. Ogni paragrafo botanico dell'Herbal si apre con un gallows come si apre una ricetta con il proprio titolo: non "Preparazione Calmante", ma "Processo-che-passa-per-NE-poi-SW".

---

## Evidenza corpus

| Sezione | Paragrafi aprono con gallows | % |
|---------|------------------------------|---|
| Herbal | 107/112 | **95.5%** |
| Stars2 | verificato | **100%** |
| Balneo | ~16/62 | **25.8%** |

Il Balneo basso si spiega: il Balneo descrive processi di macerazione dove l'ingresso è il materiale vegetale generico, non un tipo di preparazione nominato. Non si apre con il titolo della ricetta perché non è una ricetta — è una procedura operativa standard.

**Distribuzione degli opener nell'Herbal** (corpus Takahashi):
- p = 45.5% (SW/essiccatura — passo intermedio)
- k = 19.6% (NE/decozione)
- t = 18.8% (SE/infusione oleosa)
- cth = 2.7% (multi-corner, processo a caldo in olio)

**Paradosso cth risolto**: cth è l'operazione INTERNA più comune nel body text (22.5% delle gallows totali) ma solo 2.7% degli opener. Questo perché cth non *nomina* il tipo di ricetta — *esegue* l'estrazione oleosa a caldo che è il cuore operativo di molte ricette. Il nome della ricetta (l'opener) è il tipo di preparazione, non l'operazione più frequente al suo interno.

---

## Il doppio quadripolo della rosetta f85r

La rosetta 3×3 di f85r ospita **due quadripoli sovrapposti** sulla stessa griglia.

### Primo quadripolo (già noto)
Solventi ai midpoint degli assi cardinali:
| Punto cardinale | Solvente | Morfema |
|----------------|----------|---------|
| N | Acqua | k |
| S | Olio | t |
| W | Aceto | s |
| E | Alcool | l |

**Nota critica**: questi cardinali sono CONFERMATI da Alessandro. Non invertire. Questa è la Bibbia.

### Secondo quadripolo (sess.90 — nuovo)
Trasformazioni di stato fisico ai corner angolari, ruotato di 45° rispetto al primo.

Ogni corner ha **due letture operative dipendenti dalla direzione del tratto**:

| Corner | Stato fisico | Dir. A | Dir. B |
|--------|-------------|--------|--------|
| NE | caldo + umido | Bollitura (decozione) | Distillazione |
| NW | freddo + umido → solido | Filtratura | Cristallizzazione (ipotesi) |
| SW | freddo + secco | Essiccatura | Reidratazione → pasta (ipotesi: elettuario, NON "sciogli in acqua") |
| SE | caldo + fluido | Scioglimento alcolico / Tintura | Emulsificazione (olio+alcool in dispersione stabile) |

**Assi del secondo quadripolo**:
- G→C (SW→NE): secco ↔ umido
- A→I (NW→SE): solido ↔ non-solido

### Il centro è trasparente
Il nodo centrale della griglia 3×3 rappresenta il **corpo del paziente** — il ricevitore implicito dell'intera preparazione. Non è un passo della preparazione. Non viene mai codificato nel percorso delle gallows. Spiega perché non esiste un morfema "E" (centro) nel sistema.

---

## Encoding direzionale nel glifo

Le gallows non sono simboli — sono *tratti direzionali* che tracciano un percorso sulla griglia:

| Direzione | Trasformazione fisica |
|-----------|----------------------|
| → (destra) | Riscalda |
| ← (sinistra) | Raffredda |
| ↑ (su) | Idrata |
| ↓ (giù) | Essicca / Toglie acqua |

**Curl (ricciolino) intorno a un corner** = attivazione di quella trasformazione di stato
**Angolo retto** = cambio di direzione puro, senza attivazione di trasformazione

### Bench characters nel modello geometrico
- **ch** = tratto verso →/NE (corner vapore, direzione caldo)
- **sh** = tratto verso ←/NW (corner cristallizzazione, direzione freddo)

Non sono solo etichette termiche — sono direzioni precise sulla mappa dello spazio di stati.

---

## Mappatura gallows base → corner

| Gallows | Corner | Processo primario | Posizione nella sequenza |
|---------|--------|-------------------|--------------------------|
| k | NE | Decozione (estrazione acquosa per ebollizione) | Primaria |
| t | SE | Infusione oleosa (caldo+fluido) | Primaria |
| f | NW | Concentrazione/filtrazione fredda | Primaria |
| p | SW | Essiccatura/polverizzazione | **Intermedia** |

### p come passo intermedio — non classe parallela
p apre il 45.5% dei paragrafi Herbal ma appare raramente nel body text delle ricette (8.6% delle gallows totali). La spiegazione è fisicamente coerente: SW = essiccatura/polveri = freddo+secco, che viene *dopo* un'estrazione primaria (k o t). L'essiccatura è un passo successivo alla decozione o all'infusione oleosa, non un tipo di preparazione alternativo.

Il dato 45.5% degli opener si legge così: quasi metà dei fogli botanici dell'Herbal descrivono come operazione centrale della scheda proprio il passo di essiccatura/polverizzazione del materiale già estratto. È farmacologicamente ovvio: molte piante medicinali vengono estratte e poi essiccate per conservarle o combinarle come polveri.

### Compound forms = percorsi multi-corner
| Token | Percorso | Processo |
|-------|----------|----------|
| cth | t(SE=olio) + ch(→NE=vapore) | Estrazione oleosa a caldo |
| ckh | k(NE=vapore) + ch | Decozione rafforzata |
| cph | p(SW=essiccatura) + ch | Polverizzazione con fase calda |

---

## Prossimità solvente-corner (coerenza chimica)

La posizione dei solventi ai cardinali e delle trasformazioni ai corner non è casuale — la prossimità rispetta la chimica:

| Corner | Tra i solventi | Coerenza |
|--------|---------------|----------|
| NE | acqua(N) + alcool(E) | NE = bollitura/distillazione — entrambi i solventi sono volatili, la distillazione separa alcool da acqua |
| NW | acqua(N) + aceto(W) | NW = filtratura/cristallizzazione — precipitazione acetica e filtrazione fredda sono processi acquosi-acidi |
| SW | aceto(W) + olio(S) | SW = essiccatura — aceto e olio non evaporano facilmente a freddo, l'essiccatura rimuove il residuo acquoso |
| SE | olio(S) + alcool(E) | SE = tintura/emulsificazione — le resine oleose si sciolgono in alcool (tintura), e olio+alcool formano emulsioni |

---

## Implicazioni per il paper

### Sezione proposta: "La grammatica dello spazio fisico"

P70 fornisce il collegamento mancante tra la morfologia testuale e l'iconografia della rosetta. Il paper può ora argomentare che il sistema ha **tre livelli di codifica integrati**:

1. **Livello testuale**: morfemi che descrivono operazioni (solventi, verbi, quantificatori)
2. **Livello iconico-procedurale**: gallows che nominano la ricetta come percorso nello spazio di stati
3. **Livello posizionale**: rosetta come mappa di riferimento condivisa tra le operatrici

La cifratura distribuita non è solo testuale — coinvolge anche la capacità di leggere i glifi come diagrammi di percorso sulla rosetta. Chi non conosce la rosetta non può decodificare il nome della ricetta, anche se capisce la morfologia del testo.

### Nota sulla farmacia medievale professionale

Il sistema iconico-procedurale è coerente con la pratica farmaceutica medievale attestata: le ricette nei codici medici arabi e latini usano termini tecnici precisi per i processi (decozione, macerazione, infusione) che corrispondono esattamente alle trasformazioni di stato codificate dal secondo quadripolo. Non è folk medicine con simboli magici — è farmacia professionale con una notazione grafica proprietaria.

---

## Test di falsificazione

1. **Test ductus**: analisi IIIF dei tratti costitutivi delle gallows — se l'ipotesi è corretta, il ductus (direzione e sequenza dei tratti) delle gallows k/t/f/p dovrebbe essere mappabile sui corner NE/SE/NW/SW della rosetta. Le compound forms (cth, ckh, cph) dovrebbero mostrare tratti che "combinano" due corner.

2. **Test distribuzione sezionale**: la densità di gallows come opener dovrebbe essere massima nelle sezioni che descrivono preparazioni complete (Herbal, Stars) e minima nelle sezioni procedurali generiche (Balneo). Confermato parzialmente: 95.5% vs 25.8%.

3. **Test compound forms**: se cth = t+ch = SE+NE, le compound forms dovrebbero apparire più frequentemente in ricette che descrivono processi in due fasi (olio prima, caldo poi). Verificabile su IIIF allineando testo e iconografia.

4. **Test Petersen chart**: il Petersen ductus chart mostra i tratti costitutivi di ogni gallows. Allineare la mappatura corner-per-corner con il ductus effettivo — questa è la verifica principale non ancora completata.

---

## Errori da non ripetere in fase di scrittura

- NON descrivere le gallows come "simboli arbitrari associati a classi farmacologiche"
- NON trattare p come una quarta classe parallela a k/t/f — è un passo intermedio
- NON leggere i corner angolari come "convergenze di solventi" — sono punti di cambio stato
- NON confondere la funzione definitoria dei gallows (opener = nome della ricetta) con la funzione referenziale (gallows nel body text = shorthand operativo)
- Il centro E della rosetta NON è un'operazione — è il corpo del paziente, trasparente

---

## Riferimenti

- Sessione: `voynich-memory/sessions/notes/2026-03-30-sess90-gallows-doppio-quadripolo.md`
- Rosetta f85r: Yale IIIF `https://collections.library.yale.edu/manifests/2002046`
- Petersen ductus chart: `https://voynichportal.com/wp-content/uploads/2017/06/VMSAscenderChart092.pdf`
- Dosaggi f85r: `ROSETTA_DOSAGGI.md` (locale)
- SKILL v7.9: `voynich-memory/skills/SKILL_v7.9.md`
