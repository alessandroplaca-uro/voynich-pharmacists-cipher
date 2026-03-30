# The Pharmacists' Cipher
## Grammar, Dictionary, and Production Calendar of MS 408

*Working draft — vt1.6 — session 81-86 — 29 March 2026*
*Alessandro Placa (Uroboro.io)*

---

> **Posizionamento**: questo paper è il terzo documento di una trilogia. Non riscrive i due precedenti — li cita, li presuppone, e costruisce su di essi. Il contributo originale di questo paper è triplice: (1) il sistema verbale completo di MS 408 (Sezione 1); (2) il dizionario morfematico consolidato con correzioni esplicite (Sezione 2); (3) la decodifica del sistema iconografico-calendariale della sezione zodiacale con 40+ ipotesi testabili (Sezione 3).
>
> **Nota per il lettore senza accesso ai paper precedenti**: la Sezione 2 è *self-contained*. Ogni morfema è presentato con lo stato attuale, la frequenza corpus e — dove applicabile — la ragione esplicita della revisione rispetto a interpretazioni precedenti. È possibile leggere §2 come dizionario autonomo senza aver letto Paper 1 o il Companion.

---

## Riferimenti ai paper precedenti

**Paper 1** — Placa, A. (2026). *The Pharmacist's Cipher: Six Statistical Tests Supporting a Pharmaceutical Reading of the Voynich Manuscript (MS 408)*. Preprint v1.2. https://doi.org/10.5281/zenodo.19197846

Dimostra con 6 test corpus-based che la struttura morfologica di MS 408 è incompatibile con il testo casuale e coerente con un registro farmaceutico professionale. Corpus: ~37.000 token Takahashi (IVTFF). Risultati chiave:
- R1: Stabilità cross-trascrittore (deriva C/H < 3% su tutti gli 11 prefissi)
- R2: Gap morfologico binario (sedy=0, shedy=424 — s- e sh- sono morfemi distinti)
- R3: Riuso cross-sezionale asimmetrico (Pharma→Stars=26, Stars→Pharma=0; p=0.0002)
- R4: Vincolo posizionale (COMPL in posizione finale nel 68.2% delle righe, Z=26.6)
- R5: Profili morfologici sezionali (l- arricchito 1.97× in Stars; ot- arricchito 2.43× in Zodiac)
- R6: Gerarchia dei volumi ee-frequency (Spearman ρ=0.900, p=0.042)

**Paper 2 (Companion)** — Placa, A. (2026b). *The Pharmacist's Cipher II — A Morphological Framework, Visual-Textual Convergences, and Testable Predictions for MS 408*. Preprint v1.0. https://doi.org/10.5281/zenodo.19228231

Presenta il framework morfologico completo: grammatica agglutinante, quartetto solventi (ok-/t-/l-/s-), class markers terapeutici, bench characters (ch-/sh-), sequenza sintattica solventi, identità visiva delle 4 operatrici (f86v4), sistema di dosaggi (f85r), 17 identificazioni botaniche con protocollo sealed-envelope, 26 ipotesi falsificate, 39 predizioni testabili in 3 livelli di confidenza.

---

# SEZIONE 1 — NOVITÀ POST-COMPANION

*Questa sezione presenta solo le scoperte sviluppate dopo la pubblicazione del Companion (26 marzo 2026). Per il framework morfologico di base, vedere Paper 2.*

---

## Errata e revisioni rispetto ai paper precedenti

Le seguenti interpretazioni — presentate come ipotesi di lavoro in Placa (2026a) o Placa (2026b) — sono state falsificate o sostanzialmente superate nelle sessioni 76–86. Il riepilogo completo con motivazioni è in §2.16; le voci contrassegnate con ❌ sono chiuse; quelle con ⚠️ sono revisioni che producono un modello sostitutivo.

| # | Interpretazione precedente | Fonte | Stato | Dettaglio |
|---|---------------------------|-------|-------|-----------|
| 1 | **d = verbo contestuale** (Herbal="prendi", Balneo="immergi", Stars="lavora") | Companion | ❌ FALSIFICATO (sess.84) | d è SEMPRE NOMINALE — puntatore anaforico al materiale corrente. §2.1, §1.6.2 |
| 2 | **ar = direttivo "a/per" / or = congiunzione "e/con"** (quadripolo connettivale) | Companion | ⚠️ SUPERSEDED — P66 (sess.85) | ar = il pressato (via meccanica); or = il filtrato (via liquida); r = stato finale. §2.2, §1.6.3 |
| 3 | **qo = unità lessicale autonoma** (possibile coalescenza con significato "misura/dose") | Companion | ❌ FALSIFICATO (sess.83/85) | qo è sempre q+o (dispersivo+locativo). qok/qot/qol = q+o+[solvente]. §2.5, §1.6.1 |
| 4 | **Glosse qok/qot/qol originali** ("friggi", "bolli in acqua", "raffreddare in olio", "una misura di") | Companion | ⚠️ RISCRITTE — P52 (sess.78) | Il verbo base è q ("diluisci/dispersi"); la temperatura è modificatore secondario. §2.5 |
| 5 | **Balneo = guida a bagni terapeutici / somministrazione** | Companion | ⚠️ SUPERSEDED — P61 (sess.81) | Balneo = guida alla macerazione. Le donnine nelle vasche sono materiale vegetale in immersione, non pazienti. §1.3 |
| 6 | **Zodiaco = 365 ricette Stars indipendenti** | Companion | ⚠️ SUPERSEDED — P62 (sess.81) | Le ~365 operazioni sono fasi di un sottoinsieme di ricette composte — il Zodiaco è una lookup table temporale a fasi multiple. §1.4 |
| 7 | **4 chiavi simmetriche** (fornitore come quarta partner con chiave propria) | Companion | ⚠️ SUPERSEDED — P64 (sess.82) | 3 chiavi private + 1 ruolo fornitore aperto senza chiave. L'Herbal era dizionario iconografico interno, non chiave del fornitore. §1.5 |
| 8 | **s- correlato con F-ABORT** (aceto come solvente degli abortivi) | Companion (implicito) | ❌ FALSIFICATO (sess.86) | s-% per gallows class: p=2.95%, k=3.26%, t=3.55%, f=2.76% — F-ABORT ha il minimo. Sistema gallows×solvente è ortogonale. §2.4, §1.6.5 |
| 9 | **Sequenza sintattica solventi ok→t→l** (modello sess.6e) | Paper 1 / Companion | ⚠️ CORRETTA — P42 | Sequenza corretta: t(0.291)→s(0.401)→ok(0.522)→l(0.651). Olio prima, spirito ultimo. §2.4 |
| 10 | **Sistema verbale come quadruplo di morfemi equivalenti** (y/q/d equiparabili) | Companion | ⚠️ SUPERSEDED — P50/P51/P52/P67 (sess.76–85) | Sistema asimmetrico: y-iniziale (estrattivo) ≠ y-finale (causativo); d = NOMINALE; q = dispersivo opposto di y. §2.1, §1.1, §1.6.4 |

*Per tutti gli altri errata minori (s-=rosa, s-=secco, -am=marham, cheor=artemisia, pol=oppio, ornate=calligrafia) vedere §2.16.*

---

## 1.1 Il sistema verbale completo — Una lingua senza verbi d'azione diretti (P50–P52, P67, sessioni 76–78)

Il Companion descrive il quadripolo solventi e i class markers terapeutici. Mancava una teoria coerente del sistema verbale. Le sessioni 76–78 hanno risolto questo punto.

Nella lettura proposta, il sistema verbale di MS 408 è strutturato attorno a quattro morfemi con distribuzioni posizionali distinte e statisticamente verificabili:

| Morfema | Posizione media | Lettura operativa proposta | Evidenza distribuzionale |
|---------|----------------|---------------------------|--------------------------|
| y-iniziale | 0.349 | "estrai" — apre la riga, precede oggetti nominali | precede daiin×21, aiin×20, chor×16 |
| q- | 0.474 | "diluisci/dispersi" — mai a fine parola | 0/37.067 token in posizione finale |
| d- / -d- | bimodale (~0.0 e ~0.7) | nominale — puntatore anaforico (non verbale) | OR=3.64 senza y-finale; distribuzione bimodale |
| y-finale | 0.513 | causativo — chiude il token in istruzione | 14.176 occ; q...q=0, y...q=0 |

**y-iniziale ≠ y-finale**: Mann-Whitney p < 10⁻³⁰. Due omografi con funzioni opposte — il morfema estrattivo apre la riga, il causativo la chiude.

**q- come opposto simmetrico di y-**: pos. media q- (0.474) > y- (0.347), Mann-Whitney p=4.3e-33. Distribuzione sezionale speculare: HERBAL y arricchito (OR=2.87, p≈0) / BALNEO q dominante (q/y=6.42, p≈0). Ordine y→q nel 63.1% delle righe con entrambi: estrai-poi-diluisci. Strutture circum-fisse: q...y=2.571 occ (diluizione completata), y...y=721 occ (estrazione completata). q...q=0, y...q=0 — solo y chiude, mai q.

**Il confine nome/verbo è marcato morfologicamente** (Fisher p < 10⁻¹⁹): token senza y-finale = sostantivi (daiin, aiin, ol, chor); token con y-finale = processi (chedy, qokeey, shedy).

**Implicazione per la struttura di riga**: [sostantivo/anaforico] — [verbi con y] — [sostantivo prodotto]. La lingua di MS 408 è VERBO-OGGETTO senza soggetto esplicito; il soggetto è l'operatrice agente (implicito, identificata dall'acconciatura nel Zodiaco — vedi §2, Blocco C).

## 1.2 L'o-segnaposto posizionale (P53, sessione 79)

Il Companion identifica le 4 acconciature delle donnine zodiacali come marcatori delle 4 operatrici del quadripolo. Mancava la spiegazione del fenomeno "o-iniziale ubiquo" nelle label zodiacali e nei rosoni COSMO.

**Ipotesi P53 (APERTA FORTE)**: la lettera "o" iniziale nei token zodiacali (odaiin, okain, olain) e nei rosoni di f85r non è sempre la preposizione locativa "in" — in specifici contesti è un *segnaposto* per un fonema implicito, fornito da un elemento visivo esterno al testo.

- In f85r: la posizione nel rosone (Nord/Sud/Est/Ovest) → fonema iniziale implicito
- In Zodiaco: l'acconciatura della donnina adiacente → fonema iniziale implicito

**Parte già testata (corpus)**: COSMO o%=27.6% vs HERBAL 16.6% (Fisher p=6.9e-08). "o" scalza "c" come lettera più frequente in COSMO (HERBAL: c=24.8% > o=16.9%; COSMO: o=27.6% > c=11%). Cross-validazione con P48: il gradiente stagionale ot% si vede sia nel corpus complessivo (ρ=-0.83, p=0.0008) sia nella sottoclasse o-iniziali zodiacali (ρ=-0.709, p=0.0067) — due segnali indipendenti della stessa struttura.

P53 costituisce un **terzo livello di cifratura distribuita**: posizionale (rosone/acconciatura) → fonema iniziale. Si aggiunge ai due descritti nel Companion (interno: gallows×solvente V=0.513; esterno: termico×suffisso V=0.12–0.20).

**Parte in attesa di verifica IIIF** (predizioni falsificabili, non ancora testate):
- IIIF f85r: rosoni diversi della griglia 3×3 dovrebbero mostrare distribuzioni ot*/ok* diverse, coerenti con il solvente del rosone
- IIIF Zodiac: folii con donnine "olio" in mesi invernali (f70v2: ot%=69.4%) dovrebbero avere concentrazione di ot* nelle label adiacenti
- Predizione precisa: f72v2–f72v3 (ot%=31–37%) → acconciatura dominante "acqua" o "spirito"

## 1.3 Il Balneo come guida alla macerazione (P61, sessione 81)

**Ipotesi P61 (APERTA FORTE)**: la sezione Balneologica di MS 408 NON descrive bagni terapeutici né la somministrazione di preparati — descrive la MACERAZIONE. Le donnine nelle vasche non sono pazienti: sono la rappresentazione visiva del materiale vegetale immerso nel solvente a temperatura controllata.

**Evidenza corpus**:

| Indicatore | Valore Balneo | Confronto |
|-----------|--------------|-----------|
| sh% (processi freddi/controllati) | **14.7%** | Herbal 11.0%, Stars 10.1% — massimo tra tutte le sezioni |
| Ratio sh/ch | **0.73** | Herbal 0.36, Stars 0.36 — Balneo è l'unica sezione con quasi-parità freddo/caldo |
| q/y ratio | **6.42** | massimo tra tutte le sezioni (Fisher OR=0.113, p≈0) |

Il dominio della dispersione (q) sulla concentrazione (y) è coerente con la macerazione: il materiale viene *disperso* nel solvente, non estratto da esso. La prevalenza di sh- (freddo/controllato) è coerente con la macerazione di principi attivi termolabili, che non reggono all'ebollizione.

**Coerenza strutturale**: la macerazione è esattamente il secondo livello del sistema produttivo a 5 livelli (vedi §1.4): il materiale grezzo identificato nell'Herbal viene macerato nel Balneo prima di essere combinato in Pharma.

**La somministrazione era dominio clinico**: la prescrizione medica al paziente era una funzione del medico, non della farmacista. Un libro cifrato professionale non avrebbe motivo di descrivere la somministrazione — avrebbe motivo di documentare il processo produttivo.

*Falsificato SE*: la distribuzione sh/ch nel Balneo rispecchia quella dell'Herbal su trascrizioni alternative (Currier, inter-linea); oppure le vasche mostrano iconografia incompatibile con contenitori industriali su analisi IIIF sistematica.

---

## 1.4 La struttura gerarchica del manoscritto (ipotesi sistemica, sessione 81)

Il lavoro delle sessioni 74–81 converge verso un'interpretazione del manoscritto come **sistema produttivo farmaceutico a 5 livelli funzionali più un meta-documento**. Questa è l'ipotesi di più alto livello dell'intera trilogia — la più potente se confermata, la più esposta se falsificata.

| Livello | Sezione | Funzione | Indicatore linguistico principale |
|---------|---------|----------|----------------------------------|
| 1 | **Herbal** | Materie prime: profilo della pianta + protocollo di estrazione degli attivi | ch dominante (decozioni, operazioni a caldo) |
| 2 | **Balneo** | Macerazione: solvente, temperatura, durata | sh dominante (processi freddi/controllati); q/y massimo |
| 3 | **Pharma** | Semilavorati combinati: preparazioni intermedie con estratti Herbal + macerati Balneo | bilanciamento ch/sh; -am (completamento) |
| 4 | **Stars** | Preparazioni finali ("specialità della casa"): ricette composte che usano i semilavorati di Pharma come ingredienti | l- arricchito (1.97×); -ory; ol+or massimo |
| 5 | **Zodiaco** | Piano di produzione annuale: calendario con puntatori a Stars (lookup table a fasi multiple, P62) | ok- morfema zodiacale per eccellenza; 0 imperativi y-iniziale nelle label |
| META | **Cosmo** (f85r + f86v4) | Meta-documento: sistema di riferimento, 4 operatrici, dosaggi, dashboard operativo | o% massimo (27.6%); y segnaposto posizionale |

**Predizione testabile (nuovo test)**: la densità di gallows (class markers del principio attivo: k/t/f/p) dovrebbe essere massima in Herbal e Stars, minima nel Balneo. La macerazione è un processo generico, non class-specific — non dipende dal tipo di principio attivo. La preparazione finale (Stars) invece deve sapere la classe terapeutica per dosarla correttamente.

**Implicazione cross-sezionale**: un singolo ingrediente vegetale compie un percorso documentato: Herbal (profilo) → Balneo (macerazione) → Pharma (semilavorato) → Stars (ricetta finale) → Zodiaco (quando produrlo). Se questo percorso è tracciabile per almeno 5 delle 17 piante identificate, il sistema integrato è confermato (H-I03, §3).

---

## 1.5 Il meta-documento f86v4 e il sistema dei ruoli (P63–P65, sessione 82)

**P63 — Struttura della cifratura distribuita: implicazioni (APERTA FORTE)**

La cifratura a tre livelli (gallows×solvente / termico×suffisso / posizionale) ha una proprietà strutturale rilevante: nessun sottoinsieme delle parti è sufficiente per la lettura completa del testo. Un lettore che conosca solo la corrispondenza gallows×principio attivo non può risolvere i parametri termici; chi conosce solo i bench characters non può identificare la classe terapeutica. La distribuzione è modulare, non ridondante. La conseguenza è che la trasmissione completa del sistema richiede la trasmissione di tutte e tre le componenti. Qualsiasi ipotesi sulla storia sociale di questo sistema — chi lo usava, come veniva trasmesso, perché è cifrato — appartiene al programma di ricerca storiografico (M-01), non alle conclusioni della corpus analysis.

**P64 — Le quattro figure di f86v4: domini funzionali e struttura del sistema (APERTA FORTE)**

Il sistema morfologico ha quattro assi ortogonali: quattro solventi (ok/t/l/s), quattro class markers gallows (p/k/t/f), quattro sezioni principali (Herbal/Balneo/Pharma/Stars). Il folio f86v4 presenta quattro figure umane disposte ai punti cardinali. Una lettura coerente con la struttura del sistema è che queste figure rappresentino i quattro domini operativi che il manoscritto presuppone: botanico (identificazione e fornitura della materia prima), fisico (estrazione e trattamento), chimico (combinazione dei semilavorati), medico (dosaggio e prescrizione).

La figura Nord — l'unica di spalle, l'unica che non presenta attributi frontalmente riconoscibili — mostra un'asimmetria iconografica sistematica rispetto alle altre tre. Nella lettura proposta questo corrisponde al dominio botanico: il ruolo di fornitura della materia prima è strutturalmente aperto (i fornitori sono intercambiabili), a differenza dei tre domini con competenza tecnica diretta sul sistema scritto. Le altre tre figure frontali rappresenterebbero i ruoli che detengono le componenti del sistema di cifratura.

*Test iconografico*: le tre figure frontali presentano attributi sistematicamente differenziati e coerenti con i rispettivi domini? La figura Nord è iconograficamente distinta dalle altre tre in modo sistematico? Verifica richiede analisi IIIF ad alta risoluzione.

**P65 — Chi erano gli operatori? (direzione di ricerca)**

Il modello fin qui è agnostico sull'identità degli operatori. La morfologia e l'iconografia non impongono per sé un genere: le figure di f86v4 possono essere lette come allegorie funzionali, come rappresentazioni di ruoli, o come ritratti di persone reali. Tutte e tre le letture sono compatibili con il sistema morfologico.

Una domanda più precisa è: esistevano, nell'area geografica e nella finestra temporale compatibili con la datazione al radiocarbonio (1404–1438, Beinecke), operatori con il profilo di competenza che il sistema presuppone — specializzati, organizzati, con accesso a reti di fornitura e clientela di alto livello?

Questo è un argomento di plausibilità storica, non di identificazione. Il salto logico da "operatrici di questo tipo esistevano" a "queste sono le autrici del manoscritto" non è supportato da questo paper.

La risposta archivistica è affermativa. Gli Archivi di Stato di Genova documentano, nell'area del Golfo del Tigullio e nell'arco 1410–1438, almeno due casi di professionisti della cura riconosciuti formalmente dalle istituzioni della Repubblica: con esenzioni fiscali concesse per meriti terapeutici, salvacondotti rilasciati dal doge, clientela ai più alti livelli del patriziato. La fonte primaria è Ferretto (1901), *Giornale Storico e Letterario della Liguria*, pp. 277–296, verificata sul testo originale. Questi casi documentati sono, specificamente, di donne.

Non è possibile escludere — e una lettura attenta di questi documenti rende la direzione non arbitraria — che gli operatori del sistema fossero donne. La coincidenza di area, finestra temporale, livello di specializzazione e autonomia professionale con il profilo che il modello presuppone è significativa. Il paper non avanza oltre questo punto: l'identificazione degli operatori specifici è un problema storiografico aperto (M-01), che richiede ricerca archivistica indipendente.

*Questo è il punto di caduta che questo paper intende stabilire: il modello farmaceutico-professionale è storicamente plausibile. Chi fossero gli operatori appartiene a una fase successiva della ricerca.*

---

## 1.6 Scoperte post-companion: sessioni 83–86

### 1.6.1 qo come morfema autonomo: FALSIFICATO (sess.83/85)

La struttura "qo" (che in versioni precedenti era stata trattata come possibile coalescenza con significato "misura/dose") non esiste come unità lessicale autonoma. La verifica corpus dimostra che qo è sempre q+o (dispersivo + locativo). Le strutture qok/qot/qol si leggono q+o+[solvente] = "diluisci in acqua/olio/spirito". La glossa precedente ("una misura di") era sbagliata: il verbo base è q ("diluisci"), la temperatura (ch/sh) è il modificatore secondario. L'unica coalescenza confermata che produce un token lessicalizzato rimane daiin (d+aiin).

### 1.6.2 d = NOMINALE: risoluzione definitiva (sess.84)

La questione aperta dalla sessione 45 in poi — d come verbo contestuale o puntatore nominale — è risolta definitivamente in sess.84 con evidenza empirica. **d è SEMPRE NOMINALE.** Evidenza: distribuzione bimodale (pos~0.0: 26.9% = d-prefix; pos~0.7: 26.0% = -d- in -dy); OR=3.64 (d-iniziali senza y-finale = 84% vs 59% corpus, p<0.001). Tutti i token d-iniziali tendono a NON avere y-finale = sono sostantivi, non comandi.

**Parsing aggiornato (sess.87–88)**: `dy` = VERBO ATOMICO "produci" (inseparabile — non scomporre in d+y). `chy`="scalda", `shy`="raffredda" sono ugualmente atomici. Verbi composti e+y: `ey`="mescola", `eey`="mescola bene", `eeey`="agita". Gerarchia verbale per intensità: dy=produci | ey=mescola | eey=mescola bene | eeey=agita | ody=incorpora.

Conseguenza per dchedy: `dchedy` = d(la preparazione) + ch(caldo) + ey(mescola) = "**mescola la preparazione a caldo**". La vecchia parsing "d+ch+e+dy" era sbagliata: e non è un quantificatore q.b. qui, è parte del verbo composto ey=mescola.

### 1.6.3 P66 — ar/or come stati di purificazione (APERTA FORTE, sess.85)

Il morfema **r** è un marcatore di STATO FINALE (purezza/essenza) condiviso tra ar e or. **ar** = a(su/sopra)+r(puro) = il pressato (prodotto della via meccanica); **or** = o(in/dentro)+r(puro) = il filtrato (prodotto della via liquida). Con y-causativo: ary = "causa pressing!"; ory = "causa filtering!". Evidenza posizionale: ar/or appaiono DOPO y-finale nella riga (66%/49%) = sono prodotti, non verbi. Tripletta posizionale confermata: chor(pos 0.339) / ychor(pos 0.000, sempre primo token) / chory(pos 0.541). Pattern generalizza su 105+46 token.

### 1.6.4 P67 — Sistema verbale completo: nessun verbo d'azione autonomo (APERTA FORTE, sess.85)

La lingua di MS 408 NON ha verbi d'azione autonomi per operazioni fisiche. Ha STATI causati da y. "Scalda" non esiste — esiste "causa che sia caldo" (chedy). La costruzione universale è: y + [stato fisico/termico] = azione causata. I bench characters ch/sh sono il contesto più frequente prima di y-finale (n=2227 occorrenze). Parallelo strutturale: ligure *fa' scaldare* e arabo forma II causativa. Implicazione: ogni "verbo" nel corpus è in realtà la causazione di uno stato — non un'azione diretta. Questo rafforza la grammatica agglutinante e spiega la produttività dei morfemi combinatoriali.

### 1.6.5 s- come solvente generalista: nota metodologica (sess.86)

Test corpus diretto (sess.86): s-% per gallows class risulta p=2.95%, k=3.26%, t=3.55%, f=2.76%. F-ABORT ha la percentuale acetica più BASSA di tutte le classi. Ratio s- in folii f vs P/K/T = 0.09x. L'aceto era un solvente generalista medievale per qualsiasi tipo di estrazione — non un marcatore di abortività. Il sistema 4×4 (gallows × solvente) è empiricamente ortogonale: la classe terapeutica è indipendente dal solvente. Implicazione per plant-id: le identificazioni F-ABORT si basano su gallows f + iconografia, mai su profilo acetico. Questo esito rafforzale tesi della produzione farmaceutica a 360°.

---

## 1.7 Scoperte post-companion: sessione 88 — Sistema ciclico y-iniziale e causativo telico

### 1.7.1 P68 — y-iniziale con e* post-solvente = cicli di estrazione (APERTA FORTE, sess.88)

I token con y-iniziale seguiti da solvente e poi da e* rivelano un sistema di conteggio cicli d'estrazione. Test corpus su 36.183 token Takahashi:

**Distribuzione solventi post-y-iniziale**: yk*=564 (35%), yt*=473 (30%), ych*=229 (14%), ysh*=86 (5%), ys* puro=11 (0.7%), yl*=17 (1.1%). La predizione farmacologica è **confermata**: non esistono estrazioni primarie con aceto (s) né alcool (l) — i pochi token residui sono probabilmente artefatti di trascrizione. L'estrazione usa acqua e olio come solventi primari; i bench termici ch/sh (229+86 token) codificano la temperatura del processo estrattivo.

**e* sempre post-solvente**: su 412 token con pattern y+solvente+e*+verbo-finale, solo 4 mostrano e* pre-solvente (< 1%). La struttura è fissa: y(apre) + solvente + e*(cicli) + verbo(chiude).

**Gradiente**: e=173, ee=219, eee=19. La forma doppia (ee) è la più frequente — parallelo con aiin come standard del doppio passaggio estrattivo medievale (mathbūkh arabo). Il doppio ciclo è la norma, non l'eccezione.

**Nominali paralleli confermati**: i token ykee+X senza y-finale esistono (47 token): ykeeol=11, ykeeo=7, ykees=4, ykeeor=3, ykeear=2. Stessa struttura radice del comando (ykeey, ykeedy) con suffisso prodotto invece di y-finale. Coppia simmetrica: comando y+k+ee+y(FAI) / nominale y+k+ee+ol (lo spirito della doppia estrazione acquosa). Struttura identica alla coppia aiin/daiin — il prodotto nominale del processo verbale.

*Falsificato SE*: e* mostra distribuzione pre-solvente in trascrizioni alternative (Currier/Zandbergen); oppure yk*/yt* non differiscono da ys*/yl* in studi corpus indipendenti.

### 1.7.2 y-finale come causativo telico (raffinamento P51)

Il morfema y-finale non è solo "causativo universale FAI" — è specificamente un **causativo telico**: non "esegui un'azione" (atelic, imperativo semplice) ma "porta a compimento l'operazione" (telic, causativo di completamento). La distinzione è rilevante per la struttura del circumfix y...y: y-iniziale apre il frame dell'estrazione, y-finale lo chiude come telic. La struttura d'insieme è: y(apri-estrazione) + solvente + e*(cicli) + y(porta-a-compimento). Parallelo: arabo Forma II come causativa telic; ligure *fa' scaldare* come causativo di completamento. Un operatore originale non "estrae" — "fa sì che l'estrazione si compia".

---

# SEZIONE 2 — DIZIONARIO MORFEMATICO CONSOLIDATO

*Stato dell'arte al 29/03/2026 — sessione 86*

Questa sezione raccoglie tutti i morfemi interpretati fino ad oggi, con lo stato epistemico attuale, la frequenza corpus, e — dove rilevante — una nota di correzione rispetto a interpretazioni precedenti superate. I morfemi marcati `[Placa 2026b]` sono stati presentati nel Companion; quelli marcati `[NUOVO]` sono stati identificati nelle sessioni 76–80, dopo la pubblicazione del Companion.

**Avvertenza metodologica**: la morfologia di MS 408 è *domain-compatible* (coerente con la lettura farmaceutica), non *domain-specific* (esclusiva di essa). La convergenza di morfologia + iconografia + distribuzione sezionale + identificazioni botaniche (Bax) è il fondamento del modello — nessun morfema preso isolatamente è conclusivo.

**Convenzione confidenza**: 🟢 SOLIDA (testata, non falsificata) | 🟡 APERTA FORTE (evidenza preliminare convincente, test non eseguito) | 🔵 STRUTTURA SOLIDA / LETTURA APERTA (struttura misurabile, semantica ipotetica) | 🔴 OPACA (dato strutturale presente, semantica ignota) | ❌ FALSIFICATA

---

## 2.1 Operatori grammaticali

Il sistema verbale di MS 408 è composto da quattro morfemi distinti che operano in posizioni diverse nella riga. I morfemi y-iniziale e y-finale sono omografi con funzioni opposte — la distinzione posizionale è supportata da Mann-Whitney p < 10⁻³⁰.

| Morfema | Posizione media | Funzione | Freq. | Stato | Fonte |
|---------|----------------|----------|-------|-------|-------|
| **y-** (iniziale) | 0.349 | Verbo estrattivo "estrai" — apre la riga, precede oggetti diretti (daiin×21, aiin×20, chor×16) | 919 occ (tipi A) | 🟡 APERTA FORTE | [NUOVO — P51] |
| **y-** (finale) | 0.513 | Causativo universale "fai (fare)" — chiude qualsiasi token in istruzione esecutiva; token senza y-finale = sostantivi | 14.176 occ | 🟡 APERTA FORTE | [NUOVO — P51] |
| **q-** | 0.474 | Dispersivo "diluisci/dispersi" — opposto simmetrico di y-iniziale; mai a fine parola (0/37.067 token); BALNEO q/y=6.42, HERBAL q/y=0.35 | ~6.800 occ | 🟡 APERTA FORTE | [NUOVO — P52] |
| **d-** / **-d-** | bimodale (pos~0.0 e ~0.7) | **NOMINALE — puntatore anaforico al materiale corrente.** MAI un verbo. d-prefix = "la preparazione" (gloss confermata sess.87); -d- in -dy = parte del verbo atomico dy="produci" (inseparabile). Distribuzione bimodale: pos~0.0 (26.9%) = d-prefix; pos~0.7 (26.0%) = -d- in -dy. OR=3.64 (d-iniziali senza y-finale = 84% vs 59% corpus, p<0.001). | variabile | 🟡 APERTA FORTE | [NUOVO — P50, RISOLTO sess.84/87] |

> ✗ **CORREZIONE (sess.84/87 — DEFINITIVA)** — *d NON è un verbo contestuale.* d è SEMPRE NOMINALE: puntatore anaforico al materiale corrente. La glossa corretta è "la preparazione" (NON "questa sostanza" né "prendi/immergi"). Strutture con d: (A) d-prefix = "la preparazione" (puntatore, pos~0.0); (B) dy = VERBO ATOMICO "produci" (inseparabile — NON d+y). Verbi atomici: dy="produci", chy="scalda", shy="raffredda". Verbi composti e+y: ey="mescola", eey="mescola bene", eeey="agita". `dchedy` = d(la preparazione) + ch(caldo) + ey(mescola) = "mescola la preparazione a caldo" (NON d+ch+e+dy). La q-dominanza nel Balneo (6.42) si spiega: d(la preparazione) → q(la disperde nel solvente). Evidenza: HERBAL_A -dy/-d-init=0.2 (nominali); BALNEO -dy/-d-init=3.6 (comandi con verbo atomico dy).

**Struttura circum-fissa confermata**: q...y = 2.571 occ (diluizione completata); y...y = 721 occ (estrazione completata). q...q = 0; y...q = 0: solo y chiude, mai q.

**Struttura di riga**: [sostantivo/anaforico] — [verbi con y] — [sostantivo prodotto]. Lingua VERBO-OGGETTO senza soggetto esplicito.

---

## 2.2 Quadripolo grammaticale

Il quadripolo ol/or/al/ar è un sistema di quattro connettivi con funzioni grammaticali distinte. La distinzione -l (strutturale) vs -r (relazionale) e o- (aperto) vs a- (chiuso) è stata confermata da distribuzione posizionale, sezionale, e dai bigrammi [Placa 2026b].

| Morfema | Funzione | Freq. | Stato |
|---------|----------|-------|-------|
| **ol** | Genitivo "di" | 610 | 🟢 SOLIDA [Placa 2026b] |
| **or** | "il filtrato" — o(in)+r(puro) = prodotto della via liquida verso purezza | 380 | 🟡 REVISIONE P66 [NUOVO sess.85] |
| **al** | Articolo/specificatore | 288 | 🟢 SOLIDA [Placa 2026b] |
| **ar** | "il pressato" — a(su)+r(puro) = prodotto della via meccanica verso purezza | 331 | 🟡 REVISIONE P66 [NUOVO sess.85] |

Composizioni produttive: chol=399 ("della lavorazione"), chor=204 ("con la lavorazione"), char=70 ("per la lavorazione"). or domina nelle sezioni descrittive (erbario, balneo); ar in quelle operative (farmacia, zodiaco).

> ⚠️ **Revisione P66 (sess.85) — ar/or come stati di purificazione (APERTA FORTE)**: la lettura precedente (ar=direttivo, or=congiunzione) è superseded. P66 propone: **r** = morfema di STATO FINALE (purezza/essenza) condiviso tra ar e or. **ar** = a(su/sopra)+r(puro) = il pressato (via meccanica). **or** = o(in/dentro)+r(puro) = il filtrato (via liquida). Con y-causativo: **ary** = "causa pressing!"; **ory** = "causa filtering!". Evidenza posizionale: ar/or appaiono DOPO y-finale nella riga (66%/49%) = sono prodotti, non verbi. Tripletta posizionale confermata corpus: chor(pos 0.339)=sostantivo-prodotto / ychor(pos 0.000)=agentivo / chory(pos 0.541)=causativo. Pattern generalizza: y-[X]or pos 0.197 vs [X]ory pos 0.414 (n=105 vs 46). FALSIFICATO SE: ar/or non mostrano distribuzione posizionale post-verbale; oppure ary/ory non sono arricchiti in sezioni di produzione.

---

## 2.3 Preposizione locativa

| Morfema | Funzione | Note | Stato |
|---------|----------|------|-------|
| **o-** | Preposizione locativa "in" | ok = o+k = "in acqua". NON prefisso fuso. In contesti COSMO/Zodiaco può anche essere segnaposto posizionale (P53 — vedi §1.2) | 🟢 SOLIDA per funzione preposizionale; 🟡 APERTA FORTE per segnaposto |

---

## 2.4 Radici nominali — solventi farmaceutici

Il quartetto solventi ok-/t-/l-/s- è il nucleo del sistema farmaceutico. Ogni solvente ha un paradigma verbale associato (qok-/qot-/qol-) e un rapporto caldo/freddo (ch/sh) caratteristico, che costituisce un *registro esperto*: il solvente disambigua l'intensità della temperatura.

| Morfema | Gloss | Freq. (corpus) | Ratio ch/sh | Stato |
|---------|-------|----------------|-------------|-------|
| **ok-** | acqua / preparazione acquosa | okaiin=447; tipi: ~399 | 6.83:1 | 🟢 SOLIDA [Placa 2026b] |
| **t-** | olio/grasso | 970 tipi | 12.1:1 | 🟢 SOLIDA [NUOVO — sess.6d] |
| **l-** | spirito/tintura alcolica | ~1.310 tipi | 2.67:1 | 🟡 APERTA FORTE [NUOVO — sess.6e] |
| **s-** | aceto | 40‰ Balneo | 2.5:1 | 🟡 APERTA FORTE [NUOVO — sess.6e] *(vedi §1.6.5: s- NON è correlato con F-ABORT — sistema gallows×solvente ortogonale)* |

> **Nota metodologica**: L'attribuzione acqua/olio/spirito alcolico/aceto ai quattro solventi non deriva da etimologie. Le lettere k, t, l, s sono simboli grafici del sistema — la loro pronuncia originale è sconosciuta e non rilevante per il modello. L'ipotesi è emersa dall'osservazione diretta della rosetta (f85r) e dell'iconografia del manoscritto. È stata poi sottoposta a verifica corpus (frequenze, ratio ch/sh per ciascun solvente, coerenza con la struttura gerarchica delle sezioni) e ha superato tutti i test disponibili. La convergenza con le farmacopee arabo-medievali (M-02) è un test esterno da eseguire — non un'assunzione del modello.

**Registro esperto — scoperta chiave** [NUOVO, Placa 2026b]: ch- (scalda) cambia significato in base al solvente: ok+ch = ebollizione (~100 °C); t+ch = frittura (~180 °C); l+ch = bagnomaria (40–60 °C). Il testo presuppone un lettore professionista.

**Sequenza sintattica solventi** (P42, [Placa 2026b]): t(0.291)→s(0.401)→ok(0.522)→l(0.651). Olio prima, spirito ultimo. Farmacologicamente: estrai in olio → acidifica con aceto → lava in acqua → conserva in spirito.

> ✗ **CORREZIONE** — *s- ≠ rosa* (FALSIFICATO: rank e distribuzione incompatibili); *s- ≠ secco* (FALSIFICATO: 2× Balneo = liquido, non secco).

> ⚠️ **Nota metodologica critica (sess.86) — s- NON è correlato con F-ABORT**: test corpus diretto su distribuzione s-% per gallows class: p=2.95%, k=3.26%, **t=3.55%, f=2.76%** (F-ABORT ha la percentuale acetica più BASSA). Ratio s- in folii f vs P/K/T = 0.09x. L'aceto è un solvente generalista medievale (oxymel, antisettici, conservazioni di erbe di qualsiasi classe). L'identificazione F-ABORT si basa esclusivamente su gallows f + iconografia — mai su profilo acetico. Qualsiasi plant-id che abbia usato co-occorrenza s- come criterio per abortività va ricontrollata indipendentemente. Il sistema 4×4 (gallows × solvente) è empiricamente ortogonale.

---

## 2.5 Paradigmi verbali solvente-temperatura

Le strutture qok, qot, qol sono composizioni q+o+[solvente]: q (dispersivo "diluisci") + o (in, locativo) + k/t/l (acqua/olio/alcool). qok* è stato verificato come paradigma verbale e non come quantificatore (51.1% termina in -y processivo; posizione centrale 0.473; 0 istanze nude). La glossa base di ogni paradigma riflette il morfema verbale q ("diluisci/dispersi"), la temperatura è aggiunta dai bench characters ch/sh.

| Morfema | Componenti | Funzione | Freq. | Stato |
|---------|-----------|----------|-------|-------|
| **qok-** | q+o+k | "diluisci in acqua" | 3.079 occ, 271 forme | 🟢 SOLIDA [Placa 2026b] |
| **qokch\*** | qok+ch | "diluisci in acqua, a caldo / bolli" | 280 occ | 🟢 SOLIDA [Placa 2026b] |
| **qoksh\*** | qok+sh | "diluisci in acqua, a freddo / infondi" | 41 occ | 🟢 SOLIDA [Placa 2026b] |
| **qot-** | q+o+t | "diluisci in olio" | 1.117 occ, 175 forme | 🟢 SOLIDA [NUOVO] |
| **qotch\*** | qot+ch | "diluisci in olio, a caldo / scalda" | 218 occ | 🟢 SOLIDA [NUOVO] |
| **qotsh\*** | qot+sh | "diluisci in olio, a freddo / macera" | 18 occ | 🟢 SOLIDA [NUOVO] |
| **qol** | q+o+l | "diluisci in alcool/spirito" | 610+ | 🟢 SOLIDA [Placa 2026b — REVISIONE vt1.3] |

> ✗ **CORREZIONE vt1.3** — *glosse qok/qot/qol riscritta da P52*: le glosse precedenti ("riscalda in olio / friggi", "raffredda in olio", "bolli in acqua", "una misura di") non riflettevano q come verbo base. P52 (sess.78) stabilisce q = "diluisci/dispersi": il verbo primario in tutti questi paradigmi è la dispersione nel solvente; la temperatura (ch/sh) è un modificatore secondario. La glossa corretta mostra q come verbo base + indicazione termica come modalità. Conseguenza: "qo" non è un'unità lessicale autonoma — è sempre q+o (dispersivo+locativo).

---

## 2.6 Radice farmaceutica principale

| Morfema | Gloss | Etimologia | Paradigma | Stato |
|---------|-------|-----------|-----------|-------|
| **da-** | medicina/farmaco | dāru (persiano, دارو) | daiin=833, dar=284, dal=238 | 🟢 SOLIDA [Placa 2026b] |
| **daiin** | essenza medicinale | da + aiin | token più frequente del corpus | 🟢 SOLIDA |
| **dar** | medicamento (congiuntivo) | da + r | domina in erbario | 🟢 SOLIDA |
| **dal** | del medicamento (gen.) | da + l | bilancia dar in ricettario | 🟢 SOLIDA |

---

## 2.7 Marcatori di processo termico

| Morfema | Processo | Esempi | Freq. tipi | Stato |
|---------|----------|--------|-----------|-------|
| **ch-** | Caldo: decozione, cottura, ebollizione | cheey=185, chol=399, chor=204 | ~1.193 | 🟢 SOLIDA [Placa 2026b] |
| **sh-** | Freddo: infusione, macerazione | sheey=149, sheol=11 | ~8 stem unici | 🟢 SOLIDA [Placa 2026b] |

Evidenza Balneo (ch/sh=1.07) = unico contesto dove caldo ≈ freddo (la macerazione usa entrambe le temperature a seconda del materiale — freddo per princìpi termolabili, caldo per quelli stabili; P61); sh- precede ch- nel 60% delle righe miste (macera prima a freddo, scalda dopo).

---

## 2.8 Morfema passivo/riflessivo

| Morfema | Funzione | Pattern chiave | Stato |
|---------|----------|---------------|-------|
| **ot-** | Passivo/riflessivo "si/viene preparato" | otol.chol.daiin = "si consuma cotta, dell'essenza di"; ot-→ch- 15.5% vs ot-→sh- 7.2% (ratio 2:1 replica ch/sh globale) | 🟢 SOLIDA [Placa 2026b] |

---

## 2.9 Sistema quantitativo — solvente e concentrazione

Il sistema quantitativo opera su due assi ortogonali e posizioni morfologiche distinte (~0.39 vs ~0.46). I due assi non sono intercambiabili.

**Asse E — quantità solvente** (posizione ~0.39):

| Morfema | Quantità | Note | Stato |
|---------|----------|------|-------|
| **e** | q.b. / quantità base | prefix-specific (NON gradiente universale) | 🟡 APERTA FORTE [Placa 2026b] |
| **ee** | abbondante | permutation test ρ=1.0 p=0.0417; OR=1.659 p<10⁻⁶ morfologia-matched | 🟢 SOLIDA [Placa 2026b] |
| **eee** | copioso/massimo | correlato con solventi ad alto volume | 🟡 APERTA FORTE [Placa 2026b] |

> ✗ **CORREZIONE** — *gradiente e/ee/eee NON universale*: è prefix-specific. "Sciacqua" come gloss per gradiente e/ee FALSIFICATO.

**Asse AIN — grado di estrazione** (posizione ~0.46):

| Morfema | Estrazione | Note | Stato |
|---------|-----------|------|-------|
| **-ain** | leggera (singola) | estratto leggero — raro rispetto ad -aiin | 🟡 APERTA FORTE [Placa 2026b] |
| **-aiin** | standard (doppia) | mathbūkh arabo: doppia estrazione come standard canonico; forma dominante (~10× ain) | 🟢 SOLIDA [Placa 2026b] |
| **-aiiin** | concentrata (tripla) | estratto potenziato | 🟡 APERTA FORTE [Placa 2026b] |

> ✗ **ATTENZIONE**: ee e ii NON sono intercambiabili — posizioni morfologiche diverse (~0.39 vs ~0.46) e quasi mutualmente esclusivi (OR=0.066, p<0.001). Il gradiente è sul numero di ripetizioni, non sulla lettera in sé.

> ⚠️ **Nota P68 (sess.88) — `e` in contesto y-iniziale = cicli di estrazione**: quando `e*` appare tra il solvente e il verbo finale in token con y-iniziale (pattern y+solvente+e*+verbo), la funzione non è "quantità del solvente" ma **numero di cicli di estrazione**. e=1 ciclo, ee=2 cicli (standard: 219 token, più frequente di e=173, parallelo con aiin > ain), eee=3 cicli (19 token). Evidenza: (a) e* è SEMPRE post-solvente (412 vs 4 pre-solvente); (b) ys*/yl* quasi-zero (11/17 vs yk=564/yt=473 — nessuna estrazione con aceto/alcool primario); (c) nominali esistono: ykeeol=11, ykeeor=3 = stessa struttura radice senza y-finale = sostantivi prodotto. Coppia comando/nominale simmetrica. Il sistema `e*` in contesto verbale è ortogonale all'Asse E nominale — stesso glifo, funzione distinta.

---

## 2.10 Suffissi processuali e aspettuali

| Morfema | Analisi | Funzione | Freq. | Stato |
|---------|---------|----------|-------|-------|
| **-eey** | ee + y | "mescola bene" — verbo composto e+y con ee=gradiente intensità | 1.874 occ, 270 prefissi unici | 🟢 SOLIDA [Placa 2026b — gloss aggiornata sess.88] |
| **-edy** | e + dy | modifier + produci (dy = atomico "produci") | molto frequente | 🟢 SOLIDA [Placa 2026b — parsing corretto sess.87] |
| **-eedy** | ee + dy | 2 cicli + produci (in contesto y-iniziale = 2 cicli di estrazione; in contesto verbale generico = intensificatore) | frequente | 🟢 SOLIDA [Placa 2026b — parsing corretto sess.88] |
| **-ody** | o + d + y | "incorpora" — morfema agglutinato o(direzionale)+d+y | 1.079 occ | 🟡 APERTA FORTE [P50 — gloss rafforzata sess.88] |
| **-ary** | — | PRESSA ("su/sopra" = forza che scende) | OR=3.57 Zodiaco p=0.0002 | 🟢 SOLIDA [Placa 2026b] |
| **-ory** | — | FILTRO ("in/dentro" = liquido che passa) | OR=3.75 Cancro p=0.0002 | 🟢 SOLIDA [Placa 2026b] |
| **-eo** | — | evaporare/ridurre/essiccare | 435 (eo), 2.006 tot | 🟢 SOLIDA [NUOVO — sess.6e] |

> ✗ **CORREZIONE** — *-ary e -ory NON sono invertibili*. -ary = PRESSA (forza dall'alto), -ory = FILTRO (passaggio). Le inversioni precedenti sono state corrette in sess.74. *chary = 0 nel Zodiaco* (la pressa calda è una tecnica dell'erbario/ricette, non del calendario zodiacale).

Usi principali di -eo: ycheo (y+ch+eo = "fai evaporare a caldo", pos.0.064 = prima istruzione della riga); firma solventi: ok=80%, t=0%, l arricchito +102% — l'evaporazione è per acqua e spirito, mai per olio.

---

## 2.11 Marcatore di chiusura formula

| Morfema | Funzione | Distribuzione | Stato |
|---------|----------|--------------|-------|
| **-am** | Marcatore di chiusura/completamento formula (copula aspettuale "è pronto/fatto") | Posiz. 0.742; nulla segue nel 95%+ dei casi; Herbal 34.6‰ > Pharma 20.5‰ > Balneo 7.5‰ *(⚠️ verifica corpus — le due sezioni erano invertite in bozze precedenti)*; libero su tutti i prefissi (da-am, ch-am, ot-am, ok-am) | 🔵 TIER B [NUOVO — sess.5c] |

> ✗ **CORREZIONE CRITICA** — *-am ≠ marham (unguento)*. FALSIFICATO con 3/5 predizioni contraddette: (1) domina in erbario, non in pharma; (2) assente da @Lf (1.4%); (3) cluster in M7-M11, non in M1-M6. L'interpretazione "forma galenica unguento" è ABBANDONATA. La funzione attuale è marcatore di completamento formulaico.

---

## 2.12 Sistema gallows — classi terapeutiche

Le quattro lettere gallows (k, t, f, p) sono *class markers terapeutici*, non traslitterazioni fonetiche. La distinzione è supportata da distribuzione sezionale, combinazione con morfemi di processo, e dai 35 token @Lf del ricettario. Le lettere gallows ornate (ckh, cth, cfh, cph) rappresentano la versione "concentrata termicamente" di ciascuna classe.

**Gallows semplici**:

| Morfema | Classe | Azione farmacologica | Freq. approx. | Stato |
|---------|--------|---------------------|---------------|-------|
| **k** | K-EXCIT | stimolanti, espettoranti, tonici | alta | 🟢 SOLIDA [Placa 2026b] |
| **t** | T-PROT | protettivi, antinfiammatori, astringenti | alta (940 ornata cth) | 🟢 SOLIDA [Placa 2026b] |
| **f** | F-ABORT | abortivi, emmenagoghi forti, purganti | bassa (74 ornata cfh) | 🟢 SOLIDA [Placa 2026b] |
| **p** | P-CALM | calmanti, analgesici, sedativi | media | 🟢 SOLIDA [Placa 2026b] |

**Entropie posizionali** (evidenza di funzione grammaticale, non ornamentale): f=0.832 (vincolata, quasi sempre pos.1 = classe formulaica); k=1.99; t=2.94; p=3.69.

**Gallows ornate** (compressione morfografica — [Placa 2026b]):

| Morfema | Componenti | Funzione | Freq. | Stato |
|---------|-----------|----------|-------|-------|
| **ckh** | c + k + h | concentrato termico K-EXCIT | 904 | 🟡 APERTA [Placa 2026b] |
| **cth** | c + t + h | concentrato termico T-PROT | 940 | 🟡 APERTA [Placa 2026b] |
| **cfh** | c + f + h | concentrato termico F-ABORT | 74 | 🟡 APERTA [Placa 2026b] |
| **cph** | c + p + h | concentrato termico P-CALM | 215 | 🟡 APERTA [Placa 2026b] |

> ✗ **CORREZIONI**: (1) *ornate ≠ calligrafia* (Modello A FALSIFICATO, χ²=244.8); (2) *ornate ≠ cross-solvent markers* (FALSIFICATO sess.67); (3) *ornate NON inserite post-hoc* — integrate nel token.

**Bench characters** (glifi unitari, non coppie):

| Morfema | Processo | Note |
|---------|----------|------|
| **ch** | Caldo | Glifo singolo — NON scomponibile in c+h |
| **sh** | Freddo | Glifo singolo — NON scomponibile in s+h |

> ✗ **CORREZIONE** — *c/s NON sono coppia parallela* (FALSIFICATO sess.68). sh- e ch- sono bench characters unitari indipendenti.

---

## 2.13 Marcatori posizionali di riga

| Morfema | Posizione media | Funzione contestuale | Stato |
|---------|----------------|---------------------|-------|
| **sol** | 0.19 | Apre righe Balneo — "l'essenza [poi processa]" | 🟡 APERTA |
| **oly** | 0.93 | Marcatore di chiusura di riga | 🟡 APERTA |
| **yy** | finale | Chiusura rituale (f86v4 — canzone mnemonica) | 🔵 STRUTTURA SOLIDA |

---

## 2.14 Composti decodificati — selezione

I token seguenti hanno alta confidenza di interpretazione perché combinano morfemi già validati con distribuzioni sezionali coerenti. Riportati per frequenza decrescente.

| Token | Analisi | Significato | Freq. | Stato |
|-------|---------|------------|-------|-------|
| **daiin** | da + aiin | "essenza medicinale" | 833 | 🟢 SOLIDA |
| **okaiin** | ok + aiin | "infusione acquosa" | 447 | 🟢 SOLIDA |
| **chol** | ch + ol | "della lavorazione" | 399 | 🟢 SOLIDA |
| **qokchy** | qok + ch + y | "diluisci in acqua a caldo, fai" | 68 | 🟢 SOLIDA |
| **qokchdy** | qok + ch + d + y | "diluisci in acqua a caldo, tratta, fai" | 56 | 🟢 SOLIDA |
| **dar** | da + r | "medicamento (congiuntivo)" | 284 | 🟢 SOLIDA |
| **dal** | da + l | "del medicamento" | 238 | 🟢 SOLIDA |
| **chor** | ch + or | "con la lavorazione" | 204 | 🟢 SOLIDA |
| **cheey** | ch + eey | "fai decotto" | 185 | 🟢 SOLIDA |
| **okeey** | ok + eey | "in acqua abbondante" (operazione acquosa ad alto volume; "diluisci" è funzione di q-, non di ok) | 144 | 🟢 SOLIDA |
| **ycheo** | y + ch + eo | "fai evaporare a caldo" (prima istruzione) | 15 | 🟢 SOLIDA |
| **ykeey** | y(estrai) + k(acqua) + ee(2 cicli) + y(FAI) | "esegui 2 cicli di estrazione acquosa" [causativo telico] — n=53; coppia nominale: ykeeol=11 (lo spirito della doppia estrazione acquosa) | 53 | 🟡 APERTA FORTE [P68 sess.88] |
| **ykeedy** | y(estrai) + k(acqua) + ee(2 cicli) + dy(produci) | "produci con 2 cicli di estrazione acquosa" | 25 | 🟡 APERTA FORTE [P68 sess.88] |
| **qol** | q + o + l | "diluisci in alcool/spirito" | 610+ | 🟢 SOLIDA — REVISIONE vt1.3 |
| **otal** | ot + al | "il preparato [di]" | 3 | 🟡 APERTA |
| **otaiin** | ot + aiin | "si prepara l'essenza" | freq. | 🟡 APERTA |

---

## 2.15 Morfemi ancora opachi

| Token/Famiglia | Freq. | Nota |
|---------------|-------|------|
| **-ody** | 1.079 | Struttura o+d+y = "in [medium], [farmaco], fai" — vedi P50/§2.10. Non più opaco ma lettura aperta in attesa di test settoriale. |
| **raiin** | 75 | Probabile r+aiin (terzo paradigma -aiin, "essenza pura") |
| **-eos** | 210 | Possibile secondo quadripolo (eol/eor/eos/eod) |
| **gallows ornate — nomi originali** | — | p/k/t/f sono codici EVA, non traslitterazioni fonetiche |
| **weirdos** (~100 forme rare) | ~300 | Glifi non standard; possibili errori di copiatura o hapax specialistici |

---

## 2.16 Falsificazioni — riepilogo correzioni

Questa sezione documenta esplicitamente le interpretazioni abbandonate, con il motivo della falsificazione. Un modello rigoroso deve registrare cosa ha smesso di funzionare con la stessa precisione con cui registra cosa funziona.

| Interpretazione precedente | Stato | Motivo della falsificazione |
|---------------------------|-------|----------------------------|
| **-am = marham** (unguento/pomata) | ❌ FALSIFICATO | 3/5 predizioni contraddette: domina in Herbal (non Pharma come predetto da marham = galenica da preparazione), assente da @Lf (1.4%), cluster M7-M11 non M1-M6. Vedi §2.11 per dettaglio completo. |
| **s- = rosa** | ❌ FALSIFICATO | Rank troppo basso, distribuzione incompatibile |
| **s- = secco** | ❌ FALSIFICATO | 2× Balneo = liquido, non secco |
| **dam = sangue** | ❌ FALSIFICATO | Correlazione dam↔daiin r=0.988 → dam = da+m (agglutinante), non lessema indipendente |
| **ornate = calligrafia** | ❌ FALSIFICATO | χ²=244.8 — distinzione morfologica produttiva |
| **ornate = cross-solvent markers** | ❌ FALSIFICATO | Sessione 67 |
| **c/s = coppia parallela** | ❌ FALSIFICATO | Sessione 68 |
| **gradiente e/ee/eee universale** | ❌ FALSIFICATO | Prefix-specific, non universale |
| **"sciacqua" come gloss per gradiente e/ee** | ❌ FALSIFICATO | Funzione non supportata dalla distribuzione |
| **cheor = artemisia** | ❌ FALSIFICATO | Distribuzione sezionale incompatibile con profilo artemisia; identificazione alternativa aperta |
| **Zodiaco = melothesia** | ❌ SUPERSEDED | Produzione industriale spiega meglio tutti i dati (P43 SOLIDA) |
| **M1-M6 = unguenti / M7-M11 = orali** | ❌ FALSIFICATO | Fondato su -am=marham; cade con la falsificazione di -am |
| **pol = oppio** | ❌ FALSIFICATO | pol = preparazione calmante in soluzione alcolica |
| **-ary / -ory invertiti** | ❌ CORREZIONE | -ary = PRESSA (forza dall'alto); -ory = FILTRO (passaggio). Sessione 74. |
| **Balneo = bagni terapeutici / somministrazione** | ❌ SUPERSEDED | P61 (sess.81): le donnine nelle vasche sono materiale vegetale in macerazione, non pazienti. La sezione Balneo è una guida alla macerazione industriale, non alla somministrazione. La somministrazione era dominio clinico orale, non documentato in un testo di produzione cifrato. |
| **d = verbo contestuale** (Herbal="prendi", Balneo="immergi", Stars="lavora") | ❌ FALSIFICATO (sess.84) | d è SEMPRE NOMINALE — puntatore anaforico al materiale corrente. OR=3.64 (d-iniziali senza y-finale = 84% vs 59% corpus). Distribuzione bimodale incompatibile con funzione verbale. |
| **qo = unità lessicale autonoma / "misura di"** | ❌ FALSIFICATO (sess.83/85) | qo è sempre q+o (dispersivo+locativo). Le strutture qok/qot/qol = q+o+[solvente], non coalescenze qo+solvente. La glossa "una misura di" era errata — il verbo è q ("diluisci"), la misura non è codificata in qo. |
| **s- correlato con F-ABORT / aceto = solvente degli abortivi** | ❌ FALSIFICATO (sess.86) | Test corpus: s-% per gallows class p=2.95%, k=3.26%, t=3.55%, f=2.76% (F-ABORT ha il minimo). Ratio s- in folii f vs P/K/T = 0.09x. L'aceto è solvente generalista. Il sistema gallows × solvente è ortogonale. |
| **ar = direttivo "a/per" / or = congiunzione "e/con"** | ❌ SUPERSEDED (P66, sess.85) | ar = a(su)+r(puro) = il pressato; or = o(in)+r(puro) = il filtrato. r = morfema di stato finale. Le vecchie glosse connettivali non reggono alla distribuzione posizionale (ar/or appaiono DOPO y-finale nella riga). |

---

## 2.17 Coalescenze morfematiche confermate

Una coalescenza è una fusione di due morfemi in un'unità lessicalizzata con comportamento distribuzionale autonomo. La condizione è che il token risultante mostri frequenza, distribuzione posizionale e combinatoria non predicibili dalla semplice somma delle parti.

**Coalescenza confermata**:

| Morfemi | Risultato | Evidenza | Freq. | Stato |
|---------|-----------|----------|-------|-------|
| da + aiin | **daiin** | Frequenza (833 occ) e distribuzione non predicibili da da- e aiin- separati; token più frequente del corpus | 833 | 🟢 SOLIDA |

**Composizioni dirette (NON coalescenze)**:

Le strutture qok, qot, qol sono composizioni q+o+[solvente] — tre morfemi in sequenza, non due morfemi fusi. Il comportamento distribuzionale è interamente predicibile dai componenti: q (dispersivo) + o (locativo "in") + k/t/l (acqua/olio/spirito). Non esiste un morfema intermedio "qo" con significato autonomo (FALSIFICATO sess.83/85). Classificarle come coalescenze sarebbe inconsistente con §1.6.1 e §2.5.

| Struttura | Componenti | Funzione | Freq. |
|-----------|-----------|----------|-------|
| **qok** | q + o + k | "diluisci in acqua" | 3.079 |
| **qot** | q + o + t | "diluisci in olio" | 1.117 |
| **qol** | q + o + l | "diluisci in spirito" | 610+ |

---

*Fine Sezione 2 — Dizionario Morfematico Consolidato*

---

# SEZIONE 3 — IL SISTEMA ICONOGRAFICO-CALENDARIALE

## Premessa metodologica

Le ipotesi della Sezione 3 hanno status epistemico significativamente più basso della Sezione 1 e del Companion. Si basano su: (a) evidenza corpus limitata (35 label @Lz per 12 folii), (b) osservazione iconografica diretta non ancora sistematizzata su IIIF ad alta risoluzione, (c) coerenza con il sistema linguistico già stabilito — che è una condizione necessaria ma non sufficiente.

Il rischio specifico di questa sezione è la coerenza narrativa: un modello sufficientemente ricco può rendere qualsiasi dettaglio iconografico "coerente". Il test che conta non è la coerenza interna ma la predizione discriminante — cioè l'ipotesi che esclude alternative specifiche, non solo quella che include l'osservazione nel modello esistente.

**Gerarchia di priorità empirica** — le ipotesi non hanno tutte lo stesso peso:

| Priorità | Ipotesi | Motivo |
|---------|---------|--------|
| Alta (già parzialmente testata) | H-A01, H-A02, H-B01/B02 | Test statistici già superati; conteggio IIIF è il solo test residuo |
| Media (predizioni discriminanti precise) | H-C01, H-C02, H-L01/L02 | Predizioni falsificabili su distribuzioni attese; test su IIIF eseguibile |
| Bassa (coerenti, non testate, non discriminanti) | H-C03/C04, H-D-series, H-E-series, H-P-series | Osservazioni iconografiche ancora non discriminanti rispetto ad alternative |

Ogni ipotesi riporta il test di falsificazione. Le ipotesi già presenti nelle 39 predizioni del Companion sono indicate con `[vedi Placa 2026b]`; quelle nuove (post-Companion) con `[NUOVO]`.

**Avvertenza**: le ipotesi classificate APERTA in questa sezione non costituiscono evidenza — sono un programma di test. Nessuna va citata come supporto al modello prima che il test corrispondente sia eseguito e superato.

**Legenda stati**: [SOLIDA] = test statistico superato con p < 0.05 | [APERTA FORTE] = evidenza preliminare convincente, predizione discriminante formulabile | [APERTA] = coerente col modello, non ancora discriminante | [DA TESTARE IIIF] = richiede analisi visiva sistematica prima di qualsiasi valutazione

---

### BLOCCO A — Struttura calendriale generale

**H-A01 [SOLIDA — vedi Placa 2026b] — Una figura = un giorno**
~365 figure totali nelle ruote zodiacali (300 presenti + ~65 nei folii mancanti Capricorno/Acquario). Inizio del calendario: Pesci (25 marzo, capodanno medievale pisano). Tre test già superati: χ² distribuzione mensile (p < 0.001); corrispondenza con calendari agricoli medievali (p < 0.001); gradiente ot% coerente con ciclo reale dell'olio d'oliva (ρ=-0.83, p=0.0008).
*Test aperto*: conteggio sistematico preciso su IIIF. Unico test che può trasformare la stima 365 in dato esatto.

**H-A02 [SOLIDA — vedi Placa 2026b] — I due folii mancanti esistevano**
Capricorno e Acquario assenti fisicamente, ma il gradiente P48 predice ot%≈20–25% per quei mesi — non zero. La rimozione è intenzionale (taglio fisico, non perdita accidentale). Motivazione ignota.
*Test aperto*: ricerca storica su menzioni dei folii prima della sparizione.

**H-A03 [SOLIDA — vedi Placa 2026b] — Ariete e Toro = 1 mese ciascuno (non 2)**
I due folii per Ariete (f70v1+f71r) e per Toro (f71v+f72r1) rappresentano due metà dello stesso mese (~15+15 giorni). Coerente con il modello 1figura/giorno solo se la coppia = 1 mese.

**H-A04 [APERTA FORTE — vedi Placa 2026b] — Gradiente stagionale olio**
ot% decresce da Pesci (31.5%) a Sagittario (16.7%): ρ=-0.83, p=0.0008. Tre meccanismi concentrici confermati da fonti indipendenti: (1) shelf life olio in terracotta medievale 3–6 mesi (fresco solo dic–apr); (2) prescrizione Avicenna di massaggi oleosi in inverno (Dalk); (3) patologie invernali richiedono unguenti. Test corpus: ok% ρ=+0.212 p=0.556 (non significativo) — l'olio cala ma non viene sostituito da acqua.
*Falsificato SE*: ok% o s% mostrano gradiente inverso simmetrico.

**H-A05 [APERTA — NUOVO] — Anomalia Bilancia: secondo ciclo oleoso autunnale**
ot% in Bilancia = 23.0%, sopra la media estiva (Vergine 14.5%, Scorpione 18.8%). Ipotesi: raccolta olive autunnali + semi oleosi autunnali creano un secondo picco produttivo.
*Test*: densità di t- + -ary (pressa oleosa) in Bilancia > media mesi estivi.

---

### BLOCCO B — Codice delle tinozze

**H-B01 [SOLIDA — vedi Placa 2026b] — Tinozza verticale = immersione/macerazione**
Figure con tinozza verticale (corpo immerso): operazione di macerazione. In f70v2 (Pesci), anello esterno = 19 figure tutte con tinozze verticali, zero eccezioni.

**H-B02 [SOLIDA — vedi Placa 2026b] — Tinozza orizzontale = estrazione**
Figure con tinozza rovesciata/orizzontale: operazione di estrazione/spremitura. In f70v2, anello interno = 10 figure, 4 con tinozze orizzontali (40%). La transizione verticale→orizzontale = metti in ammollo → tira fuori.

**H-B03 [APERTA — NUOVO] — Posizione relativa tinozza = ordine sequenziale**
Tinozze in posizioni diverse attorno alla figura (a sinistra, a destra, sopra) potrebbero codificare l'ordine dell'operazione nella sequenza giornaliera.
*Test*: analisi sistematica posizioni tinozze su IIIF per tutti i 12 folii. Se casuale, ipotesi cade.

---

### BLOCCO C — Codice delle acconciature / quadripolo operatrici

**H-C01 [SOLIDA — vedi Placa 2026b] — 4 acconciature = 4 operatrici del quadripolo**
Quattro tipi sistematici: (1) doppi rosette = Dottoressa; (2) riccioli = Fisica; (3) capelli lunghi = [ruolo in revisione — vedi P64]; (4) capelli alle spalle = Chimica. Corrispondenza con le 4 figure cardinali di f86v4 già confermata (doppi rosette = figura Ovest).

> ⚠️ **Revisione P64 (sess.82)**: la figura Nord di f86v4 (di spalle) rappresenta un ruolo fornitore strutturalmente aperto, non una quarta partner con chiave propria. L'acconciatura (3) potrebbe identificare un ruolo operativo variabile, non un soggetto fisso. Il numero di chiavi private del sistema è 3, non 4. Test: verifica sistematica su IIIF se l'acconciatura (3) mostra maggiore variabilità morfologica rispetto alle altre tre.

**H-C02 [APERTA FORTE — NUOVO, P54] — Acconciatura = fonema iniziale della label**
Estensione di P53 al Zodiaco. L'acconciatura della donnina fornisce il fonema mancante nei token o-iniziali adiacenti: donnina-acqua→k, donnina-olio→t, donnina-spirito→l. La label "odaiin" con donnina-acqua si legge "kodaiin"; con donnina-olio si legge "todaiin".
*Test*: folii con ot% alto (inverno — P48) dovrebbero avere prevalenza di donnine-olio. Predizione precisa: f70v2 (ot%=69.4%) → acconciatura dominante "olio"; f72v2 (ot%=31–37%) → acconciatura dominante "acqua" o "spirito".
*Falsificato SE*: distribuzione acconciature non varia tra folii con ot% alto e basso.

**H-C03 [APERTA — NUOVO] — Acconciatura Dottoressa = giorni di dosaggio**
Donnine con doppi rosette nel Zodiaco = giorni in cui viene eseguito il dosaggio finale (consegna al cliente). Non lavorazione, ma somministrazione.
*Test*: label adiacenti a donnine-Dottoressa dovrebbero mostrare densità di -am (completamento) > media.

**H-C04 [APERTA — NUOVO] — Figura maschile (Gemelli) = processo duale o scambio**
L'unica figura maschile sistematica (Gemelli) non rientra nelle 4 operatrici. Due ipotesi: (a) marcatore di processo duale/distillazione — coerente con H-D03; (b) quinta categoria (transazione/consegna).
*Test*: presenza di figure maschili in altri folii zodiacali e loro contesto.

**H-C05 [APERTA — NUOVO] — Distribuzione acconciature = frequenza di turno per specializzazione**
Mesi con alta densità ot* dovrebbero avere più donnine-olio; mesi con alta densità -ory più donnine-Fisica.
*Test*: conteggio per tipo acconciatura × mese su IIIF, correlazione con profilo morfologico corpus.

---

### BLOCCO D — Segni specifici

**H-D01 [APERTA FORTE — NUOVO, P56] — Ariete/Toro: doppia pressatura primaverile**
La zampa alzata verso la tinozza nell'iconografia di Ariete e Toro = gesto convenzionale di pressa. I due segni primaverili hanno doppio spazio produttivo dedicato alla pressatura delle erbe primaverili. Non essiccatura — PRESSATURA.
*Test*: frequenza -ary nei fogli Ariete/Toro vs media zodiacale. Atteso OR > 2 (benchmark: -ary in Cancro ha OR=3.57, p=0.0002).

**H-D02 [SOLIDA — vedi Placa 2026b] — Cancro = estrazione essenza/distillazione**
OR=3.75 (p=0.0002) per ol+or vs resto zodiaco. Stelle caudate presenti (attrezzatura specializzata). Morfema -ary arricchito. Mese di estrazione dell'essenza dopo la raccolta estiva.

**H-D03 [APERTA FORTE — NUOVO, P59] — Gemelli = distillazione / scambio di stato fisico**
Uomo + donna che si scambiano un anello = iconografia dello scambio reciproco → cambio di stato fisico della materia (evaporazione/condensazione). Mese con massima densità attesa di -eo (evaporare/ridurre, morfema confermato). Coerente con la distillazione come processo a due fasi: vapore ↔ liquido.
*Test*: frequenza di ycheo/ysheo nei folii Gemelli vs media zodiacale. Atteso OR > 3.

**H-D04 [APERTA FORTE — NUOVO, P57] — Bilancia = misurazione e confezionamento**
Settembre: mese dedicato alla pesatura e al confezionamento delle preparazioni pronte. Il simbolo della bilancia come non-coincidenza iconografica. Coerente con l'anomalia ot% di H-A05 (secondo ciclo oleoso autunnale) e con il profilo atteso di "chiusura di processo".
*Test*: densità -am (completamento) in Bilancia > media zodiacale. Profilo inverso rispetto a Cancro (estrazione).

**H-D05 [SOLIDA — vedi Placa 2026b] — Sagittario = chiusura annuale**
orary + chory + -am al massimo = pressa essenze + filtrazione calda + prodotti finali. Il ciclo si chiude prima del Capricorno.

**H-D06 [APERTA — NUOVO] — Pesci = riattivazione delle scorte dell'anno precedente**
Il ciclo inizia a marzo con le scorte essiccate raccolte in estate/autunno precedenti. Prima operazione: macerazione delle materie prime dell'anno passato.
*Test*: densità sh- (infusione/macerazione a freddo) in Pesci > media zodiacale.

**H-D07 [APERTA — NUOVO] — Scorpione = apertura stagione di pressa calda**
La struttura iconografica di Scorpione simile a Vergine (stella con coda + prima donnina con marcatore speciale) suggerisce apertura di una sotto-stagione con pressa calda specializzata.
*Test*: frequenza chary + -ary in Scorpione vs mesi autunnali limitrofi.

---

### BLOCCO E — Stella caudata

**H-E01 [SOLIDA — vedi Placa 2026b] — Stella caudata = attrezzatura specializzata**
Le stelle con coda marcano operazioni che richiedono strumenti fisici (torchio, filtro di seta, alambicco). Grove conta 18 stelle caudate su 33 righe in Cancro — concentrazione massima dello Zodiaco.

**H-E02 [APERTA FORTE — NUOVO, P55] — Lunghezza coda = durata/intensità filtraggio**
La coda non è decorativa: la sua lunghezza è proporzionale alla durata o all'intensità del processo di filtrazione. Coerente con -ory = FILTRO (P46 SOLIDA nel Companion).
*Test*: classificare su IIIF tutte le stelle caudate per lunghezza della coda. Coda lunga → -ory nelle label adiacenti > -ary; coda corta → distribuzione uniforme.
*Falsificato SE*: stelle con coda lunga appaiono sistematicamente senza -ory.

**H-E03 [APERTA — NUOVO] — Stelle caudate in Stars = ricette con strumento obbligatorio**
Le stelle con coda nella sezione Stars (non nel Zodiaco) marcano ricette non eseguibili senza attrezzatura specifica.
*Test*: righe adiacenti a stelle caudate in Stars → morfemi di strumento specializzato con frequenza maggiore rispetto a stelle normali.

**H-E04 [APERTA — NUOVO] — Stelle caudate in Herbal = piante che richiedono spremitura**
Se il pattern si estende all'erbario, le illustrazioni con stelle caudate dovrebbero corrispondere a piante note per richiedere pressatura (olive, semi oleosi, radici).
*Test*: confronto stelle caudate in Herbal con le 17 piante identificate e letteratura farmacobotanica medievale.

---

### BLOCCO F — Colorazione e pigmenti

**H-F01 [SOLIDA — vedi Placa 2026b] — Colore giallo su stelle della rosetta = moltiplicatore ×2**
In f85r, il giallo su uno spicchio del rosone-olio indica "moltiplica per due" il dosaggio. Confermato nell'analisi del sistema di dosaggi (Companion).

**H-F02 [APERTA FORTE — NUOVO, P60] — Stelle gialle nel Zodiaco = marcatura operatore secondario**
Le stelle colorate in giallo in certi folii zodiacali non sono originali: sono annotazioni di una mano posteriore che ha segnato le ricette che poteva (o voleva) replicare. Questo operatore conosceva il sistema ma aveva capacità produttiva ridotta.
*Test primario*: quando le label zodiacali saranno decifrate, le ricette con stella gialla dovrebbero avere: (a) meno ingredienti; (b) morfemi più semplici; (c) concentrazione su stagioni con materie prime accessibili.
*Test secondario*: analisi paleografica/cromatica per distinguere il pigmento giallo originale vs il pigmento delle stelle marcate.
*Falsificato SE*: stelle gialle e non-gialle distribuzioni uniformi per complessità morfologica; oppure concentrate su un singolo folio (artefatto di conservazione, non selezione).

**H-F03 [APERTA — vedi Placa 2026b] — Pigmento blu post-hoc nel rosone acqua = correzione dosaggio**
Le stelle ricoperte da blu in f85r sono revisioni d'urgenza: il dosaggio originale era troppo alto. Il blu sgraziato (incongruente con la precisione del MS) è la firma di una correzione pratica.
*Test*: analisi multispettrale (IR/UV) per rilevare stelle sotto il pigmento blu.

**H-F04 [APERTA — NUOVO] — Pigmento rosso intenso = tossicità o controindicazione**
In alcune illustrazioni erbarie il rosso intenso (non il rosso-arancio normale dei contorni) potrebbe marcare piante tossiche o a dosaggio critico.
*Test*: confronto piante con rosso intenso con le 17 identificazioni e la letteratura tossicologica medievale.

---

### BLOCCO G — Figure anomale e marcatori speciali

**H-G01 [APERTA FORTE — NUOVO, P58] — Corona = marcatore di inizio ciclo operativo stagionale**
La donnina coronata come prima figura di Vergine (settembre) e la struttura simile in Scorpione indicano apertura di un ciclo produttivo, non rango gerarchico.
*Test*: la corona appare esclusivamente come prima figura del segno (posizione 1/30) o anche in posizioni interne? Se solo in posizione 1, è marcatore funzionale.

**H-G02 [APERTA — NUOVO] — Doppia corona = inizio del ciclo annuale**
Un eventuale marcatore doppio nella prima figura di Pesci (25 marzo) potrebbe marcare l'inizio dell'anno.
*Test*: verifica IIIF di f70v1 per marcatori doppi sulla prima figura.

**H-G03 [APERTA — NUOVO] — Posture gestuali verso il testo = operatrice che esegue**
Donnine che indicano verso le label o verso il testo adiacente potrebbero identificare l'operatrice responsabile della lettura (= l'operatrice che esegue l'operazione del giorno).
*Test*: classificare posture gestuali su IIIF e correlare con il tipo di acconciatura.

**H-G04 [APERTA — NUOVO] — Figura senza tinozza = giorno di transizione o riposo**
Le donnine senza tinozza potrebbero indicare giorni di inizio/fine mese o di riposo produttivo.
*Test*: conteggio figure con/senza tinozza per folio. Se si concentrano a inizio/fine mese, è marcatore di transizione.

---

### BLOCCO H — Struttura sintattica delle label zodiacali

**H-H01 [SOLIDA — vedi Placa 2026b] — @Lz = etichette nominali**
35 token @Lz su 12 folii: 0 imperativi y-. Le label zodiacali sono nomi di preparazioni, non istruzioni procedurali.

**H-H02 [APERTA FORTE — NUOVO, P53/P54] — Token o-iniziale = puntatore cross-sezionale a Stars**
I token o-iniziali zodiacali (con fonema implicito dato dall'acconciatura) sono gli indirizzi delle ricette corrispondenti nella sezione Stars. Il token Stars corrispondente ha il fonema esplicito (es: label zodiacale "odaiin" con donnina-acqua → ricerca "kodaiin" in Stars).
*Test*: in Stars, ogni token k+base dovrebbe comparire con frequenza compatibile con il numero di giorni zodiacali in cui quella ricetta è prescritta.

**H-H03 [APERTA — NUOVO] — Hapax zodiacali = ricette su misura (non standard)**
L'80.9% dei token zodiacali è hapax. Non è rumore: ogni preparazione è specifica per quel giorno/contesto stagionale.
*Test*: in eventuali folii zodiacali multipli, se alcune label si ripetono a distanza di esattamente 1 anno, la personalizzazione è stagionale, non giornaliera.

**H-H04 [APERTA — NUOVO] — Densità di label per figura = complessità della ricetta**
Figure zodiacali con 2–3 label vs quelle con 1 label sola: le multi-label corrispondono a ricette più complesse.
*Test*: correlazione numero di label per figura × lunghezza media del token adiacente.

---

### BLOCCO I — Connessione Zodiaco ↔ Stars

**H-I01 [APERTA FORTE — NUOVO] — Stars = indice delle ricette finali**
Stars non è una sezione astronomica — è l'indice dei prodotti finiti. Ogni stella = una ricetta completata con dosaggio. Le stelle caudate marcano le ricette che richiedono strumenti speciali.
*Test*: Stars dovrebbe avere: alta densità -am, bassa densità y-iniziale, alta densità ol/or. Profilo opposto a Pharma.

**H-I02 [APERTA FORTE — NUOVO, P62] — Il Zodiaco come lookup table a fasi multiple**
Le ~365 operazioni zodiacali non corrispondono a 365 ricette Stars indipendenti, ma a 365 fasi di un sottoinsieme di ricette Stars composte. Una singola ricetta Stars ha 2–5 fasi distribuite nell'anno: primavera=macerazione, estate=estrazione, autunno=filtrazione, inverno=conservazione. Il Zodiaco prescrive *quando* e *chi*; Stars descrive *come*. Il Zodiaco ha dipendenze temporali implicite: per produrre la preparazione finale W entro il mese M, certi semilavorati devono essere stati avviati nei mesi precedenti — il che implica una pianificazione industriale multi-mese, non giornaliera.
*Test prioritario*: quando le label zodiacali saranno decifrate, giorni consecutivi con acconciature diverse dovrebbero avere label con radice comune (stessa ricetta, diversa fase).
*Test corpus*: token Stars con prefisso esplicito (k/t/l/s) dovrebbero comparire in cluster temporali compatibili con il calendario zodiacale (inverno=t-, estate=k-, spirito=finale d'anno).

**H-I03 [APERTA — NUOVO] — Il percorso completo di una pianta: Herbal → Pharma → Stars → f85r → Zodiaco**
Una pianta identificata in Herbal dovrebbe comparire come ingrediente in almeno una ricetta Pharma, come operazione in Stars, come dosaggio in f85r, e come assegnazione in almeno un giorno zodiacale.
*Test*: tracciare il percorso cross-sezionale completo per almeno 5 delle 17 piante identificate. Se il percorso è completo per tutte e 5, il sistema integrato è confermato.

---

### BLOCCO L — Il sistema di dosaggi (f85r)

*Questi risultati sono descritti nel Companion. Inclusi qui per completezza della connessione con il sistema zodiacale.*

**H-L01 [APERTA FORTE — vedi Placa 2026b] — Stella = goccia; scala farmacologicamente coerente**
Aceto 8–10 gocce; acqua ~12; olio 12–30 (con moltiplicatore giallo ×2); narghilè/corpo 68 esatte; vapore 80–100. Alcool = veicolo, nessuna dose propria.
*Test aperto*: verificare il numero 68 nella farmacopea araba medievale.

**H-L02 [APERTA — vedi Placa 2026b] — Colore rosone = solvente/via di somministrazione**
*Test*: analisi cromatica sistematica f85r su IIIF.

**H-L03 [APERTA FORTE — vedi Placa 2026b] — Croce blu = gate interazioni olio/alcool**
La croce blu centrale è un divieto: oil-in-alcohol ≠ alcohol-in-oil.
*Test*: densità t-+l- nella stessa riga depleta vs baseline.

---

### BLOCCO M — Agenda di ricerca aperta

Le seguenti domande richiedono competenze o materiali esterni al corpus testuale. Ordinate per priorità: le prime due sono test falsificanti diretti, le ultime due richiedono collaborazione con discipline esterne.

---

**M-04 — `CRITICO` — Conteggio sistematico delle 365 figure**
Il numero preciso (atteso 365, stima attuale: 300+~65) richiede conteggio manuale su IIIF alta risoluzione. È il test più critico dell'intera trilogia: se il conteggio finale è significativamente diverso da 365, H-A01 (SOLIDA) decade e con essa l'intera interpretazione calendriale. Fattibile individualmente con accesso IIIF.

**M-05 — `CRITICO` — Analisi sistematica delle acconciature**
La classificazione di 300 figure (12 folii) in 4 tipi di acconciatura è il test diretto di H-C01 (SOLIDA) e H-C02 (APERTA FORTE). Richiede competenza iconografica medievale. Domanda collaterale: esiste un corpus di confronto per le acconciature femminili nell'Italia settentrionale del XV secolo? Test falsificante: se le acconciature non sono classificabili in 4 tipi sistematici, H-C01 cade.

**M-03 — `ALTA PRIORITÀ` — Analisi multispettrale**
Le correzioni post-hoc (stelle blu nel rosone-acqua di f85r, stelle gialle nel Zodiaco) sono confermabili con infrarosso o UV come strati di pigmento distinti? Esistono analisi multispettrali già eseguite su MS 408? Questo test distingue tra correzione intenzionale (H-F03 APERTA) e variazione di conservazione.

**M-02 — `ALTA PRIORITÀ` — Confronto con farmacopee coeve**
Le combinazioni solvente/pianta di MS 408 corrispondono a formulazioni in Ibn Sīnā, Pseudo-Mesue, al-Zahrāwī? I 17 ingredienti identificati (con alta confidenza: ginepro, elleboro, timo) sono sufficienti per un confronto formale. Un match sistematico eleverebbe significativamente la forza probatoria esterna del modello.

**M-01 — `APERTURA ESTERNA` — Identificazione storica delle autrici**
Una farmacia professionale femminile con sistema di scrittura cifrato in Nord Italia (XV sec.) è storicamente attestata? Documenti notarili, registri corporativi, atti parrocchiali, carteggi corporativi? Questa domanda richiede uno storico del tardo Medioevo italiano specializzato in storia delle corporazioni e della medicina pratica.

*Punto di partenza archivistico (P65, sess.82)*: gli Archivi di Stato di Genova conservano almeno due attestazioni documentate — area del Golfo del Tigullio, arco temporale 1410–1438 — di professioniste della cura riconosciute formalmente dalla Repubblica: esenzioni fiscali concesse per meriti terapeutici, salvacondotti rilasciati dal doge, clientela al più alto livello del patriziato genovese. Fonte primaria: Ferretto (1901), *Giornale Storico e Letterario della Liguria*, pp. 277–296, verificata sul testo originale. La finestra temporale è compatibile con la datazione al radiocarbonio del manoscritto (1404–1438, Beinecke). Queste attestazioni stabiliscono che il *tipo* di operatrice che il modello presuppone esisteva nell'area e nel periodo giusti — non identificano le autrici del manoscritto. L'identificazione delle persone specifiche è l'oggetto di M-01, non la sua risposta, e richiede competenza storiografica indipendente.

---

## Conclusione

Il presente paper completa la trilogia iniziata con i 6 test statistici (Paper 1) e il framework morfologico (Companion). Il contributo originale è la **decodifica sistematica della sezione zodiacale** come sistema iconografico-calendariale a tre livelli.

La forza del modello non è in nessuna singola glossa ma nella **convergenza a quattro tipi di evidenza metodologicamente distinti**: lo stesso quadripolo (4 solventi, 4 operatrici, 4 class markers) appare nel testo morfologico (Paper 1 + Companion), nell'iconografia delle donnine (H-C01–H-C02), nelle figure cardinali di f86v4 (Companion), e nella struttura dei rosoni di f85r (Companion + H-L01–H-L03). Questa convergenza non è spiegabile da sistemi alternativi senza perdere la coerenza interna — ed è la ragione per cui il modello regge come struttura unitaria pur avendo ancora ampia distanza dalla forza probatoria esterna richiesta per una tesi di decifrazione conclusa.

I tre livelli della decodifica zodiacale, che questa convergenza sostiene, sono:

1. **Temporale**: ogni giorno dell'anno ha un'operazione farmaceutica assegnata (H-A01, SOLIDA)
2. **Operativo**: l'acconciatura della donnina identifica l'operatrice in turno e il fonema iniziale della label (H-C01 SOLIDA + H-C02 APERTA FORTE)
3. **Referenziale**: il token o-iniziale della label è l'indirizzo della ricetta corrispondente nella sezione Stars (H-H02, APERTA FORTE)

**Stato delle ipotesi al 29/03/2026 (sessioni 81–86)** — SOLIDE: 41 | STRUTTURA SOLIDA / LETTURA APERTA: 12 | APERTE FORTI: 63 | INDEBOLITA: 1 | FALSIFICATE: 31+. Dettaglio per categoria: `voynich-memory/scorecard/SCORECARD_DETTAGLIATA.md`.

Il programma di ricerca aperto: conteggio sistematico IIIF, analisi multispettrale degli inchiostri, confronto formale con farmacopee arabo-medievali, identificazione storica delle autrici tramite ricerca archivistica indipendente.

*La comunità di ricerca è invitata a contribuire su questi quattro fronti aperti.*

---

**Citation**

```bibtex
@unpublished{Placa2026c,
  author = {Placa, Alessandro},
  title  = {The Pharmacists' Cipher: Grammar, Dictionary,
            and Production Calendar of {MS} 408},
  year   = {2026},
  note   = {Working draft vt1.6. Builds on Placa (2026a, 2026b).},
  url    = {https://github.com/alessandroplaca-uro/voynich-pharmacists-cipher}
}
```

**Riferimenti**

Placa, A. (2026a). *The Pharmacist's Cipher: Six Statistical Tests Supporting a Pharmaceutical Reading of the Voynich Manuscript (MS 408)*. Preprint v1.2. https://doi.org/10.5281/zenodo.19197846

Placa, A. (2026b). *The Pharmacist's Cipher II — A Morphological Framework, Visual-Textual Convergences, and Testable Predictions for MS 408*. Preprint v1.0. https://doi.org/10.5281/zenodo.19228231

---

*Working draft vt1.6 — sess.81-86 — 29/03/2026*
*Workspace: Voynich Manuscript folder — archivio bozza precedente: PAPER_BOZZA_v1.md*
