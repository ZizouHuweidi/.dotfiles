import os
from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord, DropDown, ScratchPad
from libqtile import extension

# default variables
mod = "mod4"
terminal = "kitty"
home_dir = os.path.expanduser("~")
sys_info = "alacritty -e htop"
fileman = "alacritty -e ranger"
browser1 = "brave"
browser2 = "firefox"
browser3 = "qutebrowser"
music1 = "spotify"
music2 = "alacritty -e ncmpcpp"
codev = "kitty -e nvim"
codec = "vscodium"
codes = "subl"



dmenu_theme = { "dmenu_font": "Source Code Pro Medium",
                    "background": '#282828',
                    "foreground": '#d5c4a1',
                    "selected_background": "#d79921",
                    "selected_foreground": "#282828",
                    "dmenu_height": 32,  
              }



keys = [

 

#################################################################
#     APPS
#################################################################
 

### Browsers
    KeyChord([mod], "F1",[
        Key([], "b", lazy.spawn(browser1)),
        Key([], "f", lazy.spawn(browser2)),
        Key([], "q", lazy.spawn(browser3)),],
        mode="Browsers"
    ),


### Mail
    KeyChord([mod], "F2",[
        Key([], "d", lazy.spawn("discord")),
        Key([], "m", lazy.spawn("mailspring")),
        Key([], "t", lazy.spawn("telegram-desktop")),
        Key([], "s", lazy.spawn("com.slack.Slack"))],
        mode="Mail"
    ),

### Gaming
    KeyChord([mod], "F3",[
        Key([], "l", lazy.spawn("lutris")),
        Key([], "p", lazy.spawn("prime-run pcsx2")),
        Key([], "s", lazy.spawn("steam"))],
        mode="Gaming"
    ),


    Key([mod], "x", lazy.spawn("archlinux-logout")),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "e", lazy.spawn("kitty -e nvim")),
    Key([mod, "shift"], "c", lazy.spawn("vscodium")),
    Key([mod], "s", lazy.spawn("pavucontrol")),
    Key([mod, "shift"], "v", lazy.spawn("virtualbox")),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod, "control"], "Return", lazy.spawn("pcmanfm")),
    #ranger
    #htop
    Key(["mod1", "control"],"l", lazy.spawn("i3lock -i ~/Media/memes/error.png --scale")),
    #Key([""],"", lazy.spawn("swaylock -i ~/Media/memes/error.png --scale")),



#################################################################
#     Rofi
#################################################################
    Key([mod], "r", lazy.spawn("./.config/rofi/bin/launcher")),

    #Powermenu 
    # Key([mod], "x", lazy.spawn("./.config/rofi/bin/powermenu")),

    #Network
    #Key([mod, "shift"], "n", lazy.spawn(".config/rofi/bin/network")),
    # Key([mod, "shift"], "n", lazy.spawn(".config/rofi/bin/network_menu")),

    # Key([mod], "m", lazy.spawn("./.config/rofi/bin/mpd")),
    Key([mod], "w", lazy.spawn("./.config/rofi/bin/windows")),
    #    Key(["mod1"], "q", lazy.spawn("rofi quicklinks")),
    #    Key(["mod1"], "b", lazy.spawn("rofi bookmarks")),
   
#################################################################
#     Dmenu
#################################################################
   Key([mod], 'd', lazy.run_extension(extension.DmenuRun(**dmenu_theme,dmenu_prompt= "run: >"))),
   Key([mod, "shift"], 'd', lazy.run_extension(extension.J4DmenuDesktop(**dmenu_theme,dmenu_prompt= "Apps: >"))),


#### Config files    
    Key([mod], 'c', lazy.run_extension(extension.CommandSet(
        commands={
            
            'qtile': 'kitty -e nvim .config/qtile',
            'qtile keys': 'kitty -e nvim .config/qtile/modules/keys.py',
            'qtile bar': 'kitty -e nvim .config/qtile/modules/screens.py',
            'zsh': 'kitty -e nvim .config/zsh/.zshrc',
            'nvim': 'kitty -e nvim .config/nvim',
            'rofi': 'kitty -e nvim .config/rofi',
                                               
            },
        #pre_commands=[''],
        **dmenu_theme,dmenu_prompt= "config:"))),
    
 
##### Coding Projects

    Key([mod], 'p', lazy.run_extension(extension.CommandSet(
        commands={
            # 'Library': 'kitty -e nvim Projects/Library',
            'Library Server': 'kitty -e nvim Projects/Library/Library-server',
            'Library Client': 'kitty -e nvim Projects/Library/Library-client',
            # 'Library (code)': 'vscodium Projects/Library',
            # 'BasedApp': 'kitty -e nvim Projects/BasedApp',
            'BasedApp Server': 'kitty -e nvim Projects/BasedApp/based-server',
            'BasedApp Client': 'kitty -e nvim Projects/BasedApp/based-client',
            },
        #pre_commands=[''],
        **dmenu_theme,dmenu_prompt= "coding:"))),
 
##### Quicklinks 
   # Key([mod], 'c', lazy.run_extension(extension.CommandSet(
   #     commands={
   #         
   #         'qtile': 'kitty -e nvim .config/qtile',
   #         'i3': 'kitty -e nvim .config/i3/config',
   #         'nvim': 'kitty -e nvim .config/nvim',
   #         'polybar': 'kitty -e nvim .config/polybar',
   #         'rofi': 'kitty -e nvim .config/rofi',
   #         'zsh': 'kitty -e nvim .zshrc',
   #         'bash': 'kitty -e nvim .bashrc',
   #         'ArchZizou': 'kitty -e nvim ArchZizou',
   #         'Install Script': 'kitty -e nvim install.sh',
   #         },
   #     #pre_commands=[''],
   #     **dmenu_theme,dmenu_prompt= "config:"))),
   
#### notes   
    #Key([mod, "shift"], 'n', lazy.run_extension(extension.CommandSet(
    #    commands={
    #        'general': 'kitty -e nvim Documents/notes/general.norg',
    #        'uni': 'kitty -e nvim Documents/notes/uni.norg',
    #        'tech': 'kitty -e nvim Documents/notes/tech.norg',
    #        'reminders': 'kitty -e nvim Documents/notes/reminders.norg',
    #        'health': 'kitty -e nvim Documents/notes/health.norg',
    #        },
    #    #pre_commands=[''],
    #    **dmenu_theme,dmenu_prompt= "notes:"))),


#################################################################
# Window Management 
#################################################################
 

# SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "m", lazy.window.toggle_minimize()),
    Key([mod, "control"], "m", lazy.window.toggle_maximize()),
    Key([mod, "mod1"], "j", lazy.group.next_window()),
    Key([mod, "mod1"], "k", lazy.group.prev_window()()),

# SUPER + SHIFT KEYS

    Key([mod, "shift"], "r", lazy.restart()),


# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),


# STACK LAYOUT

    #split/stack toggle
    Key([mod, "mod1"], "t", lazy.layout.toggle_split()),

    #navigating between stacks
    Key([mod, "mod1"], "Right", lazy.layout.next()),
    Key([mod, "mod1"], "Left", lazy.layout.previous()),
    Key([mod, "mod1"], "h", lazy.layout.next()),
    Key([mod, "mod1"], "l", lazy.layout.previous()),
    
    #sending between stacks
    Key(["mod1", "shift"], "Right", lazy.layout.client_to_next()),
    Key(["mod1", "shift"], "Left", lazy.layout.client_to_previous()),
    Key(["mod1", "shift"], "h", lazy.layout.client_to_next()),
    Key(["mod1", "shift"], "l", lazy.layout.client_to_previous()),
    Key(["mod1", "shift"], "f", lazy.layout.rotate()),



# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),

# # FLIP LAYOUT FOR BSP
#     Key([mod, "mod1"], "k", lazy.layout.flip_up()),
#     Key([mod, "mod1"], "j", lazy.layout.flip_down()),
#     Key([mod, "mod1"], "l", lazy.layout.flip_right()),
#     Key([mod, "mod1"], "h", lazy.layout.flip_left()),
#
# # MOVE WINDOWS UP OR DOWN BSP LAYOUT
#     Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
#     Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
#     Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
#     Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    Key([mod, "control"], "c", lazy.window.center()),
    Key([mod, "control"], "f", lazy.window.bring_to_front()),

#Hide/Show bar
    Key([mod], "b", lazy.hide_show_bar("top")),

#################################################################
#     Functions keys
#################################################################
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 150+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 150-")),
 
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master 1+ toggle")),
   #Key([], "XF86AudioMicMute", lazy.spawn("mictoggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 10%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 10%+")),


    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),
    #Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    #Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    #Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    #Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#####Screenshot
    Key([], "Print", lazy.spawn("scrot '%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir Media/screenshots)'")),

    ]


