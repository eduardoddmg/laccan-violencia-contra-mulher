"""Package imports"""
import json
import os
import logging

"""Source imports"""
from src.get_text import urls, scrape_noticias, scrape_noticias_2

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filemode='w')
EventWriter = logging.getLogger(__name__)

async def ministerio_mulheres():
    func_name = "ministerio_mulheres: "
    EventWriter.info(func_name+"Iniciando raspagem...")
    
    file_path = "json/Ministério das Mulheres.json"
    if os.path.exists(file_path):
        EventWriter.info(func_name+"JSON existente, carregando noticias...")
        with open(file_path, "r", encoding="utf-8") as json_file:
            todas_noticias = json.load(json_file)
    else:
        EventWriter.info(func_name+"Arquivo JSON não existe. Criando um JSON...")
        todas_noticias = []
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
    
    page_num = 1
    
    for i in range(1, 100000, 30):
        EventWriter.info(f"{func_name}Processando Página: {page_num}")
        url = urls["ministerio_mulheres"].format(i)
        noticias_pagina = scrape_noticias(url, file_path)
        quantidade_noticias = len(noticias_pagina)
        if noticias_pagina:
            EventWriter.info(func_name+f"{quantidade_noticias} encontradas.")
            todas_noticias.extend(noticias_pagina)
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
        else:
            EventWriter.info(func_name+"Não há itens novos")
            break
        page_num += 1

async def ministerio_saude():
    func_name = "ministerio_saude"
    EventWriter.info(func_name+"Iniciando raspagem...")
    
    file_path = "json/Ministério da Saúde.json"
    if os.path.exists(file_path):
        EventWriter.info(func_name+"JSON existente, carregando noticias...")
        with open(file_path, "r", encoding="utf-8") as json_file:
            todas_noticias = json.load(json_file)
    else:
        EventWriter.info(func_name+"Arquivo JSON não existe. Criando um JSON...")
        todas_noticias = []
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
    
    page_num = 1
    
    for i in range(1, 100000, 30):
        EventWriter.info(f"{func_name}Processando Página: {page_num}")
        url = urls["ministerio_saude"].format(i)
        noticias_pagina = scrape_noticias_2(url, file_path)
        quantidade_noticias = len(noticias_pagina)
        if noticias_pagina:
            EventWriter.info(func_name+f"{quantidade_noticias} encontradas.")
            todas_noticias.extend(noticias_pagina)
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
        else:
            EventWriter.info(func_name+"Não há itens novos")
            break
        page_num += 1


async def ministerio_direitos_humanos():
    func_name = 'ministerio_direitos_humanos'
    EventWriter.info(func_name+"Iniciando raspagem...")
    
    file_path = "json/Ministério dos Direitos Humanos.json"
    if os.path.exists(file_path):
        EventWriter.info(func_name+"JSON existente, carregando noticias...")
        with open(file_path, "r", encoding="utf-8") as json_file:
            todas_noticias = json.load(json_file)
    else:
        EventWriter.info(func_name+"Arquivo JSON não existe. Criando um JSON...")
        todas_noticias = []
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
    
    page_num = 1
    
    for i in range(1, 100000, 30):
        EventWriter.info(f"{func_name}Processando Página: {page_num}")
        url = urls["ministerio_direitos_humanos"].format(i)
        noticias_pagina = scrape_noticias_2(url, file_path)
        quantidade_noticias = len(noticias_pagina)
        if noticias_pagina:
            EventWriter.info(func_name+f"{quantidade_noticias} encontradas.")
            todas_noticias.extend(noticias_pagina)
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump(todas_noticias, json_file, ensure_ascii=False, indent=4)
        else:
            EventWriter.info(func_name+"Não há itens novos")
            break
        page_num += 1
