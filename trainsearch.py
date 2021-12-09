# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:42:39 2021

@author: 皮皮卡卡
"""
import webbrowser, time
import pyautogui as gui
import pyperclip as pypl

url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime'
webbrowser.open(url)
time.sleep(3)

def click_paste(x, y, words):
    
    gui.click(x, y, duration=0.5)

    try:
        #pypl.copy(words)
        time.sleep(1)
        gui.write(words)
        #return print(str(words)+'be written.')
    except:
        return print(words+'could not be written on screen.')
    
'''
gui.click(700,598 duration=0.5) #起始站設定位置
gui.write('1000')
time.sleep(1)
gui.click(997,615, duration=1) #終點站設定位置


'''

click_paste(700, 605, '1000')
click_paste(997, 615, '1100')
gui.click(1540, 886, duration=1)


