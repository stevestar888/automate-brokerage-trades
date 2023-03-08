# https://digital.fidelity.com/ftgw/digital/trade-equity/index

import pyautogui
import time


ACCOUNT_DROPDOWN = (412, 315)
AREA_CLOSE_TO_PREVIEW = (930, 840)


def place_order(account_position):
    pyautogui.scroll(30) #scroll up
    
    time.sleep(0.1)

    pyautogui.moveTo(ACCOUNT_DROPDOWN)
    pyautogui.click()
    time.sleep(0.2)
    
    for _ in range(account_position):
        pyautogui.hotkey("down")
        time.sleep(0.02)

    time.sleep(0.3)
    pyautogui.hotkey("enter")
    time.sleep(1)

    # I found that clicking somewhere close to "Preview" and then pressing tab is 
    # much more reliable than actually straight up clicking "Preview"
    pyautogui.moveTo(AREA_CLOSE_TO_PREVIEW)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey("space")
    time.sleep(2)

    print(f'placing trade on account {account_position}')
    print("\n")
    pyautogui.hotkey("space")
    time.sleep(1.4)

# --------------------------- 

OFFSET = 0

# NOTE: num of dropdowns required = num accounts - 1
NUM_ACCOUNTS = 5

for i in range(NUM_ACCOUNTS):
    print("Placing trade #{}".format(i+1))
    place_order(i + OFFSET)