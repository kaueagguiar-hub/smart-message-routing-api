from flask import Flask, request, jsonify
from flasgger import Swagger
from services.ai_service import classify_message
from services.action_service import execute_action
import json
import logging
import os

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'AI Automation Agent API',
    'uiversion': 3
}

swagger = Swagger(app)

# --- Logging estruturado ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

LOGS_PATH = os.environ.get("LOGS_PATH", "data/logs.json")
MAX_MESSAGE_LENGTH = int(os.environ.get("MAX_MESSAGE_LENGTH", 2000))


def load_logs() -> list:
    """Carrega logs do arquivo JSON com tratamento de erro."""
    try:
        with open(LOGS_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"Arquivo de logs não encontrado: {LOGS_PATH}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Erro ao decodificar logs JSON: {e}")
        return []


# --- Health check para load balancers / Kubernetes ---
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json(silent=True)

    if not data or not isinstance(data, dict):
        return jsonify({"error": "Payload JSON inválido."}), 400

    message = data.get("message", "")

    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "O campo 'message' é obrigatório e deve ser uma string não vazia."}), 400

    if len(message) > MAX_MESSAGE_LENGTH:
        return jsonify({"error": f"Mensagem excede o limite de {MAX_MESSAGE_LENGTH} caracteres."}), 400

    try:
        classification = classify_message(message)
        action = execute_action(classification, message)
        logger.info(f"Mensagem classificada como '{classification}'")
        return jsonify({"classification": classification, "action": action}), 200
    except Exception as e:
        logger.error(f"Erro ao classificar mensagem: {e}", exc_info=True)
        return jsonify({"error": "Erro interno ao processar a mensagem."}), 500


@app.route("/logs", methods=["GET"])
def get_logs():
    logs = load_logs()
    return jsonify(logs), 200


@app.route("/stats", methods=["GET"])
def get_stats():
    """
    Retorna estatísticas das mensagens
    ---
    responses:
      200:
        description: Estatísticas retornadas com sucesso
    """
    logs = load_logs()

    stats: dict[str, int] = {}
    for log in logs:
        classification = log.get("classification")
        if classification:
            stats[classification] = stats.get(classification, 0) + 1

    return jsonify(stats), 200

print(app.url_map)

if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode)