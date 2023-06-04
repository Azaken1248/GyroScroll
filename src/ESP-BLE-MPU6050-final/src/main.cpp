#include <Arduino.h>
#include "BluetoothSerial.h"
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

BluetoothSerial SerialBT;
Adafruit_MPU6050 mpu;
//double current_z, last_z = 9;
unsigned long lastActionTime = 0;

void setup() {

  Serial.begin(115200);
  SerialBT.begin("GyroScroll");

  mpu.begin();
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_5_HZ);

}

void loop() {

  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  
  if(((millis()-lastActionTime)>3000)&&(g.gyro.x<-1.5)){
    SerialBT.println(1);
    lastActionTime = millis();
  }

  /*
  alternatively:
  if((current_z-last_z)<-3.5){
    SerialBT.println(1);
  }
  last_z = current_z;
  delay(500);
  */

  delay(300);
  
}