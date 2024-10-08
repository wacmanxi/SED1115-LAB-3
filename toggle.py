from machine import Pin
import utime  # to handle the timing and button deboune

# Define the LED and Button pins on the expansion board
led1 = Pin(18, Pin.OUT)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

led_state = False  # Starts with the LED off
last_press_time = 0  # Tracks the last button press time
debounce_delay = 200  # This is the debounce time in milliseconds

while True:
    current_time = utime.ticks_ms()  # Gets current time and converts to milliseconds
    
    # Checks if the button is pressed
    if sw5.value() == 1 and utime.ticks_diff(current_time, last_press_time) > debounce_delay:
        led_state = not led_state  # Toggles the LED state
        if led_state:
            led1.on()  # Turns on the LED
        else:
            led1.off()  # Turns off the LED
            
        last_press_time = current_time  # Updates the last press time
        
    utime.sleep_ms(10)  # Incorporation of a small delay to reduce CPU usage
