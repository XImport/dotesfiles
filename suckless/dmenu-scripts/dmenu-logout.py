import dmenu
import os


class Main:
    def __init__(self):
        self.current_user = "import"
        menu_prompt = ["Exit", "Poweroff", "Hibernate", "Reboot"]
        self.choices = ["NO", "YES"]
        prompt = dmenu.show(menu_prompt,
                            lines=20,
                            prompt="What Would like me to do ??")
        if prompt == menu_prompt[0]:
            self.exit()
        if prompt == menu_prompt[1]:
            self.poweroff()
        if prompt == menu_prompt[2]:
            self.hibernate()
        if prompt == menu_prompt[3]:
            self.reboot()

    def exit(self):
        confirme = dmenu.show(self.choices, prompt="Choose ?", lines=2)
        if confirme == self.choices[1]:
            os.system(f"killall -u {self.current_user}")

    def poweroff(self):
        confirme = dmenu.show(self.choices, prompt="Choose ?", lines=2)
        if confirme == self.choices[1]:
            os.system("poweroff")

    def hibernate(self):
        confirme = dmenu.show(self.choices, prompt="Choose ?", lines=2)
        if confirme == self.choices[1]:
            os.system("systemctl hibernate")

    def reboot(self):
        confirme = dmenu.show(self.choices, prompt="Choose ?", lines=2)
        if confirme == self.choices[1]:
            os.system("systemctl reboot ")


Main()