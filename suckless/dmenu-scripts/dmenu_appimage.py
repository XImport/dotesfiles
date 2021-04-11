import os
import dmenu

PATH = os.chdir("/home/import/Applications/")
Applications = os.listdir(PATH)
for app in Applications:
    os.system(f"chmod +x {app}")
    rename = os.rename(app, app.split("-")[0])
Lancher = dmenu.show(Applications, prompt="Applications://>>", lines=100)
os.system(f"./{Lancher}")
