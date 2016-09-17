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
  
  Serial.print("Light:");
  Serial.println(photocellReading);     // the raw analog reading

  airHumidity = dht.readHumidity();
  airTemperature = dht.readTemperature();

  Serial.print("Humidity:");
  Serial.println(airHumidity);
  Serial.print("Temp:");
  Serial.println(airTemperature);

  Serial.print("Moisture:");
  Serial.println(analogRead(moisturePin));

  Serial.println(" ");
  
  delay(2000);
}
