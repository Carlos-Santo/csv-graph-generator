# CSV Graph Generator

Uma aplicação web para gerar gráficos interativos a partir de arquivos CSV. Feita em **Python** com **Flask** e **Plotly**.

## Funcionalidades
- Lista todos os CSVs em uma pasta.
- Permite selecionar colunas para os eixos X e Y.
- Filtra dados por período de datas.
- Gera gráficos interativos usando Plotly.

## Pré-requisitos
- Python 3.10 ou superior
- Pip

## Estrutura do projeto
csv-graph-generator/
│
├── app.py                # Código principal da aplicação
├── templates/
│   └── index.html        # HTML da interface
├── csvs/                 # Pasta para colocar arquivos CSV
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo

> A pasta `csvs/` deve conter os arquivos CSV que você deseja visualizar.

## Instalação
Clone o repositório:
git clone https://github.com/seu-usuario/csv-graph-generator.git
cd csv-graph-generator

Crie um ambiente virtual (recomendado):
# Linux / Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt

## Como rodar a aplicação
Execute o arquivo principal:
python app.py

Abra seu navegador e acesse:
http://127.0.0.1:5000

Selecione o CSV, configure os eixos e datas, e clique em “Gerar gráfico”.

## Dependências
- Flask
- Pandas
- Plotly

## Observações
- Certifique-se de que os CSVs tenham colunas numéricas para o eixo Y.
- Se houver colunas de data, o sistema tentará detectá-las automaticamente para filtrar pelo período selecionado.
