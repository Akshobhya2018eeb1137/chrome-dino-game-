from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *
import webbrowser
class coordinates:
    replay_btn = (341,415)
    dino_head = (162,423)


def restart():
    pyautogui.click(coordinates.replay_btn)
    pyautogui.keyDown('down')

def playGame():
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    url = 'chrome://dino//'
    webbrowser.get('chrome').open(url)
    time.sleep(0.2)
    pyautogui.write('chrome://dino/', interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')
    restart()

def colliding():
    image = ImageGrab.grab().convert('L')
    data = image.load()
    #for birds
    for i in range(250, 300):
        for j in range(410, 560):
            if data[i, j] < 100:
                pyautogui.keyDown("down")
                return 
    #for cactus
    for i in range(275, 325):
        for j in range(560, 650):
            if data[i, j] < 100:
                pyautogui.keyDown("up")
                return 
    return 

def main():
    playGame()
    time.sleep(2)
    pyautogui.keyDown("up")
    time.sleep(1)
    while True:
        colliding()
pyautogui.FAILSAFE = False

def check():
    playGame()
    time.sleep(2)
    pyautogui.keyDown("up")
    time.sleep(3)
    image = ImageGrab.grab().convert('L')
    data = image.load()
    #for birds
    for i in range(300, 415):
        for j in range(410, 560):
            data[i, j] = 10
    #for cactus
    for i in range(300, 415):
        for j in range(560, 650):
            data[i, j] = 190
    image.show()

#check()      
main()
