import json
from pathlib import Path


MEMORY_FILE = Path("memory_store.json")


def load_memory():
    if not MEMORY_FILE.exists():
        return {
            "user_facts": {},
            "inventory": []
        }

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return {
            "user_facts": data.get("user_facts", {}),
            "inventory": data.get("inventory", [])
        }

    except Exception:
        return {
            "user_facts": {},
            "inventory": []
        }


def save_memory(user_facts, inventory):
    data = {
        "user_facts": user_facts,
        "inventory": inventory
    }

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)