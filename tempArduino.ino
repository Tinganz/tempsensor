#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);  

DallasTemperature sensors(&oneWire);

int deviceCount = 0;
float tempC;

void setup(void)
{
  sensors.begin();  // Start up the library
  Serial.begin(9600);
  
  Serial.print("Locating devices...");
  Serial.print("Found ");
  deviceCount = sensors.getDeviceCount();
  Serial.print(deviceCount, DEC);
  Serial.println(" devices.");
  Serial.println("");
   Serial.print("Parasite power is: "); 
  if (sensors.isParasitePowerMode()) Serial.println("ON");
  else Serial.println("OFF");
  
}

void loop(void)
{ 
  sensors.requestTemperatures(); 
 
  for (int i = 0;  i < deviceCount;  i++)
  {
    Serial.print("Sensor ");
    Serial.print(i+1);
    Serial.print(":");
    tempC = sensors.getTempCByIndex(i);
    Serial.print(tempC);
    char chr = 97;
    Serial.print("°");
    Serial.print("C");
    Serial.print(":");
  }
  
  Serial.println("");
  delay(1000);
}
