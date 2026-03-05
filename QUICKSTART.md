# ⚡ Quick Start - 5 Minuti

Segui questi 5 semplici passaggi per avere la tua app online!

---

## Passo 1️⃣: Prepara i file

Hai ricevuto una cartella `java-interactive-course/` con questi file:
- `app.py` (l'app principale)
- `requirements.txt` (dipendenze)
- `README.md` (documentazione)
- `.gitignore` (file da escludere)
- `LICENSE` (licenza MIT)
- `.streamlit/config.toml` (configurazione)
- `SETUP_GUIDE.md` (guida dettagliata)

✅ **Se hai tutti questi file, sei a buon punto!**

---

## Passo 2️⃣: Crea repository su GitHub

1. Vai a https://github.com/new
2. Nome repo: `java-interactive-course`
3. Descrizione: `Interactive Java SE Course`
4. **Seleziona "Public"** (importante!)
5. Clicca "Create repository"

---

## Passo 3️⃣: Carica i file su GitHub

Apri il terminale/PowerShell e digita:

```bash
cd java-interactive-course

git init
git add .
git commit -m "Initial commit: Java Interactive Course"
git branch -M main
git remote add origin https://github.com/TUONOME/java-interactive-course.git
git push -u origin main
```

**⚠️ Sostituisci `TUONOME` con il tuo username GitHub!**

Se chiede username/password: usa il tuo GitHub username e un Personal Access Token (vedi guida)

---

## Passo 4️⃣: Deploy su Streamlit Cloud

1. Vai a https://share.streamlit.io
2. Clicca "Sign in with GitHub" e accedi
3. Clicca "New app"
4. Scegli:
   - Repository: `TUONOME/java-interactive-course`
   - Branch: `main`
   - Main file: `app.py`
5. Clicca "Deploy"

Aspetta 1-2 minuti... ⏳

---

## Passo 5️⃣: La tua app è online! 🎉

Vedrai un link come:
```
https://tuonome-java-interactive-course.streamlit.app
```

**Clicca e aprila!** L'app è adesso visibile a tutti!

---

## 📱 Condividi il link

Puoi condividere l'URL con:
- 👥 Studenti
- 📧 Email
- 🐦 Social media
- 📚 Siti web
- 📲 QR code (genera da https://qrcode.com)

---

## 🚀 Come aggiornare l'app

Quando vuoi aggiungere lezioni o esercizi:

```bash
# Modifica i file localmente (es: app.py)
git add .
git commit -m "Add module 2 content"
git push
```

L'app si aggiornerà automaticamente in 10-30 secondi!

---

## ❓ Se qualcosa non funziona

1. Verifica che il repository sia **Public** (non Private)
2. Controlla che il branch sia **main** (non master)
3. Verifica che `app.py` sia nella **root folder** (non in una sottocartella)
4. Controlla i **logs** in Streamlit Cloud (clicca l'app → Manage app → View logs)

Se hai problemi, leggi `SETUP_GUIDE.md` per una guida dettagliata.

---

## 📚 Cosa contiene l'app

✅ **11 Moduli** (44 ore di contenuto)
✅ **Lezioni teoriche** con spiegazioni
✅ **Esempi in Python** per ogni concetto Java
✅ **3 tipi di esercizi** per modulo (Multiple Choice, Coding, Vero/Falso)
✅ **Dashboard** con tracking del progresso
✅ **Design moderno** con dark theme

---

## 💡 Prossimi Step

1. **Aggiungi più lezioni** - Modifica `COURSE_MODULES` in `app.py`
2. **Migliora gli esercizi** - Aggiungi più domande e sfide di coding
3. **Personalizza i colori** - Cambia il tema nello `<style>` del CSS
4. **Invita gli studenti** - Condividi il link della tua app

---

## 📖 Documentazione

- **SETUP_GUIDE.md** - Guida dettagliata completa
- **README.md** - Documentazione completa dell'app
- **app.py** - Codice commentato dell'applicazione

---

**Versione**: 1.0  
**Data**: Marzo 2024

🎉 **Sei pronto! Buona fortuna!** 🚀
