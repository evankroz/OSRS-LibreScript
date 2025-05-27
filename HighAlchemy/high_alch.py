import pyautogui as pg
from time import sleep
from tqdm import tqdm
from pynput import keyboard
import random

'''
NOTE: ESC is the hotkey to terminate the script, do not try and stop manually
NOTE: Make sure cursor position is captured once at the start of the script
NOTE: PyAutoGui has a failsafe feature, if you get your mouse to any of the 4 corners of the screen
the failsafe will activiate the program will be disabled, just in case if ESC does not work.
'''


class HighAlch(object):
    def __init__(self):

        """try:
            self.magic_location = pg.locateOnScreen(image="assets/spell.png", minSearchTime=10, region=(get_win_info()), confidence=1)
            print(self.magic_location)
        except pg.ImageNotFoundException:
            print("Image Not Found")
            print("Please Manually Place Your Cursor on HighAlchemy Spell")"""

        self.x_val = 0
        self.y_val = 0

    def clicker(self):
        # while points are available to click on, and running = True, run the loop
        while self.x_val and self.y_val and running:
            # DANGER: DO NOT remove "and running" as there would be no means to stop the script

            # works for 27 inch monitor, 2k
            local_x_val = self.x_val+random.randrange(-3, 3)
            local_y_val = self.y_val+random.randrange(-3, 3)

            magic_menu_delay = random.uniform(.2, .5)
            norm_inv_delay = random.uniform(1.65, 1.95)

            # magic delay and moving functions for mouse

            pg.moveTo(x=local_x_val, y=local_y_val, duration=0.3, tween=pg.easeInQuad)
            print(f"x pos: {local_x_val}, y pos: {local_y_val}")
            pg.click()
            print(f"Magic Menu Delay: {magic_menu_delay}")
            sleep(magic_menu_delay)

            pg.click()
            print(f"Inventory Delay: {norm_inv_delay}")
            sleep(norm_inv_delay)

    def start(self):
        print("Program booting up...")
        for _ in tqdm(range(5)):
            sleep(1)
        inp = input("Are you ready to begin program? Y/N")
        if inp.capitalize() == "Y":
            print("Loading dependencies...")
            print("Program starting, be ready, have cursor on high alchemy spell in magic tab")
            for _ in tqdm(range(5)):
                sleep(1)
            self.x_val, self.y_val = pg.position()

            print("Program has begun")
        else:
            print("")
            print("Application Quit")


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

# Expected type '(Key | KeyCode | None) -> None | None', got '(key: {__eq__}) -> bool' instead?
listener = keyboard.Listener(on_press=on_press)
listener.start()


if __name__ == "__main__":
    main = HighAlch()
    try:
        while running:
            main.start()
            main.clicker()
    except KeyboardInterrupt:
        print("Program Interrupted")
    print("Program Terminated")
    