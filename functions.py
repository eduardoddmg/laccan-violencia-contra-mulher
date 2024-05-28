from get_text import urls, scrape_noticias ,scrape_noticias_2
import json
import os

def ministerio_mulheres(file_path):
    print("MINISTÉRIO DAS MULHERES")
    todas_noticias = []
    
    p = 1
    for i in range(1, 100000, 30):
        print(f"Processando página {p}")
        url = urls["ministerio_mulheres"].format(i)
        noticias_pagina = scrape_noticias(url)
        if noticias_pagina:
            todas_noticias.extend(noticias_pagina)
        else:
            break
        p+=1
    
    diretorio = os.path.dirname(file_path)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Salvar as notícias no arquivo JSON
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)


def ministerio_saude(file_path):
    print("MINISTÉRIO DA SAÚDE")
    todas_noticias = []
    
    p = 1
    
    for i in range(1, 100000, 15):
        print(f"Processando Página: {p}")
        url = urls["ministerio_saude"].format(i)
        noticias_pagina = scrape_noticias_2(url)
        if noticias_pagina:
            todas_noticias.extend(noticias_pagina)
        else:
            break
        p+=1

    diretorio = os.path.dirname(file_path)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Salvar as notícias no arquivo JSON
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)

def ministerio_direitos_humanos(file_path):
    print("MINISTÉRIO DOS DIREITOS HUMANOS")
    
    todas_noticias = []
    
    p = 1
    
    for i in range(1, 100000, 30):
        print(f"Processando Página: {p}")
        url = urls["ministerio_direitos_humanos"].format(i)
        noticias_pagina = scrape_noticias_2(url)
        if noticias_pagina:
            todas_noticias.extend(noticias_pagina)
        else:
            break
        p+=1

    diretorio = os.path.dirname(file_path)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Salvar as notícias no arquivo JSON
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)