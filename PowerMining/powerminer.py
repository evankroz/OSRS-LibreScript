import pyautogui as pg
from CoreFunctions.core import get_win_info

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
        self.click_color = (256, 0, 0)
        self.click = pg.position()

    def miner(self):
        #screen range is self.screen_size.
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


if __name__ == "__main__":
    miner = PowerMiner()
    miner.start()
    print(f"{miner.screen()[0]}, {miner.screen()[1]}")


