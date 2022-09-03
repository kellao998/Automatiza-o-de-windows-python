from webbrowser import Chrome
import pyautogui
import time
import random



n=('good game', 'good luck for all', 'Hello my friends, good luck! 🍀 ', 'good games for all', 'best of luck my friends', 'hello everyone', 'have a nice day guys')
a=(' ',' ','@kellao91','@xaras','@etheisen',' ')
t=('100','150','120','160','101','125','240','210','155','165')

f=random.choice(t)


for i in range(72):
     
    pyautogui.press("win")
    time.sleep(2)
    pyautogui.write("chrome")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(x=2263, y=110, clicks=1)
    time.sleep(2)
    pyautogui.write("https://wolf.bet/pt")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=2955, y=955, clicks=3)
    time.sleep(4)
    pyautogui.write(random.choice(a),random.choice(n))
    time.sleep(3)
    pyautogui.click(x=3158, y=1015, clicks=1)
    time.sleep(4)

    pyautogui.hotkey("ctrl","T")
    time.sleep(3)
    pyautogui.click(x=2168, y=107, clicks=1)
    time.sleep(3)    
    pyautogui.write("https://casinoroyale.bet/games")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=2055, y=923, clicks=2)
    time.sleep(4)
    pyautogui.write(random.choice(n))
    time.sleep(3)
    pyautogui.click(x=2060, y=979, clicks=1)
    time.sleep(6)


    pyautogui.hotkey("ctrl","T")
    time.sleep(3)
    pyautogui.click(x=2168, y=107, clicks=1)
    time.sleep(3)    
    pyautogui.write("https://luckydiamond.io/")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=2955, y=1019, clicks=2)
    time.sleep(4)
    pyautogui.write(random.choice(n))
    time.sleep(3)
    pyautogui.click(x=3163, y=1013, clicks=1)
    time.sleep(6)

    pyautogui.hotkey("ctrl","T")
    time.sleep(3)
    pyautogui.click(x=2168, y=107, clicks=1)
    time.sleep(3)    
    pyautogui.write("https://pasino.com/")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=3002, y=1029, clicks=2)
    time.sleep(4)
    pyautogui.write(random.choice(n))
    time.sleep(3)
    pyautogui.click(x=3167, y=1021, clicks=1)
    time.sleep(6)
    pyautogui.hotkey("alt","F4")
    time.sleep(f)
