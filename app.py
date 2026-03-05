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
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
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
    }
    
    .stRadio > label {
        color: #e2e8f0;
        font-weight: 500;
    }
    
    .stCheckbox > label {
        color: #e2e8f0;
        font-weight: 500;
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
        "current_exercise_level": 1,
        "show_hint": {}
    }

# ==================== COURSE DATA - MODULI COMPLETI ====================
COURSE_MODULES = [
    {
        "id": 1,
        "title": "Tipi di Dati e Operatori",
        "hours": 3,
        "description": "Comprensione dei tipi di dati primitivi e non primitivi, operatori aritmetici, di confronto e logici.",
        "content": """
## 🎯 Tipi di Dati Primitivi

In Java, i tipi di dati primitivi sono i fondamenti del linguaggio. Rappresentano valori semplici memorizzati direttamente in memoria.

### Tipi Principali:
- **byte**: 8 bit, range -128 a 127
- **short**: 16 bit, range -32,768 a 32,767
- **int**: 32 bit, range -2,147,483,648 a 2,147,483,647 (uso generale)
- **long**: 64 bit, per numeri molto grandi (es: 1000000000000L)
- **float**: 32 bit, per decimali (meno preciso) - 3.14f
- **double**: 64 bit, per decimali (più preciso) - 3.14159
- **boolean**: true o false
- **char**: singolo carattere Unicode - 'A'

### Esempio Java:
```java
byte age = 25;
short year = 2024;
int salary = 50000;
long bigNumber = 9223372036854775807L;
float temperature = 36.5f;
double pi = 3.14159265359;
boolean isActive = true;
char grade = 'A';
```

### Equivalente in Python:
```python
age = 25                    # int (Python inferne il tipo)
year = 2024                 # int
salary = 50000              # int
big_number = 9223372036854775807  # int (illimitato!)
temperature = 36.5          # float
pi = 3.14159265359          # float
is_active = True            # bool
grade = 'A'                 # str
```

**Differenza chiave**: Java richiede la dichiarazione esplicita del tipo per **sicurezza** e **performance**, mentre Python è **dinamico**.

---

## 🔢 Operatori Aritmetici

Gli operatori permettono di eseguire operazioni matematiche sui dati.

```java
int a = 10, b = 3;
a + b   // 13 (addizione)
a - b   // 7 (sottrazione)
a * b   // 30 (moltiplicazione)
a / b   // 3 (divisione intera - scarta resto)
a % b   // 1 (modulo - resto della divisione)
```

### In Python:
```python
a, b = 10, 3
a + b   # 13
a - b   # 7
a * b   # 30
a // b  # 3 (divisione intera)
a % b   # 1 (modulo)
a / b   # 3.3333... (divisione float)
```

---

## ⚖️ Operatori di Confronto

Confrontano due valori e restituiscono un booleano (true/false).

```java
int x = 10, y = 5;
x == y  // false (uguale a)
x != y  // true (diverso da)
x > y   // true (maggiore di)
x < y   // false (minore di)
x >= y  // true (maggiore o uguale)
x <= y  // false (minore o uguale)
```

---

## 🔗 Operatori Logici

Combinano o invertono valori booleani.

```java
true && false  // false (AND - entrambi veri)
true || false  // true (OR - almeno uno vero)
!true          // false (NOT - inverte)

// Esempio pratico:
int age = 25;
boolean hasLicense = true;

if (age >= 18 && hasLicense) {
    System.out.println("Puoi guidare!");
}
```

### In Python:
```python
True and False  # False
True or False   # True
not True        # False
```

---

## 📚 Best Practice

✅ Usa **int** per numeri interi (è il default)  
✅ Usa **double** per numeri decimali  
✅ Dichiara variabili con nomi **significativi**  
✅ Commenta il codice **complesso**  
✅ Usa **costanti** (final) per valori fissi
"""
    },
    {
        "id": 2,
        "title": "Controllo di Flusso",
        "hours": 4,
        "description": "Condizioni if/else, cicli while, do-while, for. Controllo del flusso di esecuzione.",
        "content": """
## 🎯 Condizioni e Operatori Relazionali

Le condizioni permettono di eseguire codice solo se una determinata espressione è vera.

### if - else if - else:

```java
int age = 20;

if (age < 13) {
    System.out.println("Sei un bambino");
} else if (age < 18) {
    System.out.println("Sei un adolescente");
} else if (age < 65) {
    System.out.println("Sei un adulto");
} else {
    System.out.println("Sei un anziano");
}
```

### In Python:
```python
age = 20

if age < 13:
    print("Sei un bambino")
elif age < 18:
    print("Sei un adolescente")
elif age < 65:
    print("Sei un adulto")
else:
    print("Sei un anziano")
```

---

## 🔄 Ciclo while

Esegue un blocco di codice finché una condizione è vera.

```java
int count = 0;

while (count < 5) {
    System.out.println("Iterazione: " + count);
    count++;  // incrementa count di 1
}
// Output: Iterazione: 0, 1, 2, 3, 4
```

### In Python:
```python
count = 0

while count < 5:
    print(f"Iterazione: {count}")
    count += 1
```

---

## 🔄 Ciclo do-while

Esegue il blocco **almeno una volta**, poi controlla la condizione.

```java
int number = 0;

do {
    System.out.println("Numero: " + number);
    number++;
} while (number < 3);
// Esegue almeno una volta, anche se number < 3 è falso
```

**Python non ha do-while**, ma puoi usare while con break.

---

## 🔄 Ciclo for

Perfetto quando sai quante iterazioni fare.

```java
// Sintassi: for (inizializzazione; condizione; incremento)
for (int i = 0; i < 5; i++) {
    System.out.println("i = " + i);
}
// Output: 0, 1, 2, 3, 4

// For-each per array:
String[] nomi = {"Alice", "Bob", "Charlie"};
for (String nome : nomi) {
    System.out.println(nome);
}
```

### In Python:
```python
for i in range(5):
    print(f"i = {i}")

nomi = ["Alice", "Bob", "Charlie"]
for nome in nomi:
    print(nome)
```

---

## ⛔ Break e Continue

**break** esce dal ciclo:
```java
for (int i = 0; i < 10; i++) {
    if (i == 5) break;  // esce quando i = 5
    System.out.println(i);
}
// Output: 0, 1, 2, 3, 4
```

**continue** salta all'iterazione successiva:
```java
for (int i = 0; i < 5; i++) {
    if (i == 2) continue;  // salta quando i = 2
    System.out.println(i);
}
// Output: 0, 1, 3, 4
```

---

## 📚 Best Practice

✅ Usa **if/else** per decisioni semplici  
✅ Usa **for** quando sai il numero di iterazioni  
✅ Usa **while** quando non conosci il numero di iterazioni  
✅ Usa **break** per uscire da un ciclo  
✅ Evita **cicli infiniti** (sempre specificare quando finire)
"""
    },
    {
        "id": 3,
        "title": "Array e Stringhe",
        "hours": 4,
        "description": "Dichiarazione e utilizzo degli array, manipolazione di stringhe e metodi associati.",
        "content": """
## 🎯 Array in Java

Un array è una collezione di elementi dello **stesso tipo**, indicizzati da 0.

### Dichiarazione e Inizializzazione:

```java
// Modo 1: Dichiara e inizializza con dimensione
int[] numeri = new int[5];  // array di 5 interi (default = 0)

// Modo 2: Dichiara e inizializza con valori
int[] voti = {18, 20, 25, 30, 28};

// Modo 3: Accedi agli elementi
System.out.println(voti[0]);  // 18
System.out.println(voti[2]);  // 25
voti[1] = 22;  // modifica elemento

// Lunghezza array
System.out.println(voti.length);  // 5
```

### Array Multidimensionali:

```java
// Matrice 2D (3 righe x 3 colonne)
int[][] matrice = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

System.out.println(matrice[0][1]);  // 2
System.out.println(matrice[2][2]);  // 9
```

### In Python:
```python
numeri = [0] * 5           # lista di 5 zeri
voti = [18, 20, 25, 30, 28]
print(voti[0])             # 18
print(len(voti))           # 5

# Matrice
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrice[0][1])       # 2
```

---

## 📝 Stringhe e Metodi

Una stringa è una sequenza di caratteri. Le stringhe sono **immutabili** in Java.

```java
String nome = "Alice";

// Metodi comuni:
nome.length()              // 5 (numero di caratteri)
nome.charAt(0)             // 'A' (carattere alla posizione 0)
nome.substring(0, 3)       // "Ali" (da indice 0 a 3)
nome.toUpperCase()         // "ALICE"
nome.toLowerCase()         // "alice"
nome.contains("ice")       // true
nome.startsWith("Al")      // true
nome.endsWith("ce")        // true
nome.equals("Alice")       // true
nome.equalsIgnoreCase("alice")  // true
nome.indexOf('i')          // 2 (posizione di 'i')
nome.replace('A', 'B')     // "Blice"
nome.trim()                // rimuove spazi da inizio e fine
nome.split(" ")            // array di parole
```

### Concatenazione di Stringhe:

```java
// Modo 1: operatore +
String saluto = "Ciao " + "mondo";  // "Ciao mondo"

// Modo 2: metodo concat()
String msg = "Hello".concat(" Java");  // "Hello Java"

// Modo 3: StringBuilder (più efficiente per molte concatenazioni)
StringBuilder sb = new StringBuilder();
sb.append("Ciao ");
sb.append("mondo");
String risultato = sb.toString();  // "Ciao mondo"
```

### In Python:
```python
nome = "Alice"
print(len(nome))           # 5
print(nome[0])             # 'A'
print(nome[0:3])           # 'Ali'
print(nome.upper())        # 'ALICE'
print(nome.lower())        # 'alice'
print('ice' in nome)       # True
print(nome.startswith('Al'))  # True

# Concatenazione
saluto = "Ciao " + "mondo"
msg = f"Hello {nome}"
```

---

## 📚 Best Practice

✅ Usa array per **collezioni omogenee**  
✅ Ricorda che gli indici **partono da 0**  
✅ Non accedere **oltre la lunghezza** (IndexOutOfBoundsException)  
✅ Per stringhe: usa **StringBuilder** per molte concatenazioni  
✅ Usa **equals()** per confrontare stringhe (non ==)
"""
    },
    {
        "id": 4,
        "title": "Oggetti e Classi",
        "hours": 8,
        "description": "OOP: classi, oggetti, ereditarietà, polimorfismo, incapsulamento, interfacce.",
        "content": """
## 🎯 Introduzione agli Oggetti

La programmazione orientata agli oggetti (OOP) organizza il codice in **classi** e **oggetti**.

Una **classe** è un modello (blueprint) che definisce:
- **Attributi** (proprietà/variabili): cosa ha l'oggetto
- **Metodi** (funzioni): cosa fa l'oggetto

Un **oggetto** è un'istanza della classe.

### Esempio: Classe Person

```java
public class Person {
    // Attributi (proprietà)
    public String name;
    public int age;
    
    // Costruttore (inizializza l'oggetto)
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // Metodo
    public void sayHello() {
        System.out.println("Ciao, sono " + name + " e ho " + age + " anni");
    }
    
    // Metodo che restituisce un valore
    public boolean isAdult() {
        return age >= 18;
    }
}

// Utilizzo:
Person alice = new Person("Alice", 25);
alice.sayHello();  // Output: Ciao, sono Alice e ho 25 anni
System.out.println(alice.isAdult());  // true
```

---

## 🔒 Incapsulamento e Access Modifiers

L'incapsulamento **protegge i dati** usando access modifiers:

```java
public class Persona {
    // private: accessibile solo dentro la classe
    private String nome;
    private int eta;
    
    // public: accessibile da ovunque
    public Persona(String nome, int eta) {
        this.nome = nome;
        this.eta = eta;
    }
    
    // Metodi getter (lettura)
    public String getNome() {
        return nome;
    }
    
    public int getEta() {
        return eta;
    }
    
    // Metodi setter (scrittura con validazione)
    public void setNome(String nome) {
        if (nome != null && !nome.isEmpty()) {
            this.nome = nome;
        }
    }
    
    public void setEta(int eta) {
        if (eta > 0 && eta < 150) {
            this.eta = eta;
        }
    }
}

// Utilizzo:
Persona p = new Persona("Bob", 30);
p.getNome();      // "Bob"
p.setEta(31);     // valido
p.setEta(-5);     // rifiutato (validazione)
```

### Access Modifiers:
- **public**: accessibile da ovunque
- **private**: accessibile solo dentro la classe
- **protected**: accessibile dalla stessa classe e sottoclassi
- **default** (nessun modificatore): accessibile dentro lo stesso package

---

## 👨‍👩‍👦 Ereditarietà

Una classe può **ereditare** da un'altra usando **extends**.

```java
// Classe genitore (parent/superclass)
public class Animal {
    protected String nome;
    
    public Animal(String nome) {
        this.nome = nome;
    }
    
    public void makeSound() {
        System.out.println("Suono generico...");
    }
}

// Classe figlia (child/subclass)
public class Dog extends Animal {
    public Dog(String nome) {
        super(nome);  // chiama il costruttore della classe genitore
    }
    
    @Override  // sovrascrivi il metodo della classe genitore
    public void makeSound() {
        System.out.println("Bau bau!");
    }
    
    public void fetch() {
        System.out.println(nome + " sta recuperando la palla");
    }
}

// Utilizzo:
Dog dog = new Dog("Rex");
dog.makeSound();  // Bau bau!
dog.fetch();      // Rex sta recuperando la palla
```

---

## 🔄 Polimorfismo

Lo stesso metodo può comportarsi diversamente a seconda della classe.

```java
Animal animal1 = new Dog("Rex");
Animal animal2 = new Cat("Whiskers");
Animal animal3 = new Bird("Tweety");

animal1.makeSound();  // Bau bau!
animal2.makeSound();  // Miao!
animal3.makeSound();  // Cip cip!
```

---

## 📚 Best Practice

✅ Usa **private** per attributi  
✅ Fornisci **getter/setter** pubblici  
✅ Usa **ereditarietà** per evitare duplicazione  
✅ Sovrascrivi metodi con **@Override**  
✅ Usa **polimorfismo** per flessibilità  
✅ Nomina classi con **PascalCase** (PersonClass)  
✅ Nomina metodi con **camelCase** (getPersonName)
"""
    },
    {
        "id": 5,
        "title": "Eccezioni",
        "hours": 4,
        "description": "Gestione delle eccezioni, try-catch-finally, throw, throws, custom exceptions.",
        "content": """
## 🎯 Introduzione alle Eccezioni

Un'eccezione è un **evento anomalo** che interrompe il flusso normale di esecuzione.

Esempi:
- Dividere per zero
- Accedere a indice inesistente in un array
- File non trovato
- Connessione di rete persa

### try-catch-finally:

```java
try {
    // Codice che potrebbe generare un'eccezione
    int[] numeri = {1, 2, 3};
    System.out.println(numeri[10]);  // IndexOutOfBoundsException!
} catch (ArrayIndexOutOfBoundsException e) {
    // Gestisci l'errore specifico
    System.out.println("Indice non valido: " + e.getMessage());
} catch (Exception e) {
    // Cattura qualsiasi altra eccezione
    System.out.println("Errore generico: " + e.getMessage());
} finally {
    // Esegui sempre, che ci sia eccezione o no
    System.out.println("Operazione completata");
}
```

### In Python:
```python
try:
    numeri = [1, 2, 3]
    print(numeri[10])
except IndexError as e:
    print(f"Indice non valido: {e}")
except Exception as e:
    print(f"Errore generico: {e}")
finally:
    print("Operazione completata")
```

---

## 🚀 throw e throws

**throw**: lancia un'eccezione esplicitamente
```java
public void checkAge(int age) {
    if (age < 0) {
        throw new IllegalArgumentException("L'eta non puo' essere negativa");
    }
}
```

**throws**: dichiara che il metodo potrebbe lanciare un'eccezione
```java
public void readFile(String filename) throws IOException {
    // Metodo che potrebbe lanciare IOException
    // Il chiamante deve gestirla con try-catch
}

// Utilizzo:
try {
    readFile("dati.txt");
} catch (IOException e) {
    System.out.println("Errore di lettura file: " + e.getMessage());
}
```

---

## 📊 Gerarchia delle Eccezioni

```
Throwable
├── Error (non recuperabile, es: OutOfMemoryError)
└── Exception (recuperabile)
    ├── Checked (obbligatorio catturare)
    │   ├── IOException
    │   ├── SQLException
    │   └── ...
    └── Unchecked / Runtime (facoltativo catturare)
        ├── NullPointerException
        ├── ArrayIndexOutOfBoundsException
        ├── IllegalArgumentException
        └── ...
```

---

## 👨‍💼 Custom Exceptions

Puoi creare eccezioni personalizzate:

```java
// Crea un'eccezione personalizzata
public class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String message) {
        super(message);
    }
}

// Usa l'eccezione:
public class BankAccount {
    private double balance = 100;
    
    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount > balance) {
            throw new InsufficientFundsException("Fondi insufficienti!");
        }
        balance -= amount;
    }
}

// Gestisci l'eccezione:
try {
    account.withdraw(150);
} catch (InsufficientFundsException e) {
    System.out.println(e.getMessage());
}
```

---

## 📚 Best Practice

✅ Cattura **eccezioni specifiche** prima di quelle generiche  
✅ Non ignorare le eccezioni (non fare catch vuoti)  
✅ Usa **finally** per pulire risorse  
✅ Crea eccezioni **personalizzate** quando appropriato  
✅ Fornisci messaggi di errore **descrittivi**  
✅ Usa **try-with-resources** per file/connessioni
"""
    },
    {
        "id": 6,
        "title": "Collections Framework",
        "hours": 4,
        "description": "ArrayList, LinkedList, HashSet, HashMap, TreeMap, Queue.",
        "content": """
## 🎯 Introduzione alle Collections

Le collections sono strutture dati che memorizzano **gruppi di oggetti** in modo dinamico.

### Gerarchia:
```
Collection
├── List (ordine, duplicati permessi)
│   ├── ArrayList
│   ├── LinkedList
│   └── Vector
├── Set (no duplicati, no ordine garantito)
│   ├── HashSet
│   ├── TreeSet
│   └── LinkedHashSet
└── Queue (FIFO - First In First Out)
    ├── LinkedList
    └── PriorityQueue

Map (chiave-valore, no ordine)
├── HashMap
├── TreeMap
└── LinkedHashMap
```

---

## 📋 ArrayList

Array dinamico che cresce/shrink automaticamente.

```java
import java.util.ArrayList;

ArrayList<Integer> numeri = new ArrayList<>();

// Aggiungi elementi
numeri.add(10);
numeri.add(20);
numeri.add(30);

// Accedi a elementi
System.out.println(numeri.get(0));  // 10

// Modifica elementi
numeri.set(1, 25);  // cambia 20 in 25

// Rimuovi elementi
numeri.remove(0);  // rimuove 10

// Lunghezza
System.out.println(numeri.size());  // 2

// Itera
for (Integer num : numeri) {
    System.out.println(num);
}

// Contiene
if (numeri.contains(25)) {
    System.out.println("25 è presente");
}
```

### In Python:
```python
numeri = []
numeri.append(10)
numeri.append(20)
print(numeri[0])    # 10
numeri[1] = 25
numeri.remove(10)
print(len(numeri))  # 1
for num in numeri:
    print(num)
```

---

## 🗂️ HashMap

Mappa chiave-valore.

```java
import java.util.HashMap;

HashMap<String, Integer> etaPersone = new HashMap<>();

// Aggiungi coppie chiave-valore
etaPersone.put("Alice", 25);
etaPersone.put("Bob", 30);
etaPersone.put("Charlie", 28);

// Leggi con chiave
System.out.println(etaPersone.get("Alice"));  // 25

// Controlla se esiste una chiave
if (etaPersone.containsKey("Bob")) {
    System.out.println("Bob esiste");
}

// Itera su chiavi
for (String nome : etaPersone.keySet()) {
    System.out.println(nome + ": " + etaPersone.get(nome));
}

// Itera su valori
for (Integer eta : etaPersone.values()) {
    System.out.println(eta);
}

// Rimuovi
etaPersone.remove("Bob");

// Dimensione
System.out.println(etaPersone.size());  // 2
```

### In Python:
```python
eta_persone = {}
eta_persone["Alice"] = 25
eta_persone["Bob"] = 30
print(eta_persone["Alice"])  # 25
if "Bob" in eta_persone:
    print("Bob esiste")
for nome, eta in eta_persone.items():
    print(f"{nome}: {eta}")
```

---

## 🔗 LinkedList

Lista collegata (veloce in inserimento/rimozione, lenta in accesso).

```java
import java.util.LinkedList;

LinkedList<String> lista = new LinkedList<>();
lista.add("primo");
lista.add("secondo");
lista.addFirst("all'inizio");
lista.addLast("alla fine");

lista.removeFirst();
lista.removeLast();
System.out.println(lista.getFirst());  // "primo"
```

---

## 🏷️ HashSet

Set di elementi unici (no duplicati).

```java
import java.util.HashSet;

HashSet<String> frutti = new HashSet<>();
frutti.add("mela");
frutti.add("banana");
frutti.add("mela");  // non aggiunge il duplicato

System.out.println(frutti.size());  // 2

if (frutti.contains("banana")) {
    System.out.println("Banana è nel set");
}

for (String frutto : frutti) {
    System.out.println(frutto);
}
```

---

## 📚 Best Practice

✅ Usa **ArrayList** per collezioni generiche  
✅ Usa **HashMap** per mapping chiave-valore  
✅ Usa **HashSet** per collezioni senza duplicati  
✅ Usa **generic types** per type safety  
✅ Itera con **for-each** quando possibile  
✅ Usa **TreeMap/TreeSet** se hai bisogno di ordine
"""
    },
    {
        "id": 7,
        "title": "Input/Output e Stream",
        "hours": 4,
        "description": "Lettura/scrittura file, stream, serializzazione degli oggetti.",
        "content": """
## 🎯 Lettura e Scrittura di File

### Scrivere su File:

```java
import java.io.FileWriter;
import java.io.IOException;

// Modo 1: FileWriter
try {
    FileWriter writer = new FileWriter("output.txt");
    writer.write("Ciao mondo!\\n");
    writer.write("Seconda riga");
    writer.close();  // importante: chiudi il file
} catch (IOException e) {
    System.out.println("Errore: " + e.getMessage());
}

// Modo 2: PrintWriter (più facile)
import java.io.PrintWriter;

try (PrintWriter writer = new PrintWriter("output.txt")) {
    writer.println("Riga 1");
    writer.println("Riga 2");
    // try-with-resources chiude automaticamente
} catch (IOException e) {
    System.out.println("Errore: " + e.getMessage());
}
```

### Leggere da File:

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

// Modo 1: BufferedReader
try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"))) {
    String linea;
    while ((linea = reader.readLine()) != null) {
        System.out.println(linea);
    }
} catch (IOException e) {
    System.out.println("Errore: " + e.getMessage());
}

// Modo 2: Scanner
import java.util.Scanner;

try (Scanner scanner = new Scanner(new File("input.txt"))) {
    while (scanner.hasNextLine()) {
        String linea = scanner.nextLine();
        System.out.println(linea);
    }
} catch (IOException e) {
    System.out.println("Errore: " + e.getMessage());
}
```

### In Python:
```python
# Scrivere
with open("output.txt", "w") as f:
    f.write("Ciao mondo!\\n")
    f.write("Seconda riga")

# Leggere
with open("input.txt", "r") as f:
    for linea in f:
        print(linea.strip())

# Alternativa
lines = open("input.txt").readlines()
```

---

## 💾 Serializzazione degli Oggetti

Converte un oggetto in sequenza di byte per memorizzarlo su file.

```java
import java.io.*;

// La classe deve implementare Serializable
public class Person implements Serializable {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // getter e setter...
}

// Salva su file:
try {
    Person person = new Person("Alice", 25);
    
    ObjectOutputStream oos = new ObjectOutputStream(
        new FileOutputStream("person.ser")
    );
    oos.writeObject(person);
    oos.close();
    System.out.println("Oggetto salvato!");
} catch (IOException e) {
    e.printStackTrace();
}

// Leggi da file:
try {
    ObjectInputStream ois = new ObjectInputStream(
        new FileInputStream("person.ser")
    );
    Person person = (Person) ois.readObject();
    ois.close();
    System.out.println("Nome: " + person.getName());
} catch (IOException | ClassNotFoundException e) {
    e.printStackTrace();
}
```

---

## 📂 Classe File

Rappresenta un file o cartella nel file system.

```java
import java.io.File;

File file = new File("data.txt");

// Proprietà
System.out.println(file.exists());      // true/false
System.out.println(file.isFile());      // true se è file
System.out.println(file.isDirectory()); // true se è cartella
System.out.println(file.length());      // dimensione in byte
System.out.println(file.getAbsolutePath());  // percorso completo
System.out.println(file.getName());     // nome file
System.out.println(file.getParent());   // cartella genitore

// Operazioni
file.delete();              // elimina file
file.renameTo(new File("new.txt"));  // rinomina

// Cartelle
File dir = new File("myfolder");
dir.mkdir();                // crea cartella
String[] files = dir.list();  // lista file in cartella
```

---

## 📚 Best Practice

✅ Usa **try-with-resources** per chiudere automaticamente  
✅ Gestisci sempre **IOException**  
✅ Implementa **Serializable** per serializzazione  
✅ Controlla se il file **esiste** prima di leggere  
✅ Usa **BufferedReader** per file grandi  
✅ Usa **PrintWriter** per output facile  
✅ Chiudi sempre i file (o usa try-with-resources)
"""
    },
    {
        "id": 8,
        "title": "Java Time API",
        "hours": 2,
        "description": "LocalDate, LocalTime, LocalDateTime, ZonedDateTime, Period, Duration.",
        "content": """
## 🎯 Java Time API

Gestione moderna e thread-safe di date e orari (introdotta in Java 8).

### LocalDate (solo data)

```java
import java.time.LocalDate;

// Crea date
LocalDate oggi = LocalDate.now();  // data odierna
LocalDate natale = LocalDate.of(2024, 12, 25);

// Proprietà
System.out.println(oggi.getYear());    // 2024
System.out.println(oggi.getMonth());   // MARCH
System.out.println(oggi.getDayOfMonth());  // 5
System.out.println(oggi.getDayOfWeek());   // THURSDAY

// Operazioni
LocalDate domani = oggi.plusDays(1);
LocalDate il_mese_prossimo = oggi.plusMonths(1);
LocalDate l_anno_prossimo = oggi.plusYears(1);

// Confronti
if (natale.isAfter(oggi)) {
    System.out.println("Natale è dopo oggi");
}

// Differenza tra date
import java.time.Period;
Period differenza = Period.between(oggi, natale);
System.out.println(differenza.getDays());    // giorni
System.out.println(differenza.getMonths());  // mesi
System.out.println(differenza.getYears());   // anni
```

### In Python:
```python
from datetime import date, timedelta

oggi = date.today()
natale = date(2024, 12, 25)

print(oggi.year)
print(oggi.month)
print(oggi.day)

domani = oggi + timedelta(days=1)
il_mese_prossimo = oggi + timedelta(days=30)

if natale > oggi:
    print("Natale è dopo oggi")

differenza = natale - oggi
print(differenza.days)
```

---

### LocalTime (solo orario)

```java
import java.time.LocalTime;

LocalTime ora_attuale = LocalTime.now();
LocalTime mezzogiorno = LocalTime.of(12, 0, 0);

System.out.println(ora_attuale.getHour());    // ora
System.out.println(ora_attuale.getMinute());  // minuti
System.out.println(ora_attuale.getSecond());  // secondi

LocalTime dopo_un_ora = ora_attuale.plusHours(1);
LocalTime tra_30_minuti = ora_attuale.plusMinutes(30);
```

---

### LocalDateTime (data + orario)

```java
import java.time.LocalDateTime;

LocalDateTime adesso = LocalDateTime.now();
LocalDateTime capodanno = LocalDateTime.of(2025, 1, 1, 0, 0, 0);

System.out.println(adesso.getYear());
System.out.println(adesso.getMonth());
System.out.println(adesso.getHour());
System.out.println(adesso.getMinute());

// Operazioni
LocalDateTime domani_stesso_orario = adesso.plusDays(1);
LocalDateTime tra_2_ore = adesso.plusHours(2);

// Confronti
if (capodanno.isAfter(adesso)) {
    System.out.println("Capodanno è nel futuro");
}
```

---

### Duration (durata tra istanti)

```java
import java.time.Duration;

LocalDateTime inizio = LocalDateTime.of(2024, 1, 1, 10, 0);
LocalDateTime fine = LocalDateTime.of(2024, 1, 1, 14, 30);

Duration durata = Duration.between(inizio, fine);
System.out.println(durata.toHours());      // 4
System.out.println(durata.toMinutes());    // 270
System.out.println(durata.getSeconds());   // 16200
```

---

### ZonedDateTime (con fuso orario)

```java
import java.time.ZonedDateTime;
import java.time.ZoneId;

ZonedDateTime adesso = ZonedDateTime.now();
ZonedDateTime a_tokyo = ZonedDateTime.now(ZoneId.of("Asia/Tokyo"));
ZonedDateTime a_new_york = ZonedDateTime.now(ZoneId.of("America/New_York"));

System.out.println(adesso);
System.out.println(a_tokyo);
System.out.println(a_new_york);
```

---

### Formattazione

```java
import java.time.format.DateTimeFormatter;

LocalDate data = LocalDate.now();

// Formati predefiniti
System.out.println(data.format(DateTimeFormatter.ISO_DATE));
System.out.println(data.format(DateTimeFormatter.BASIC_ISO_DATE));

// Formato personalizzato
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");
System.out.println(data.format(fmt));  // 05/03/2024

// Parse (da stringa a data)
String dataString = "25/12/2024";
LocalDate natale = LocalDate.parse(dataString, fmt);
```

---

## 📚 Best Practice

✅ Usa **LocalDate/LocalTime/LocalDateTime** (non Date/Calendar vecchie)  
✅ Usa **ZonedDateTime** se hai bisogno di fusi orari  
✅ Usa **Period** per differenze tra date  
✅ Usa **Duration** per differenze tra orari  
✅ Usa **DateTimeFormatter** per formattazione  
✅ Java Time è **thread-safe** (a differenza di Date)
"""
    },
    {
        "id": 9,
        "title": "Generics",
        "hours": 4,
        "description": "Classi generiche, interfacce generiche, wildcards, bounded types.",
        "content": """
## 🎯 Introduzione ai Generics

I generics permettono di scrivere codice **type-safe** e **riusabile** per diversi tipi di dati.

### Classi Generiche:

```java
// Classe generica (T è un placeholder per il tipo)
public class Box<T> {
    private T content;
    
    public Box(T content) {
        this.content = content;
    }
    
    public T getContent() {
        return content;
    }
    
    public void setContent(T content) {
        this.content = content;
    }
}

// Utilizzo:
Box<String> stringBox = new Box<>("Ciao");
String messaggio = stringBox.getContent();  // No casting!

Box<Integer> intBox = new Box<>(42);
int numero = intBox.getContent();

Box<Double> doubleBox = new Box<>(3.14);
double valore = doubleBox.getContent();

// SENZA generics (tipo non sicuro):
Box box = new Box("Ciao");
String msg = (String) box.getContent();  // Casting! Pericoloso!
```

---

## 🔤 Metodi Generici:

```java
public class Utilities {
    // Metodo generico
    public static <T> void printArray(T[] array) {
        for (T elemento : array) {
            System.out.println(elemento);
        }
    }
    
    // Metodo generico con return
    public static <T> T getFirst(T[] array) {
        return array.length > 0 ? array[0] : null;
    }
}

// Utilizzo:
Integer[] numeri = {1, 2, 3};
String[] parole = {"Ciao", "mondo"};

Utilities.printArray(numeri);  // 1, 2, 3
Utilities.printArray(parole);  // Ciao, mondo

Integer primo = Utilities.getFirst(numeri);  // 1
String primaParola = Utilities.getFirst(parole);  // "Ciao"
```

---

## 🎯 Bounded Types (Tipi Limitati):

```java
// Limita T a tipi che estendono Number
public class Calculator<T extends Number> {
    public double sum(T a, T b) {
        return a.doubleValue() + b.doubleValue();
    }
}

// Utilizzo:
Calculator<Integer> intCalc = new Calculator<>();
System.out.println(intCalc.sum(5, 10));  // 15.0

Calculator<Double> doubleCalc = new Calculator<>();
System.out.println(doubleCalc.sum(5.5, 10.5));  // 16.0

// Errore: String non estende Number
// Calculator<String> stringCalc = new Calculator<>();  // Errore!
```

---

## 🃏 Wildcards (?):

**Unbounded wildcard** (qualsiasi tipo):
```java
public void printList(List<?> list) {
    for (Object elemento : list) {
        System.out.println(elemento);
    }
}

List<String> stringList = Arrays.asList("a", "b", "c");
List<Integer> intList = Arrays.asList(1, 2, 3);

printList(stringList);  // OK
printList(intList);     // OK
```

**Bounded wildcard** (con limiti):
```java
// ? extends Number: accetta Number e sottoclassi
public void sumOfNumbers(List<? extends Number> list) {
    double sum = 0;
    for (Number num : list) {
        sum += num.doubleValue();
    }
    System.out.println("Somma: " + sum);
}

// ? super Integer: accetta Integer e superclassi
public void addIntegers(List<? super Integer> list) {
    list.add(10);
    list.add(20);
}
```

---

## 📚 Generics con Collections:

```java
import java.util.ArrayList;
import java.util.HashMap;

// ArrayList generico
ArrayList<String> nomi = new ArrayList<>();
nomi.add("Alice");
nomi.add("Bob");
// nomi.add(123);  // Errore! Solo String

// HashMap generico
HashMap<String, Integer> eta = new HashMap<>();
eta.put("Alice", 25);
eta.put("Bob", 30);

// Itera con type-safety
for (String nome : eta.keySet()) {
    Integer ePersona = eta.get(nome);  // No casting!
    System.out.println(nome + ": " + ePersona);
}
```

---

## 📚 Best Practice

✅ Usa **generics** per type-safety  
✅ Evita **raw types** (List invece di List<String>)  
✅ Usa **bounded types** per limitare i tipi  
✅ Usa **wildcards** quando non conosci il tipo esatto  
✅ I generics sono **rimossi in runtime** (type erasure)  
✅ Non puoi usare tipi primitivi in generics (usa Integer, Double, ecc.)
"""
    },
    {
        "id": 10,
        "title": "Lambda Expressions",
        "hours": 4,
        "description": "Lambda expressions, functional interfaces, method references.",
        "content": """
## 🎯 Introduzione alle Lambda

Una lambda è una **funzione anonima** breve che può essere passata come parametro.

Introdotta in Java 8 per rendere il codice più conciso e funzionale.

### Sintassi di base:

```java
// Sintassi: (parametri) -> { corpo }

// Lambda senza parametri
() -> System.out.println("Ciao!");

// Lambda con un parametro
x -> x * 2

// Lambda con più parametri
(x, y) -> x + y

// Lambda con corpo multiplo
(x, y) -> {
    int risultato = x + y;
    return risultato * 2;
}
```

---

## 🎯 Interfacce Funzionali

Una lambda richiede un'**interfaccia funzionale** (con un solo metodo astratto).

```java
// Interfaccia funzionale (può avere solo 1 metodo astratto)
@FunctionalInterface
public interface Operazione {
    int esegui(int a, int b);
}

// Utilizzo con lambda:
Operazione addizione = (x, y) -> x + y;
Operazione sottrazione = (x, y) -> x - y;
Operazione moltiplicazione = (x, y) -> x * y;

System.out.println(addizione.esegui(5, 3));      // 8
System.out.println(sottrazione.esegui(5, 3));    // 2
System.out.println(moltiplicazione.esegui(5, 3));  // 15
```

---

## 🔧 Interfacce Funzionali Predefinite:

```java
import java.util.function.*;

// Consumer: accetta un valore, non restituisce nulla
Consumer<String> stampa = s -> System.out.println(s);
stampa.accept("Ciao");  // Ciao

// Supplier: non accetta parametri, restituisce un valore
Supplier<String> saluto = () -> "Buongiorno";
System.out.println(saluto.get());  // Buongiorno

// Function: trasforma un valore
Function<Integer, Integer> raddoppia = x -> x * 2;
System.out.println(raddoppia.apply(5));  // 10

// Predicate: testa una condizione (restituisce boolean)
Predicate<Integer> èPositivo = x -> x > 0;
System.out.println(èPositivo.test(5));   // true
System.out.println(èPositivo.test(-5));  // false
```

---

## 📚 Lambda con Collezioni:

```java
import java.util.ArrayList;
import java.util.List;

List<Integer> numeri = new ArrayList<>();
numeri.add(1);
numeri.add(2);
numeri.add(3);
numeri.add(4);
numeri.add(5);

// forEach con lambda
numeri.forEach(n -> System.out.println(n));

// filter (mantenere solo numeri pari)
List<Integer> pari = new ArrayList<>();
numeri.forEach(n -> {
    if (n % 2 == 0) pari.add(n);
});
System.out.println(pari);  // [2, 4]

// map (raddoppiare ogni numero)
List<Integer> raddoppiati = new ArrayList<>();
numeri.forEach(n -> raddoppiati.add(n * 2));
System.out.println(raddoppiati);  // [2, 4, 6, 8, 10]
```

---

## 🔗 Method References:

Un'alternativa ancora più concisa alle lambda.

```java
import java.util.ArrayList;
import java.util.List;

List<String> nomi = new ArrayList<>();
nomi.add("Alice");
nomi.add("Bob");
nomi.add("Charlie");

// Lambda
nomi.forEach(nome -> System.out.println(nome));

// Method reference (equivalente, più conciso)
nomi.forEach(System.out::println);

// Altre forme:
// ClassName::staticMethod
// instance::instanceMethod
// ClassName::instanceMethod
// ClassName::new (costruttore)

// Esempi:
Function<Integer, String> intToString = Integer::toString;
System.out.println(intToString.apply(42));  // "42"

List<String> ordinati = nomi;
ordinati.sort(String::compareTo);  // ordina alfabeticamente
```

---

## 📚 Best Practice

✅ Usa **lambda** per codice breve e semplice  
✅ Usa **method references** quando disponibili  
✅ Ricorda che le lambda richiedono interfacce funzionali  
✅ Usa le interfacce predefinite (Consumer, Function, Predicate)  
✅ Le lambda catturano variabili **final o effectively final**  
✅ Evita lambda complesse (uso metodi normali)
"""
    },
    {
        "id": 11,
        "title": "Design Pattern",
        "hours": 4,
        "description": "Singleton, Factory, Observer, Adapter, Facade pattern.",
        "content": """
## 🎯 Introduzione ai Design Pattern

I design pattern sono **soluzioni riusabili** a problemi comuni nella programmazione.

Ci sono 3 categorie:
- **Creazionali**: come creare oggetti
- **Strutturali**: come organizzare relazioni tra oggetti
- **Comportamentali**: come gli oggetti comunicano

---

## 1️⃣ Singleton Pattern (Creazionale)

Garantisce che una classe abbia **una sola istanza** globale.

```java
public class Logger {
    // Istanza statica privata
    private static Logger instance;
    
    // Costruttore privato (non puoi istanziare direttamente)
    private Logger() {
    }
    
    // Metodo pubblico per ottenere l'istanza
    public static Logger getInstance() {
        if (instance == null) {
            instance = new Logger();
        }
        return instance;
    }
    
    public void log(String messaggio) {
        System.out.println("[LOG] " + messaggio);
    }
}

// Utilizzo:
Logger logger1 = Logger.getInstance();
Logger logger2 = Logger.getInstance();
logger1.log("Messaggio 1");  // [LOG] Messaggio 1

System.out.println(logger1 == logger2);  // true (stessa istanza)
```

---

## 2️⃣ Factory Pattern (Creazionale)

Crea oggetti senza specificare esattamente quale classe istanziare.

```java
// Interfaccia
public interface Shape {
    void draw();
}

// Implementazioni
public class Circle implements Shape {
    @Override
    public void draw() {
        System.out.println("Disegnando un cerchio");
    }
}

public class Rectangle implements Shape {
    @Override
    public void draw() {
        System.out.println("Disegnando un rettangolo");
    }
}

// Factory
public class ShapeFactory {
    public static Shape createShape(String tipo) {
        if (tipo.equals("circle")) {
            return new Circle();
        } else if (tipo.equals("rectangle")) {
            return new Rectangle();
        }
        return null;
    }
}

// Utilizzo:
Shape shape1 = ShapeFactory.createShape("circle");
shape1.draw();  // Disegnando un cerchio

Shape shape2 = ShapeFactory.createShape("rectangle");
shape2.draw();  // Disegnando un rettangolo
```

---

## 3️⃣ Observer Pattern (Comportamentale)

Un oggetto (subject) notifica altri oggetti (observers) di cambiamenti di stato.

```java
import java.util.ArrayList;
import java.util.List;

// Subject (colui che notifica)
public class NewsAgency {
    private String ultimaNotizia;
    private List<Observer> osservatori = new ArrayList<>();
    
    // Observer si registra
    public void registra(Observer observer) {
        osservatori.add(observer);
    }
    
    // Observer si deregistra
    public void deregistra(Observer observer) {
        osservatori.remove(observer);
    }
    
    // Quando c'è una nuova notizia, notifica tutti
    public void setUltimaNotizia(String notizia) {
        this.ultimaNotizia = notizia;
        notificaOsservatori();
    }
    
    private void notificaOsservatori() {
        for (Observer obs : osservatori) {
            obs.update(ultimaNotizia);
        }
    }
}

// Observer (ascoltatore)
public interface Observer {
    void update(String notizia);
}

public class Giornalista implements Observer {
    private String nome;
    
    public Giornalista(String nome) {
        this.nome = nome;
    }
    
    @Override
    public void update(String notizia) {
        System.out.println(nome + " ha ricevuto: " + notizia);
    }
}

// Utilizzo:
NewsAgency agenzia = new NewsAgency();

Giornalista mario = new Giornalista("Mario");
Giornalista lucia = new Giornalista("Lucia");

agenzia.registra(mario);
agenzia.registra(lucia);

agenzia.setUltimaNotizia("Breaking news!");
// Mario ha ricevuto: Breaking news!
// Lucia ha ricevuto: Breaking news!
```

---

## 4️⃣ Adapter Pattern (Strutturale)

Adatta l'interfaccia di una classe a un'altra interfaccia.

```java
// Interfaccia vecchia
public interface VecchioSistema {
    void esegui();
}

// Classe vecchia che non puoi modificare
public class ClasseVecchia {
    public void operazione() {
        System.out.println("Esecuzione vecchia operazione");
    }
}

// Adapter che adatta ClasseVecchia a VecchioSistema
public class AdapterAdapter implements VecchioSistema {
    private ClasseVecchia vecchiaClasse;
    
    public AdapterAdapter(ClasseVecchia vecchiaClasse) {
        this.vecchiaClasse = vecchiaClasse;
    }
    
    @Override
    public void esegui() {
        // Traduce l'interfaccia
        vecchiaClasse.operazione();
    }
}

// Utilizzo:
ClasseVecchia vecchia = new ClasseVecchia();
VecchioSistema adapter = new AdapterAdapter(vecchia);
adapter.esegui();  // Esecuzione vecchia operazione
```

---

## 5️⃣ Facade Pattern (Strutturale)

Fornisce un'interfaccia semplificata a un sottosistema complesso.

```java
// Sottosistema complesso
public class DatabaseConnection {
    public void connect() {
        System.out.println("Connessione al database...");
    }
}

public class Authentication {
    public void authenticate(String user, String pass) {
        System.out.println("Autenticazione di " + user);
    }
}

public class PaymentProcessor {
    public void process(double amount) {
        System.out.println("Elaborazione pagamento: €" + amount);
    }
}

// Facade (interfaccia semplice)
public class OnlineStoreFacade {
    private DatabaseConnection db = new DatabaseConnection();
    private Authentication auth = new Authentication();
    private PaymentProcessor payment = new PaymentProcessor();
    
    public void purchaseProduct(String user, String pass, double price) {
        db.connect();
        auth.authenticate(user, pass);
        payment.process(price);
        System.out.println("Acquisto completato!");
    }
}

// Utilizzo:
OnlineStoreFacade store = new OnlineStoreFacade();
store.purchaseProduct("alice@example.com", "password123", 29.99);
// Output semplice da una sola chiamata, ma esegue molte operazioni
```

---

## 📚 Best Practice

✅ Usa **Singleton** per risorse globali (Logger, Config)  
✅ Usa **Factory** per creare famiglie di oggetti correlati  
✅ Usa **Observer** per loosely coupled communication  
✅ Usa **Adapter** quando integri codice legacy  
✅ Usa **Facade** per semplificare sistemi complessi  
✅ Impara quando usare ogni pattern (non usarli ovunque!)
"""
    }
]

# ==================== EXERCISE DATA ====================
EXERCISES_DATA = {
    1: {  # Modulo 1: Tipi di Dati e Operatori
        "multiple_choice": [
            {
                "q": "Quale tipo di dato occupa 32 bit ed è il più comune per interi?",
                "options": ["byte", "short", "int", "long"],
                "correct": 2,
                "explanation": "int occupa 32 bit. byte=8bit, short=16bit, long=64bit."
            },
            {
                "q": "Cosa restituisce l'operatore % (modulo)?",
                "options": ["La divisione intera", "Il resto della divisione", "Il prodotto", "La potenza"],
                "correct": 1,
                "explanation": "% restituisce il resto. Es: 10 % 3 = 1"
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Dichiara 3 variabili (int, double, boolean) e stampale in console.",
                "template": """public class TypeDeclaration {
    public static void main(String[] args) {
        // Dichiara int myInt, double myDouble, boolean myBool
        
        
        // Stampa le tre variabili
        
        
    }
}""",
                "solution_example": """public class TypeDeclaration {
    public static void main(String[] args) {
        // Dichiara int myInt, double myDouble, boolean myBool
        int myInt = 42;
        double myDouble = 3.14159;
        boolean myBool = true;
        
        // Stampa le tre variabili
        System.out.println("Int: " + myInt);
        System.out.println("Double: " + myDouble);
        System.out.println("Boolean: " + myBool);
    }
}""",
                "solution_check": ["int", "double", "boolean", "println"],
                "explanation": "Ottimo! Hai correttamente dichiarato i tipi primitivi."
            },
            {
                "level": 2,
                "description": "Calcola il resto della divisione di 17 per 5 usando l'operatore modulo e stampa il risultato.",
                "template": """public class ModuloChallenge {
    public static void main(String[] args) {
        // Usa l'operatore % per calcolare 17 % 5
        
        
    }
}""",
                "solution_example": """public class ModuloChallenge {
    public static void main(String[] args) {
        // Usa l'operatore % per calcolare 17 % 5
        int a = 17;
        int b = 5;
        int risultato = a % b;
        System.out.println("17 % 5 = " + risultato);
    }
}""",
                "solution_check": ["%", "println", "17"],
                "explanation": "Perfetto! 17 % 5 = 2"
            }
        ],
        "true_false": [
            {
                "statement": "Il tipo long occupa 64 bit e può memorizzare numeri più grandi di int",
                "correct": True,
                "explanation": "Vero. long usa 64 bit mentre int usa 32 bit."
            },
            {
                "statement": "In Java, l'operatore == confronta il valore per i tipi primitivi",
                "correct": True,
                "explanation": "Corretto. Per i tipi primitivi == confronta il valore. Per gli oggetti confronta il riferimento."
            },
            {
                "statement": "In Java, float è sempre più preciso di double",
                "correct": False,
                "explanation": "Falso. double è più preciso (64 bit) rispetto a float (32 bit)."
            },
            {
                "statement": "L'operatore && (AND logico) restituisce true solo se entrambe le condizioni sono vere",
                "correct": True,
                "explanation": "Esatto. && restituisce true solo se entrambi gli operandi sono true."
            }
        ]
    },
    2: {  # Modulo 2: Controllo di Flusso
        "multiple_choice": [
            {
                "q": "Quale ciclo esegue il blocco almeno una volta prima di controllare la condizione?",
                "options": ["for", "while", "do-while", "foreach"],
                "correct": 2,
                "explanation": "do-while esegue il blocco almeno una volta, poi controlla la condizione."
            },
            {
                "q": "Quale istruzione esce completamente da un ciclo?",
                "options": ["continue", "break", "return", "exit"],
                "correct": 1,
                "explanation": "break esce dal ciclo. continue salta all'iterazione successiva."
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Scrivi un ciclo for che stampi i numeri da 1 a 5.",
                "template": """public class ForLoop {
    public static void main(String[] args) {
        // Scrivi un ciclo for da 1 a 5
        
        
    }
}""",
                "solution_example": """public class ForLoop {
    public static void main(String[] args) {
        // Scrivi un ciclo for da 1 a 5
        for (int i = 1; i <= 5; i++) {
            System.out.println(i);
        }
    }
}""",
                "solution_check": ["for", "println", "i < 5", "i++"],
                "explanation": "Bene! Il ciclo for è corretto."
            },
            {
                "level": 2,
                "description": "Scrivi un ciclo while che stampi i numeri da 10 a 1 in ordine decrescente.",
                "template": """public class WhileLoop {
    public static void main(String[] args) {
        // Scrivi un ciclo while da 10 a 1
        
        
    }
}""",
                "solution_example": """public class WhileLoop {
    public static void main(String[] args) {
        // Scrivi un ciclo while da 10 a 1
        int i = 10;
        while (i >= 1) {
            System.out.println(i);
            i--;
        }
    }
}""",
                "solution_check": ["while", "println", "i--", "10"],
                "explanation": "Perfetto! Hai usato un ciclo while decrescente."
            }
        ],
        "true_false": [
            {
                "statement": "Il ciclo for serve quando conosci il numero di iterazioni",
                "correct": True,
                "explanation": "Vero. for è ideale quando sai quante volte iterare."
            },
            {
                "statement": "break e continue hanno lo stesso effetto",
                "correct": False,
                "explanation": "Falso. break esce dal ciclo, continue salta all'iterazione successiva."
            },
            {
                "statement": "Un ciclo while può non eseguirsi mai se la condizione è inizialmente falsa",
                "correct": True,
                "explanation": "Corretto. while controlla la condizione prima di eseguire."
            }
        ]
    },
    3: {  # Modulo 3: Array e Stringhe
        "multiple_choice": [
            {
                "q": "Quale è l'indice del primo elemento di un array?",
                "options": ["1", "0", "-1", "non definito"],
                "correct": 1,
                "explanation": "In Java gli indici partono da 0. Il primo elemento è array[0]."
            },
            {
                "q": "Quale metodo restituisce la lunghezza di una stringa?",
                "options": ["size()", "getLength()", "length()", "len()"],
                "correct": 2,
                "explanation": "length() restituisce il numero di caratteri. Array usa .length (senza parentesi)."
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Crea un array di 5 interi, popolalo con valori da 1 a 5, e stampa il primo e l'ultimo elemento.",
                "template": """public class ArrayBasics {
    public static void main(String[] args) {
        // Dichiara e inizializza un array di 5 interi
        
        
        // Stampa il primo elemento (indice 0)
        
        // Stampa l'ultimo elemento (indice 4)
        
    }
}""",
                "solution_example": """public class ArrayBasics {
    public static void main(String[] args) {
        // Dichiara e inizializza un array di 5 interi
        int[] array = {1, 2, 3, 4, 5};
        
        // Stampa il primo elemento (indice 0)
        System.out.println("Primo: " + array[0]);
        
        // Stampa l'ultimo elemento (indice 4)
        System.out.println("Ultimo: " + array[4]);
    }
}""",
                "solution_check": ["int[]", "new int[5]", "array[0]", "array[4]"],
                "explanation": "Ottimo! Hai correttamente acceduto agli elementi dell'array."
            },
            {
                "level": 2,
                "description": "Scrivi un programma che crea una stringa, la converte in maiuscole, e stampa la lunghezza.",
                "template": """public class StringManipulation {
    public static void main(String[] args) {
        // Dichiara una stringa
        
        
        // Converti in maiuscole
        
        // Stampa la lunghezza
        
    }
}""",
                "solution_example": """public class StringManipulation {
    public static void main(String[] args) {
        // Dichiara una stringa
        String str = "Java Programming";
        
        // Converti in maiuscole
        String maiuscola = str.toUpperCase();
        
        // Stampa la lunghezza
        System.out.println("Stringa: " + maiuscola);
        System.out.println("Lunghezza: " + maiuscola.length());
    }
}""",
                "solution_check": ["String", "toUpperCase()", "length()", "println"],
                "explanation": "Perfetto! Hai usato i metodi di String correttamente."
            }
        ],
        "true_false": [
            {
                "statement": "In Java gli array sono indicizzati da 0",
                "correct": True,
                "explanation": "Vero. array[0] è il primo elemento."
            },
            {
                "statement": "Per confrontare due stringhe devi usare ==",
                "correct": False,
                "explanation": "Falso. Usa equals() per confrontare il contenuto. == confronta il riferimento."
            },
            {
                "statement": "array.length è una proprietà (non un metodo)",
                "correct": True,
                "explanation": "Corretto. Array usa .length senza parentesi. String usa .length()."
            }
        ]
    },
    4: {  # Modulo 4: Oggetti e Classi
        "multiple_choice": [
            {
                "q": "Quale parola chiave crea un'istanza di una classe?",
                "options": ["class", "new", "instance", "create"],
                "correct": 1,
                "explanation": "new crea una nuova istanza e chiama il costruttore."
            },
            {
                "q": "Quale modificatore protegge i dati da accessi non autorizzati?",
                "options": ["public", "protected", "private", "final"],
                "correct": 2,
                "explanation": "private rende visibile solo dentro la classe. public è accessibile da ovunque."
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Crea una classe Person con attributi name e age, un costruttore, e un metodo toString().",
                "template": """public class Person {
    // Attributi
    
    
    // Costruttore
    
    
    // Metodo toString
    
    
}""",
                "solution_example": """public class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\\'' +
                ", age=" + age +
                '}';
    }
}""",
                "solution_check": ["String name", "int age", "public Person", "toString"],
                "explanation": "Bene! Hai creato una classe OOP corretta."
            },
            {
                "level": 2,
                "description": "Crea una classe Account con attributi privati, getter/setter, e un metodo deposit().",
                "template": """public class Account {
    // Attributi privati
    
    
    // Getter e setter
    
    
    // Metodo deposit
    
    
}""",
                "solution_example": """public class Account {
    private double balance;
    
    public Account(double initialBalance) {
        this.balance = initialBalance;
    }
    
    public double getBalance() {
        return balance;
    }
    
    public void setBalance(double balance) {
        if (balance >= 0) {
            this.balance = balance;
        }
    }
    
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Depositato: €" + amount);
        }
    }
}""",
                "solution_check": ["private", "double balance", "getBalance", "setBalance", "deposit"],
                "explanation": "Perfetto! Hai applicato l'incapsulamento."
            }
        ],
        "true_false": [
            {
                "statement": "Un oggetto è un'istanza di una classe",
                "correct": True,
                "explanation": "Vero. Una classe è il modello, un oggetto è l'istanza."
            },
            {
                "statement": "I metodi privati possono essere chiamati da altre classi",
                "correct": False,
                "explanation": "Falso. private limita l'accesso solo alla stessa classe."
            },
            {
                "statement": "Il costruttore viene sempre chiamato automaticamente quando crei un oggetto",
                "correct": True,
                "explanation": "Corretto. new istanzia l'oggetto e chiama il costruttore."
            }
        ]
    },
    5: {  # Modulo 5: Eccezioni
        "multiple_choice": [
            {
                "q": "Quale blocco viene eseguito sempre, anche se c'è un'eccezione?",
                "options": ["try", "catch", "finally", "else"],
                "correct": 2,
                "explanation": "finally si esegue sempre, con o senza eccezioni."
            },
            {
                "q": "Quale eccezione viene lanciata quando accedi a un indice inesistente?",
                "options": ["IOException", "NullPointerException", "ArrayIndexOutOfBoundsException", "IllegalArgumentException"],
                "correct": 2,
                "explanation": "ArrayIndexOutOfBoundsException quando accedi oltre i limiti dell'array."
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Scrivi un try-catch che catturi ArrayIndexOutOfBoundsException quando accedi a un indice invalido.",
                "template": """public class ExceptionHandling {
    public static void main(String[] args) {
        int[] numeri = {1, 2, 3};
        try {
            // Accedi a un indice invalido
            
            
        } catch (ArrayIndexOutOfBoundsException e) {
            // Stampa il messaggio di errore
            
            
        }
    }
}""",
                "solution_check": ["try", "catch", "numeri[10]", "e.getMessage"],
                "explanation": "Buono! Hai correttamente catturato l'eccezione."
            },
            {
                "level": 2,
                "description": "Crea un metodo che lancia un'eccezione personalizzata quando un numero è negativo.",
                "template": """class NegativeNumberException extends Exception {
    public NegativeNumberException(String message) {
        super(message);
    }
}

public class CustomException {
    public static void checkPositive(int num) throws NegativeNumberException {
        // Lancia eccezione se negativo
        
        
    }
    
    public static void main(String[] args) {
        try {
            checkPositive(-5);
        } catch (NegativeNumberException e) {
            System.out.println(e.getMessage());
        }
    }
}""",
                "solution_check": ["throws", "throw new", "NegativeNumberException", "if (num < 0)"],
                "explanation": "Perfetto! Hai creato un'eccezione personalizzata."
            }
        ],
        "true_false": [
            {
                "statement": "try-catch serve per gestire le eccezioni",
                "correct": True,
                "explanation": "Vero. try contiene il codice che potrebbe lanciare, catch la gestisce."
            },
            {
                "statement": "Se non catturi un'eccezione, il programma continua normalmente",
                "correct": False,
                "explanation": "Falso. Se non catturi, il programma crasha."
            },
            {
                "statement": "finally è sempre eseguito, anche se c'è un return nel catch",
                "correct": True,
                "explanation": "Corretto. finally si esegue sempre prima di uscire dal metodo."
            }
        ]
    },
    6: {  # Modulo 6: Collections Framework
        "multiple_choice": [
            {
                "q": "Quale collection mantiene l'ordine di inserimento?",
                "options": ["HashSet", "HashMap", "ArrayList", "TreeSet"],
                "correct": 2,
                "explanation": "ArrayList mantiene l'ordine. HashSet no, TreeSet ordina alfabeticamente."
            },
            {
                "q": "Quale metodo aggiungi un elemento a una ArrayList?",
                "options": ["insert()", "push()", "add()", "put()"],
                "correct": 2,
                "explanation": "add() aggiunge a ArrayList. put() è per HashMap."
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Crea una ArrayList di stringhe, aggiungi 3 nomi, e stampa tutti usando for-each.",
                "template": """import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        // Crea ArrayList<String>
        
        
        // Aggiungi tre nomi
        
        
        
        // Stampa con for-each
        
        
    }
}""",
                "solution_check": ["ArrayList", "String", "add", "for (String", "println"],
                "explanation": "Ottimo! Hai usato ArrayList correttamente."
            },
            {
                "level": 2,
                "description": "Crea una HashMap che mappa nomi a età, aggiungi 3 persone, e stampa tutte le coppie.",
                "template": """import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        // Crea HashMap<String, Integer>
        
        
        // Aggiungi tre persone (nome, età)
        
        
        
        // Stampa con iterator
        for (String nome : map.keySet()) {
            System.out.println(nome + ": " + map.get(nome));
        }
    }
}""",
                "solution_check": ["HashMap", "String", "Integer", "put", "keySet"],
                "explanation": "Perfetto! Hai usato HashMap con accesso alle coppie."
            }
        ],
        "true_false": [
            {
                "statement": "ArrayList permette duplicati",
                "correct": True,
                "explanation": "Vero. ArrayList è una lista, permette elementi uguali."
            },
            {
                "statement": "HashSet mantiene l'ordine di inserimento",
                "correct": False,
                "explanation": "Falso. HashSet non garantisce ordine. LinkedHashSet sì."
            },
            {
                "statement": "HashMap mappa chiavi a valori",
                "correct": True,
                "explanation": "Corretto. HashMap è una struttura chiave-valore."
            }
        ]
    },
    7: {  # Modulo 7: I/O
        "multiple_choice": [
            {
                "q": "Quale classe usi per leggere un file di testo?",
                "options": ["FileWriter", "BufferedReader", "FileOutputStream", "ObjectOutputStream"],
                "correct": 1,
                "explanation": "BufferedReader legge un file di testo. FileWriter scrive."
            },
            {
                "q": "Qual è il vantaggio di try-with-resources?",
                "options": ["Più sicuro", "Chiude automaticamente le risorse", "Più veloce", "Più leggibile"],
                "correct": 1,
                "explanation": "try-with-resources chiude automaticamente file, stream, ecc."
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Scrivi un programma che salva testo su un file usando PrintWriter.",
                "template": """import java.io.PrintWriter;

public class FileWriteExample {
    public static void main(String[] args) {
        try {
            // Crea PrintWriter per il file
            
            
            // Scrivi tre righe
            
            
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}""",
                "solution_check": ["PrintWriter", "println", "close", "try"],
                "explanation": "Bene! Hai scritto correttamente su un file."
            },
            {
                "level": 2,
                "description": "Scrivi un programma che legge un file e stampa tutte le righe in reverse.",
                "template": """import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class FileReadExample {
    public static void main(String[] args) {
        ArrayList<String> linee = new ArrayList<>();
        try {
            // Leggi il file
            
            
            
            // Stampa in reverse
            for (int i = linee.size() - 1; i >= 0; i--) {
                System.out.println(linee.get(i));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}""",
                "solution_check": ["BufferedReader", "FileReader", "readLine", "ArrayList", "for"],
                "explanation": "Perfetto! Hai letto il file e stampato in reverse."
            }
        ],
        "true_false": [
            {
                "statement": "IOException è un'eccezione checked che devi catturare",
                "correct": True,
                "explanation": "Vero. IOException deve essere catturata o dichiarata con throws."
            },
            {
                "statement": "BufferedReader è più veloce di FileReader",
                "correct": True,
                "explanation": "Corretto. BufferedReader usa un buffer per migliori performance."
            },
            {
                "statement": "try-with-resources chiude automaticamente le risorse",
                "correct": True,
                "explanation": "Esatto. Non devi chiamare .close() manualmente."
            }
        ]
    },
    8: {  # Modulo 8: Java Time API
        "multiple_choice": [
            {
                "q": "Quale classe Java usі per memorizzare solo una data (senza ora)?",
                "options": ["LocalTime", "LocalDateTime", "LocalDate", "ZonedDateTime"],
                "correct": 2,
                "explanation": "LocalDate memorizza solo la data. LocalDateTime ha anche ora."
            },
            {
                "q": "Come ottieni la data attuale?",
                "options": ["new Date()", "LocalDate.today()", "LocalDate.now()", "System.currentDate()"],
                "correct": 2,
                "explanation": "LocalDate.now() restituisce la data odierna."
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Crea una LocalDate di Natale 2024 e stampa il giorno della settimana.",
                "template": """import java.time.LocalDate;

public class DateExample {
    public static void main(String[] args) {
        // Crea la data di Natale 2024
        
        
        // Stampa il giorno della settimana
        
        
    }
}""",
                "solution_check": ["LocalDate", "of", "2024", "12", "25", "getDayOfWeek", "println"],
                "explanation": "Ottimo! Hai creato e manipolato una data correttamente."
            },
            {
                "level": 2,
                "description": "Calcola i giorni tra oggi e il prossimo anno nuovo, usando Period.",
                "template": """import java.time.LocalDate;
import java.time.Period;

public class PeriodExample {
    public static void main(String[] args) {
        LocalDate oggi = LocalDate.now();
        LocalDate capodanno = LocalDate.of(2025, 1, 1);
        
        // Calcola il periodo tra le due date
        
        
        // Stampa i giorni rimasti
        
        
    }
}""",
                "solution_check": ["Period", "between", "getDays", "println"],
                "explanation": "Perfetto! Hai usato Period per calcolare la differenza."
            }
        ],
        "true_false": [
            {
                "statement": "LocalDate è thread-safe",
                "correct": True,
                "explanation": "Vero. Java Time API è thread-safe, a differenza di Date."
            },
            {
                "statement": "Duration misura la differenza tra due date",
                "correct": False,
                "explanation": "Falso. Duration misura tra istanti (orari). Period misura tra date."
            },
            {
                "statement": "ZonedDateTime tiene conto del fuso orario",
                "correct": True,
                "explanation": "Corretto. ZonedDateTime include il fuso orario."
            }
        ]
    },
    9: {  # Modulo 9: Generics
        "multiple_choice": [
            {
                "q": "Quale è il vantaggio principale dei Generics?",
                "options": ["Performance", "Type safety", "Minore memoria", "Meno righe di codice"],
                "correct": 1,
                "explanation": "Generics forniscono type safety a compile-time, evitando casting."
            },
            {
                "q": "Cosa significa <T> in una classe generica?",
                "options": ["Una variabile", "Un placeholder per un tipo", "Una costante", "Una collezione"],
                "correct": 1,
                "explanation": "T è un type parameter che sarà sostituito al momento dell'utilizzo."
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Crea una classe generica Box<T> con metodi get() e set().",
                "template": """public class Box<T> {
    private T content;
    
    // Costruttore
    
    
    // Metodo get
    
    
    // Metodo set
    
    
}""",
                "solution_check": ["<T>", "private T", "getContent", "setContent", "public"],
                "explanation": "Bene! Hai creato una classe generica corretta."
            },
            {
                "level": 2,
                "description": "Crea un metodo generico che stampa gli elementi di un array.",
                "template": """public class GenericMethods {
    public static <T> void printArray(T[] array) {
        // Itera sull'array e stampa ogni elemento
        
        
        
    }
    
    public static void main(String[] args) {
        Integer[] numeri = {1, 2, 3};
        String[] parole = {"A", "B", "C"};
        
        printArray(numeri);
        printArray(parole);
    }
}""",
                "solution_check": ["<T>", "printArray", "for", "array", "println"],
                "explanation": "Perfetto! Hai creato un metodo generico riusabile."
            }
        ],
        "true_false": [
            {
                "statement": "I Generics forniscono type-checking a compile-time",
                "correct": True,
                "explanation": "Vero. Il compilatore verifica i tipi prima dell'esecuzione."
            },
            {
                "statement": "Puoi usare int come type parameter in Generics",
                "correct": False,
                "explanation": "Falso. Devi usare Integer (classe wrapper), non int (primitivo)."
            },
            {
                "statement": "ArrayList<String> e ArrayList<Integer> sono lo stesso tipo a runtime",
                "correct": True,
                "explanation": "Corretto. I Generics sono rimossi in runtime (type erasure)."
            }
        ]
    },
    10: {  # Modulo 10: Lambda
        "multiple_choice": [
            {
                "q": "Una lambda richiede quale tipo di interfaccia?",
                "options": ["Interfaccia normale", "Interfaccia funzionale", "Classe astratta", "Interface generica"],
                "correct": 1,
                "explanation": "Una interfaccia funzionale ha esattamente 1 metodo astratto."
            },
            {
                "q": "Quale sintassi è corretta per una lambda senza parametri?",
                "options": ["() -> x", "() -> { return x; }", "-> {}", "() -> System.out.println()"],
                "correct": 3,
                "explanation": "La sintassi corretta è () -> corpo, dove () significa nessun parametro."
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Crea un'interfaccia funzionale Greet e usa una lambda per implementarla.",
                "template": """@FunctionalInterface
interface Greet {
    void sayHello(String name);
}

public class LambdaExample {
    public static void main(String[] args) {
        // Crea una lambda che implementa Greet
        
        
        
        // Chiama il metodo
        
        
    }
}""",
                "solution_check": ["@FunctionalInterface", "Greet", "->", "sayHello"],
                "explanation": "Ottimo! Hai usato una lambda con un'interfaccia funzionale."
            },
            {
                "level": 2,
                "description": "Usa una lambda con ArrayList forEach per stampare i numeri del 1 al 5.",
                "template": """import java.util.ArrayList;

public class LambdaArrayList {
    public static void main(String[] args) {
        ArrayList<Integer> numeri = new ArrayList<>();
        for (int i = 1; i <= 5; i++) {
            numeri.add(i);
        }
        
        // Usa forEach con lambda
        
        
    }
}""",
                "solution_check": ["forEach", "->", "System.out.println", "numeri"],
                "explanation": "Perfetto! Hai usato lambda con forEach."
            }
        ],
        "true_false": [
            {
                "statement": "Una lambda è una funzione anonima che implementa un'interfaccia funzionale",
                "correct": True,
                "explanation": "Vero. Le lambda sono funzioni anonime e brevi."
            },
            {
                "statement": "Puoi usare una lambda con qualsiasi interfaccia",
                "correct": False,
                "explanation": "Falso. L'interfaccia deve essere funzionale (1 solo metodo astratto)."
            },
            {
                "statement": "Method references sono un'alternativa più concisa alle lambda",
                "correct": True,
                "explanation": "Corretto. Es: System.out::println invece di x -> System.out.println(x)"
            }
        ]
    },
    11: {  # Modulo 11: Design Pattern
        "multiple_choice": [
            {
                "q": "Quale pattern garantisce una sola istanza di una classe?",
                "options": ["Factory", "Observer", "Singleton", "Adapter"],
                "correct": 2,
                "explanation": "Singleton garantisce un'unica istanza globale."
            },
            {
                "q": "Quale pattern notifica più oggetti di un cambiamento?",
                "options": ["Singleton", "Factory", "Observer", "Facade"],
                "correct": 2,
                "explanation": "Observer implementa il pattern publish-subscribe."
            }
        ],
        "coding_challenges": [
            {
                "level": 1,
                "description": "Implementa il pattern Singleton per una classe Config.",
                "template": """public class Config {
    // Istanza statica privata
    
    
    // Costruttore privato
    
    
    // Metodo getInstance
    
    
    
    // Metodo di esempio
    public void printConfig() {
        System.out.println("Configurazione caricata");
    }
}""",
                "solution_check": ["private static", "getInstance", "private Config", "instance"],
                "explanation": "Bene! Hai implementato il pattern Singleton."
            },
            {
                "level": 2,
                "description": "Implementa il pattern Factory per creare diversi tipi di animali.",
                "template": """interface Animal {
    void sound();
}

class Dog implements Animal {
    public void sound() { System.out.println("Bau!"); }
}

class Cat implements Animal {
    public void sound() { System.out.println("Miao!"); }
}

public class AnimalFactory {
    // Metodo factory
    public static Animal createAnimal(String type) {
        // Ritorna l'animale corretto basato su type
        
        
        
        return null;
    }
    
    public static void main(String[] args) {
        Animal dog = AnimalFactory.createAnimal("dog");
        dog.sound();
    }
}""",
                "solution_check": ["createAnimal", "if", "Dog", "Cat", "Animal"],
                "explanation": "Perfetto! Hai implementato il pattern Factory."
            }
        ],
        "true_false": [
            {
                "statement": "Il pattern Singleton è utile per logger e configurazioni",
                "correct": True,
                "explanation": "Vero. Singleton garantisce una sola istanza globale."
            },
            {
                "statement": "Il pattern Factory ti permette di creare oggetti senza specificare la classe esatta",
                "correct": True,
                "explanation": "Corretto. Factory astrae la creazione di oggetti."
            },
            {
                "statement": "Il pattern Adapter converte un'interfaccia in un'altra",
                "correct": True,
                "explanation": "Esatto. Adapter adatta classi incompatibili."
            }
        ]
    }
}

# ==================== EXERCISE FUNCTIONS ====================
def show_multiple_choice(module_id: int):
    """Mostra esercizio multiple choice"""
    st.markdown(f"### 📝 Esercizio Multiple Choice")
    
    exercises = EXERCISES_DATA.get(module_id, {}).get("multiple_choice", [])
    if not exercises:
        st.info("Nessun esercizio disponibile per questo modulo.")
        return False
    
    q = exercises[0]
    
    response = st.radio(
        q["q"],
        q["options"],
        key=f"mc_q_{module_id}"
    )
    
    if st.button("Verifica Risposta", key=f"mc_btn_{module_id}"):
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

def execute_java_code(code: str) -> tuple[bool, str]:
    """
    Esegue codice Java usando TutorialsPoint API (online)
    Ritorna (successo, output/errore)
    """
    import requests
    import json
    
    # API TutorialsPoint - Gratuito e affidabile
    url = "https://api.tutorialspoint.com/api/v1/execution/execute"
    
    # Assicurati che la classe sia "Main"
    modified_code = code
    if "public class" in code:
        import re
        class_match = re.search(r'public\s+class\s+(\w+)', code)
        if class_match:
            old_name = class_match.group(1)
            if old_name != "Main":
                modified_code = code.replace(f"public class {old_name}", "public class Main")
    
    payload = {
        "language": "java",
        "code": modified_code,
        "stdin": ""
    }
    
    try:
        response = requests.post(url, json=payload, timeout=15)
        
        if response.status_code == 200:
            result = response.json()
            
            # Controlla se c'è un output
            if result.get("output"):
                return True, result.get("output", "")
            elif result.get("error"):
                return False, result.get("error", "Errore sconosciuto")
            else:
                return True, "(Nessun output)"
        else:
            return False, f"Errore API: Status {response.status_code}"
            
    except requests.exceptions.Timeout:
        return False, "Timeout: Il codice ha impiegato troppo tempo"
    except requests.exceptions.ConnectionError:
        return False, "Errore di connessione. Controlla la tua connessione internet."
    except Exception as e:
        return False, f"Errore: {str(e)}\n\nAssicurati che il codice sia sintatticamente corretto!"


def show_coding_challenge(module_id: int, level: int = 1):
    """Mostra coding challenge con editor e output in due colonne"""
    st.markdown(f"### 💻 Coding Challenge - Livello {level}")
    
    exercises = EXERCISES_DATA.get(module_id, {}).get("coding_challenges", [])
    if not exercises or level > len(exercises):
        st.info("Nessun esercizio di coding disponibile.")
        return False
    
    challenge = exercises[level - 1]
    
    st.markdown(f"**Descrizione:**\n{challenge['description']}")
    
    with st.expander("📋 Template Codice"):
        st.code(challenge["template"], language="java")
    
    # Salva il codice nello session_state
    code_key = f"code_{module_id}_{level}"
    if code_key not in st.session_state:
        st.session_state[code_key] = ""
    
    # Dividi in due colonne: Editor e Output
    col_editor, col_output = st.columns([1, 1], gap="medium")
    
    with col_editor:
        st.markdown("### 📝 Editor di Codice")
        code_input = st.text_area(
            "Scrivi il tuo codice Java:",
            height=350,
            value=st.session_state[code_key],
            key=code_key,
            on_change=lambda: st.session_state.update({code_key: st.session_state[code_key]})
        )
    
    with col_output:
        st.markdown("### 📤 Output del Programma")
        output_container = st.container()
    
    # Bottoni sotto l'editor
    st.markdown("---")
    col_run, col_verify = st.columns(2, gap="medium")
    
    with col_run:
        if st.button("▶️ Esegui Codice", use_container_width=True, key=f"run_btn_{module_id}_{level}"):
            if code_input.strip():
                with col_output:
                    with st.spinner("⏳ Esecuzione del codice in corso..."):
                        success, output = execute_java_code(code_input)
                        
                        if success:
                            st.success("✅ Esecuzione Completata!")
                            # Styling per l'output di successo
                            st.markdown(f"""
                            <div style="
                                background-color: #ffffff;
                                color: #000000;
                                padding: 15px;
                                border-radius: 8px;
                                border: 2px solid #10b981;
                                font-family: 'Courier New', monospace;
                                font-size: 14px;
                                white-space: pre-wrap;
                                word-wrap: break-word;
                                line-height: 1.5;
                            ">{output}</div>
                            """, unsafe_allow_html=True)
                        else:
                            st.error("❌ Errore nell'Esecuzione")
                            # Styling per l'output di errore
                            st.markdown(f"""
                            <div style="
                                background-color: #fff5f5;
                                color: #c53030;
                                padding: 15px;
                                border-radius: 8px;
                                border: 2px solid #fc8181;
                                font-family: 'Courier New', monospace;
                                font-size: 14px;
                                white-space: pre-wrap;
                                word-wrap: break-word;
                                line-height: 1.5;
                            ">{output}</div>
                            """, unsafe_allow_html=True)
            else:
                st.warning("⚠️ Scrivi del codice prima di eseguirlo!")
    
    with col_verify:
        if st.button("✔️ Verifica Soluzione", use_container_width=True, key=f"code_btn_{module_id}_{level}"):
            if not code_input.strip():
                st.warning("⚠️ Scrivi del codice prima di verificare!")
            else:
                checks_passed = sum(1 for check in challenge['solution_check'] if check.lower() in code_input.lower())
                
                if checks_passed >= len(challenge['solution_check']) * 0.7:
                    st.markdown(f"""
                    <div class="success-box">
                    <strong>✅ Soluzione Accettata!</strong><br>
                    {challenge['explanation']}<br><br>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Mostra soluzione di esempio
                    st.markdown("### 📚 Esempio di Soluzione Corretta:")
                    st.code(challenge["solution_example"], language="java")
                    
                    if level < len(exercises):
                        st.markdown("---")
                        if st.button(f"→ Prossimo Livello Coding (Livello {level + 1})", key=f"next_{module_id}_{level}"):
                            st.session_state.course_state["current_exercise_level"] = level + 1
                            st.rerun()
                    else:
                        st.success("🎉 Hai completato tutti gli esercizi di coding per questo modulo!")
                    
                    return True
                else:
                    st.markdown(f"""
                    <div class="error-box">
                    <strong>⚠️ Soluzione Incompleta</strong><br>
                    Hai implementato {checks_passed}/{len(challenge['solution_check'])} elementi richiesti.<br>
                    Suggerimento: Assicurati di includere tutti gli elementi: {', '.join(challenge['solution_check'])}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("### 📚 Esempio di Soluzione Corretta:")
                    st.code(challenge["solution_example"], language="java")
                    
                    return False

def show_true_false(module_id: int):
    """Mostra esercizio vero/falso"""
    st.markdown(f"### ✓/✗ Vero o Falso")
    
    exercises = EXERCISES_DATA.get(module_id, {}).get("true_false", [])
    if not exercises:
        st.info("Nessun esercizio vero/falso disponibile.")
        return False
    
    answers = {}
    for idx, stmt in enumerate(exercises):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{idx + 1}. {stmt['statement']}**")
        with col2:
            answers[idx] = st.radio("", ["Vero", "Falso"], key=f"tf_{module_id}_{idx}", horizontal=True)
    
    if st.button("Verifica Risposte", key=f"tf_btn_{module_id}"):
        score = 0
        for idx, stmt in enumerate(exercises):
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
        <strong>Risultato:</strong> {score}/{len(exercises)} risposte corrette
        </div>
        """, unsafe_allow_html=True)
        
        return score == len(exercises)

# ==================== MAIN APP ====================
def main():
    # Header
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("# ☕")
    with col2:
        st.markdown("# Java SE Interactive Course")
    
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 📊 Progresso del Corso")
        
        total_modules = len(COURSE_MODULES)
        completed = len(st.session_state.course_state["modules_completed"])
        
        st.metric("Moduli Completati", f"{completed}/{total_modules}")
        st.metric("Esercizi Completati", len(st.session_state.course_state["exercises_completed"]))
        st.metric("Punteggio Totale", f"{st.session_state.course_state['score']} punti")
        
        progress = completed / total_modules if total_modules > 0 else 0
        st.progress(progress, text=f"{int(progress*100)}%")
        
        st.markdown("---")
        st.markdown("### 🎓 Moduli del Corso")
        
        for idx, module in enumerate(COURSE_MODULES):
            completed_marker = "✅" if idx in st.session_state.course_state["modules_completed"] else "⭕"
            if st.button(f"{completed_marker} {idx+1}. {module['title'][:30]}", key=f"sidebar_{idx}", use_container_width=True):
                st.session_state.course_state["current_module"] = idx
                st.session_state.course_state["current_exercise_level"] = 1
                st.rerun()
        
        st.markdown("---")
        if st.button("🔄 Resetta Corso", use_container_width=True):
            st.session_state.course_state = {
                "current_module": 0,
                "modules_completed": {},
                "exercises_completed": {},
                "score": 0,
                "started": False,
                "current_exercise_level": 1,
                "show_hint": {}
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
            <li><strong>📚 Lezioni teoriche complete</strong> con spiegazioni dal materiale ALTEN</li>
            <li><strong>🔄 Esempi comparati con Python</strong> per migliore comprensione</li>
            <li><strong>📝 Esercizi Multiple Choice</strong> per verificare la teoria</li>
            <li><strong>💻 Coding Challenges progressivi</strong> con validazione del codice</li>
            <li><strong>✓ Esercizi Vero/Falso</strong> per consolidare i concetti</li>
        </ul>
        
        <h3>📋 Struttura del Corso:</h3>
        <p><strong>11 moduli progressivi</strong> da Intermedio ad Avanzato, con <strong>44 ore</strong> di contenuti.</p>
        
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Inizia il Corso", use_container_width=True, key="start"):
            st.session_state.course_state["started"] = True
            st.rerun()
    
    else:
        current_module = st.session_state.course_state["current_module"]
        module = COURSE_MODULES[current_module]
        
        st.markdown(f"### Modulo {current_module + 1}: {module['title']}")
        st.markdown(f"**⏱️ Durata:** {module['hours']} ore")
        st.markdown("---")
        
        tab1, tab2, tab3, tab4 = st.tabs(["📚 Lezione", "📝 Multiple Choice", "💻 Coding", "✓ Vero/Falso"])
        
        with tab1:
            st.markdown(f"<div class='lesson-box'>", unsafe_allow_html=True)
            st.markdown(module["content"])
            st.markdown("</div>", unsafe_allow_html=True)
        
        with tab2:
            show_multiple_choice(current_module + 1)
        
        with tab3:
            show_coding_challenge(current_module + 1, st.session_state.course_state["current_exercise_level"])
        
        with tab4:
            show_true_false(current_module + 1)
        
        st.markdown("---")
        
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
