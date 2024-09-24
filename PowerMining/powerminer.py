import pyautogui as pg
from time import sleep
from tqdm import tqdm
from pynput import keyboard
import random
import PIL.ImageGrab
from core import get_win_info

'''
TODO:create main skeleton for script
TODO:find pixel color sorting library for python or build own for challenge?
TODO:finalize method on efficiency of script and method.
'''


class PowerMiner(object):
    def __init__(self):

        #if self.inventory_full == False, then inventory can handle more
        self.username = "PureBerr"  # -> change this depending on your osrs username in-game
        self.screen_size = get_win_info(self.username)
        self.ore_locate = (0, 0)
        self.inventory_full = False
        self.color = (256, 0, 0)
        self.click = pg.position()

        self.s = pg.screenshot()
        for x in range(self.s.width):
            for y in range(self.s.height):
                pass

    def miner(self):
        while self.inventory_full is False:
            #mining  function
            pass
        pass

    def screen(self):
        return self.screen_size

    def ore_dropper(self):
        pass
        '''
        while inventory is full:
            drop ore based on color
        when all ores are dropped,
        continue with main/mining function
        until inventory is full of ore again.

        '''

    def start(self):
        pass


miner = PowerMiner()
print(f"{miner.screen()[0]}, {miner.screen()[1]}")
