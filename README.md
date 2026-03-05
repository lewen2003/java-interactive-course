# ☕ Java SE Interactive Course

Un'applicazione web interattiva per imparare Java SE dai concetti intermedi agli argomenti avanzati, con lezioni teoriche, esempi comparativi con Python, e esercitazioni variegate.

![Java SE](https://img.shields.io/badge/Java-SE%2017-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 📚 Caratteristiche

✅ **11 Moduli Progressivi** (44 ore di contenuto)
- Tipi di Dati e Operatori
- Controllo di Flusso
- Array e Stringhe
- Oggetti e Classi (OOP)
- Eccezioni
- Collections Framework
- Input/Output e Stream
- Java Time API
- Generics
- Lambda Expressions
- Design Pattern

✅ **Esercitazioni Interattive per Modulo**
- 📝 Esercizi Multiple Choice con feedback immediato
- 💻 Coding Challenges con validazione del codice
- ✓ Esercizi Vero/Falso con spiegazioni dettagliate

✅ **Esempi Comparativi**
- Ogni concetto Java ha un equivalente Python per chiarire le differenze
- Aiuta a comprendere meglio le peculiarità di Java

✅ **Tracking dei Progressi**
- Visualizzazione in tempo reale del progresso
- Punteggio cumulativo
- Moduli marcati come completati

✅ **Design Moderno**
- Interfaccia dark theme elegante
- Responsive e intuitiva
- Navigazione facile tra i moduli

## 🚀 Quick Start

### Opzione 1: Local Development

```bash
# 1. Clona il repository
git clone https://github.com/tuonome/java-interactive-course.git
cd java-interactive-course

# 2. Crea un virtual environment
python -m venv venv
source venv/bin/activate  # su Windows: venv\Scripts\activate

# 3. Installa le dipendenze
pip install -r requirements.txt

# 4. Avvia l'app
streamlit run app.py
```

L'app si aprirà automaticamente su `http://localhost:8501`

### Opzione 2: Deploy su Streamlit Cloud 

#### Prerequisiti
- Account GitHub
- Account Streamlit Cloud (gratuito)

#### Passaggi

1. **Crea un repository GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Java Interactive Course"
   git branch -M main
   git remote add origin https://github.com/tuonome/java-interactive-course.git
   git push -u origin main
   ```

2. **Accedi a Streamlit Cloud**
   - Vai a https://share.streamlit.io
   - Fai login con il tuo account GitHub
   - Clicca su "New App"

3. **Configura il Deploy**
   - Repository: seleziona il tuo repository
   - Branch: `main`
   - File path: `app.py`
   - Clicca "Deploy"

4. **La tua app sarà online!**
   - L'URL sarà qualcosa come: `https://tuonome-java-course.streamlit.app`

## 📁 Struttura del Progetto

```
java-interactive-course/
│
├── app.py                          # App principale Streamlit
├── requirements.txt               # Dipendenze Python
├── README.md                      # Questo file
├── .streamlit/
│   └── config.toml               # Configurazione Streamlit
└── .gitignore                    # File da escludere da Git
```

## 🛠️ Tecnologie Utilizzate

- **Streamlit** (1.28.1): Framework per web apps Python
- **Python** (3.8+): Linguaggio di programmazione
- **HTML/CSS**: Styling personalizzato

## 📖 Come Usare il Corso

1. **Inizia il corso** cliccando il pulsante sulla home
2. **Studia la lezione** nel tab "Lezione" di ogni modulo
3. **Completa gli esercizi**:
   - Multiple Choice: verifica la tua comprensione teorica
   - Coding Challenge: implementa il codice Java
   - Vero/Falso: consolida i concetti
4. **Naviga tra i moduli** usando i pulsanti o la sidebar
5. **Traccia il tuo progresso** nel dashboard sulla sinistra

## 🎯 Obiettivi di Apprendimento

Dopo completare questo corso, sarai in grado di:

- ✅ Comprendere e utilizzare tutti i tipi di dati Java
- ✅ Controllare il flusso di esecuzione con condizioni e cicli
- ✅ Lavorare con array e stringhe efficacemente
- ✅ Progettare e implementare classi con OOP
- ✅ Gestire le eccezioni correttamente
- ✅ Utilizzare Collections Framework
- ✅ Leggere/scrivere file e stream
- ✅ Lavorare con date e ore
- ✅ Usare Generics e Lambda expressions
- ✅ Implementare design pattern comuni

## 🔧 Customizzazione

### Aggiungere più lezioni
Modifica il dizionario `COURSE_MODULES` in `app.py` per aggiungere nuove lezioni ai moduli.

### Modificare il tema
I colori e lo stile sono definiti nel blocco `<style>` in `app.py`. Modifica i valori per personalizzare.

### Aggiungere nuovi esercizi
Estendi i dizionari nelle funzioni `show_multiple_choice()`, `show_coding_challenge()`, e `show_true_false()`.

## 📊 Funzionalità Future

- [ ] Quiz multipli per ogni modulo
- [ ] Certificato di completamento
- [ ] Sistema di badge/achievement
- [ ] Glossario terminologico
- [ ] Forum di discussione
- [ ] Integrazione con IDE online (repl.it, ideone)
- [ ] Soluzioni videonumerate
- [ ] Esercizi di gruppo/collaborativi

## 🐛 Bug Report

Se trovi un bug, per favore apri un [Issue su GitHub](https://github.com/tuonome/java-interactive-course/issues).

Includi:
- Descrizione del problema
- Passaggi per riprodurlo
- Screenshot (se applicabile)
- Versione di Python e Streamlit

## 🤝 Contributi

I contributi sono benvenuti! Se vuoi aiutare a migliorare il corso:

1. Fork il repository
2. Crea un branch per la tua feature (`git checkout -b feature/nuova-lezione`)
3. Commit i tuoi cambiamenti (`git commit -m 'Add nuova lezione su Topic X'`)
4. Push al branch (`git push origin feature/nuova-lezione`)
5. Apri una Pull Request



**Versione:** 1.0.0  
**Ultimo aggiornamento:** Marzo 2024  
**Status:** ✅ In Sviluppo Attivo

### ⭐ Se questo progetto ti è stato utile, considerano di lasciare una stella! ⭐
