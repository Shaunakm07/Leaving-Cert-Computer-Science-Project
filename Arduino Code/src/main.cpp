#include <Arduino.h>
#include <read_sensor_data.h>


void setup() {
  Serial.begin(9600);
  initiateDHT();
}

void loop() {
  int moisture_sensor = readSoilMoisture();
  Serial.print("Current Moisture: ");
  Serial.print(moisture_sensor);
  Serial.print("\t");

  float temperature_sensor = readTemperatureSensor();
  Serial.print("Current Temperature: ");
  Serial.print(temperature_sensor);
  Serial.print("\t");

  float humidity_sensor = readHumitidySensor();
  Serial.print("Current humidity: ");
  Serial.print(humidity_sensor);
  Serial.print("\t");

  Serial.print("\n");

  delay(1000);
}
