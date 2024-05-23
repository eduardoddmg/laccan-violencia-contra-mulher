import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm
from get_text import extrair_texto_div
import os

ministerio_mulher = "https://portalunico.estaleiro.serpro.gov.br/api/search/?q=violencia%20contra%20mulher&aba=noticias&ordenacao=-data&site=%2F%2Fwww.gov.br%2Fmulheres&categoriasFiltro=&orgaosFiltro=&orgaoId=ministerio-das-mulheres&tipo=Campanha%7CNews%20Item%7Ccollective.nitf.content&pagina=1&tam_pagina=10000"

ministerio_saude = "https://portalunico.estaleiro.serpro.gov.br/api/search/?q=violencia%20contra%20mulher&aba=noticias&ordenacao=-data&site=%2F%2Fwww.gov.br%2Fsaude&categoriasFiltro=&orgaosFiltro=&orgaoId=ministerio-da-saude&tipo=Campanha%7CNews%20Item%7Ccollective.nitf.content&pagina=1&tam_pagina=10000"

ministerio_direitos_humanos = "https://portalunico.estaleiro.serpro.gov.br/api/search/?q=violencia%20contra%20mulher&aba=noticias&ordenacao=-data&site=%2F%2Fwww.gov.br%2Fmdh&categoriasFiltro=&orgaosFiltro=&orgaoId=ministerio-da-mulher-da-familia-e-dos-direitos-humanos&tipo=Campanha%7CNews%20Item%7Ccollective.nitf.content&pagina=1&tam_pagina=10000"

def scrape_noticias(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        lista_noticias = soup.find("ul", class_="noticias")

        if lista_noticias:
            noticias_list = []

            for noticia in tqdm(lista_noticias.find_all("li"), desc="Scraping de notícias"):
                link_element = noticia.find("div", class_="conteudo").find("h2", class_="titulo").find("a")
                
                if link_element:
                    titulo = link_element.text.strip()
                    href = link_element.get("href")
                    texto_news = extrair_texto_div(href)
                    
                    noticia_dict = {"title": titulo, "href": href, "text": texto_news}
                    
                    noticias_list.append(noticia_dict)
                else:
                    print("Elemento <a> não encontrado.")
            
            return noticias_list
        else:
            print("Lista de notícias não encontrada.")
            return
    else:
        print("Erro ao acessar a página:", response.status_code)

def get_json(url, file_path):
    res = requests.get(url)
    if res.status_code == 200:
        content = res.json()  # Parse the response content as JSON
        os.makedirs("json", exist_ok=True)  # Ensure the directory exists
        with open(f"json/{file_path}", 'w', encoding='utf-8') as json_file:
            json.dump(content, json_file, indent=4, ensure_ascii=False)
        print(f"JSON {file_path} gerado com sucesso!")
    else:
        print(f"Failed to retrieve JSON from {url}, status code: {res.status_code}")
n = input("Digite a opção\n[1]: Ministério da Saúde\n[2]: Ministério dos Direitos Humanos\n[3]: Ministério das Mulheres\n")

nome_arquivo = "ministerio_saude.json"

if (n == '1'): 
    nome_arquivo = "ministerio_saude.json"
    get_json(ministerio_saude, nome_arquivo)
elif (n == '2'):
    nome_arquivo = "ministerio_direitos_humanos.json"
    get_json(ministerio_direitos_humanos, nome_arquivo)
elif (n == '3'):
    nome_arquivo = "ministerio_mulheres.json"
    get_json(ministerio_mulher, nome_arquivo)
else:
    print("Número inválido")
    os._exit(0)

with open(f"json/{nome_arquivo}", "r+", encoding="utf-8") as json_file:
    data = json.load(json_file)
    items = data["items"]
    c = 0
    for item in items:
        c+=1
        url = item["dados_noticia"][0]["url_noticia"]
        page = extrair_texto_div(url)
        item['text'] = page
        print(f"Em fase de processamento -> {c}/{len(items)}")
    
    json_file.seek(0)
    json.dump(data, json_file, ensure_ascii=False, indent=4)
    json_file.truncate()


print(f"{nome_arquivo} processado com sucesso!")