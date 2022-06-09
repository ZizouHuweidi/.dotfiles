import os
from libqtile import layout
from libqtile.config import Match




##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 7, 
                "font": "Source Code Pro Medium",
                "font_size": 12,
                "border_focus": "#d79921",
                "border_normal": "#32302f"
                }

# window layouts
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Stack(num_stacks=2,**layout_theme),
    #layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
    #layout.MonadThreeCol(**layout_theme),
    #layout.TreeTab(**layout_theme, active_bg='#50fa7b', inactive_bg='#44475a',  active_fg='#bd93f9', bg_color='#282a36', fg_color='#f8f8f2', panel_width=35),
    #layout.Tile(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    #layout.MonadWide(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Slice(**layout_theme, width='300', side= 'right'),
    #layout.Spiral(**layout_theme),
]


floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='Viewnior'),  # Photos/Viewnior 
    Match(wm_class='Alafloat'),  # Floating Alacritty Terminal 
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='confirm'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='Arcolinux-tweak-tool.py'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='download'),
    Match(wm_class='error'),
], **layout_theme)

