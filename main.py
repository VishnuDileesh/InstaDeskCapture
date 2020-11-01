import pyautogui as bot
import time


def rest(n):
    time.sleep(n)


rest(2)

# bot.click(1371, 759)

rest(1)


def activeWallpaperScript():

    bot.hotkey('winleft', 'enter')  # open terminal

    rest(1)

    bot.write('bash -l')  # switch from zsh to bash
    bot.press('enter')

    rest(2)

    # open i3 config to active wallpaper script
    bot.write('nvim ~/.config/i3/config')
    bot.press('enter')

    rest(3)

    bot.press('esc')

    bot.hotkey('2', '3', 'shift', 'g')
    rest(1)
    bot.press(['d', 'd'])
    bot.press('i')
    bot.write('exec_always "./wpaper.sh"')
    bot.press('enter')
    bot.press('esc')

    rest(1)

    bot.hotkey('shift', ':', 'w', 'q')
    bot.press('enter')

    rest(1)

    bot.hotkey('winleft', 'c')

    rest(1)


# work flow

activeWallpaperScript()

bot.hotkey('winleft', 'shift', 'r')