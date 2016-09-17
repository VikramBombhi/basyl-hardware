/* Hack the North 2016 */
#include <DHT.h>

#define DHTPIN (A1)
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

float airHumidity;
float airTemperature;

int photocellPin = 0;     // the cell and 10K pulldown are connected to a0
int photocellReading;     // the analog reading from the sensor divider

int moisturePin = A2;

void setup(void) { 
  pinMode(A1, OUTPUT);
  digitalWrite(A1, HIGH);
  
  Serial.begin(9600);   
  dht.begin();
}
 
void loop(void) {
  photocellReading = analogRead(photocellPin);  
  airHumidity = dht.readHumidity();
  airTemperature = dht.readTemperature();
  Serial.print("light:");
  Serial.println(photocellReading); // the raw analog reading
  Serial.print("humidity:");
  Serial.println(airHumidity);
  Serial.print("temp:");
  Serial.println(airTemperature);
  Serial.print("moisture:");
  Serial.println(analogRead(moisturePin));
  
  delay(2000);
}
