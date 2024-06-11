# LaCCAN - Violência Contra a Mulher

Este repositório possui os scripts para realização do scraping de dados dos websites do Ministério das Mulheres, Ministério da Saúde e Ministério dos Direitos Humanos.

### Primeiros passos

#### Rodando no terminal
1. Instale o virtualenv caso não tenha;
2. No diretório principal do projeto crie um ambiente virtual ```.venv``` com ```virtualenv .venv```;
3. Inicie o ambiente virtual: ```source .venv/bin/activate``` (no Linux)
4. Agora instale as bibliotecas necessárias com ```pip install -r requirements.txt```;
5. Inicie a aplicação com ```python app.py```

#### Rodando no Docker

1. Caso não tenha o Docker instalado, primeiro efetue a instalação
2. Com o Docker instalado abra o terminal, navegue até o diretório do projeto e digite ```docker build -t scrap .```
('scrap' é o nome da imagem que o docker irá construir e conterá nossa aplicação)
3. Agora digite o seguinte comando para inicializar o container ```docker run -d -v caminho/ate/projeto/json:app/json```
(o docker inicializará o container e montará um volume do diretório json da sua máquina com o do container)