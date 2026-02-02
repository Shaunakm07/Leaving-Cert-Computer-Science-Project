#include <Arduino.h>

const int soilMoisturePin = A5;

int readSoilMoisture(){
    int raw = analogRead(soilMoisturePin);
    return raw;
}

