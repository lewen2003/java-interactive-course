# 📖 Guida Completa: Setup e Deployment

## 🎯 Obiettivo
Deployare l'applicazione Java Interactive Course su Streamlit Cloud gratuitamente e condividerla.

---

## 📋 Prerequisiti

- ✅ Account GitHub (gratuito): https://github.com/signup
- ✅ Account Streamlit Cloud (gratuito): https://share.streamlit.io
- ✅ Git installato sulla tua macchina
- ✅ Python 3.8+ (puoi verificare con `python --version`)

---

## 🚀 Passo 1: Preparare il Progetto Localmente

### 1.1 Crea la cartella del progetto

```bash
# Crea una cartella
mkdir java-interactive-course
cd java-interactive-course

# Inizializza git
git init
```

### 1.2 Aggiungi i file

Copia questi file nella cartella:
- `app.py` (il file principale dell'app)
- `requirements.txt` (dipendenze)
- `README.md` (documentazione)
- `.gitignore` (file da escludere)
- `LICENSE` (licenza MIT)

Crea la cartella `.streamlit/` e aggiungi:
- `config.toml` (configurazione Streamlit)

La struttura dovrebbe essere:

```
java-interactive-course/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── .streamlit/
    └── config.toml
```

### 1.3 Prova localmente (opzionale ma consigliato)

```bash
# Installa le dipendenze
pip install -r requirements.txt

# Avvia l'app
streamlit run app.py
```

Apri il browser a `http://localhost:8501` e testa l'app.

---

## 🔗 Passo 2: Carica su GitHub

### 2.1 Crea un repository su GitHub

1. Vai a https://github.com/new
2. Inserisci il nome: `java-interactive-course`
3. Descrizione: "Interactive Java SE Course with Streamlit"
4. Seleziona "Public" (obbligatorio per Streamlit Cloud gratuito)
5. **NON** aggiungere README (lo hai già)
6. Clicca "Create repository"

### 2.2 Carica i file su GitHub

```bash
# Dalla cartella del progetto
git add .
git commit -m "Initial commit: Java Interactive Course"
git branch -M main
git remote add origin https://github.com/TUONOME/java-interactive-course.git
git push -u origin main
```

**Sostituisci `TUONOME`** con il tuo username GitHub.

Se chiede credenziali:
- Per nome utente: il tuo username GitHub
- Per password: un "Personal Access Token" (guarda il Passo 2.3)

### 2.3 (Se necessario) Genera Personal Access Token

Se Git chiede credenziali:

1. Vai a https://github.com/settings/tokens
2. Clicca "Generate new token" → "Generate new token (classic)"
3. Dai un nome: "GitHub Push Token"
4. Seleziona scope: `repo` (leggi/scrivi repository)
5. Clicca "Generate token"
6. **Copia il token** (non potrai vederlo di nuovo!)
7. Usalo come password quando Git lo chiede

---

## 🌐 Passo 3: Deploy su Streamlit Cloud

### 3.1 Accedi a Streamlit Cloud

1. Vai a https://share.streamlit.io
2. Clicca "Sign in with GitHub"
3. Autorizza Streamlit a accedere ai tuoi repository

### 3.2 Crea una nuova app

1. Clicca su "New app" (in alto a destra)
2. Seleziona le opzioni:
   - **Repository**: `TUONOME/java-interactive-course`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. Clicca "Deploy"

### 3.3 Attendi il deploy

- Streamlit builderà l'app (circa 1-2 minuti)
- Vedrai i log del build in tempo reale
- Una volta completato, vedrai l'app live!

**L'URL della tua app sarà**: `https://tuonome-java-interactive-course.streamlit.app`

---

## ✅ Verifiche Post-Deploy

1. **Accedi all'app** dal link fornito
2. **Testa le funzionalità**:
   - Clicca su moduli diversi nella sidebar
   - Prova gli esercizi (Multiple Choice, Coding, Vero/Falso)
   - Verifica che il punteggio aumenti
   - Testa il reset del corso

3. **Se c'è un errore**:
   - Controlla i log in Streamlit Cloud (clicca su "Manage app" → "View logs")
   - Verifica che `requirements.txt` sia corretto
   - Controlla che `app.py` non abbia errori di sintassi

---

## 🔄 Come Fare Aggiornamenti

Quando vuoi aggiungere nuove lezioni o esercizi:

### Metodo 1: Via Git (consigliato)

```bash
# Modifica i file localmente
# Es: edit app.py per aggiungere nuove lezioni

# Carica i cambiamenti
git add .
git commit -m "Add new lessons: Module 2 content"
git push
```

Streamlit aggiornerà automaticamente l'app live in pochi secondi!

### Metodo 2: Direttamente su GitHub

1. Vai al tuo repository su GitHub
2. Clicca su un file per modificarlo
3. Clicca il pulsante ✏️ (edit)
4. Fai le modifiche
5. Clicca "Commit changes"
6. Streamlit si aggiornerà automaticamente

---

## 🎨 Personalizzazione

### Cambiare il tema colori

Nel file `app.py`, modifica questa sezione:

```python
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);  /* Cambia questi colori */
        ...
    }
</style>
""", unsafe_allow_html=True)
```

### Aggiungere nuove lezioni

Nel file `app.py`, trova `COURSE_MODULES` e aggiungi un nuovo modulo:

```python
{
    "id": 12,
    "title": "Nuovo Argomento",
    "hours": 4,
    "description": "Descrizione del modulo",
    "lessons": [
        {
            "title": "Lezione 1",
            "content": "Contenuto della lezione con codice, spiegazioni, ecc."
        }
    ]
}
```

### Aggiungere nuovi esercizi

Modifica le funzioni:
- `show_multiple_choice()` - Aggiungi domande nel dizionario `questions`
- `show_coding_challenge()` - Aggiungi sfide nel dizionario `challenges`
- `show_true_false()` - Aggiungi affermazioni nel dizionario `statements`

---

## 📊 Monitorare l'Utilizzo

Nel dashboard di Streamlit Cloud (https://share.streamlit.io):

1. Seleziona la tua app
2. Clicca su "Manage app"
3. Visualizza:
   - **Usage**: quante persone stanno usando l'app
   - **Logs**: errori e messaggi di debug
   - **Settings**: configura secrets, timeout, ecc.

---

## 🔐 Secrets e Variabili d'Ambiente (Se necessario)

Se in futuro aggiungerai API keys o database:

1. Nella app su Streamlit Cloud, clicca "Manage app"
2. Clicca "Secrets"
3. Aggiungi le variabili nel formato TOML:

```toml
OPENAI_API_KEY = "sk-..."
DATABASE_URL = "postgresql://..."
```

Nel tuo `app.py` accedi con:

```python
api_key = st.secrets["OPENAI_API_KEY"]
```

---

## 🆘 Troubleshooting

### Errore: "App file not found"
- Verifica che `app.py` sia nella cartella root del repository

### Errore: "ModuleNotFoundError"
- Verifica che tutte le importazioni di `app.py` siano in `requirements.txt`
- Aggiorna: `pip freeze > requirements.txt`

### L'app è lenta
- Streamlit Cloud ha risorse gratuite limitate
- Ottimizza caricamento dati, evita loop pesanti
- Usa `@st.cache_data` per cachare dati

### Non vedo gli aggiornamenti
- Aspetta 30 secondi dopo il push (tempo di build)
- Fai refresh della pagina browser (Ctrl+Shift+R)
- Controlla i logs di Streamlit Cloud

---

## 📈 Prossimi Step

1. **Aggiungi più lezioni** - Completa tutti i 11 moduli
2. **Migliora gli esercizi** - Valida il codice Java più rigorosamente
3. **Aggiungi database** - Salva i progressi degli utenti
4. **Integra forum** - Permetti agli studenti di fare domande
5. **Certificati** - Genera certificati di completamento
6. **Mobile App** - Usa Streamlit per creare una versione mobile

---

## 📞 Supporto Ulteriore

- **Documentazione Streamlit**: https://docs.streamlit.io
- **GitHub Docs**: https://docs.github.com
- **Python Package Index**: https://pypi.org
- **Stack Overflow**: Tag con `streamlit` e `python`

---

**Ultimo aggiornamento**: Marzo 2024  
**Versione**: 1.0

Buona fortuna con il tuo corso! 🚀
