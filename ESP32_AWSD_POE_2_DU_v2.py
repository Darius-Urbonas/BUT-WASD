import serial
import time
import threading
import keyboard  # For global hotkeys and key presses

# Configuration
serial_port = "COM8"  # Adjust to match the ESP32's COM port
baud_rate = 115200
key_repeat_rate = 0.05  # Time in seconds between repeated keypresses

# Initialize serial communication
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Mapping directions to keys
key_map = {
    "FORWARD": "w",
    "BACKWARD": "s",
    "LEFT": "a",
    "RIGHT": "d"
}

# State control
script_active = False  # Initially, the script is inactive
active_keys = {}  # Tracks which keys are currently being held down

def press_key_repeatedly(key):
    """Simulate holding a key by repeatedly pressing it."""
    while key in active_keys:
        keyboard.press(key)
        time.sleep(key_repeat_rate)

def start_pressing_key(key):
    """Start pressing a key."""
    if key not in active_keys:
        active_keys[key] = True
        threading.Thread(target=press_key_repeatedly, args=(key,), daemon=True).start()
        print(f"Started pressing: {key}")

def stop_pressing_key(key):
    """Stop pressing a key."""
    if key in active_keys:
        del active_keys[key]
        keyboard.release(key)
        print(f"Stopped pressing: {key}")

def process_serial_data():
    """Read and process data from the ESP32."""
    global script_active

    if not script_active:
        return  # Ignore ESP32 data if the script is not active

    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        print(f"Received: {data}")

        if data == "CENTER":
            # Stop all keys when centered
            for key in list(active_keys.keys()):
                stop_pressing_key(key)
            return

        directions = data.split()
        received_keys = {key_map[dir] for dir in directions if dir in key_map}

        # Start pressing new keys
        for key in received_keys:
            start_pressing_key(key)

        # Stop pressing keys that are no longer active
        for key in list(active_keys.keys()):
            if key not in received_keys:
                stop_pressing_key(key)

def toggle_script_active():
    """Toggle the active state of the script."""
    global script_active

    script_active = not script_active
    if script_active:
        print("Script activated! Listening to ESP32 input...")
    else:
        print("Script deactivated! Stopping all keypresses...")
        for key in list(active_keys.keys()):
            stop_pressing_key(key)

def main():
    """Main function to run the script."""
    print("Press Ctrl+Shift+S to start the script.")
    print("Press Ctrl+Shift+X to stop the script and exit.")

    # Register hotkeys
    keyboard.add_hotkey("ctrl+shift+s", toggle_script_active)
    keyboard.add_hotkey("ctrl+shift+x", lambda: (toggle_script_active(), exit(0)))

    try:
        while True:
            process_serial_data()
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Exiting...")
        for key in list(active_keys.keys()):
            stop_pressing_key(key)

if __name__ == "__main__":
    main()
