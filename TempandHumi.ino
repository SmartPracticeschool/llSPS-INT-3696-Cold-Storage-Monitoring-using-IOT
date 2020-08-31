#include<dht11.h>
#define DHT11PIN 4
#define ldrPin A0

dht11 DHT11;

void setup()
{
  pinMode(ldrPin, INPUT);
  Serial.begin(9600);
}




void loop()
{
  DHT11.read(DHT11PIN);
  float Humidity=(DHT11.humidity, 2);
  Serial.print("The Humidity : ");
  Serial.println(Humidity);
  float Temperature=(DHT11.temperature, 2);
  Serial.print("The Temperature : ");
  Serial.println(Temperature);
  int ldrStatus = analogRead(ldrPin);
  Serial.print("The Intensity of Light : ");
  Serial.println(ldrStatus);
  delay(2000);
}
