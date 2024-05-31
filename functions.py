import json

def verify_json(arquivo_json, valor_procurado):
    with open(arquivo_json, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return any(valor_procurado in str(item.values()) for item in data)

