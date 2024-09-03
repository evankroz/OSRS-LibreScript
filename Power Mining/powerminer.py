import pyautogui as pg
from time import sleep
from tqdm import tqdm
from pynput import keyboard
import random

'''
TODO:create main skeleton for script
TODO:find pixel color sorting library for python or build own for challenge?
TODO:finalize method on effieciency of script and method.
'''


class PowerMiner(object):
    def __init__(self):
        #if self.inventory_full == False, then inventory can handle more
        self.in_inventory = False
        self.color = (0,0,0)
        self.click = pg.position()

    def miner(self):
        while self.in_inventory is False:
            #mining  function
            pass
        pass

    def ore_dropper(self):
        '''
        while inventory is full:
            drop ore based on color
        when all ores are dropped,
        continue with main/mining function
        until inventory is full of ore again.

        '''
        pass
    def start(self):
        pass




if __name__ == "__main__":
    miner = PowerMiner()

    miner.miner()
    miner.ore_dropper()
