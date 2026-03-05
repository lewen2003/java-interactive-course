import streamlit as st
import json
from datetime import datetime
from typing import Dict, List, Optional
import random

# ==================== CONFIG ====================
st.set_page_config(
    page_title="Java SE Course - Interactive",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com",
        "Report a bug": "https://github.com",
        "About": "# Java SE Interactive Course\n\nCorso Java avanzato con esercitazioni interattive"
    }
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #e2e8f0;
    }
    
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.95);
        border-right: 2px solid #0ea5e9;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background-color: rgba(30, 41, 59, 0.8);
        border-radius: 10px;
        padding: 5px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(51, 65, 85, 0.6);
        border-radius: 8px;
        color: #cbd5e1;
        padding: 12px 20px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0ea5e9, #06b6d4);
        color: white;
        font-weight: 600;
    }
    
    .metric-box {
        background: rgba(51, 65, 85, 0.8);
        padding: 20px;
        border-radius: 12px;
        border-left: 4px solid #0ea5e9;
        margin: 10px 0;
    }
    
    .lesson-box {
        background: rgba(30, 41, 59, 0.9);
        padding: 25px;
        border-radius: 12px;
        border: 1px solid rgba(14, 165, 233, 0.3);
        margin: 15px 0;
        line-height: 1.8;
    }
    
    .exercise-box {
        background: rgba(51, 65, 85, 0.7);
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #10b981;
        margin: 15px 0;
    }
    
    .success-box {
        background: rgba(16, 185, 129, 0.2);
        border-left: 4px solid #10b981;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    .error-box {
        background: rgba(239, 68, 68, 0.2);
        border-left: 4px solid #ef4444;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    .hint-box {
        background: rgba(59, 130, 246, 0.2);
        border-left: 4px solid #3b82f6;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    .code-block {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid #0ea5e9;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        font-family: 'Courier New', monospace;
        font-size: 13px;
        overflow-x: auto;
    }
    
    h1, h2, h3 {
        color: #f1f5f9;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    
    h1 {
        font-size: 2.5em;
        background: linear-gradient(135deg, #0ea5e9, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    h2 {
        font-size: 1.8em;
        border-bottom: 2px solid #0ea5e9;
        padding-bottom: 10px;
    }
    
    h3 {
        font-size: 1.3em;
        color: #0ea5e9;
    }
    
    button {
        background: linear-gradient(135deg, #0ea5e9, #06b6d4) !important;
        border: none !important;
        border-radius: 8px !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 10px 20px !important;
        transition: all 0.3s ease !important;
    }
    
    button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 16px rgba(14, 165, 233, 0.4) !important;
    }
    
    .stRadio > label {
        color: #e2e8f0;
        font-weight: 500;
    }
    
    .stCheckbox > label {
        color: #e2e8f0;
        font-weight: 500;
    }
    
    .stTextInput > label {
        color: #e2e8f0;
    }
    
    .progress-bar {
        background: rgba(51, 65, 85, 0.8);
        border-radius: 20px;
        height: 10px;
        margin: 10px 0;
        overflow: hidden;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #0ea5e9, #06b6d4);
        height: 100%;
        transition: width 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# ==================== INITIALIZATION ====================
if "course_state" not in st.session_state:
    st.session_state.course_state = {
        "current_module": 0,
        "modules_completed": {},
        "exercises_completed": {},
        "score": 0,
        "started": False,
        "current_exercise_level": 1
    }

# ==================== COURSE DATA ====================
COURSE_MODULES = [
    {
        "id": 1,
        "title": "Tipi di Dati e Operatori",
        "hours": 3,
        "description": "Comprensione dei tipi di dati primitivi e non primitivi, operatori aritmetici, di confronto e logici.",
        "lessons": [
            {
                "title": "Tipi di Dati Primitivi",
                "content": """
I tipi di dati primitivi in Java sono i fondamenti del linguaggio. Rappresentano valori semplici memorizzati direttamente in memoria.

**Tipi principali:**
- `byte`: 8 bit, range -128 a 127
- `short`: 16 bit, range -32,768 a 32,767
- `int`: 32 bit, range -2,147,483,648 a 2,147,483,647
- `long`: 64 bit, per numeri molto grandi
- `float`: 32 bit, per decimali (meno preciso)
- `double`: 64 bit, per decimali (più preciso)
- `boolean`: true o false
- `char`: singolo carattere Unicode

**Esempio Java:**
```java
int age = 25;
double salary = 2500.50;
boolean isActive = true;
char grade = 'A';
```

**Equivalente in Python:**
In Python non hai tipi primitivi distinti - Python inferne automaticamente il tipo:
```python
age = 25           # int
salary = 2500.50   # float
is_active = True   # bool
grade = 'A'        # str
```

**Differenza chiave:** Java richiede la dichiarazione esplicita del tipo per sicurezza e performance.
"""
            },
            {
                "title": "Operatori Aritmetici e di Confronto",
                "content": """
Gli operatori permettono di eseguire operazioni sui dati.

**Operatori Aritmetici:**
```java
int a = 10, b = 3;
a + b  // 13
a - b  // 7
a * b  // 30
a / b  // 3 (divisione intera)
a % b  // 1 (modulo/resto)
```

**Operatori di Confronto:**
```java
a == b   // false
a != b   // true
a > b    // true
a < b    // false
a >= b   // true
a <= b   // false
```

**Operatori Logici:**
```java
true && false  // false (AND)
true || false  // true (OR)
!true          // false (NOT)
```

**In Python:**
```python
a, b = 10, 3
a + b       # 13
a // b      # 3 (divisione intera)
a % b       # 1 (modulo)
a == b      # False
a and b     # 0 (comportamento diverso)
```

**Best Practice:** Usa sempre nomi significativi per le variabili e commenta il codice complesso.
"""
            }
        ]
    },
    {
        "id": 2,
        "title": "Controllo di Flusso",
        "hours": 4,
        "description": "Condizioni if/else, cicli while, do-while, for. Controllo del flusso di esecuzione.",
        "lessons": [
            {
                "title": "Cicli e Condizioni",
                "content": "Contenuto del modulo 2..."
            }
        ]
    },
    {
        "id": 3,
        "title": "Array e Stringhe",
        "hours": 4,
        "description": "Dichiarazione e utilizzo degli array, manipolazione di stringhe e metodi associati.",
        "lessons": [
            {
                "title": "Array in Java",
                "content": "Contenuto del modulo 3..."
            }
        ]
    },
    {
        "id": 4,
        "title": "Oggetti e Classi",
        "hours": 8,
        "description": "OOP: classi, oggetti, ereditarietà, polimorfismo, incapsulamento, interfacce.",
        "lessons": [
            {
                "title": "Fondamenti OOP",
                "content": "Contenuto del modulo 4..."
            }
        ]
    },
    {
        "id": 5,
        "title": "Eccezioni",
        "hours": 4,
        "description": "Gestione delle eccezioni, try-catch-finally, throw, throws, custom exceptions.",
        "lessons": [
            {
                "title": "Exception Handling",
                "content": "Contenuto del modulo 5..."
            }
        ]
    },
    {
        "id": 6,
        "title": "Collections Framework",
        "hours": 4,
        "description": "ArrayList, LinkedList, HashSet, HashMap, TreeMap, Queue.",
        "lessons": [
            {
                "title": "Collections",
                "content": "Contenuto del modulo 6..."
            }
        ]
    },
    {
        "id": 7,
        "title": "Input/Output e Stream",
        "hours": 4,
        "description": "Lettura/scrittura file, stream, serializzazione degli oggetti.",
        "lessons": [
            {
                "title": "I/O e Stream",
                "content": "Contenuto del modulo 7..."
            }
        ]
    },
    {
        "id": 8,
        "title": "Java Time API",
        "hours": 2,
        "description": "LocalDate, LocalTime, LocalDateTime, ZonedDateTime, Period, Duration.",
        "lessons": [
            {
                "title": "Time API",
                "content": "Contenuto del modulo 8..."
            }
        ]
    },
    {
        "id": 9,
        "title": "Generics",
        "hours": 4,
        "description": "Classi generiche, interfacce generiche, wildcards, bounded types.",
        "lessons": [
            {
                "title": "Generics",
                "content": "Contenuto del modulo 9..."
            }
        ]
    },
    {
        "id": 10,
        "title": "Lambda",
        "hours": 4,
        "description": "Lambda expressions, functional interfaces, metodi di riferimento.",
        "lessons": [
            {
                "title": "Lambda Expressions",
                "content": "Contenuto del modulo 10..."
            }
        ]
    },
    {
        "id": 11,
        "title": "Design Pattern",
        "hours": 4,
        "description": "Singleton, Factory, Observer, Adapter, Facade pattern.",
        "lessons": [
            {
                "title": "Design Pattern",
                "content": "Contenuto del modulo 11..."
            }
        ]
    }
]

# ==================== EXERCISE FUNCTIONS ====================
def show_multiple_choice(module_id: int, question_num: int):
    """Mostra esercizio multiple choice"""
    st.markdown(f"### 📝 Esercizio Multiple Choice #{question_num}")
    
    questions = {
        1: {
            "q": "Quale tipo di dato occupa 32 bit e può contenere numeri interi?",
            "options": ["byte", "int", "long", "short"],
            "correct": 1,
            "explanation": "int occupa 32 bit ed è il tipo standard per interi. byte=8bit, short=16bit, long=64bit."
        },
        2: {
            "q": "Cosa restituisce l'operatore % (modulo)?",
            "options": ["La divisione intera", "Il resto della divisione", "La moltiplicazione", "La potenza"],
            "correct": 1,
            "explanation": "L'operatore % restituisce il resto della divisione. Es: 10 % 3 = 1"
        }
    }
    
    q = questions.get(question_num, questions[1])
    
    response = st.radio(
        q["q"],
        q["options"],
        key=f"mc_q{question_num}"
    )
    
    if st.button("Verifica Risposta", key=f"mc_btn_{question_num}"):
        if q["options"].index(response) == q["correct"]:
            st.markdown(f"""
            <div class="success-box">
            <strong>✅ Corretto!</strong><br>
            {q["explanation"]}
            </div>
            """, unsafe_allow_html=True)
            return True
        else:
            st.markdown(f"""
            <div class="error-box">
            <strong>❌ Sbagliato</strong><br>
            Risposta corretta: {q["options"][q["correct"]]}<br>
            {q["explanation"]}
            </div>
            """, unsafe_allow_html=True)
            return False

def show_coding_challenge(module_id: int, level: int = 1):
    """Mostra coding challenge"""
    st.markdown(f"### 💻 Coding Challenge - Livello {level}")
    
    challenges = {
        1: {
            1: {
                "description": "Scrivi un programma che dichiari tre variabili (int, double, boolean) e le stampi in console.",
                "template": """public class TypeDeclaration {
    public static void main(String[] args) {
        // Dichiara le tre variabili qui
        
        // Stampa le variabili
        
    }
}""",
                "solution_check": ["int", "double", "boolean", "println"],
                "explanation": "Hai correttamente dichiarato i tipi di dati primitivi!"
            },
            2: {
                "description": "Scrivi un programma che calcoli il resto della divisione tra 17 e 5 usando l'operatore modulo.",
                "template": """public class ModuloChallenge {
    public static void main(String[] args) {
        int a = 17;
        int b = 5;
        // Calcola il modulo e stampa il risultato
        
    }
}""",
                "solution_check": ["%", "println", "2"],
                "explanation": "Perfetto! 17 % 5 = 2"
            }
        }
    }
    
    challenge = challenges.get(module_id, {}).get(level, challenges[1][1])
    
    st.markdown(f"**Descrizione:**\n{challenge['description']}")
    
    with st.expander("📋 Template Codice"):
        st.markdown(f"```java\n{challenge['template']}\n```")
    
    code_input = st.text_area(
        "Scrivi il tuo codice qui:",
        height=200,
        key=f"code_challenge_{module_id}_{level}"
    )
    
    if st.button("Verifica Soluzione", key=f"code_btn_{module_id}_{level}"):
        # Simple check - in production sarebbe più robusto
        checks_passed = sum(1 for check in challenge['solution_check'] if check.lower() in code_input.lower())
        
        if checks_passed >= len(challenge['solution_check']) * 0.7:
            st.markdown(f"""
            <div class="success-box">
            <strong>✅ Soluzione Accettata!</strong><br>
            {challenge['explanation']}<br><br>
            <em>Prova ora la versione più difficile del livello {level + 1}</em>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"→ Prossimo Livello Coding (Livello {level + 1})", key=f"next_level_{module_id}"):
                st.session_state.course_state["current_exercise_level"] = level + 1
                st.rerun()
            
            return True
        else:
            st.markdown(f"""
            <div class="error-box">
            <strong>⚠️ Soluzione Incompleta</strong><br>
            Suggerimento: Assicurati di includere tutti gli elementi richiesti.<br>
            Riprova o consulta la teoria.
            </div>
            """, unsafe_allow_html=True)
            return False

def show_true_false(module_id: int, question_num: int = 1):
    """Mostra esercizio vero/falso"""
    st.markdown(f"### ✓/✗ Vero o Falso #{question_num}")
    
    statements = {
        1: [
            {
                "statement": "Il tipo `long` occupa 64 bit ed è più grande di `int`",
                "correct": True,
                "explanation": "Corretto. `long` usa 64 bit mentre `int` usa 32 bit, permettendo di memorizzare numeri molto più grandi."
            },
            {
                "statement": "L'operatore == confronta il valore di due variabili primitive",
                "correct": True,
                "explanation": "Vero. Per i tipi primitivi, == confronta il valore. Per gli oggetti, confronta il riferimento."
            },
            {
                "statement": "In Java il tipo `double` è sempre più efficiente di `float`",
                "correct": False,
                "explanation": "Falso. `float` usa meno memoria (32 bit vs 64 bit) ed è più efficiente, anche se meno preciso."
            }
        ]
    }
    
    stmts = statements.get(module_id, statements[1])
    
    answers = {}
    for idx, stmt in enumerate(stmts):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{idx + 1}. {stmt['statement']}**")
        with col2:
            answers[idx] = st.radio("", ["Vero", "Falso"], key=f"tf_{module_id}_{idx}", horizontal=True)
    
    if st.button("Verifica Risposte", key=f"tf_btn_{module_id}"):
        score = 0
        for idx, stmt in enumerate(stmts):
            user_answer = answers[idx] == "Vero"
            correct = user_answer == stmt["correct"]
            
            status = "✅" if correct else "❌"
            st.markdown(f"""
            <div class="{'success-box' if correct else 'error-box'}">
            {status} {stmt['statement']}<br>
            <em>{stmt['explanation']}</em>
            </div>
            """, unsafe_allow_html=True)
            
            if correct:
                score += 1
        
        st.markdown(f"""
        <div class="metric-box">
        <strong>Risultato:</strong> {score}/{len(stmts)} risposte corrette
        </div>
        """, unsafe_allow_html=True)
        
        return score == len(stmts)

# ==================== MAIN APP ====================
def main():
    # Header
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.markdown("# ☕ Java SE")
    with col2:
        st.markdown("## Interactive Course")
    with col3:
        pass
    
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 📊 Progresso del Corso")
        
        # Progress metrics
        total_modules = len(COURSE_MODULES)
        completed = len(st.session_state.course_state["modules_completed"])
        
        st.metric("Moduli Completati", f"{completed}/{total_modules}")
        st.metric("Esercizi Completati", len(st.session_state.course_state["exercises_completed"]))
        st.metric("Punteggio Totale", f"{st.session_state.course_state['score']} punti")
        
        # Progress bar
        progress = completed / total_modules if total_modules > 0 else 0
        st.progress(progress, text=f"{int(progress*100)}% completato")
        
        st.markdown("---")
        st.markdown("### 🎓 Moduli del Corso")
        
        for idx, module in enumerate(COURSE_MODULES):
            completed_marker = "✅" if idx in st.session_state.course_state["modules_completed"] else "⭕"
            if st.button(f"{completed_marker} {idx+1}. {module['title']}", key=f"sidebar_module_{idx}", use_container_width=True):
                st.session_state.course_state["current_module"] = idx
                st.rerun()
        
        st.markdown("---")
        if st.button("🔄 Resetta Corso", use_container_width=True):
            st.session_state.course_state = {
                "current_module": 0,
                "modules_completed": {},
                "exercises_completed": {},
                "score": 0,
                "started": False,
                "current_exercise_level": 1
            }
            st.rerun()
    
    # Main content
    if not st.session_state.course_state["started"]:
        st.markdown("""
        <div class="lesson-box">
        <h2>Benvenuto nel Corso Java SE Interattivo! 👋</h2>
        
        <p>Questo corso copre argomenti avanzati di Java, dalla gestione dei tipi di dati ai design pattern.
        Ogni modulo include:</p>
        
        <ul>
            <li><strong>📚 Lezioni teoriche</strong> con spiegazioni chiare</li>
            <li><strong>🔄 Esempi comparati con Python</strong> per migliore comprensione</li>
            <li><strong>📝 Esercizi Multiple Choice</strong> per verificare la teoria</li>
            <li><strong>💻 Coding Challenges</strong> con validazione del codice</li>
            <li><strong>✓ Esercizi Vero/Falso</strong> per consolidare i concetti</li>
        </ul>
        
        <h3>Struttura del Corso:</h3>
        <p><strong>11 moduli</strong> che progrediscono da Intermedio ad Avanzato, con un totale di <strong>44 ore</strong> di contenuti.</p>
        
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Inizia il Corso", use_container_width=True, key="start_course"):
            st.session_state.course_state["started"] = True
            st.rerun()
    
    else:
        current_module = st.session_state.course_state["current_module"]
        module = COURSE_MODULES[current_module]
        
        st.markdown(f"### Modulo {current_module + 1}: {module['title']}")
        st.markdown(f"**⏱️ Durata:** {module['hours']} ore | **Descrizione:** {module['description']}")
        st.markdown("---")
        
        # Tabs for lessons and exercises
        tab1, tab2, tab3, tab4 = st.tabs(["📚 Lezione", "📝 Multiple Choice", "💻 Coding", "✓ Vero/Falso"])
        
        with tab1:
            st.markdown(f"<div class='lesson-box'>", unsafe_allow_html=True)
            for lesson in module['lessons']:
                st.markdown(f"## {lesson['title']}")
                st.markdown(lesson['content'])
            st.markdown("</div>", unsafe_allow_html=True)
        
        with tab2:
            if show_multiple_choice(current_module + 1, 1):
                st.session_state.course_state["score"] += 10
        
        with tab3:
            if show_coding_challenge(current_module + 1, st.session_state.course_state["current_exercise_level"]):
                st.session_state.course_state["score"] += 25
        
        with tab4:
            if show_true_false(current_module + 1, 1):
                st.session_state.course_state["score"] += 15
        
        st.markdown("---")
        
        # Navigation buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if current_module > 0:
                if st.button("⬅️ Modulo Precedente", use_container_width=True):
                    st.session_state.course_state["current_module"] -= 1
                    st.session_state.course_state["current_exercise_level"] = 1
                    st.rerun()
        
        with col2:
            if st.button("✅ Completa Modulo", use_container_width=True):
                st.session_state.course_state["modules_completed"][current_module] = True
                st.balloons()
                st.success(f"🎉 Modulo {current_module + 1} completato!")
        
        with col3:
            if current_module < len(COURSE_MODULES) - 1:
                if st.button("➡️ Prossimo Modulo", use_container_width=True):
                    st.session_state.course_state["current_module"] += 1
                    st.session_state.course_state["current_exercise_level"] = 1
                    st.rerun()

if __name__ == "__main__":
    main()
