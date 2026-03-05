
---

# Python Sentence Generator client-side executed, with Pyodide.

### index.html

Defines the UI structure:

- chat interface
- avatar
- feedback buttons
- code viewer panel


---

### style.css

Controls the visual layout:

- responsive design
- gradient background
- central container
- chat bubbles
- code panel styling


---

### main.js

Frontend controller.

Responsibilities:

- initialize Pyodide
- load Python code
- manage UI state
- control bot thinking delay
- display generated sentences
- handle user feedback


---

### generator.py

Core procedural generation engine.

Responsibilities:

- load vocabulary data
- compute semantic compatibility
- apply grammatical rules
- build final sentence


---

### verbs.json

Verb conjugations used by the generator.


---

### voc.json

Vocabulary and semantic attributes.

Each word contains weighted semantic categories.


---

### particles.json

Contains grammatical particles:

- subjects
- prepositions
- articles


---

# Interactive Flow

The user experience works as follows:

1. The bot "thinks" for 3–4 seconds
2. A sentence is generated
3. The user evaluates it:

👍 makes sense  
👎 nonsense

4. The bot generates a new sentence


---

# Technologies Used

- Python
- Pyodide
- JavaScript
- HTML5
- CSS3
- GitHub Pages


---

# Why Pyodide?

Pyodide allows Python to run inside the browser using WebAssembly.

This means:

- instant deployment
- freedom to use scientific libraries directly in the browser (as JupyterLite)
- no backend server, fully client-side execution - means less latency, lower costs, scalability and security by design


---

# Info

Created as a procedural generation and browser-Python experiment.
