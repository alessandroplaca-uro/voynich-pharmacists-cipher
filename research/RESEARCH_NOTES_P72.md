# RESEARCH NOTES — P72: Gallows come Parti della Pianta

**Status**: APERTA FORTE
**Data**: 30 marzo 2026 (sess.91)
**Ipotesi**: Le quattro lettere-variabile K, P, T, F codificano la **parte anatomica della pianta** di riferimento nella ricetta, non solo il percorso procedurale astratto (P70 rimane valida e complementare).

---

## Ipotesi

Le gallows K, P, T, F — oltre ad essere diagrammi di percorso procedurale sulla rosetta 3×3 (P70) — codificano la **parte anatomica di origine** del materiale trattato:

| Lettera | Corner rosetta | Stato fisico | Parte pianta | Metodo tradizionale |
|---------|----------------|--------------|--------------|---------------------|
| **P** | SW (essiccatura) | freddo+secco | Radici essiccate | Essiccatura + polverizzazione |
| **K** | NE (vapore) | caldo+umido | Fiori | Estrazione a vapore (aromi volatili) |
| **T** | SE (macerazione) | caldo+fluido | Foglie | Macerazione alcolica/oleosa |
| **F** | NW (filtrazione) | freddo+umido→solido | Frutti | Conservazione sott'aceto |

**Coerenza fisica corner ↔ parte**: ogni associazione è farmacologicamente coerente con la pratica medievale:
- SW (freddo+secco) → radici: le radici si essiccano e polverizzano (shelf life lunga, principi attivi concentrati)
- NE (vapore) → fiori: l'estrazione aromatica per vapore preserva i composti volatili tipici dei fiori
- SE (macerazione caldo+fluido) → foglie: i principi attivi fogliari si estraggono per macerazione in olio o alcool
- NW (freddo+aceto) → frutti: la conservazione acetica è il metodo medievale per i frutti

---

## Evidenza corpus (test confermato sess.91)

### Test di macerazione split (Fisher's exact test)

Il test chiave è sulla distribuzione di `-edy` (morfema di macerazione, Serie B verbale) tra le lettere che codificano parti che macèrano (P=radici, T=foglie) vs parti che non macèrano (K=fiori, F=frutti):

| Gruppo | -edy% nel body text |
|--------|---------------------|
| P + T (radici + foglie) | **7.2%** |
| K + F (fiori + frutti) | **0.97%** |

**OR = 7.97, p = 6.92e-10** (Fisher's exact test)

Interpretazione biologica: radici e foglie cedono principi attivi per macerazione (processo lento, temperatura controllata, tipico del Balneo). Fiori e frutti non: i fiori si estraggono per vapore/calore rapido, i frutti si conservano per acidificazione.

### Distribuzione opener Herbal (corpus, 112 paragrafi)

| Lettera | % paragrafi Herbal | Note |
|---------|---------------------|------|
| P | 46.4% | Dominante — radici = parte principale negli erbari medievali |
| K | 18.8% | — |
| T | 18.8% | — |
| F | 8.0% | — |
| Compound/altro | 8.0% | — |

P domina perché le radici sono la parte farmacologicamente più importante e longeva degli erbari medievali (shelf life, concentrazione principi attivi).

### Profili strutturali body text per lettera (evidenza sistematica)

| Lettera | ch% body | sh% body | -edy% | -dy% | Profilo dominante |
|---------|----------|----------|-------|------|-------------------|
| K | 40% (max) | bassa | bassa | — | Hot-dominant (vapore) ✓ coerente con fiori |
| P | media | media | ≈-ey | — | Complesso misto ✓ coerente con radici (processi multipli) |
| T | media | media | — | alta | -dy dominante ✓ coerente con foglie (produzione oleosa) |
| F | bassa | 17% (max) | ~0 (assente) | — | Cold-dominant, zero macerazione ✓ coerente con frutti sott'aceto |

F-body ha il massimo sh% (freddo) e zero macerazione — esattamente quello che si attende da un corpus di conservazione acetica a freddo.

---

## Prima traduzione sperimentale a supporto (f14r)

Folio f14r apre con **pch** (P = radici, ch = elaborazione calda):

- `okcheey . okcheey . okcheey` = tre ripetizioni di "scalda abbondantemente in acqua"
- `ar` = il pressato
- `s` = acidifica con aceto

Struttura = **mathbūkh concentrato**: essiccato → bollito tre volte → pressato → acidificato.

La tripla bollitura (`okcheey ×3`) è la firma del concentrato arabo medievale. Il folio P si apre con una radice essiccata che viene lavorata con il processo più intensivo dell'erbario — coerente con P72 (radici = P = SW = essiccatura come passo di base, poi elaborazione calda).

~50% leggibilità totale. La struttura regge attraverso i token ancora opachi.

---

## Relazione con P70 (complementarità, non sostituzione)

P72 non sostituisce P70 — le due ipotesi operano su livelli di significato distinti:

- **P70**: le gallows sono **diagrammi di percorso** sulla rosetta 3×3. Il glifo descrive la *sequenza di trasformazioni fisiche* che la materia attraversa. È un'informazione procedurale.
- **P72**: le lettere codificano anche la **parte anatomica di origine**. È un'informazione botanica.

Le due letture sono compatibili perché il percorso procedurale ottimale per ogni parte della pianta è fisicamente determinato dalla sua composizione chimica:
- Radici (P): essiccatura obbligatoria → SW è il corner corretto
- Fiori (K): vapore per preservare aromi volatili → NE è il corner corretto
- Foglie (T): macerazione alcolica/oleosa → SE è il corner corretto
- Frutti (F): acidificazione conservativa → NW (filtrazione/cristallizzazione fredda) è il corner corretto

In pratica: il percorso procedurale (P70) *è* il metodo ottimale per quella parte (P72). Le due ipotesi si co-implicano.

---

## Nomenclatura operativa

**REGOLA OBBLIGATORIA**: K, P, T, F sono **lettere-variabile**, non classi farmacologiche. MAI scrivere "k-class", "p-family", "T-class" o simili nella documentazione del paper. Usare solo la lettera maiuscola.

---

## Test di falsificazione

### Test primario (IIIF iconografico — non ancora eseguito)
**Predizione**: nei folii Herbal, la parte botanica più prominente nell'illustrazione dovrebbe corrispondere alla lettera-opener del testo:
- Folii P-opener → radici prominenti nell'illustrazione
- Folii K-opener → fiori prominenti
- Folii T-opener → foglie prominenti
- Folii F-opener → frutti/bacche prominenti

Questo test è il più diretto ed è fattibile via Yale IIIF (`https://collections.library.yale.edu/manifests/2002046`).

### Test secondario (corpus alternativo)
P72 è falsificata se:
- La distribuzione -edy tra P+T vs K+F non è significativa su trascrizioni alternative (Zandbergen, FSG)
- I profili ch/sh per lettera non replicano su trascrizioni alternative
- Folii iconograficamente verificati mostrano la parte sbagliata rispetto alla predizione

### Test terziario (cross-sezione)
Se K=fiori, allora nei folii K-opener di Stars o Pharma (dove ci sono preparazioni a base di fiori) il profilo dovrebbe mostrare dominanza dei processi volatili (distillazione, vapore) rispetto ai folii P-opener.

---

## Stato attuale e next steps

**Corpus**: evidenza solida (OR=7.97, p=6.92e-10 per test macerazione split). Profili strutturali sistematicamente coerenti per tutte e 4 le lettere.

**Iconografia**: non ancora verificata — è il test critico che può elevare P72 a SOLIDA o falsificarla.

**Next step immediato**: aprire Yale IIIF e verificare 10-15 folii Herbal, annotando la parte botanica prominente nell'illustrazione vs la lettera-opener del testo.

**Implicazione per il paper**: se P72 viene confermata iconograficamente, il sistema di codifica delle gallows diventa tri-livello:
1. Il glifo come **percorso procedurale** (P70)
2. La lettera come **parte anatomica di origine** (P72)
3. I suffissi e modificatori come **parametri di esecuzione**

Questo è un sistema di encoding di straordinaria complessità e praticità per un manuale farmaceutico professionale.