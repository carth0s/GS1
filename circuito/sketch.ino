// Lê um sensor de umidade (simulado) e envia dados via Serial para o Python

const int pinoUmidade = 34; // Pino analógico (A2 no Wokwi ESP32)

void setup() {
  Serial.begin(9600);             // Inicia a comunicação serial
  pinMode(pinoUmidade, INPUT);    // Configura o pino como entrada
  randomSeed(analogRead(0));      // Inicializa o gerador de números aleatórios
}

void loop() {
  // Lê a umidade real do pino analógico
  int leitura = analogRead(pinoUmidade); // valor entre 0 e 4095
  int umidade = map(leitura, 0, 4095, 0, 100); // transforma em percentual

  // Simula outros dados
  float aceleracao = random(0, 30) / 10.0; // 0.0 a 2.9 m/s²
  int inclinacao = random(5, 46);          // 5° a 45°
  int chuva = random(0, 101);              // 0 a 100 mm

  // Monta e envia linha simulada
  String linha = String(umidade) + "," + String(aceleracao, 1) + "," + String(inclinacao) + "," + String(chuva);
  Serial.println(linha);

  delay(3000); // espera 3 segundos
}
