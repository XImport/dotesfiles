
import os
import pyperclip
import dmenu


class Main:
    def __init__(self):
        color_prompt = ["RED", "BLUE", "GREEN", "YELLOW",
                        "PURPLE", "PINK", "CYAN", "ORANGE", "WHITE", "BLACK"]
        cmd = dmenu.show(color_prompt, lines=10, prompt="CHOOSE COLOR")
        if cmd == "RED":
            pyperclip.copy("#ff005d")
            os.system(
                ''' notify-send "Color has been successfully copied to clipboard." ''')
        if cmd == "BLUE":
            pyperclip.copy("#2200ff")
            os.system(
                ''' notify-send "Color has been successfully copied to clipboard." ''')
        if cmd == "GREEN":
            pyperclip.copy("#37ff00")
            os.system(
                ''' notify-send "Color has been successfully copied to clipboard." ''')
        if cmd == "YELLOW":
            pyperclip.copy("#f2ff00")
            os.system(
                ''' notify-send "Color has been successfully copied to clipboard." ''')
        if cmd == "PURPLE":
            pyperclip.copy("#9200fa")
            os.system(
                ''' notify-send "Color has been successfully copied to clipboard." ''')
        if cmd == "PINK":
            pyperclip.copy("#ff00dd")
            os.system(
                ''' notify-send "Color has been successfully copied to clipboard." ''')
        if cmd == "CYAN":
            pyperclip.copy("#005577")
            os.system(
                ''' notify-send "Color has been successfully copied to clipboard." ''')
        if cmd == "ORANGE":
            pyperclip.copy("#ff8c00")
            os.system(
                ''' notify-send "Color has been successfully copied to clipboard." ''')
        if cmd == "WHITE":
            pyperclip.copy("#FFFFFF")
            os.system(
                ''' notify-send "Color has been successfully copied to clipboard." ''')
        if cmd == "BLACK":
            pyperclip.copy("#000000")
            os.system(
                ''' notify-send "Color has been successfully copied to clipboard." ''')


if __name__ == "__main__":
    Main()
