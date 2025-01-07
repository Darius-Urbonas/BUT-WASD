#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

float pitch = 0, roll = 0;
float pitch_home = 0, roll_home = 0;
const float threshold = 3.0;  // Minimum angle (in degrees) to detect a tilt direction

void setup() {
  Serial.begin(115200);
  Wire.begin();

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  Serial.println("MPU6050 Found!");
  mpu.setAccelerometerRange(MPU6050_RANGE_4_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  delay(1000);
  homeAccelerometer(); // Initialize home position
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // Calculate pitch and roll
  pitch = atan2(a.acceleration.x, sqrt(a.acceleration.y * a.acceleration.y + a.acceleration.z * a.acceleration.z)) * 180 / PI;
  roll = atan2(a.acceleration.y, sqrt(a.acceleration.x * a.acceleration.x + a.acceleration.z * a.acceleration.z)) * 180 / PI;

  // Adjust for home position
  float adjusted_pitch = pitch - pitch_home;
  float adjusted_roll = roll - roll_home;

  String direction = "";

  // Detect diagonal and single-axis tilts based on new mapping
  if (adjusted_roll > threshold) {
    direction += "FORWARD ";
  } else if (adjusted_roll < -threshold) {
    direction += "BACKWARD ";
  }

  if (adjusted_pitch > threshold) {
    direction += "RIGHT";
  } else if (adjusted_pitch < -threshold) {
    direction += "LEFT";
  }

  direction.trim(); // Remove trailing spaces

  if (direction == "") {
    Serial.println("CENTER"); // No tilt detected
  } else {
    Serial.println(direction); // Send the detected direction
  }

  delay(100);  // Small delay to avoid flooding the serial port
}

void homeAccelerometer() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  pitch_home = atan2(a.acceleration.x, sqrt(a.acceleration.y * a.acceleration.y + a.acceleration.z * a.acceleration.z)) * 180 / PI;
  roll_home = atan2(a.acceleration.y, sqrt(a.acceleration.x * a.acceleration.x + a.acceleration.z * a.acceleration.z)) * 180 / PI;

  Serial.println("Accelerometer homed!");
}
