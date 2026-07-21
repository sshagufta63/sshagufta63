# Wednesday

## Objective

Understand how a Python application communicates with a local LLM using Ollama and recognize that AI integration is fundamentally another API integration.

---

## Topics Covered

* Ollama Python Library
* Local LLM Integration
* AI API Calls
* Prompt → Response Flow
* Model Parameter
* Prompt Iteration

---

## Coding Challenges Completed

* [x] Connected Python to Ollama
* [x] Executed first prompt using a local LLM
* [x] Changed prompts and observed different responses
* [x] Executed multiple prompts using a loop
* [x] Stored Day 3 code in GitHub

---

## Key Learnings

* Calling an LLM from Python is similar to calling any other service through an API.
* The prompt changes the response, while the API call remains the same.
* The model is selected through a parameter rather than requiring changes to the application logic.
* A well-designed application should allow models to be swapped with minimal code changes.

---

## Question of the Day

### What did I learn?

Changing the model should not require rewriting the application. The application communicates through a stable interface, while the selected model is a configurable component.

Different models may produce different responses because they have different training data and capabilities, but the application's communication pattern remains unchanged.

---

## Reflection

### What surprised me?

Interacting with a local LLM from Python was much simpler than expected. It felt like integrating with any other service.

### What confused me?

Initially, I mixed up the concepts of the **model** and the **API**. I now understand that the API is the communication interface, while the model is the component that generates responses.

### How can I apply this at work?

I can build Java or Python applications that treat AI models as interchangeable backend services. This makes it easier to experiment with different models without redesigning the application.

---

## Files Created

```text
Week01/
└── Day03/
    ├── challenge1.py
    ├── challenge2.py
    ├── challenge3.py
    └── notes.md
```

---

## Progress

### Week 1 Status

| Day       | Status          |
| --------- | --------------- |
| Monday    | ✅ Completed     |
| Tuesday   | ✅ Completed     |
| Wednesday | ✅ Completed     |
| Thursday  | ⬜ Pending       |
| Friday    | ⬜ Pending       |
| Saturday  | ⬜ Pending       |
| Sunday    | ⬜ Review & Quiz |

**Overall Progress:** 3 of 7 days completed (≈43%)
