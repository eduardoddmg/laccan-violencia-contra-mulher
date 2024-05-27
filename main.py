import json
from get_text import extrair_texto_div
from functions import *

def generate_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for idx, item in enumerate(data):
        if 'text' not in item or item['text'] is None:
            try:
                item['text'] = extrair_texto_div(item['href'])
                print(f"Processed {idx+1} of {len(data)}")

                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

            except Exception as e:
                print(f"Error processing item {idx+1}: {e}")
                continue


ministerio_mulheres()
ministerio_direitos_humanos()
ministerio_saude()

generate_json("json/Ministério das Mulheres.json")
generate_json("json/Ministério dos Direitos Humanos.json")
generate_json("json/Ministério da Saúde.json")