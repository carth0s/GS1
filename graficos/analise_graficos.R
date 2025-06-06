# Carrega bibliotecas
library(ggplot2)
library(dplyr)
library(readr)

# Lê o dataset
df <- read_csv("Dataset_Modelo.csv")

# Boxplot: Umidade por risco
ggplot(df, aes(x = risco, y = umidade, fill = risco)) +
  geom_boxplot() +
  theme_minimal() +
  labs(title = "Distribuição da Umidade por Nível de Risco", y = "Umidade (%)", x = "Risco")

# Boxplot: Chuva por risco
ggplot(df, aes(x = risco, y = chuva_mm, fill = risco)) +
  geom_boxplot() +
  theme_minimal() +
  labs(title = "Distribuição da Chuva por Nível de Risco", y = "Chuva acumulada (mm)", x = "Risco")

# Boxplot: Inclinação por risco
ggplot(df, aes(x = risco, y = inclinacao, fill = risco)) +
  geom_boxplot() +
  theme_minimal() +
  labs(title = "Distribuição da Inclinação por Nível de Risco", y = "Inclinação (graus)", x = "Risco")

# Gráfico de barras: Frequência de risco
ggplot(df, aes(x = risco, fill = risco)) +
  geom_bar() +
  theme_minimal() +
  labs(title = "Distribuição de Riscos no Dataset", x = "Risco", y = "Frequência")

# Densidade de chuva por risco
ggplot(df, aes(x = chuva_mm, fill = risco)) +
  geom_density(alpha = 0.5) +
  theme_minimal() +
  labs(title = "Distribuição de Chuva por Risco", x = "Chuva acumulada (mm)", y = "Densidade")

# Dispersão: Inclinação vs Chuva por risco
ggplot(df, aes(x = inclinacao, y = chuva_mm, color = risco)) +
  geom_point(alpha = 0.7) +
  theme_minimal() +
  labs(title = "Risco em função de Inclinação e Chuva", x = "Inclinação (graus)", y = "Chuva acumulada (mm)")

