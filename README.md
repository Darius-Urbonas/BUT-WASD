# BUT-WASD
BUTT-WASD lets you control in-game movement using device tilt mapped to WASD keys. Powered by an ESP32 accelerometer, it translates tilt directions into continuous key presses for an immersive gaming experience. Perfect for games like Path of Exile 2, with customizable start/stop hotkeys.


Physical Parts Needed:
A pivot chair (see the image attached)

ESP32 Development Board:

The ESP32 is the main microcontroller used to read accelerometer data and send the tilt information over Bluetooth or Serial. It has built-in Wi-Fi and Bluetooth, making it perfect for wireless communication with your PC.
Accelerometer (Optional if not using the ESP32's built-in one):

If you're using an external accelerometer (e.g., MPU6050, ADXL345), you'll need it connected to the ESP32 via I2C or SPI communication. However, the ESP32 has built-in accelerometer capabilities, so you may not need an additional one.
USB Cable:

A USB cable to power the ESP32 and connect it to your PC (for Serial communication).
(Optional) Case or Mounting Bracket:

You might want to 3D print a case or holder to mount your ESP32 and keep everything secure during gameplay.

3D Printed Parts (Optional, 3D model for a pivot chair having 40 mm diameter added):
ESP32 Case (Optional):

A 3D-printed enclosure for the ESP32 board can help protect the device and give it a neat, organized appearance. You can find many open-source designs on platforms like Thingiverse or design one yourself.
Material: PLA or PETG would work well for a basic protective case.
Mounting Bracket for Accelerometer (if external):

If you're using an external accelerometer, you may want a 3D-printed mount to hold the sensor securely at a specific angle or location on your device.
Material: PLA or ABS is good for creating simple mounts.

Instructions:

Required Materials
ESP32 Development Board

This is the main microcontroller for the project, with built-in Bluetooth and Wi-Fi.
Example: ESP32 DevKitC or any other compatible model.
Accelerometer (Optional)

If you plan to use an external accelerometer, you’ll need one like the MPU6050 or ADXL345. The ESP32 has a built-in accelerometer, but external sensors offer more flexibility and precision.
USB Cable

A standard USB cable for connecting the ESP32 to your PC.
(Optional) 3D Printed Parts

ESP32 Case: To house and protect the ESP32.
Accelerometer Mounting Bracket: A holder for positioning the accelerometer properly.
(Optional) Mounting Tape/Velcro

To attach the accelerometer to your device or holder.
Step 1: Wiring the Hardware (If Using External Accelerometer)
If you're using an external accelerometer (e.g., MPU6050), follow these wiring instructions:

MPU6050 Accelerometer Wiring:
VCC → 3.3V or 5V on the ESP32
GND → GND on the ESP32
SCL → GPIO22 (I2C clock)
SDA → GPIO21 (I2C data)
If you use an accelerometer with a different pinout (like ADXL345), consult its datasheet for the wiring details.

Step 2: Mounting the Accelerometer
Mounting Recommendations:
Mount the accelerometer as low as possible on the ESP32 or your device to ensure better accuracy in reading tilt angles.
Mounting near the center of the device is ideal for more consistent tilt detection.
If using external mounting, ensure the accelerometer is secure and oriented along the axes (pitch for forward/backward and roll for left/right).
Use Velcro or tape to attach it if you want flexibility, or 3D-print a bracket that can hold the accelerometer in place at the desired angle.
Step 3: Preparing the Software for ESP32
Install Arduino IDE:

Download and install the Arduino IDE: Arduino IDE Download
Install ESP32 Board Support:

Open Arduino IDE.
Go to File > Preferences, and in the Additional Boards Manager URL field, add this URL:
arduino
Copy code
https://dl.espressif.com/dl/package_esp32_index.json
Go to Tools > Board > Boards Manager and search for ESP32.
Install the ESP32 package.
Set Up the Code:

Open a new file in Arduino IDE and paste the code attached to read the accelerometer and send the tilt data to the PC via Serial.

Threshold Adjustments: The code sends the command only when the tilt angle exceeds 5 degrees from the center. You can reduce this threshold by changing the 5 to a smaller number (e.g., 2) for more sensitive control.
Step 4: Set Up Python Script for Key Presses
Install Python & Libraries:

Install Python from python.org if you don’t have it already.
Install pyautogui for controlling key presses:
bash
Copy code
pip install pyautogui
Create Python Script:

Python code to receive serial data from the ESP32 and simulate key presses based on the received tilt data can be found in the attached file (you will need to define your com port to which the ESP32 is connected).

Step 5: Test and Calibration
Upload Code to ESP32:

Upload the Arduino code to your ESP32 using the Upload button in Arduino IDE.
Run the Python Script:

Run the Python script on your computer.
The ESP32 will send tilt information over the serial connection, and the Python script will simulate the appropriate key press.
Testing:

Tilt the device forward (W), backward (S), left (A), and right (D).
The keys should be simulated in the game, and the output will be continuous as long as the tilt condition is met.
Final Recommendations:
Fine-tuning: You can adjust the tilt threshold in the Arduino code to make the movement more or less sensitive.
Mounting Tips: Keep the accelerometer as low as possible to achieve more accurate and consistent readings.
Game Settings: Ensure the game is running in windowed or borderless mode for the best experience when controlling via the keyboard.
