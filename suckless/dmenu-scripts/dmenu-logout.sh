#!/usr/bin/env bash

# dmenu theming


opt1="Exit\nRestart\nPowerOFF"
opt2="YES\nNO"


ask() {
    answer="$( echo -e $1 | dmenu -l 4 -p "What Would Want me To Do"  )"
}

ask "$opt1" "$first_prompt"

case $answer in
    "Exit")
        ask "$opt2"  "DO YOU WANT REALLY EXIT AWESOME ?"
        if [[ $answer == "YES" ]]; then
            pkill -KILL -u import
        fi
        exit 0
        ;;
    "Restart")
        ask "$opt2" "DO YOU REALLY WANT TO RESTART THE SYSTEM ?"
        if [[ $answer == "YES" ]]; then
            systemctl reboot
        fi
        exit 0
        ;;
    "PowerOFF")
        ask "$opt2" "DO YOU  REALLY WANT TO SHUTDOWN THE COMPUTER ?"
        if [[ $answer == "YES" ]]; then
            systemctl poweroff
        fi
        exit 0
        ;;
esac

exit 0
