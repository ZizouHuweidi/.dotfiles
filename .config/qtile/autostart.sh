#!/bin/env bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# Kill if already running
#killall -9 picom xfce4-power-manager ksuperkey dunst sxhkd eww


# Launch notification daemon
dunst -config $HOME/.config/dunst/dunstrc &

# Start udiskie
#udiskie &

# Start mpd
run mpd &

#starting utility applications at boot time
run nm-applet &
run xfce4-power-manager &
numlockx on &
blueberry-tray &
picom --config $HOME/.config/qtile/bin/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

#starting user applications at boot time
#run volumeicon &
#run discord &
# nitrogen --restore &
#run firefox &
#run spotify &
#run telegram-desktop &
#run variety &
