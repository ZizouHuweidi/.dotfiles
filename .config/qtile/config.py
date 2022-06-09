# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
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

from typing import List  

import re
import socket
import subprocess
import os

from libqtile import qtile
from libqtile import hook 
from libqtile.widget import base
from libqtile.config import Group, Key, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.command import lazy


#################################################################
#module imports
#################################################################
 
from modules.keys import keys, mod, terminal, home_dir
from themes.colors import colors 
from modules.screens import screens
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse

#################################################################

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)



#################################################################
# custom workspace names and initialization
#################################################################
 
class Groupings:

    def init_group_names(self):
        return [
                ("", {"layout": "monadtall"}), 
                ("", {"layout": "max"}), 
                ("", {"layout": "monadtall"}),     
                ("", {"layout": "monadtall"}),      
                ("", {"layout": "max"}),
                ("", {"layout": "floating"}),
                                                ]

    def init_groups(self):
        return [Group(name, **kwargs) for name, kwargs in group_names]


if __name__ in ["config", "__main__"]:
    group_names = Groupings().init_group_names()
    groups = Groupings().init_groups()


#################################################################
###############CHANGE WORKSPACES
#################################################################
 
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))                                      # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))                               # Switch window to another group and stay on group 
#    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name), lazy.group[name].toscreen())) # Switch window to another group and follow
    keys.append(Key([mod], "Tab", lazy.screen.next_group()))                                          # Switch to next group
    keys.append(Key(["mod1"], "Right", lazy.screen.next_group()))                                          # Switch to next group
    keys.append(Key(["mod1"], "l", lazy.screen.next_group()))                                          # Switch to next group
    keys.append(Key([mod, "shift" ], "Tab", lazy.screen.prev_group()))                                # Switch to previous group
    keys.append(Key(["mod1"],"Left" , lazy.screen.prev_group()))                                # Switch to previous group
    keys.append(Key(["mod1"],"h" , lazy.screen.prev_group()))                                # Switch to previous group
    keys.append(Key(["mod1"], "Tab", lazy.screen.next_group()))                                       # Switch to next group 
    keys.append(Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()))                              # Switch to previous group



#################################################################
# assign apps to groups/workspace
#################################################################
 
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}

    # assign deez apps
    d[group_names[0][0]] = ['neovide']
    d[group_names[1][0]] = ['brave-browser', 'Navigator', 'qutebrowser']
    d[group_names[2][0]] = ['vscodium', 'org.pwmt.zathura', 'mongodb compass', 'postman', "Eclipse"]
    d[group_names[3][0]] = ['pavucontrol','pcmanfm', 'arandr','xfce4-appfinder']
    d[group_names[4][0]] = ['discord', 'mailspring', 'telegram-desktop', 'slack']
    d[group_names[5][0]] = ['deadbeef', 'Steam','pcsx2','Lutris','VirtualBox Manager' ]




    wm_class = client.window.get_wm_class()[0]
    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)



#################################################################
#    scratchpads
#################################################################
 
conf = {
    "warp_pointer": False,
    "on_focus_lost_hide": False,
    "opacity": 1,
}

groups.append(
    ScratchPad("scratchpad",[
        DropDown("drop", "kitty", height=0.4, **conf),
        DropDown("music", "deadbeef", x=0.12, y=0.2, width=0.56, height=0.7, **conf),
        DropDown("top", "kitty -e htop", x=0.3, y=0.1, width=0.5, height=0.7, **conf),
        DropDown("notes", "obsidian", x=0.2, y=0.1, width=0.6, height=0.8, **conf),
    ]),
)

keys.append(Key([mod, "shift"], "Return", lazy.group["scratchpad"].dropdown_toggle("drop"))),
keys.append(Key([mod,"shift"], "m", lazy.group["scratchpad"].dropdown_toggle("music"))),
keys.append(Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("top"))),
keys.append(Key([mod, "shift"], "n", lazy.group["scratchpad"].dropdown_toggle("notes"))),

############################################################################


main = None
@hook.subscribe.startup
def start_once():
    start_script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([start_script])

@hook.subscribe.startup_once
def start_always():
    # fixes the cursor
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"
