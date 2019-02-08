float temp;

void setup()
{
    Serial.begin(9600);
}
void loop() {
  temp = analogRead(A0);
  temp = temp * 0.48828125;
  Serial.print("TEMPRETURE: ");
  Serial.print(temp);
  Serial.print("*c");
  Serial.println();
  delay(1000);
}
