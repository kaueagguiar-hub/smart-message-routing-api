def classify_message(message):
    message = message.lower()

    if "comprar" in message or "preço" in message:
        return "sales"
    elif "problema" in message or "erro" in message:
        return "support"
    else:
        return "general"