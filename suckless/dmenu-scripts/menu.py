#! /bin/python3.9

import dmenu
import os


class Main_Menu():
    def __init__(self):
        global TERMINAL
        TERMINAL = "st"
        self.categories = [
            "Mail", "Settings", "Graphics", "Internet", "Multimedia",
            "Devlopment", "Office", "Dotes", "Logout"
        ]
        self.prompt = dmenu.show(self.categories,
                                 prompt="Choose Categories",
                                 lines=20)
        if self.prompt == self.categories[0]:
            self.Mail_Reader()
        elif self.prompt == self.categories[1]:
            self.Settings()
        elif self.prompt == self.categories[2]:
            self.Graphics()
        elif self.prompt == self.categories[3]:
            self.Internet()
        elif self.prompt == self.categories[4]:
            self.Multimedia()
        elif self.prompt == self.categories[5]:
            self.Dev()
        elif self.prompt == self.categories[6]:
            self.Office()
        elif self.prompt == self.categories[7]:
            self.Dotes()
        elif self.prompt == self.categories[8]:
            self.Logout()

    def Mail_Reader(self):
        self.mail = ["NeoMutt", "Mailspring", "thunderbird", "Kmail", "Mutt"]
        self.mail_prompt = dmenu.show(self.mail,
                                      prompt="Choose Your Email Client",
                                      lines=20)
        if self.mail_prompt == self.mail[0]:
            os.system(f"{TERMINAL} -e neomutt")
        elif self.mail_prompt == self.mail[1]:
            os.system("mailspring")
        elif self.mail_prompt == self.mail[2]:
            os.system("thunderbird")
        elif self.mail_prompt == self.mail[3]:
            os.system("kmail")
        elif self.mail_prompt == self.mail[4]:
            os.system(f"{TERMINAL} -e mutt")

    def Settings(self):
        self.setting = [
            "Lxapperance", "Nvidia-settings", "weather", "Nitrogen", "Pcmanfm",
            "Octopi", "Pamac"
        ]
        self.settings_prompt = dmenu.show(self.setting,
                                          prompt="Settings",
                                          lines=20)
        if self.settings_prompt == self.setting[0]:
            os.system("lxappearance")
        elif self.settings_prompt == self.setting[1]:
            os.system("nvidia-settings")
        elif self.settings_prompt == self.setting[2]:
            os.system("weather")
        elif self.settings_prompt == self.setting[3]:
            os.system("nitrogen")
        elif self.settings_prompt == self.setting[4]:
            os.system("pcmanfm")
        elif self.settings_prompt == self.setting[5]:
            os.system("octopi")
        elif self.settings_prompt == self.setting[6]:
            os.system("pamac")

    def Graphics(self):
        self.graphic = ["Krita", "Gimp", "Kdenlive", "Etcher"]
        self.graphic_prompt = dmenu.show(self.graphic,
                                         prompt="Graphics",
                                         lines=20)
        if self.graphic_prompt == self.graphic[0]:
            os.system("krita")
        elif self.graphic_prompt == self.graphic[1]:
            os.system("gimp")
        elif self.graphic_prompt == self.graphic[2]:
            os.system("kdenlive")
        elif self.graphic_prompt == self.graphic[3]:
            os.system("etcher")

    def Internet(self):
        self.internet = ["FireFox", "Chrome", "Brave", "Librewolf", "Falkon"]
        self.internet_prompt = dmenu.show(self.internet,
                                          prompt="Choose Your Fav Browser",
                                          lines=20)
        if self.internet_prompt == self.internet[0]:
            os.system("firefox")
        elif self.internet_prompt == self.internet[1]:
            os.system("chrome")
        elif self.internet_prompt == self.internet[2]:
            os.system("Brave")
        elif self.internet_prompt == self.internet[3]:
            os.system("librewolf")
        elif self.internet_prompt == self.internet[4]:
            os.system("falkon")

    def Multimedia(self):
        self.multimedia = ["Spotify", "VLC", "SMTube", "MPsTube", "Audacity"]
        self.multimedia_prompt = dmenu.show(
            self.multimedia, prompt="Choose Your Multimedia App", lines=20)
        if self.multimedia_prompt == self.multimedia[0]:
            os.system("spotify")
        elif self.multimedia_prompt == self.multimedia[1]:
            os.system("vlc")
        elif self.multimedia_prompt == self.multimedia[2]:
            os.system("smtube")
        elif self.multimedia_prompt == self.multimedia[3]:
            os.system("mpsyt")
        elif self.multimedia_prompt == self.multimedia[4]:
            os.system("audacity")

    def Office(self):
        self.office = ["Libreoffice", "FreeOffice"]
        self.office_prompt = dmenu.show(self.office,
                                        prompt="Run Office ",
                                        lines=20)
        if self.office_prompt == self.office[0]:
            os.system("libreoffice")
        elif self.office_prompt == self.office[1]:
            os.system("onlyoffice-desktopeditors")

    def Dotes(self):
        os.system("./dmenu-edit.sh")

    def Dev(self):
        self.devlopment = [
            "Vscode", "Neovim", "Vim", "Pycharm", "Sublime Text"
        ]
        self.devlopment_prompt = dmenu.show(self.devlopment,
                                            prompt="Code Now ! ",
                                            lines=20)
        if self.devlopment_prompt == self.devlopment[0]:
            os.system("code")
        elif self.devlopment_prompt == self.devlopment[1]:
            os.system("st -e nvim")
        elif self.devlopment_prompt == self.devlopment[2]:
            os.system("st -e vim")
        elif self.devlopment_prompt == self.devlopment[3]:
            os.system("pycharm")
        elif self.devlopment_prompt == self.devlopment[4]:
            os.system("subl")

    def Logout(self):
        os.system("./dmenu-logout.sh")


Main_Menu()
