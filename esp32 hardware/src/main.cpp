#include <Arduino.h>
#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include "time.h"
#include "credentials.h"

const char* ntpServer = "pool.ntp.org";
const long  gmtOffset_sec = 28800;
const int   daylightOffset_sec = 0;

const int trigPin = 5;
const int echoPin = 18;

#define DHTPIN 23
#define DHTTYPE DHT11
#define speedSound 0.0349

long duration;
float distanceCM;

DHT dht(DHTPIN, DHTTYPE);

String getLocalTimeString() {
  struct tm timeinfo;
  if (!getLocalTime(&timeinfo)) {
    return "Failed to obtain time";
  }

  char timeString[64];
  strftime(timeString, sizeof(timeString), "%A, %B %d %Y %H:%M:%S", &timeinfo);
  return String(timeString);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Initializing resources");
  pinMode(LED_BUILTIN, OUTPUT);
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Not connected");
  }
  Serial.println("Connected!");
  dht.begin();

  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
  Serial.println(getLocalTimeString());

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  float temp = dht.readTemperature();
  String time = getLocalTimeString();

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distanceCM = duration * speedSound/2;

  if (WiFi.status() == WL_CONNECTED){
    WiFiClient client;
    HTTPClient http;

    http.begin(client, serverName);

    // specify content type
    http.addHeader("Content-Type", "application/json");
    String httpPostData = "{\"Sensor\": \"A\", \"Temperature\": " + String(temp) +
                      ", \"Distance\": " + String(distanceCM) + ", \"Time\": \"" + time + "\"}";

    Serial.println(httpPostData);
    int httpResponseCode = http.POST(httpPostData);
    Serial.println(httpResponseCode);
    http.end();
  }

  delay(1000); 
}

