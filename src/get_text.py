"""Package imports"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filemode='w')
EventWriter = logging.getLogger(__name__)

def verify_json(arquivo_json, valor_procurado):
    with open(arquivo_json, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return any(valor_procurado in str(item.values()) for item in data)

def scrape_noticias(url, file_path):
    func_name = "scrape_noticias: "
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
                        EventWriter.info(func_name+f"O {titulo} já existe no JSON")
                        continue
                    data = noticia.find("span", "data").text.strip()
                    dia = data.split("/")[0]
                    mes = data.split("/")[1]
                    ano = data.split("/")[2]
                    texto = extrair_texto(href)
                    tags = extrair_tags(href)
                    lastScrapping = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    
                    EventWriter.info(func_name+str(index+1)+" "+str(len(lista_noticias.find_all("li"))))
                    
                    if (int(ano) < 2019):
                        EventWriter.info(func_name+"Ano é inferior a 2019")
                        return
                    noticia_dict = {"title": titulo, "href": href, "texto": texto, "data": data, "dia": dia, "mes": mes, "ano": ano, "lastScrapping": lastScrapping, "tags": tags }
                    
                    noticias_list.append(noticia_dict)
                else:
                    EventWriter.info(func_name+"Elemento <a> não encontrado.")
            
            return noticias_list
        else:
            EventWriter.warning(func_name+"Lista de notícias não encontrada.")
            return
    else:
        EventWriter.warning(func_name+"Erro ao acessar a página:", response.status_code)

def scrape_noticias_2(url, file_path):
    func_name = "scrape_noticias_2: "
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
                        EventWriter.info(func_name+f"O {titulo} já existe no JSON")
                        continue
                    data = noticia.find("span", "summary-view-icon").text.strip()
                    dia = data.split("/")[0]
                    mes = data.split("/")[1]
                    ano = data.split("/")[2]
                    texto = extrair_texto(href)
                    tags = extrair_tags(href)
                    lastScrapping = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    
                    EventWriter.info(func_name+str(index+1)+ " " + str(len(lista_noticias)))
                    
                    if (int(ano) < 2019):
                        EventWriter.info("Ano é inferior a 2019")
                        return
                    noticia_dict = {"title": titulo, "href": href, "texto": texto, "data": data, "dia": dia, "mes": mes, "ano": ano, "lastScrapping": lastScrapping, "tags": tags }
                    
                    noticias_list.append(noticia_dict)
                else:
                    EventWriter.info("Elemento <a> não encontrado.")
            
            return noticias_list
        else:
            EventWriter.warning("Lista de notícias não encontrada.")
            return
    else:
        EventWriter.warning("Erro ao acessar a página:", response.status_code)

def extrair_texto(url):
    func_name = "extrair_texto: "
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        div_content_core = soup.find("div", id="content-core")

        if div_content_core:
            texto_div = div_content_core.text.strip()
            return texto_div
        else:
            EventWriter.info("Div com ID 'content-core' não encontrada.")
            return None
    else:
        EventWriter.warning("Erro ao acessar a página:", response.status_code)
        return None
    
def extrair_tags(url):
    func_name = "extrair_tags: "
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        tags = soup.find_all("a", "link-category")

        if tags:
            tags_text = [tag.get_text().strip() for tag in tags]
            return tags_text
        else:
            EventWriter.info("TAG não encontrada.")
            return None
    else:
        EventWriter.warning("Erro ao acessar a página:", response.status_code)
        return None



urls = {
    "ministerio_mulheres": "https://www.gov.br/mulheres/pt-br/central-de-conteudos/noticias?b_start:int={}",
    "ministerio_saude": "https://www.gov.br/saude/pt-br/assuntos/noticias?b_start:int={}",
    "ministerio_direitos_humanos": "https://www.gov.br/mdh/pt-br/assuntos/noticias?b_start:int={}"
}

