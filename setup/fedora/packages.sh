install_packages(){ echo -e "[*3*] Installing essential packages with Pacman."
    
    ## setup
    sudo pacman -Syy
    sudo pacman --needed --noconfirm -S polkit-gnome xsel flatpak arandr xclip
    sudo pacman --needed --noconfirm -S dunst rofi picom 
    paru --needed --noconfirm -S j4-dmenu-desktop arcolinux-logout

    ## hardware
    sudo pacman --needed --noconfirm -S lm_sensors lshw ncdu brightnessctl htop gparted 
    sudo pacman --needed --noconfirm -S xfce4-power-manager power-profiles-daemon upower 
    sudo pacman --needed --noconfirm -S udiskie 
    # paru --needed --noconfirm -S udiskie-dmenu-git 
    # redshift

    ## files 
    sudo pacman --needed --noconfirm -S pcmanfm-gtk3 syncthing zathura zathura-pdf-mupdf xfce4-appfinder
    sudo pacman --needed --noconfirm -S unrar unzip evince neovim 
    sudo pacman --needed --noconfirm -S ueberzug ranger qbittorrent 
    paru --needed --noconfirm devour

    ## themes
    sudo pacman --needed --noconfirm -S kvantum neofetch 
    sudo pacman --needed --noconfirm -S lxappearance-gtk3 
    paru --needed --noconfirm -S gruvbox-material-gtk-theme-git gruvbox-material-icon-theme-git
    #ly 
    #qt theming
    # sudo pacman --needed --noconfirm -S grub-customizer betterlockscreen
    # i3lock-color  

    ## audio
    sudo pacman --needed --noconfirm -S mpc mpd mpv ncdu ncmpcpp 
    sudo pacman --needed --noconfirm -S playerctl 
    #pulseaudio pulseaudio-alsa pulseaudio-bluetooth 
    sudo pacman --needed --noconfirm -S pavucontrol volume_key pasystray

    ## images
    sudo pacman --needed --noconfirm -S imagemagick shotwell feh flameshot

    ## network
    sudo pacman --needed --noconfirm -S network-manager-applet networkmanager nm-connection-editor wireless_tools
    sudo pacman --needed --noconfirm -S blueberry bluez bluez-libs bluez-tools bluez-utils

    ## browsers
    sudo pacman --needed --noconfirm -S brave-bin qutebrowser firefox firefox-ublock-origin 

    ## terminals
    sudo pacman --needed --noconfirm -S alacritty  
    sudo pacman --needed --noconfirm -S kitty kitty-shell-integration kitty-terminfo 
    sudo pacman --needed --noconfirm -S zsh zsh-completions zsh-theme-powerlevel10k-git bash-completion 
# zsh-autosuggestions-git zsh-pure-prompt-git zsh-syntax-highlighting 
# fish fisher

    ## qtile
    sudo pacman --needed --noconfirm -S qtile python-dbus-next python-mpd2 python-iwlib python-psutil python-pywayland python-pywlroots python-xdg
# qtile-git qtile-extras-git 

    ## sway
#     sudo pacman --needed --noconfirm -S swaybg swayidle swaylock-git clipman slock wl-clipboard wlroots 

    ## fonts
    sudo pacman --needed --noconfirm -S adobe-source-code-pro-fonts adobe-source-sans-fonts 
    sudo pacman --needed --noconfirm -S noto-fonts-emoji nerd-fonts-source-code-pro awesome-terminal-fonts 
    sudo pacman --needed --noconfirm -S ttf-font-awesome ttf-hack ttf-iosevka-nerd ttf-material-design-iconic-font noto-fonts-emoji
    sudo pacman --needed --noconfirm -S ttf-meslo-nerd-font-powerlevel10k ttf-ms-fonts ttf-ubuntu-font-family fontconfig 
    fc-cache

    echo -e "\n[*] Setting Zsh as default shell."
    chsh -s /bin/zsh
    sudo chsh -s /bin/zsh
    cat <<- EOF
		[*3*] Still installing packages.
		
		[*] Do you want to install optional, but useful programs? (VSCodium, LibreOffice, Dev tools, Apps)

		[1] yes
		[2] no
	
	EOF

	read -p "[?] Select option: "

	if [[ $REPLY == "1" ]]; then

    ## communicating
    # sudo pacman --needed --noconfirm -S discord telegram-desktop mailspring 
    # slack
    # betterdiscord

    ## Desktop Apps
    # sudo pacman --needed --noconfirm -S libreoffice krita

    ## reading
    sudo pacman --needed --noconfirm -S obsidian calibre 

    # dev 
    paru --needed --noconfirm -S vscodium-bin vscodium-bin-marketplace 
    sudo pacman --needed --noconfirm -S docker docker-compose fzf neovide-git 
# tmux 
# prettier
# github-cli
# postman-bin 
    ## Java dev
    sudo pacman --needed --noconfirm -S jre-openjdk jdk-openjdk
    sudo pacman --needed --noconfirm -S eclipse-java 
    #eclipse-jee intellij-idea-community-edition
    ## Go dev
    sudo pacman --needed --noconfirm -S go 
    ## Python dev
    sudo pacman --needed --noconfirm -S python python-pip 
    ## JS dev
    sudo pacman --needed --noconfirm -S nvm npm nvme-cli nodejs 
    ## DB
    # sudo pacman --needed --noconfirm -S postgres mysql sqlserver..
# rustup 

    ## virtual machines
    # sudo pacman --needed --noconfirm -S virtualbox 
# virtualbox-host-dkms virt-manager

    ## tools
    # sudo pacman --needed --noconfirm -S  etcher-bin appimagelauncher nitrogen
    paru -S --needed --noconfirm shell-color-scripts
# stow    

    ## gaming
    # sudo pacman --needed --noconfirm -S pcsx2 lutris steam

	elif [[ $REPLY == "2" ]]; then
		 echo -e "\n[*] Skipping."
	else
		echo -e "\n[!] Invalid option, exiting...\n"
		exit 1
	fi
}

install_packages
