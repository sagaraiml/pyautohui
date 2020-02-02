# -*- coding: utf-8 -*-

import pyautogui as py
#h, w = py.size()
#py.moveTo(100, 200, duration=2)
#py.position()
#py.click(x=311, y=62, duration=1.5)
#py.moveTo(100, 200, duration=2)
#py.position()
#minimize >> run firefox >> play video
#x=1279, y=5
#x=84, y=747
#x=30, y=522
# =============================================================================
# py.click(x=1279, y=5, duration=1.5)
# py.click(x=84, y=747, duration=1.5)
# py.click(x=30, y=522, duration=1.5)
# =============================================================================
#wind >> click notepad
#py.moveTo(x=20, y=750, duration=1.5)
#py.PAUSE = 3
#py.click()
#py.click(x=168, y=384, duration=1.5)
#py.PAUSE = 5
#py.typewrite('Hi Uday go fast')
#=============================idm download===========
#
py.position()
#mozila
py.moveTo(x=78, y=747, duration=1.5)
py.PAUSE = 3
py.click()
for i in range(9):
    #click downoas
    py.moveTo(x=871, y=136, duration=1)
    py.PAUSE = 3
    py.click()
    #click on start download
    py.moveTo(x=673, y=459, duration=1)
    py.PAUSE = 2
    py.click()
    #minimize
    py.moveTo(x=834, y=154, duration=1)
    py.PAUSE = 2
    py.click()
    py.PAUSE = 5
    #next video
    py.moveTo(x=995, y=345, duration=1)
    py.PAUSE = 5
    py.click()
    py.PAUSE = 10