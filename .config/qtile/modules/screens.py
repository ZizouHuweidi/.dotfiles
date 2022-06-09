from libqtile import qtile, bar, widget,extension
from libqtile.config import Screen
from modules.keys import terminal, home_dir, dmenu_theme
from themes.colors import colors 
from libqtile.lazy import lazy
from libqtile.command import lazy
from bin import storage



def init_separator():
    return widget.Sep(
                size_percent = 60,
                margin = 5,
                linewidth = 2,
                background = colors['bg'],
                foreground = "#555555")

def nerd_icon(nerdfont_icon, bg_color, fg_color):
    return widget.TextBox(
                font = "FontAwesome",
                fontsize = 13,
                text = nerdfont_icon,
                foreground = fg_color,
                background = bg_color)

def init_edge_spacer():
    return widget.Spacer(
                length = 5,
                background = colors['bg'])


sep = init_separator()
space = init_edge_spacer()

widget_defaults = dict(
    font='Source Code Pro Medium',
    fontsize=13,
    padding=5,
)
extension_defaults = widget_defaults.copy()

left = ""
right = ""

def init_widgets_list():
    widgets_list = [
            # Left Side of the bar
            space,
            # widget.Image(
            #     filename = "~/.config/qtile/icons/arch.png",
            #     background = colors['bg'],
            #     margin = 2,
            #     mouse_callbacks = {
            #         'Button1': lambda : qtile.cmd_spawn(f""),
            #     }
            # ),
            widget.CurrentLayoutIcon(
               foreground = colors['yellow1'],
               background = colors['bg'],
               scale = 0.6,
               custom_icon_paths = ["/home/zizou/.config/qtile/icons/layout-icons/gruvbox-bright_yellow"]
           ),

            space,
        
            widget.Chord(
                font = "Noto Sans Bold Bold",
                fontsize = 12,
                background = colors['bg'],
                foreground = colors['green2'],
            ),

            widget.TextBox(
                text = '|',
                font = "Ubuntu Mono",
                background = colors['bg'],
                foreground = '474747',
                padding = 2,
                fontsize = 14
            ),

             widget.TextBox(
                font= "MesloLGS NF",
                text= left,
                foreground=colors['sep1'],
                background=colors['bg'],
                padding=0,
                fontsize=18,
            ),

            widget.GroupBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                foreground = colors['fg'],
                background = colors['sep1'],
                borderwidth = 4,
                highlight_method = "text",
                this_current_screen_border = colors['yellow1'],
                active = colors['blue1'],
                inactive = colors['bg']
            ),

             widget.TextBox(
                font= "MesloLGS NF",
                text= right,
                foreground=colors['sep1'],
                background=colors['bg'],
                padding=0,
                fontsize=18,
            ),

            widget.TextBox(
                text = '|',
                font = "Ubuntu Mono",
                background = colors['bg'],
                foreground = '474747',
                padding = 2,
                fontsize = 14
            ),

            widget.TaskList(
                font = "Noto Sans Bold Bold",
                fontsize = 12,
                highlight_method = 'text',
                border = colors['yellow1'],
                borderwidth = 0.3,
                background = colors['bg'],
                foreground = colors['blue1'],
                margin_y = 2,
                icon_size = 0,
                max_title_width = 200,
            ),
            widget.Spacer(
                length = 40,
                background = colors['bg']
            ),

           # widget.TextBox(
           #     font= "MesloLGS NF",
           #     text= left,
           #     foreground=colors['sep1'],
           #     background=colors['bg'],
           #     padding=0,
           #     fontsize=18,
           # ),

            # widget.Mpd2(
            #     font = "Noto Sans Bold Bold",
            #     fontsize = 13,
            #     background = colors['sep1'],
            #     status_format='{play_status}  {artist} - {title}',
            #     play_status = {'pause': '⏸  ', 'play': '▶  ', 'stop': '■  '},
            #     idle_message = "",
            #     idle_format = "{idle_message}",   
            #     foreground = colors['fg'],
            #
            # ),    

           # widget.TextBox(
           #     font= "MesloLGS NF",
           #     text= right,
           #     foreground=colors['sep1'],
           #     background=colors['bg'],
           #     padding=0,
           #     fontsize=18,
           # ),


            widget.Spacer(
                length = 5,
                background = colors['bg']
            ),

            widget.Battery(
                font = "Noto Sans Bold Bold",
                fontsize = 12,
                low_percentage=0.3,
                low_foreground= colors['red1'],
                update_interval=1,
                charge_char='',
                discharge_char='',
                full_char = "",
                format='{char} {percent:2.0%} ',
                show_short_text = False,
                foreground = colors['green1'],
                background = colors['bg'],
                padding = 0,
                mouse_callbacks = {
                    'Button1': lazy.run_extension(extension.CommandSet(
                        commands={
                                'Power Saver': 'powerprofilesctl set power-saver',
                                'Balanced': 'powerprofilesctl set balanced',
                                'Performance': 'powerprofilesctl set performance',
                            },
                            #pre_commands=[''],
                            **dmenu_theme,dmenu_prompt= "config:")),
                }
 
            ),
            nerd_icon(
                "墳",
                colors['bg'],
                colors['orange1']
            ),
            widget.Volume(

                font = "Noto Sans Bold Bold",
                fontsize = 12,
                foreground = colors['orange1'],
                background = colors['bg'],
                padding = 3,
                mouse_callbacks = {
                    'Button3': lambda : qtile.cmd_spawn("pavucontrol")
            }
            ),

            widget.Spacer(
                length = 5,
                background = colors['bg']
            ),
            #  widget.TextBox(
            #     font= "MesloLGS NF",
            #     text= left,
            #     foreground=colors[10],
            #     background=colors['bg'],
            #     padding=0,
            #     fontsize=18,
            # ),
            
             widget.TextBox(
                font= "MesloLGS NF",
                text= left,
                foreground=colors['sep1'],
                background=colors['bg'],
                padding=0,
                fontsize=18,
            ),

            nerd_icon(
                "",
                colors['sep1'],
                colors['fg']
            ),

            widget.Clock(
                format = '%d %b',
                font = "Noto Sans Bold Bold",
                fontsize = 12,
                foreground = colors['fg'],
                background = colors['sep1']
            ),

            nerd_icon(
                "",
                colors['sep1'],
                colors['fg']
            ),

            widget.Clock(
                format = '%H:%M',
                font = "Noto Sans Bold Bold",
                fontsize = 12,
                foreground = colors['fg'],
                background = colors['sep1']
            ),
 
             widget.TextBox(
                font= "MesloLGS NF",
                text= right,
                foreground=colors['sep1'],
                background=colors['bg'],
                padding=0,
                fontsize=18,
            ),

            widget.Spacer(
                length = 5,
                background = colors['bg']
            ),

           nerd_icon(
               "",
               colors['bg'],
               colors['red1']
            ),
            widget.CPU(
               format = "{load_percent}%",
               foreground = colors['red1'],
               background = colors['bg'],
               font = "Noto Sans Bold Bold",
               fontsize = 12,
               update_interval = 2,
               mouse_callbacks = {
                   'Button1': lambda : qtile.cmd_spawn(f"{myterm} -e htop")
               }
            ),

            nerd_icon(
                "",
                colors['bg'],
                colors['blue2']
            ),
            widget.Memory(

                font = "Noto Sans Bold Bold",
                fontsize = 12,
                format = "{MemUsed:.0f}{mm}",
                foreground = colors['blue2'],
                background = colors['bg'],
                update_interval = 2,
                mouse_callbacks = {
                    'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e htop")
                }
            ),
            # nerd_icon(
            #     "",
            #     colors['bg'],
            #     colors['green2']
            # ),
            # widget.ThermalSensor(
            #
            #     foreground_alert = colors['red1'],
            #     background = colors['bg'],
            #     foreground = colors['green2'],
            #     tag_sensor = 'Package id 0' 
            # ),

            widget.ThermalZone(
                font = "Noto Sans Bold Bold",
                fontsize = 12,
                background = colors['bg'],
                fgcolor_crit = colors['red2'],
                fgcolor_high = colors['yellow1'],   
                fgcolor_normal = colors['aqua1'],
                hidden = True,
                format = ' {temp}°C',
                format_crit = ' {temp}°C',
                zone = '/sys/class/thermal/thermal_zone6/temp'
            ),

            widget.Spacer(
                length = 5,
                background = colors['bg']
            ),

            widget.CheckUpdates(
                font = "Noto Sans Bold Bold",
                fontsize = 14,
                update_interval = 300,
                distro = "Arch_checkupdates",
                execute= "kitty -e sudo pacman -Syu",
                display_format = " {updates}",
                no_update_string = "",
                colour_have_updates = colors['purple1'],
                foreground= colors['purple1'],
                padding = 0,
                background = colors['bg'],
            ),
 

            #  widget.TextBox(
            #     font= "MesloLGS NF",
            #     text= left,
            #     foreground=colors[10],
            #     background=colors['bg'],
            #     padding=0,
            #     fontsize=18,
            # ),

            #  widget.TextBox(
            #     font= "MesloLGS NF",
            #     text= right,
            #     foreground=colors[10],
            #     background=colors['bg'],
            #     padding=0,
            #     fontsize=18,
            # ),

 
            #  widget.TextBox(
            #     font= "MesloLGS NF",
            #     text= right,
            #     foreground=colors[10],
            #     background=colors['bg'],
            #     padding=0,
            #     fontsize=18,
            # ),
            
            widget.TextBox(
                text = '|',
                font = "Ubuntu Mono",
                background = colors['bg'],
                foreground = '474747',
                padding = 2,
                fontsize = 14
            ),

            widget.Systray(
                background = colors['bg'],
                iconsize = 10
            ),
                   

            space

            #nerd_icon(
            #    "",
            #    colors[10]
            #),
            #widget.GenPollText(
            #    foreground = colors['fg'],
            #    background = colors['bg'],
            #    update_interval = 5,
            #    func = lambda: subprocess.check_output(f"{home_dir}/.config/qtile/bin/num-installed-pkgs").decode("utf-8")
            #),
           #widget.Pomodoro(
           #     background = colors['bg'],
           #     color_active = colors['red1'],
           #     color_break = colors[10],
           #     color_inactive = colors[10],
           #     length_pomodori = 20,
           #     length_long_break = 20
           # ),
            #nerd_icon(
            #    "",
            #    colors[10]
            #),
            #widget.Net(
             #   format = "{down} ↓↑ {up}",
              #  foreground = colors['fg'],
              #  background = colors['bg'],
               # update_interval = 2,
               # mouse_callbacks = {
               #     'Button1': lambda : qtile.cmd_spawn("def-nmdmenu")
               # }
            #),

            #widget.StatusNotifier(
            #background = colors['bg'],

            #),
        ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [
        Screen(
            wallpaper='/home/zizou/Wallpapers/gruvbox_listentoyourheart.jpg',
            wallpaper_mode='fill',
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                size=25,
                background="#282828",
                border_color=["#282828", "#282828", "#282828", "#282828"],
                border_width=[4, 4, 4, 4],
                opacity=1,
                margin=[0, 0, 0, 0],
            )
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen2(),
                size=26,
                background="#282828",
                opacity=1,
                margin=[0, 0, 0, 0],
            )
        ),
    ]

screens = init_screens()

