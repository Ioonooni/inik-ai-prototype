import json
from pathlib import Path


MEMORY_FILE = Path("memory_store.json")


DEFAULT_MEMORY = {
    "user_facts": {},
    "inventory": [],
    "intimacy_score": 0,
    "points": 0,
    "relationship_state": {
        "trust": 0,
        "familiarity": 0,
        "curiosity": 0
    }
}


def get_default_memory():
    return {
        "user_facts": {},
        "inventory": [],
        "intimacy_score": 0,
        "points": 0,
        "relationship_state": {
            "trust": 0,
            "familiarity": 0,
            "curiosity": 0
        }
    }


def load_memory():
    if not MEMORY_FILE.exists():
        return get_default_memory()

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        memory = get_default_memory()

        memory["user_facts"] = data.get("user_facts", {})
        memory["inventory"] = data.get("inventory", [])
        memory["intimacy_score"] = data.get("intimacy_score", 0)
        memory["points"] = data.get("points", 0)
        memory["relationship_state"] = data.get(
            "relationship_state",
            {
                "trust": 0,
                "familiarity": 0,
                "curiosity": 0
            }
        )

        return memory

    except Exception:
        return get_default_memory()


def save_memory(user_facts, inventory, intimacy_score, points, relationship_state):
    data = {
        "user_facts": user_facts,
        "inventory": inventory,
        "intimacy_score": intimacy_score,
        "points": points,
        "relationship_state": relationship_state
    }

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)