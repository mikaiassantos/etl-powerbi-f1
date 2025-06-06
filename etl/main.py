import os
import pandas as pd
import requests
from datetime import datetime

# Configurações
URLS = {
    "constructors": "https://github.com/CaioSobreira/dti_arquivos/raw/main/constructors.csv",
    "drivers": "https://github.com/CaioSobreira/dti_arquivos/raw/main/drivers.csv",
    "races": "https://github.com/CaioSobreira/dti_arquivos/raw/main/races.csv",
    "results": "https://github.com/CaioSobreira/dti_arquivos/raw/main/results.csv"
}

PASTA_BASE = "etl"
PASTA_EXTRACAO = os.path.join(PASTA_BASE, "extracao")
PASTA_SAIDA = os.path.join(PASTA_BASE, "saida")

def log(mensagem):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mensagem}")

def verificar_pastas():
    os.makedirs(PASTA_EXTRACAO, exist_ok=True)
    os.makedirs(PASTA_SAIDA, exist_ok=True)
    log("Pastas verificadas")

def baixar_arquivos():
    for nome, url in URLS.items():
        caminho = os.path.join(PASTA_EXTRACAO, f"{nome}.csv")
        if not os.path.exists(caminho):
            response = requests.get(url)
            with open(caminho, "wb") as f:
                f.write(response.content)
            log(f"{nome}.csv baixado")

# Processo de transformação: Arquivo CONSTRUCTORS (montadoras)
def processar_montadoras():
    df = pd.read_csv(os.path.join(PASTA_EXTRACAO, "constructors.csv"))
    df = df[["constructorId", "name", "nationality"]]
    df.columns = ["montadora_id", "nome", "nacionalidade"]
    df = df.astype("string")
    df.to_excel(os.path.join(PASTA_SAIDA, "dim_montadora.xlsx"), index=False)
    log("dim_montadora.xlsx salvo")

# Processo de transformação: Arquivo DRIVERS (pilotos)
def processar_pilotos():
    df = pd.read_csv(os.path.join(PASTA_EXTRACAO, "drivers.csv"))
    df["nome_completo"] = df["forename"] + " " + df["surname"]
    df = df[["driverId", "nome_completo", "nationality"]]
    df.columns = ["piloto_id", "nome_completo", "nacionalidade"]
    df = df.astype("string")
    df.to_excel(os.path.join(PASTA_SAIDA, "dim_piloto.xlsx"), index=False)
    log("dim_piloto.xlsx salvo")

# Processo de transformação: Arquivo RACES (corridas)
def processar_corridas():
    df = pd.read_csv(os.path.join(PASTA_EXTRACAO, "races.csv"), parse_dates=["date"])
    df = df[["raceId", "year", "name", "date"]]
    df.columns = ["corrida_id", "ano", "nome", "corrida_data"]
    df = df.astype({
        "corrida_id": "string",
        "ano": "int32",
        "nome": "string",
        "corrida_data": "datetime64[ns]"
    })
    df.to_excel(os.path.join(PASTA_SAIDA, "dim_tempo.xlsx"), index=False)
    log("dim_tempo.xlsx salvo")

# Processo de transformação: Arquivo RESULTS (resultados)
def processar_resultados():
    df = pd.read_csv(os.path.join(PASTA_EXTRACAO, "results.csv"))
    df = df[[
        "resultId", "raceId", "driverId", "constructorId",
        "positionOrder", "points", "fastestLapTime"
    ]]
    df.columns = [
        "resultado_id", "corrida_id", "piloto_id", "montadora_id",
        "posicao_ordem", "pontos", "volta_mais_rapida_tempo"
    ]
    df = df.astype({
        "resultado_id": "int32",
        "corrida_id": "int32",
        "piloto_id": "int32",
        "montadora_id": "int32",
        "posicao_ordem": "int32",
        "pontos": "int32",
        "volta_mais_rapida_tempo": "string"
    })
    df.to_excel(os.path.join(PASTA_SAIDA, "fato_resultados.xlsx"), index=False)
    log("fato_resultados.xlsx salvo")

if __name__ == "__main__":
    print("Iniciando processo ETL...")
    verificar_pastas()
    baixar_arquivos()
    processar_montadoras()
    processar_pilotos()
    processar_corridas()
    processar_resultados()
    print("ETL finalizado com sucesso!")
