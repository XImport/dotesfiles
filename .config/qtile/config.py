# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2010 horsik
# Copyright (c) 2010 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import socket
import subprocess
import re
from libqtile.config import Group, Match, Key, ScratchPad, DropDown
from libqtile.command import lazy
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"


keys = [
    # Switch between windows

    # Window controls
    Key([mod], "k",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "j",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod, "shift"], "m",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),





    Key([mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key([mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # dmenu-scripts-Shift
    Key([mod, "shift"], "q", lazy.spawn(
        "/home/import/dmenu-scripts/dmenu-logout.sh"), desc="Shutdown Qtile"),
    Key([mod, "shift"], "s", lazy.spawn(
        "python3 /home/import/dmenu-scripts/sys-monitor.py"), desc="Sys MonitorQtile"),
    Key([mod, "shift"], "f", lazy.spawn(
        "/home/import/dmenu-scripts/dmenu-flatpak.sh"), desc="Flatpak Apps"),
    Key([mod, "shift"], "e", lazy.spawn(
        "/home/import/dmenu-scripts/dmenuemoji.sh"), desc="Dmenu EMoji"),
    Key([mod, "shift"], "a", lazy.spawn(
        "python3 /home/import/dmenu-scripts/dmenu_appimage.py"), desc="Apps Images"),
    Key([mod, "shift"], "w", lazy.spawn(
        "/home/import/Documents/scripts/wallzap"), desc="Wallpaper Changer"),

    # dmenu-scripts-Alt
    Key([mod, "mod1"], "f", lazy.spawn(
        "st -e /home/import/.config/vifm/scripts/vifmrun"), desc="Terminal FIle Manger"),
    Key([mod, "mod1"], "m", lazy.spawn(
        "st -e python3 /home/import/Documents/scripts/marocannonce.py"), desc="Job Script"),
    Key([mod, "mod1"], "t", lazy.spawn(
        "pcmanfm"), desc="Gui FIle Manger"),
    Key([mod, "mod1"], "s", lazy.spawn(
        "flameshot gui -d 2"), desc="Screenshot"),
    Key([mod, "mod1"], "m", lazy.spawn(
        "st -e neomutt"), desc="Terminal Mail"),
    Key([mod, "mod1"], "b", lazy.spawn(
        "qutebrowser"), desc="My Aweomse Qutebrowser"),
    Key([mod, "mod1"], "q", lazy.spawn(
        "calc"), desc="Gui Calculator"),
    # dmenu-scripts-key



    Key([mod], "p", lazy.spawn("/home/import/dmenu-scripts/dmenu.sh"),
        desc="Runner"),
    Key([mod], "x", lazy.spawn("i3lock-fancy -f Comic-Mono"),
        desc="Lock Screen"),
    Key([mod], "e", lazy.spawn("/home/import/dmenu-scripts/dmenu-edit.sh"),
        desc="Edit Configs"),
    Key([mod], "s", lazy.spawn("/home/import/dmenu-scripts/dmenuweb.sh"),
        desc="Surf Web"),



    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
]

group_names = [("WWW", {'layout': 'max', 'matches': [Match(wm_class=["firefox", "Brave-browser", "qutebrowser"])]}),
               ("DEV", {'layout': 'monadtall', 'matches': [
                Match(wm_class=["Sublime_text", "Code"])]}),
               ("SYS", {'layout': 'monadtall'}),
               ("DOC", {'layout': 'monadtall', 'matches': [
                Match(wm_class=["Pcmanfm"])]}),
               ("VBOX", {'layout': 'monadtall', 'matches': [
                Match(wm_class=["VirtualBox Manager", "Genymotion"])]}),
               ("CHAT", {'layout': 'monadtall', 'matches': [
                Match(wm_class=["whatsapp-nativefier-d52542"])]}),
               ("MUS", {'layout': 'monadtall'}),
               ("VID", {'layout': 'monadtall',
                        'matches': [Match(wm_class=["VLC"])]}),
               ("GFX", {'layout': 'floating', 'matches': [Match(wm_class=["Nitrogen", "Lxappearance", "Nvidia-settings"])]})]


groups = [Group(name, **kwargs) for name, kwargs in group_names]

groups.append(
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "/usr/bin/alacritty",
                 opacity=0.88, height=0.55, width=0.998, x=0),

        # define another terminal exclusively for qshell at different position
    ]), )

keys.extend([
    # Scratchpad
    # toggle visibiliy of above defined DropDown named "term"
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('term')),
])


for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))


layout_theme = {"border_width": 4,
                "margin": 5,
                "border_focus": "ff00b3",
                "border_normal": "b57da4"
                }


layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
        font="Comic Mono",
        fontsize=8,
        sections=["FIRST", "SECOND"],
        section_fontsize=8,
        bg_color="#141414",
        active_bg="100C435",
        active_fg="000000",
        inactive_bg="384323",
        inactive_fg="00eff7",
        padding_y=5,
        section_top=10,
        panel_width=320
    ),
    layout.Floating(**layout_theme)
]

colors = [["#000000", "#000000"],  # panel background
          ["#434758", "#434758"],  # background for current screen tab
          ["#ffffff", "#ffffff"],  # font color for group names
          ["#ff5555", "#ff5555"],  # border line color for current tab
          # border line color for other tab and odd widgets
          ["#8d62a1", "#8d62a1"],
          ["#668bd7", "#668bd7"],  # color for the even widgets
          ["#00FFFF", "#00FFFF"],  # color for the even widgets
          ["#f1fa8c", "#f1fa8c"],  # color for the even widgets
          ["#e1acff", "#e1acff"]]  # window name

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    font="Comic Mono",
    fontsize=11,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [

                widget.Image(
                    filename="~/.config/qtile/icons/python.png",
                    mouse_callbacks={
                        'Button1': lambda qtile: qtile.cmd_spawn('dmenu_run')}
                ),
                widget.Sep(
                    linewidth=0,
                    padding=12,
                    foreground=colors[2],
                    background=colors[0]
                ),

                widget.GroupBox(
                    font="Comic Mono",
                    fontsize=12,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=colors[3],
                    inactive=colors[2],
                    rounded=False,
                    highlight_color=colors[1],
                    highlight_method="line",
                    this_current_screen_border=colors[8],
                    this_screen_border=colors[8],
                    other_current_screen_border=colors[0],
                    other_screen_border=colors[0],
                    foreground=colors[2],
                    background=colors[0]

                ),
                widget.Sep(
                    linewidth=0,
                    padding=40,
                    foreground=colors[2],
                    background=colors[0]
                ),
                widget.Prompt(),
                widget.WindowName(
                    borderwidth=3,
                    font="Comic Mono",
                    fontsize=15,

                ),
                widget.TextBox(
                    text=" ",
                    background=colors[4],
                    fontsize=14

                ),


                widget.OpenWeather(
                    app_key="89055558a0d4f266d3213909268cb9a9",
                    cityid="2530335",
                    background=colors[4],
                    font='Comic Mono',
                    fontsize=11,
                ),
                widget.TextBox(
                    text=" ",
                    background=colors[8],
                    fontsize=14

                ),
                widget.CPU(
                    background=colors[8],
                    font='Comic Mono',
                    fontsize=11,
                    foreground=colors[0]
                ),

                widget.TextBox(
                    text="",
                    background=colors[4],
                    fontsize=14

                ),
                widget.Memory(
                    background=colors[4],
                    font='Comic Mono',
                    fontsize=11,
                    update_interval=1
                ),

                widget.TextBox(
                    text="",
                    background=colors[8],
                    fontsize=14

                ),


                widget.CheckUpdates(
                    colour_have_updates=colors[0],
                    update_interval=100,
                    background=colors[8],
                    font='Comic Mono',
                    fontsize=11,
                ),

                widget.TextBox(
                    text="",
                    background=colors[4],
                    fontsize=14
                ),
                widget.CurrentLayout(
                    background=colors[4],
                    font='Comic Mono',
                    fontsize=11,
                ),

                widget.TextBox(
                    text="",
                    background=colors[8],
                    fontsize=14
                ),


                widget.Clock(format='%Y-%m-%d  %I:%M %p',
                             background=colors[8],
                             font='Comic Mono',
                             foreground=colors[0],
                             fontsize=10),

                widget.Systray(),
            ],
            17,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='Nitrogen'),  # gitk
    Match(wm_class='Lxappearance'),  # gitk
    Match(wm_class='Nvidia-settings'),  # gitk
    Match(wm_class='Gimp'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
