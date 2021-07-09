#!/usr/bin/env bash

# dmenu theming
lines="-l 20"

selected="$(ps -a -u $USER | \
            dmenu -i -p "Type to search and select process to kill" \
            $lines   | \
            awk '{print $1" "$4}')"; 

if [[ ! -z $selected ]]; then

    answer="$(echo -e "Yes\nNo" | \
            dmenu -i  -p "$selected will be killed, are you sure?" \
            $lines   )"

    if [[ $answer == "Yes" ]]; then
        selpid="$(awk '{print $1}' <<< $selected)"; 
        kill -9 $selpid
    fi
fi

exit 0
