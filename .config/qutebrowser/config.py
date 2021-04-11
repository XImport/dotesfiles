import subprocess
import os
from qutebrowser.api import interceptor

# variables
soft_black = "#1f1f1f"
black = "#000000"
darkgrey = "#030303"
magenta = "#ff009e"
midgrey = "#544d4d"
pink = "#ff00f3"
red = "#ff0000"
white = "#ffffff"
yellow = "#ffdb00"
green = "#00e03c"

config.load_autoconfig(True)
"""
qutebrowser settings for video
for more settings check out
https://qutebrowser.org/doc/help/settings.html
"""

# ================== Youtube Add Blocking ======================= {{{


def filter_yt(info: interceptor.Request):
    """Block the given request if necessary."""
    url = info.request_url
    if (
        url.host() == "www.youtube.com"
        and url.path() == "/get_video_info"
        and "&adformat=" in url.query()
    ):
        info.block()


interceptor.register(filter_yt)


# =============================== END OF ADBLOCKER SECTION


c.url.start_pages = "/home/import/.config/qutebrowser/Minimal-StartPage/index.html"
c.zoom.default = "70%"
# ==================================== PANEL BACKGROUND COLOR : ==================
c.colors.completion.odd.bg = black
c.colors.completion.even.bg = black
# ======================================== SELECTION COLOR
c.colors.completion.item.selected.bg = pink
c.colors.completion.item.selected.border.top = black
c.colors.completion.item.selected.border.bottom = black
c.colors.statusbar.insert.bg = green
c.colors.statusbar.insert.fg = black
c.colors.tabs.pinned.selected.even.bg = green
c.content.user_stylesheets = '~/.config/qutebrowser/style.css'

c.tabs.indicator.padding = {"top": 0, "right": 0, "bottom": 0, "left": 0}
c.tabs.indicator.width = 0
c.tabs.padding = {"top": 2, "right": 2, "bottom": 2, "left": 2}
c.tabs.position = "left"
c.colors.tabs.bar.bg = black

c.tabs.title.format = ""
# =============================== KEYBDINGS FOR SHOWING OR HIDING TABS AND BAR
config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind(
    'xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')
