import pyautogui as pg
from time import sleep
from tqdm import tqdm
from pynput import keyboard
import random
import PIL.ImageGrab

'''
TODO:create main skeleton for script
TODO:find pixel color sorting library for python or build own for challenge?
TODO:finalize method on efficiency of script and method.
'''


class PowerMiner(object):
    def __init__(self):

        #if self.inventory_full == False, then inventory can handle more
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


if __name__ == "__main__":
    miner = PowerMiner()

    miner.miner()
    miner.ore_dropper()
