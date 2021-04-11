import dmenu
import os
import time

choices = ["Compling", "Copying", "Edit"]


prompt = dmenu.show(choices, prompt="What Would Like Me To DO ?! 👾", lines=3)


if prompt == "Compling":
    os.chdir("/home/import/Documents/dotes/suckless/dwm-6.2/")
    os.system("make clean install")
    time.sleep(2)
    os.system("notify-send 'Compling Done Boos 👍'")

elif prompt == "Copying":
    os.chdir("/home/import/Documents/dotes/suckless/dwm-6.2/")
    os.system("cp config.def.h config.h")


elif prompt == "Edit":
    os.chdir("/home/import/Documents/dotes/suckless/dwm-6.2/")
    os.system(" st -e nvim config.def.h")
