from flask import Flask, request, render_template
import pandas as pd
import os
import plotly.express as px
from datetime import datetime

app = Flask(__name__)
PASTA = "./csvs/"

@app.route("/")
def index():
    # Lista todos os CSVs da pasta
    arquivos = [f for f in os.listdir(PASTA) if f.endswith(".csv")]

    # Para cada CSV, lê as colunas
    csvs = []
    for arquivo in arquivos:
        caminho = os.path.join(PASTA, arquivo)
        df = pd.read_csv(caminho, sep=',', quotechar='"')
        df.columns = df.columns.str.strip().str.replace('"', '')
        csvs.append({
        "nome": arquivo,
        "colunas": df.columns.tolist()  # lista de strings
        })

    return render_template("index.html", csvs=csvs)

@app.route("/grafico")
def grafico():
    arquivo = request.args.get("arquivo")
    x_col = request.args.get("x")
    y_col = request.args.get("y")
    inicio = request.args.get("inicio")
    fim = request.args.get("fim")

    caminho = os.path.join(PASTA, arquivo)
    if not os.path.exists(caminho):
        return "<h1>Erro: arquivo não encontrado</h1>"

    # 1️⃣ Lê o CSV
    df = pd.read_csv(caminho, sep=',', quotechar='"')
    df.columns = df.columns.str.strip().str.replace('"', '')

    # 2️⃣ Detectar automaticamente a coluna de datas
    data_col = None
    for col in df.columns:
        if pd.to_datetime(df[col], errors='coerce').notna().any():
            data_col = col
            df[data_col] = pd.to_datetime(df[data_col], dayfirst=True, errors='coerce')
            break

    # 3️⃣ Transformar colunas numéricas
    if y_col in df.columns:
        df[y_col] = pd.to_numeric(df[y_col], errors='coerce')

    # 4️⃣ Ordenar pelo eixo X caso seja a coluna de data detectada
    if x_col == data_col:
        df = df.sort_values(by=x_col)

    
    # 5️⃣ Filtrar por datas se a coluna de data existe
    if data_col:
        if inicio:
            inicio_dt = pd.to_datetime(inicio, dayfirst=True, errors='coerce')
            df = df[df[data_col] >= inicio_dt]
        if fim:
            fim_dt = pd.to_datetime(fim, dayfirst=True, errors='coerce')
            df = df[df[data_col] <= fim_dt]

    # 6️⃣ Verifica se as colunas existem após limpeza
    if x_col not in df.columns or y_col not in df.columns:
        return "<h1>Erro: colunas selecionadas não existem após o tratamento</h1>"

    # 7️⃣ Criar gráfico Plotly
    fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
    grafico_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return f"""
    <html lang='pt-BR'>
    <head><meta charset='UTF-8'><title>Gráfico</title></head>
    <body style="background:#1e1e2f; color:#e0e0e0; font-family:Segoe UI; margin:20px;">
        <h1 style="text-align:center; color:white;">{y_col} vs {x_col}</h1>
        <div>{grafico_html}</div>
        <a href="/" style="color:#4caf50;">⬅ Voltar</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Porta 3000 configurada
    app.run(debug=True, host="127.0.0.1", port=3000)
