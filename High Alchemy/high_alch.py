import pyautogui as pg
from time import sleep
from tqdm import tqdm
from pynput import keyboard
import random

'''
NOTE: ESC is the hotkey to terminate the script, do not try and stop manually
NOTE: Make sure cursor position is captured once at the start of the script
'''


class HighAlch(object):
    def __init__(self):
        #isnt consistent at all, rarely actually detects, something wrong with library?
        try:
            self.magic_location = pg.locateOnScreen(image="assets/spell.png")
        except pg.ImageNotFoundException:
            print("Image Not Found")
            print("Please Manually Place Your Cursor on High Alchemy Spell")

        #initialiazes x and y values for cursor
        self.x_val = 0
        self.y_val = 0

        '''
        self.top_left_square_x, self.top_left_square_y = (self.x_val - 2, self.y_val - 2)
        self.top_right_square_x, self.top_right_square_y = (self.x_val + 2, self.y_val - 2)
        self.bottom_left_square_x, self.bottom_left_square_y = (self.x_val + 2, self.y_val + 2)
        self.bottom_right_square_x, self.bottom_right_square_y = (self.x_val - 2, self.y_val + 2)
        '''

    def clicker(self):
        #while points are available to click on, and running = True, run the loop
        while self.x_val and self.y_val and running:
            #DANGER: DO NOT remove "and running" as tehre would be no means to test the script

            #works for 27 inch monitor, 2k
            local_x_val = self.x_val+random.randrange(-3, 3)
            local_y_val = self.y_val+random.randrange(-3, 3)

            #laptop, screen
           # local_x_val = self.x_val + random.randrange(-1, 1)
           # local_y_val = self.y_val + random.randrange(-1, 1)

            magic_menu_delay = random.uniform(.2, .5)
            norm_inv_delay = random.uniform(1.9, 2.2)

            #magic delay and moving functions for mouse

            pg.moveTo(x=local_x_val, y=local_y_val, duration=0.3, tween=pg.easeInQuad)
            print(f"x pos: {local_x_val}, y pos: {local_y_val}")
            pg.click()
            print(f"Magic Menu Delay: {magic_menu_delay}")
            sleep(magic_menu_delay)

            pg.click()
            print(f"Inventory Delay: {norm_inv_delay}")
            sleep(norm_inv_delay)

    #styalized functions for cool-points
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
            self.x_val, self.y_val = pg.position() #--> initializes mouse coordinates once user has mouse already on high alch spell

            print("Program has begun")
        else:
            print("Alright, Good Morning, Good Afternoon, Good Evening, and Good Night")
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


listener = keyboard.Listener(on_press=on_press)
listener.start()


if __name__ == "__main__":
    main = HighAlch()
    try:
        while running:
            main.start()
            main.clicker()
    except KeyboardInterrupt:
        print("Program interrupted")
    print("Program Stopped")

