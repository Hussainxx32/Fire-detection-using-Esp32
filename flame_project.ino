#define FLAME_PIN 34

unsigned long t0;

void setup() {
  Serial.begin(115200);
  delay(200);

  analogReadResolution(12);
  analogSetPinAttenuation(FLAME_PIN, ADC_11db);

  t0 = millis();

  Serial.println("t_s,flame_signal");
}

void loop() {
  int raw = analogRead(FLAME_PIN);
  int flameSignal = 4095 - raw;

  float t = (millis() - t0) / 1000.0;

  Serial.print(t, 2);
  Serial.print(",");
  Serial.println(flameSignal);

  delay(1000);
}

