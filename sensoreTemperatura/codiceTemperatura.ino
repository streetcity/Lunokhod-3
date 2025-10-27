#include <DHT.h>

#define DHTPIN 11
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("Pronto a trasmettere i dati");
}

void loop() {
  delay(1000);

  float tempC = dht.readTemperature();
  if (isnan(tempC)) {
    Serial.println("Errore nella lettura della temperatura");
    return;
  }

  Serial.println(tempC, 1);
}
