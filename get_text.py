import requests
from bs4 import BeautifulSoup

def extrair_texto_div(url):
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


