#include <Arduino.h>
#include <read_sensor_data.h>


void setup() {
  Serial.begin(9600);
}

void loop() {
  int moisture_sensor = readSoilMoisture();
  Serial.print("Current Moisture: ");
  Serial.print(moisture_sensor);
  Serial.print("\t");
  delay(1000);
}
