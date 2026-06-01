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

The project currently contains two memory layers.

#### Recent Chat Memory

Stores recent conversation history and injects it into prompts.

Purpose:

* Context continuity
* Less repetitive conversations

#### Fact Memory

Stores important user facts.

Examples:

* Name
* Preferences
* Interests

Purpose:

* Personalized interactions
* Character consistency

---

### Relationship Engine

The system tracks three relationship dimensions.

#### Trust

How much personal information the user shares.

#### Familiarity

How often the user interacts with i nik.

#### Curiosity

How interested i nik becomes in the user.

These values are exposed in the UI and injected into prompts.

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

---

## Project Structure

```text
app.py
Main application

behavior.py
Behavior stage logic

character.py
Character Bible

memory.py
Recent chat memory

facts.py
Fact extraction system

relationship.py
Trust / Familiarity / Curiosity engine

rewards.py
Variable reward system

README.md
Project documentation
```

---

## System Architecture

```text
User Input
    ↓
Streamlit Interface
    ↓
Session State
    ↓
Behavior Engine
    ↓
Memory Engine
    ↓
Relationship Engine
    ↓
Prompt Construction
    ↓
Gemini API
    ↓
AI Response
    ↓
Reward System
    ↓
Inventory Update
```

---

## Implemented Features

* Streamlit chatbot UI
* Gemini API integration
* Character Bible
* Behavioral stage progression
* Intimacy score system
* Recent chat memory
* Fact memory
* Relationship engine
* Points system
* Variable reward system
* Reward inventory
* GitHub deployment

---

## Current Limitations

* Session-based memory only
* No persistent database
* Free-tier API quota limitations
* Rule-based relationship scoring
* No analytics dashboard yet

---
## Testing

Core system tests are documented in:

[TESTING.md](TESTING.md)

The test matrix covers:

- Character response
- Fact memory
- Name recall
- Relationship engine
- Curiosity signal
- Stage progression
- Reward system
- Persistent memory

---

## Future Roadmap

### Phase 2

* Persistent database memory
* User profiles
* Better fact extraction

### Phase 3

* Flowise integration
* LangChain agent layer
* n8n automation workflows

### Phase 4

* Analytics dashboard
* Lore collection system
* Advanced emotional pacing

---

## Why This Project Matters

Most chatbot projects stop at question-answer interactions.

i nik explores a different direction:

building an AI character that remembers, develops familiarity, creates small rituals, and maintains long-term engagement through behavioral design.

The project combines:

* Prompt Engineering
* Behavioral Design
* Memory Systems
* Relationship Modeling
* Gamification
* Applied AI Product Design
