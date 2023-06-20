#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <HTTPClient.h>
#include <SpeechRecognition.h>

const char* ssid = "wifiName";
const char* password = "password";
const char* server = "localhost";
const int serverPort = 5000;

const int sampleRate = 16000;
const int sampleBits = 16;
const int bufferSize = 4096;

void setup() {
  Serial.begin(115200);
  
  // Conectar ao Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("Conectado ao WiFi!");

  // Configurar a biblioteca de reconhecimento de fala
  SpeechRecognition.setLanguage("pt-BR");
  SpeechRecognition.begin();
}

void loop() {
  // Aguardar até que a conexão Wi-Fi esteja estabelecida
  if (WiFi.status() == WL_CONNECTED) {
    // Realizar o reconhecimento de fala
    String speechText = SpeechRecognition.recognizeSpeech(sampleRate, sampleBits, bufferSize);
    
    if (speechText.length() > 0) {
      Serial.println("Texto transcrito: " + speechText);

      // Enviar os dados para o servidor a cada 5 minutos
      static unsigned long lastSendTime = 0;
      if (millis() - lastSendTime >= 300000) {
        sendToServer(speechText);
        lastSendTime = millis();
      }
    }
  }
}

void sendToServer(const String& text) {
  WiFiClientSecure client;
  if (client.connect(server, serverPort)) {
    Serial.println("Conectado ao servidor");

    // Construir o corpo da solicitação POST
    String requestBody = "text=" + text;

    // Enviar a solicitação POST
    client.println("POST /sentimentAnalysis HTTP/1.1");
    client.println("Host: " + String(server));
    client.println("Content-Type: application/x-www-form-urlencoded");
    client.println("Content-Length: " + String(requestBody.length()));
    client.println();
    client.println(requestBody);
    client.println();

    Serial.println("Enviado para o servidor");
  }
  else {
    Serial.println("Falha na conexão com o servidor");
  }

  client.stop();
}