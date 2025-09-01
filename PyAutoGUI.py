import pyautogui

n = int(input())
for i in range(1, n + 1):
    line = '# ' * i
    pyautogui.write(line)
    if i < n:
        pyautogui.press('enter')