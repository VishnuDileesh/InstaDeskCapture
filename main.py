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


def activateTransparency():

    bot.hotkey('winleft', 'enter')
    rest(1)

    bot.write('compton')
    bot.press('enter')

    bot.hotkey('winleft', 'shift', '1')


def openClock():

    bot.hotkey('winleft', 'enter')
    rest(1)

    bot.write('tty-clock')
    bot.press('enter')

    # place the clock
    rest(1)
    bot.hotkey('winleft', 'shift', 'space')
    rest(1)

    # resize
    bot.hotkey('winleft', 'r')

    for x in range(31):
        bot.press('left')

    for x in range(19):
        bot.press('up')

    bot.press('esc')

    # reposition

    for x in range(22):
        bot.hotkey('winleft', 'shift', 'left')

    for x in range(11):
        bot.hotkey('winleft', 'shift', 'up')


# work flow

activeWallpaperScript()

bot.hotkey('winleft', 'shift', 'r')

rest(1)

activateTransparency()

rest(1)

bot.hotkey('winleft', '9')

openClock()