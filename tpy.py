
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
py.moveTo(x=641, y=753, duration=1.5)
py.PAUSE = 3
py.click()
py.moveTo(x=414, y=35, duration=1.5)
py.PAUSE = 1
py.click()
py.moveTo(x=596, y=573, duration=1.5)
py.PAUSE = 1
py.click()

py.scroll(clicks=-1000)
py.moveTo(x=828, y=617, duration=1.5)
py.PAUSE = 1
py.click()

for i in range(10):
    #click downoas
    py.moveTo(x=1275, y=732, duration=1)
    py.click()
    #click on start download
    py.moveTo(x=49, y=385, duration=1)
    py.click()
