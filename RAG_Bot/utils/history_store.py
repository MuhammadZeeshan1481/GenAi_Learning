import json
import os
from hashlib import md5

HISTORY_DIR = "history"

def get_file_hash(filepath):
    with open(filepath, "rb") as f:
        return md5(f.read()).hexdigest()

def get_history_path(file_hash):
    os.makedirs(HISTORY_DIR, exist_ok=True)
    return os.path.join(HISTORY_DIR, f"{file_hash}.json")

def save_query_answer(filepath, query, answer):
    file_hash = get_file_hash(filepath)
    history_path = get_history_path(file_hash)

    history = []
    if os.path.exists(history_path):
        with open(history_path, "r") as f:
            history = json.load(f)

    history.append({"query": query, "answer": answer})

    with open(history_path, "w") as f:
        json.dump(history, f, indent=2)

def load_history(filepath):
    file_hash = get_file_hash(filepath)
    history_path = get_history_path(file_hash)

    if os.path.exists(history_path):
        with open(history_path, "r") as f:
            return json.load(f)
    return []
