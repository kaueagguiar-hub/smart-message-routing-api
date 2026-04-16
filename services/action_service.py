import json
from datetime import datetime

LOG_FILE = "data/logs.json"

def save_log(data):
    try:
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    except:
        logs = []

    logs.append(data)

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

def execute_action(classification, message):
    actions = {
        "sales": "Encaminhado para equipe comercial",
        "support": "Encaminhado para suporte técnico",
        "general": "Mensagem registrada para análise"
    }

    action_result = actions.get(classification)

    save_log({
        "message": message,
        "classification": classification,
        "action": action_result,
        "timestamp": datetime.now().isoformat()
    })

    return action_result