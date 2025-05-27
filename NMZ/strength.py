from numpy import zeros
import pyautogui as pg
from time import sleep
from pynput import keyboard
import random

class Strength(object):
    def __init__(self):
        # correctly get prayer drain pos, use bar?
        self.praybar_pos = (0,0)
        # correctly click on full pray pots, predef. positions, and count number of times clicked per pos?
        self.praypot_x = None
        self.praypot_y = None
        # self.cols = [...]
        # self.rows = [...]

    def setup(self):
        self.praypot_x, self.praypot_y = pg.position()
        print(f"Top left pray pot set at {self.praypot_x}, {self.praypot_y}")

    def drink(self):
        pass

    def get_prayer_points(self):
        pass

    def loop(self):
        pass
        
running = True

def on_press(key):
    global running
    try:
        if key == keyboard.Key.esc:
            print("Escape key pressed")
            running = False
            return False
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

if __name__ == "__main__":
    bot = Strength
    bot.setup()
    try:
        bot.attack_loop()
    except KeyboardInterrupt:
        print("Program Interrupted")
    print("Program Terminated")

