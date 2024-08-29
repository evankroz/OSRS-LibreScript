import pyautogui as pg
from time import sleep
from tqdm import tqdm
from pynput import keyboard
import random
import time


'''
DONE: esc is now the global hotkey to exit the script
TODO: Consistency issues with delay, pg.locateOnScreen() is not working? --> Not important
TODO: Store cords in tuple, ex: self.top_left = (self.x_val-2, self.y_val-2) --> Not important
TODO: Create a function in class HighAlch that finds valid points to click on to avoid ban --> In development
TODO: Set mouse position cursor based on location of spell.png?
TODO: Find a way to move my cursor with ease in function from pg, and click
NOTES: 1) Make sure cursor position is captured once at the start of the script
       2) Create a seperate function for clicking? 
'''


class HighAlch(object):
    def __init__(self):
        #capturing the initial mouse cursor position
        #and evaluating corners for harder detection by anti-ban
        #corners are the farthest the mouse should be allowed to move

        try:
            self.magic_location = pg.locateOnScreen(image="assets/spell.png")
        except pg.ImageNotFoundException:
            print("Image Not Found")
            print("Please Manually Place Your Cursor on High Alchemy Spell")

        self.x_val, self.y_val = pg.position()
        '''
        self.top_left_square_x, self.top_left_square_y = (self.x_val - 2, self.y_val - 2)
        self.top_right_square_x, self.top_right_square_y = (self.x_val + 2, self.y_val - 2)
        self.bottom_left_square_x, self.bottom_left_square_y = (self.x_val + 2, self.y_val + 2)
        self.bottom_right_square_x, self.bottom_right_square_y = (self.x_val - 2, self.y_val + 2)
        '''

    def clicker(self):
        while self.x_val and self.y_val and running:
            #DANGER: DO NOT remove "and running" as tehre would be no means to test the script
            #find extremeties with pixel depth for square corners
            print(f"x pos: {self.x_val}, y pos: {self.y_val}")

            #has not been tested for accuracy yet
            self.x_val = self.x_val+random.randrange(-2, 2)
            self.y_val = self.y_val+random.randrange(-2, 2)

            #optimize this for most consistent results
            #may need more than two delays for it to be consitent
            magic_menu_delay = random.uniform(.2, .5)
            norm_inv_delay = random.uniform(1.9, 2.2)

            pg.moveTo(x=self.x_val, y=self.y_val, duration=0.1, tween=pg.easeInQuad)
            pg.click() # --> This leads to problems, as it resets to original position every half seconds messing up
            print(f"Magic Menu Delay: {magic_menu_delay}")
            sleep(magic_menu_delay)

            pg.click() # --> Also leads to problems, shuld not be implemented during testing.
            print(f"Inventory Delay: {norm_inv_delay}")
            sleep(norm_inv_delay)

    @staticmethod
    def start():
        print("Program booting up...")
        #loading bar for 10 seconds, not essential
        for i in tqdm(range(5)):
            sleep(1)
        inp = input("Are you ready to begin program? Y/N")
        if inp.capitalize() == "Y":
            print("Loading dependencies...")
            print("Program starting, be ready, have cursor on high alchemy spell in magic tab")
            for i in tqdm(range(5)):
                sleep(1)
            print("Program has begun")
        else:
            print("Alright, Good Morning, Good Afternoon, Good Evening, and Good Night")
            print("Application Quit")

    #create a main function for clicker and everything?


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

