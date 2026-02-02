#include <Arduino.h>
#include <DHT.h>


const int soilMoisturePin = A5;
const int tempHumidityPin = 8;

#define DHTPIN tempHumidityPin        
#define DHTTYPE DHT22   

DHT dht(DHTPIN, DHTTYPE);

int readSoilMoisture(){
    int raw = analogRead(soilMoisturePin);
    return raw;
}
float readHumitidySensor(){
  float humidity = dht.readHumidity();
  return humidity;
}

float readTemperatureSensor(){
  float temperature = dht.readTemperature();
  return temperature;
}

void initiateDHT(){
  dht.begin();
}