import pyautogui
import time
import pyperclip

olimp = '''sbec59/sch770192/9/r52294
sbec59/sch770192/9/r528w4
sbec59/sch770192/9/5r6q46
sbec59/sch770192/9/r26qgr
sbec59/sch770192/9/5rv2r2
sbec59/sch770192/9/rw752r
sbec59/sch770192/9/9rg3r7
sbec59/sch770192/9/43vz6r
sbec59/sch770192/9/z43v7r
sbec59/sch770192/9/9rg6v4
sbec59/sch770192/9/8rz8wr
sbec59/sch770192/9/r2695r
sbec59/sch770192/9/rq562r
sbec59/sch770192/9/49qq94
sbec59/sch770192/9/z43z7r
sbec59/sch770192/9/rg96wr
sbec59/sch770192/9/rv3qv4
sbec59/sch770192/9/9rgw3r
sbec59/sch770192/9/49q894
sbec59/sch770192/9/q49v9r
sbec59/sch770192/9/r52394
sbec59/sch770192/9/r52gw4
sbec59/sch770192/9/z4387r
sbec59/sch770192/9/r6g6v4
sbec59/sch770192/9/2r27q4
sbec59/sch770192/9/rg9vwr
sbec59/sch770192/9/wrqz74
sbec59/sch770192/9/rv35v4
sbec59/sch770192/9/8rz9w4
sbec59/sch770192/9/748q2r
sbec59/sch770192/9/rq582r
sbec59/sch770192/9/r6g924
sbec59/sch770192/9/r76v74
sbec59/sch770192/9/rg9qwr
'''

list_olim = olimp.split()
print(pyautogui.size())
INSERT_COORD = (960, 640)
ENTER_COORD = (960, 730)
EXIT_COORD = (1870, 140)
FAMILE_COORD = (1780, 140)
COMAND_COORD = (960, 50)

def chek_olimp(user):
    pyautogui.click(INSERT_COORD)
    time.sleep(0.5)
    pyautogui.write(user)
    time.sleep(0.5)
    pyautogui.click(ENTER_COORD)
    time.sleep(0.5)
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

