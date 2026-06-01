# i nik — AI Character Interaction Prototype

i nik is an AI chatbot prototype designed as a behavioral character system for a beverage shop.

Instead of functioning as a traditional assistant, i nik is designed as a character that gradually develops familiarity with users through conversation, memory, relationship signals, and reward mechanics.

---

## Project Goal

The objective of this project is to explore how AI characters can create stronger user engagement through:

* Personality progression
* Memory systems
* Relationship modeling
* Gamification loops
* Behavioral prompting

This project is built as a portfolio piece for AI Agent Development and Applied AI Product Design.

---

## Core Features

### Behavioral Stage System

i nik changes its behavior according to an Intimacy Score.

Stages:

#### Observer

* Curious
* Polite
* Observant
* Asks questions
* Learning about the user

#### Gremlin

* More playful
* Teasing
* Uses inside jokes
* References previous conversations

#### Treasure

* Warm
* Familiar
* Emotionally attentive
* Values shared memories

---

### Memory System

The project currently contains three memory layers.

#### Recent Chat Memory

Stores recent conversation history and injects it into prompts.

Purpose:

* Context continuity
* Less repetitive conversations
* More natural follow-up responses

#### Fact Memory

Stores simple user facts extracted from conversation.

Examples:

* Name
* Preferences
* Interests

Purpose:

* Personalized interactions
* Character consistency
* Direct recall of important user information

#### Persistent JSON Memory

Stores selected memory data outside the current chat session.

Saved data includes:

* User facts
* Intimacy score
* Points
* Relationship state
* Reward inventory

Purpose:

* Prevents important prototype state from resetting
* Supports repeated testing
* Demonstrates a path toward long-term memory architecture

---

### Relationship Engine

The system tracks three relationship dimensions.

#### Trust

How much personal or emotional information the user shares.

#### Familiarity

How often the user interacts with i nik.

#### Curiosity

How interested i nik becomes in the user's patterns, questions, and stories.

These values are exposed in the UI and injected into prompts to guide response behavior.

---

### Gamification System

The chatbot contains a lightweight reward loop.

Features:

* Point accumulation
* Variable rewards
* Inventory system

Examples of collectible items:

* Blue Star
* Forest Tea Leaf
* Ancient Note

Purpose:

* Retention
* Curiosity
* Progression
* Small ritual-building between the user and the character

---

## Tech Stack

Frontend:

* Streamlit

AI:

* Google Gemini API

Language:

* Python

Version Control:

* Git
* GitHub

Deployment:

* Streamlit Community Cloud

Persistence:

* JSON-based local memory for prototype testing

---

## Project Structure

```text
app.py
Main Streamlit application

behavior.py
Behavior stage logic

character.py
Character Bible and personality rules

memory.py
Recent chat memory builder

facts.py
Fact extraction and direct memory recall

relationship.py
Trust / Familiarity / Curiosity engine

rewards.py
Variable reward system

persistent_memory.py
JSON-based memory persistence

TESTING.md
Final test matrix

README.md
Project documentation
```

---

## System Architecture

```text
User
 ↓
Streamlit Frontend
 ↓
Session State Layer
 ├── Chat Messages
 ├── Intimacy Score
 ├── Points
 ├── User Facts
 ├── Relationship State
 └── Inventory
 ↓
Behavior Engine
 ├── Stage Detection
 └── Stage Description
 ↓
Memory System
 ├── Recent Chat Memory
 ├── Fact Memory
 └── Persistent JSON Memory
 ↓
Relationship Engine
 ├── Trust
 ├── Familiarity
 └── Curiosity
 ↓
Prompt Assembly
 ├── Character Bible
 ├── Stage Rules
 ├── Relationship State
 ├── Recent Chat History
 └── User Facts
 ↓
Gemini API
 ↓
AI Response
 ↓
Reward System
 ├── Points
 ├── Variable Reward
 └── Inventory Update
```

### Current Prototype Architecture

The current version uses Streamlit session state and JSON-based persistence to keep the prototype simple, inspectable, and easy to deploy.

This structure allows each system layer to be tested separately:

* `character.py` handles identity and personality rules
* `behavior.py` handles stage logic
* `memory.py` handles recent conversation memory
* `facts.py` handles simple user fact extraction and direct recall
* `relationship.py` handles relationship state
* `rewards.py` handles variable rewards
* `persistent_memory.py` handles JSON-based persistence

---

## Implemented Features

* Streamlit chatbot UI
* Gemini API integration
* Character Bible
* Behavioral stage progression
* Intimacy score system
* Recent chat memory
* Fact memory
* Persistent JSON memory
* Relationship engine
* Points system
* Variable reward system
* Reward inventory
* GitHub deployment
* Final test matrix documentation

---

## Testing

Core system tests are documented in:

[TESTING.md](TESTING.md)

The test matrix covers:

* Character response
* Fact memory
* Name recall
* Relationship engine
* Curiosity signal
* Stage progression
* Reward system
* Persistent memory

---

## Current Limitations

* Memory currently uses JSON-based persistence
* The prototype is not designed for multiple concurrent users
* There is no user authentication
* Relationship scoring is rule-based
* Fact extraction is keyword-based
* Reward logic is symbolic and not connected to real purchase behavior yet
* Gemini free-tier quota limits testing frequency
* No analytics dashboard yet

---

## Technical Debt and Scaling Plan

This prototype intentionally uses Streamlit session state and JSON-based persistence to keep the system simple, fast to build, and easy to inspect during early development.

### Why JSON Persistence Was Used

JSON storage was selected for the prototype because:

* It is easy to debug
* It requires no external database setup
* It keeps memory behavior visible and inspectable
* It is suitable for a single-user prototype
* It allows fast iteration during early-stage development

### Current Technical Debt

The current system has several limitations:

* Memory is stored locally in a JSON file
* The system is not designed for multiple concurrent users
* There is no user authentication
* Relationship values are rule-based
* Fact extraction is keyword-based
* Reward logic is simple and not yet connected to real business actions
* Streamlit session state is not enough for production-scale user memory

### Scaling Plan

If this prototype were expanded for real users, the architecture would be upgraded in phases.

#### Phase 1 — Database Persistence

Replace JSON memory with a database.

Possible options:

* SQLite for local prototype persistence
* Supabase for hosted user profiles
* PostgreSQL for production-scale memory storage

Stored data would include:

* User profile
* Intimacy score
* Relationship state
* Inventory
* Interaction history
* Reward history

#### Phase 2 — Backend Workflow Automation

Use n8n for backend workflows such as:

* Reward redemption
* Google Sheets / CRM logging
* User event tracking
* Notification workflows
* Menu recommendation workflows
* Campaign automation

#### Phase 3 — Agent Logic Layer

Use Flowise or LangChain to separate agent reasoning from the Streamlit frontend.

This would allow:

* Better prompt routing
* Tool usage
* Multi-step reasoning
* Memory retrieval
* Menu recommendation agents
* Reward decision agents

#### Phase 4 — Production Architecture

A production version would use:

* Streamlit or React frontend
* FastAPI backend
* PostgreSQL or Supabase database
* Redis caching
* n8n workflow automation
* LLM API layer
* Monitoring and analytics dashboard

### Summary

The current version is designed as a working AI character prototype.

The next production step is to move from local JSON memory to a database-backed memory system, then connect backend workflows through n8n and agent orchestration through Flowise or LangChain.

---

## Future Roadmap

### Phase 2

* Persistent database memory
* User profiles
* Better fact extraction
* More structured user preference tracking

### Phase 3

* Flowise integration
* LangChain agent layer
* n8n automation workflows
* Menu recommendation logic

### Phase 4

* Analytics dashboard
* Lore collection system
* Advanced emotional pacing
* Reward redemption flow
* Multi-user deployment architecture

---

## Why This Project Matters

Most chatbot projects stop at question-answer interactions.

i nik explores a different direction: building an AI character that remembers, develops familiarity, creates small rituals, and maintains long-term engagement through behavioral design.

The project combines:

* Prompt Engineering
* Behavioral Design
* Memory Systems
* Relationship Modeling
* Gamification
* Applied AI Product Design

This makes the prototype closer to an applied AI character system than a basic chatbot interface.

