import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega dataset 
df = pd.read_csv("../dataset/Dataset_Modelo.csv")

# Codifica variável alvo
le_risco = LabelEncoder()
df["risco_cod"] = le_risco.fit_transform(df["risco"])

# Prepara X e y 
X = df[["umidade", "aceleracao", "inclinacao", "chuva_mm"]]
y = df["risco_cod"]

# Divide os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treina modelo com pesos balanceados
modelo = RandomForestClassifier(class_weight='balanced', n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Faz previsões
y_pred = modelo.predict(X_test)

# Avalia o modelo
acc = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {acc:.2f}")

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=le_risco.classes_, yticklabels=le_risco.classes_)
plt.title("Matriz de Confusão")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.tight_layout()
plt.savefig("matriz_confusao.png")
plt.show()

# Salva o modelo e codificador
joblib.dump(modelo, "modelo_risco.pkl")
joblib.dump(le_risco, "label_encoder_risco.pkl")

# Log de treino
with open("log_treinamento.txt", "w") as f:
    f.write(f"Acurácia do modelo: {acc:.2f}\n")
    f.write("Modelo treinado com RandomForestClassifier e dataset.\n")
    f.write("Matriz de confusão salva como PNG.\n")

print("Modelo e codificador salvos com sucesso.")
