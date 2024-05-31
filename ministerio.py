from get_text import urls, scrape_noticias ,scrape_noticias_2
import json
import os

def ministerio_mulheres():
    print("MINISTÉRIO DAS MULHERES")
    
    file_path = "json/Ministério das Mulheres.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as json_file:
            todas_noticias = json.load(json_file)
    else:
        todas_noticias = []
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
    
    p = 1
    
    for i in range(1, 100000, 30):
        print(f"Processando Página: {p}")
        url = urls["ministerio_mulheres"].format(i)
        noticias_pagina = scrape_noticias(url, file_path)
        if noticias_pagina:
            todas_noticias.extend(noticias_pagina)
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
        else:
            print("Não há itens novos")
            break
        p += 1



def ministerio_saude():
    print("MINISTÉRIO DA SAÚDE")
    
    file_path = "json/Ministério da Saúde.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as json_file:
            todas_noticias = json.load(json_file)
    else:
        todas_noticias = []
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
    
    p = 1
    
    for i in range(1, 100000, 30):
        print(f"Processando Página: {p}")
        url = urls["ministerio_saude"].format(i)
        noticias_pagina = scrape_noticias_2(url, file_path)
        if noticias_pagina:
            todas_noticias.extend(noticias_pagina)
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
        else:
            print("Não há itens novos")
            break
        p += 1


def ministerio_direitos_humanos():
    print("MINISTÉRIO DOS DIREITOS HUMANOS")
    
    file_path = "json/Ministério dos Direitos Humanos.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as json_file:
            todas_noticias = json.load(json_file)
    else:
        todas_noticias = []
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
    
    p = 1
    
    for i in range(1, 100000, 30):
        print(f"Processando Página: {p}")
        url = urls["ministerio_direitos_humanos"].format(i)
        noticias_pagina = scrape_noticias_2(url, file_path)
        if noticias_pagina:
            todas_noticias.extend(noticias_pagina)
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
        else:
            print("Não há itens novos")
            break
        p += 1
