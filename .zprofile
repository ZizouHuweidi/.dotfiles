#!/bin/zsh

# Default programs:
export EDITOR="nvim"
export TERMINAL="kitty"
export BROWSER="brave"

# XDG Paths
export XDG_CONFIG_HOME=$HOME/.config
#export XDG_CACHE_HOME=$HOME/.cache
#export XDG_DATA_HOME=$HOME/.local/share

# ~/ Clean-up:
export ZDOTDIR="${XDG_CONFIG_HOME:-$HOME/.config}/zsh"
# export ZDOTDIR=$HOME/.config/zsh


# remap caps to escape
setxkbmap -option caps:escape
setxkbmap -option escape:caps
# swap escape and caps
# setxkbmap -option caps:swapescape
# swap between english and arabic keyboard layouts with alt escape
setxkbmap -layout "us,ar" -option grp:alt_caps_toggle
