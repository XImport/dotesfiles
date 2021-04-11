#! /bin/python3.9
from colorama import Back, Fore, Style
import os
import time


class Main:
    def __init__(self):
        entry = Back.RED + Fore.BLACK + f'''  dwm :{Fore.WHITE+Style.RESET_ALL}                                                                                           {Back.BLUE}{Fore.BLACK}  Dmenu-Scripts :{Fore.WHITE+Style.RESET_ALL}
{self.find("quit,                   {0}","reload dwm")}                                                                   {self.find("dmenu-logout.sh","PowerOff/Reboot/Logout")}
{self.find("logout","quit dwm")}                                                                   {self.find("dmenuweb.sh","Load Your Bookmarks")}
{self.find("sheet.sh","show help")}                                                                    {self.find("dmenuweb.sh","Load Your Bookmarks")}
{self.find(".v = dmenucmd","dwm execute prompt")}                                                                     {self.find("dmenu-edit.sh","Edit Your Configs")}
{Back.YELLOW}{Fore.BLACK}  Client :{Fore.WHITE+Style.RESET_ALL}                                                                                        {self.find("dmenu-flatpak.sh","Load Your Flatpak Apps")}
{self.find(".i = +1","focus next by index")}                                                                    {self.find("dmenuemoji.sh","Load Your Emoji")}
{self.find(".i = -1","focus pervious by index")}                                                                   {self.find("dmenu-color.py","Load Colors")}
{self.find("setmfact,               {.f = +0","increase thenumber of master clients")}
{self.find("setmfact,               {.f = -0","decrease thenumber of master clients")}
{self.find("rotatestack,            {.i = ","swap with next client by index")}
{self.find("rotatestack,            {.i = ","swap with pervious client by index")}
{self.find("killclient,             {0}","Quit Window")}
{self.find("togglefloating,         {0}","toggle floating")}
{self.find("{.v = &layouts[3]}","toggle full screen")}
{self.find("togglebar","Hide The bar and switch to Horizontal Layout")}
{self.find("view","View All open clients")}
{Back.MAGENTA}{Fore.BLACK}  Launcher :{Fore.WHITE+Style.RESET_ALL}
{self.find(".v = termcmd1","open a terminal")}
{self.find(".v = wbrowse ","open web browser")}
{self.find("pcmanfm","open file manager")}
{self.find("subl","open your editor")}
{Back.MAGENTA}{Fore.BLACK}  Layout :{Fore.WHITE+Style.RESET_ALL}
{self.find("{.v = &layouts[0]}","Tile Layout")}
{self.find(".v = &layouts[2]}","No Gaps")}
{self.find(".v = &layouts[3]}","Max Layout")}
{self.find(".v = &layouts[1]}","Float Layout")}
{Back.CYAN}{Fore.BLACK}  Screen :{Fore.WHITE+Style.RESET_ALL}
{self.find("focusmon,               {.i = +1 }","Focus on other monitor")}
{self.find("focusmon,               {.i = -1 }","Focus on previous monitor")}
{Back.YELLOW}{Fore.BLACK}  Tag :{Fore.WHITE+Style.RESET_ALL}
{Fore.RED}MODKEY+ShiftMask+1/2/3/4/5/6/7/8/9 {Fore.WHITE}: {Fore.MAGENTA}Send window to specific tag
{Fore.RED}MODKEY+ShiftMask+0 {Fore.WHITE}: {Fore.MAGENTA}Show whole open clients'''
        while True:
            print(entry)
            time.sleep(2000)

    def find(self, key, desc):
        try:
            keys = []
            with open("/home/import/.config/dwm/" + "config.h") as dwm:
                for search in dwm.readlines():
                    if key in search:
                        keys.append(search.rstrip())
            keys = keys[0].strip().replace(" ", "").split(",")
            keys = (keys[0] + keys[1]
                    ).replace("{", "").replace("XK_", "+").replace("|", "+")
            final = Fore.RED + f"{keys}" + Fore.WHITE + \
                " : " + Fore.MAGENTA + f"{desc}" + Fore.WHITE
            return final
        except:
            pass


if __name__ == "__main__":
    Main()
