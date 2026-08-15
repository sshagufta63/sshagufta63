# AI-52 Bootcamp

## Week 01 – Think Like an AI Engineer

### Week Goal

Understand how modern AI systems work from a software engineer's perspective rather than just learning AI terminology. By the end of this week, I should be able to explain the journey of a prompt from a user to an LLM and understand the role of prompts, context, APIs, and local models.

---

## Progress

### Environment Setup ✅

* [x] Python Installed
* [x] VS Code Installed
* [x] Git Installed
* [x] GitHub Repository Created
* [x] Ollama Installed
* [ ] First Local Model Executed
* [ ] First Python Program using AI
* [ ] Week 1 Mini Project Completed

---

## Day 01

### Objective

Set up the development environment and begin understanding how LLMs think and respond.

### Tasks Completed

* [x] Created AI-52 GitHub repository
* [x] Installed Python
* [x] Installed VS Code
* [x] Installed Git
* [x] Installed Ollama
* [x] Created `hello_ai.py`
* [x] Printed first Python program

---

## Today's Learning

### Key Takeaways

* LLMs are prediction engines, not execution engines.
* The quality of a response depends heavily on the prompt and the context provided.
* LLMs do not learn from individual conversations in real time.
* There is an important distinction between model training, conversation context, and persistent memory.
* AI systems become more reliable when LLMs are combined with external tools and verification.

---

## Questions Explored

### Why can an LLM write code if it only predicts the next token?

My understanding:

> LLMs are trained on enormous amounts of text, including programming languages, documentation, SQL, books, and technical content. They learn patterns in that data and generate the next most likely token based on those learned patterns.

Refinement:

> LLMs don't truly "know" Java or SQL. They generate outputs that resemble the patterns they learned during training. External tools such as compilers, databases, and test runners are needed to verify correctness.

---

### Why doesn't an LLM learn from every conversation?

My understanding:

> The model itself is not updated during a conversation. Instead, the current conversation and any available memory are supplied as context before generating a response.

Key concepts learned:

* Model Training
* Conversation Context
* Persistent Memory
* Retrieval-Augmented Generation (RAG)

---

## Files Created

```text
Week01/
├── README.md
├── Day01/
│   └── hello_ai.py
└── Notes/
```

---

## Reflection

### What surprised me?

That ChatGPT does not become smarter during a conversation. It relies on context and retrieved memory rather than changing the model itself.

### What confused me?

The distinction between model memory, conversation context, persistent memory, and how RAG ties them together. I expect this will become clearer in later weeks.

### How can I apply this at work?

I can already see opportunities to build an AI assistant for BigQuery SQL optimization by combining an LLM with company knowledge, SQL best practices, and query history instead of expecting the LLM to "know" everything.

---

## Tomorrow

* Run a local model using Ollama
* Experiment with prompt engineering
* Observe how different prompts change responses
* Build the first Python application that communicates with an LLM

---

## Weekly Status

**Week:** 1 of 52

**Progress:** ███░░░░░░░ 30%

**Current Focus:** Building a strong mental model of how AI systems work.
