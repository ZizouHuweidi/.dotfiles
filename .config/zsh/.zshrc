
export ZDOTDIR=$HOME/.config/zsh

# some useful options (man zshoptions)
setopt autocd extendedglob nomatch menucomplete
setopt interactive_comments
stty stop undef		# Disable ctrl-s to freeze terminal.
zle_highlight=('paste:none')
#share commands between terminal instances or not
setopt SHARE_HISTORY
# beeping is annoying
unsetopt BEEP


# completions
autoload -Uz compinit
compinit
zstyle ':completion:*' menu select
# zstyle ':completion::complete:lsof:*' menu yes select
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'
zmodload zsh/complist
_comp_options+=(globdots)		# Include hidden files.

autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

# Colors
autoload -Uz colors && colors

# Useful Functions
source "$ZDOTDIR/zsh-functions"

# Normal files to source
zsh_add_file "zsh-exports"
zsh_add_file "zsh-vim-mode"
zsh_add_file "zsh-aliases"
#zsh_add_file "zsh-prompt"

# Plugins
zsh_add_plugin "zsh-users/zsh-autosuggestions"
zsh_add_plugin "zsh-users/zsh-syntax-highlighting"
zsh_add_plugin "hlissner/zsh-autopair"
zsh_add_plugin "olets/zsh-abbr"
# zsh_add_completion "esc/conda-zsh-completion" false
# For more plugins: https://github.com/unixorn/awesome-zsh-plugins
# More completions https://github.com/zsh-users/zsh-completions

source /usr/share/nvm/init-nvm.sh
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme
# source /usr/share/zsh/plugins/zsh-syntax-highlighting 
# source /usr/share/zsh/plugins/zsh-autosuggestions 
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=60'


if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi
# Key-bindings
#bindkey -s '^o' 'ranger^M'
#bindkey -s '^f' 'zi^M'
#bindkey -s '^s' 'ncdu^M'
# bindkey -s '^n' 'nvim $(fzf)^M'
# bindkey -s '^v' 'nvim\n'
#bindkey -s '^z' 'zi^M'
#bindkey '^[[P' delete-char
#bindkey "^p" up-line-or-beginning-search # Up
#bindkey "^n" down-line-or-beginning-search # Down
#bindkey "^k" up-line-or-beginning-search # Up
#bindkey "^j" down-line-or-beginning-search # Down
#bindkey -r "^u"
#bindkey -r "^d"

# FZF 
#[ -f /usr/share/fzf/completion.zsh ] && source /usr/share/fzf/completion.zsh
#[ -f /usr/share/fzf/key-bindings.zsh ] && source /usr/share/fzf/key-bindings.zsh
#[ -f /usr/share/doc/fzf/examples/completion.zsh ] && source /usr/share/doc/fzf/examples/completion.zsh
#[ -f /usr/share/doc/fzf/examples/key-bindings.zsh ] && source /usr/share/doc/fzf/examples/key-bindings.zsh
#[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
#[ -f $ZDOTDIR/completion/_fnm ] && fpath+="$ZDOTDIR/completion/"
## export FZF_DEFAULT_COMMAND='rg --hidden -l ""'
#compinit

# Edit line in vim with ctrl-e:
autoload edit-command-line; zle -N edit-command-line
# bindkey '^e' edit-command-line

# TODO Remove these
#setxkbmap -option caps:escape
#xset r rate 210 40

# Speedy keys
# xset r rate 210 40

# Environment variables set everywhere
#export EDITOR="nvim"
#export TERMINAL="alacritty"
#export BROWSER="brave"

# For QT Themes
#export QT_QPA_PLATFORMTHEME=qt5ct

# remap caps to escape
# setxkbmap -option caps:escape
# swap escape and caps
# setxkbmap -option caps:swapescape

# To customize prompt, run `p10k configure` or edit ~/.config/zsh/.p10k.zsh.
[[ ! -f ~/.config/zsh/.p10k.zsh ]] || source ~/.config/zsh/.p10k.zsh
