import pyautogui
import time
import pyperclip

olimp = '''
sbip51/sch770192/10/z59v9z
sbip51/sch770192/10/4w8q5z
sbip51/sch770192/10/z2gvq4
sbip51/sch770192/10/z2g554
sbip51/sch770192/10/49wg54
sbip51/sch770192/10/z7rq64
sbip51/sch770192/10/4rq5rz
sbip51/sch770192/10/z6w8v4
sbip51/sch770192/10/zqv674
sbip51/sch770192/10/z226gz
sbip51/sch770192/10/z532rz
sbip51/sch770192/10/z6wrv4
sbip51/sch770192/10/4r9r5z
sbip51/sch770192/10/z2vqgz
sbip51/sch770192/10/4wr8qz
sbip51/sch770192/10/z2v25z
sbip51/sch770192/10/z7vq54
sbip51/sch770192/10/48vv24
'''

list_olim = olimp.split()
print(pyautogui.size())
INSERT_COORD = (960, 640)
ENTER_COORD = (960, 730)
EXIT_COORD = (1870, 140)
FAMILE_COORD = (1780, 140)
COMAND_COORD = (960, 50)


def chek_olimp(user: str):
    pyautogui.click(INSERT_COORD)
    time.sleep(0.5)
    pyautogui.write(user)
    time.sleep(0.5)
    pyautogui.click(ENTER_COORD)
    time.sleep(1)
    pyautogui.doubleClick(FAMILE_COORD)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    fam = pyperclip.paste()
    if 'Выйти' in fam:
        img = pyautogui.screenshot(f'{fam[:-5]}.png')
        time.sleep(0.5)
        pyautogui.click(EXIT_COORD)
    else:
        pyautogui.click(COMAND_COORD)
        pyautogui.press('enter')


for user in list_olim:
    print(user)
    time.sleep(1)
    chek_olimp(user)
