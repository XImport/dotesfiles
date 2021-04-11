# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/import/.zshrc'
 #navigation
alias ..='cd ..' 
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'
alias dwm='~/dotes/suckless/V2/dwm'
# git
alias addall='git add .'
alias clone='git clone'
alias commit='git commit -m'
alias pull='git pull origin'
alias push='git push origin'
alias status='git status'
alias vifm='/home/import/.config/vifm/scripts/vifmrun'



# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# pacman and yay
alias pacsyu='sudo pacman -Syyu'                 # update only standard pkgs
alias get='sudo pacman -S '                 # update only standard pkgs
alias yaysua="yay -Sua --noconfirm"              # update only AUR pkgs
alias yaysyu="yay -Syu --noconfirm"              # update standard pkgs and AUR pkgs
alias unlock="sudo rm /var/lib/pacman/db.lck"    # remove pacman lock
alias cleanup='sudo pacman -Rns $(pacman -Qtdq)' # remove orphaned packages
alias mpv="devour mpv"
alias w3m="devour w3m"
alias pdf="devour zathura"
alias cp='cp -v'
alias mv='mv -v'
alias df='df -h'
alias rank='sudo reflector --verbose -l 200 -p http --sort rate --save /etc/pacman.d/mirrorlist'
alias top='htop'
alias vim='nvim'
alias ll="exa -l"
alias la="exa -al"
alias ls="exa"
RUST_BACKTRACE=1
export EDITOR="nvim"
export SPOTIPY_CLIENT_ID='b770d4be52fe4b44b734261e3251c2cd'
export SPOTIPY_CLIENT_SECRET='950e066fe5ed49c589409674cfb8c416'
export SPOTIPY_REDIRECT_URI='https://www.spotify.com'
export TERM='xterm-256color' 


function precmd {
  vcs_info
}

autoload -Uz compinit promptinit edit-command-line colors vcs_info
autoload -Uz vcs_info
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#FFFFFF,bg=#434c5e,bold,underline"

zstyle ':completion:*' menu select
zstyle ':vcs_info:git:*' formats ' 👑 %b '
setopt PROMPT_SUBST

zmodload zsh/complist

PROMPT='%F{magenta}%${vcs_info_msg_0_}% %F{green}$ '

source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source /home/import/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

autoload -Uz compinit
compinit
# End of lines added by compinstall
export PATH=$HOME/.config/nvcode/utils/bin:$PATH
export PATH=$HOME/.config/nvcode/utils/bin:$PATH
export PATH=$HOME/.config/nvcode/utils/bin:$PATH
export PATH=$HOME/.config/nvcode/utils/bin:$PATH
