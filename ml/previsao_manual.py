import joblib
import pandas as pd

# Carrega modelo e encoder
modelo = joblib.load("modelo_risco.pkl")
le_risco = joblib.load("label_encoder_risco.pkl")

# Entrada de dados manuais
try:
    umidade = float(input("Umidade (%): "))
    aceleracao = float(input("Aceleração (m/s²): "))
    inclinacao = float(input("Inclinação (°): "))
    chuva = float(input("Chuva acumulada (mm): "))
except ValueError:
    print("Valor inválido digitado. Encerrando.")
    exit()

# Cria DataFrame de entrada
entrada_df = pd.DataFrame([[umidade, aceleracao, inclinacao, chuva]],
                          columns=["umidade", "aceleracao", "inclinacao", "chuva_mm"])

# Faz previsão
risco_cod = modelo.predict(entrada_df)[0]
risco_label = le_risco.inverse_transform([risco_cod])[0]

# Exibe resultado
print(f"\nPrevisão de risco: {risco_label.upper()}")
