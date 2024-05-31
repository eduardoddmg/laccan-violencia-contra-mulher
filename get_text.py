import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime
from functions import *

def scrape_noticias(url, file_path):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        lista_noticias = soup.find("ul", class_="noticias")

        if lista_noticias:
            noticias_list = []

            for index, noticia in enumerate(lista_noticias.find_all("li")):
                link_element = noticia.find("div", class_="conteudo").find("h2", class_="titulo").find("a")
                
                if link_element:
                    titulo = link_element.text.strip()
                    href = link_element.get("href")
                    if (verify_json(file_path, href)):
                        print(f"O {titulo} já existe no JSON")
                        continue
                    data = noticia.find("span", "data").text.strip()
                    dia = data.split("/")[0]
                    mes = data.split("/")[1]
                    ano = data.split("/")[2]
                    texto = extrair_texto(href)
                    lastScrapping = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    
                    print(index+1, len(lista_noticias.find_all("li")))
                    
                    if (int(ano) < 2019):
                        print("Ano é inferior a 2019")
                        return
                    noticia_dict = {"title": titulo, "href": href, "texto": texto, "data": data, "dia": dia, "mes": mes, "ano": ano, "lastScrapping": lastScrapping }
                    
                    noticias_list.append(noticia_dict)
                else:
                    print("Elemento <a> não encontrado.")
            
            return noticias_list
        else:
            print("Lista de notícias não encontrada.")
            return
    else:
        print("Erro ao acessar a página:", response.status_code)

def scrape_noticias_2(url, file_path):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        lista_noticias = soup.find_all("article", "tileItem")
        if lista_noticias:
            noticias_list = []

            for index, noticia in enumerate(lista_noticias):
                link_element = noticia.find("a", "url")
                if link_element:
                    titulo = link_element.text.strip()
                    href = link_element.get("href")
                    if (verify_json(file_path, href)):
                        print(f"O {titulo} já existe no JSON")
                        continue
                    data = noticia.find("span", "summary-view-icon").text.strip()
                    dia = data.split("/")[0]
                    mes = data.split("/")[1]
                    ano = data.split("/")[2]
                    texto = extrair_texto(href)
                    lastScrapping = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    
                    print(index+1, len(lista_noticias))
                    
                    if (int(ano) < 2019):
                        print("Ano é inferior a 2019")
                        return
                    noticia_dict = {"title": titulo, "href": href, "texto": texto, "data": data, "dia": dia, "mes": mes, "ano": ano, "lastScrapping": lastScrapping }
                    
                    noticias_list.append(noticia_dict)
                else:
                    print("Elemento <a> não encontrado.")
            
            return noticias_list
        else:
            print("Lista de notícias não encontrada.")
            return
    else:
        print("Erro ao acessar a página:", response.status_code)

def extrair_texto(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        div_content_core = soup.find("div", id="content-core")

        if div_content_core:
            texto_div = div_content_core.text.strip()
            return texto_div
        else:
            print("Div com ID 'content-core' não encontrada.")
            return None
    else:
        print("Erro ao acessar a página:", response.status_code)
        return None



urls = {
    "ministerio_mulheres": "https://www.gov.br/mulheres/pt-br/central-de-conteudos/noticias?b_start:int={}",
    "ministerio_saude": "https://www.gov.br/saude/pt-br/assuntos/noticias?b_start:int={}",
    "ministerio_direitos_humanos": "https://www.gov.br/mdh/pt-br/assuntos/noticias?b_start:int={}"
}

