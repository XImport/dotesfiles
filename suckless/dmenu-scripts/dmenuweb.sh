#!/bin/bash

#
#
#
#(_)                          | |
# _ _ __ ___  _ __   ___  _ __| |_
#| | '_ ` _ \| '_ \ / _ \| '__| __|
#| | | | | | | |_) | (_) | |  | |_
#|_|_| |_| |_| .__/ \___/|_|   \__|
#            | |
#            |_|
#
#
# SURF WEB BY DMENU






search=(Bookmarks DuckDuckGo Google YouTube Wikipedia ArchWiki Reddit)
urls=("" "https://duckduckgo.com/?q=" "https://www.google.com/search?q=" "https://www.youtube.com/results?search_query=" "https://en.wikipedia.org/wiki/" "https://www.archlinux.org/packages/?q=" "https://www.reddit.com/search/?q=")
homepages=("" "https://duckduckgo.com" "https://www.google.com" "https://www.youtube.com" "https://en.wikipedia.org/wiki/Main_Page" "https://www.archlinux.org/" "https://www.reddit.com/")

menu=$(printf '%s\n' "${search[@]}" | dmenu -p "Surf >>" -h 18)

for i in "${!search[@]}"; do
  if [ ! -z "$menu" ] && [[ $menu = "Bookmarks" ]]; then
    bookmark_list=$(tr '\t\n' ' ' < ~/.bookmarks)
    IFS=' ' read -r -a bookmarks <<< "$bookmark_list"
    declare -a bookmark_names=()
    for (( x=0; x<${#bookmarks[@]}; x+=2 )); do
      bookmark_names+=("${bookmarks[x]}")
    done
    declare -a bookmark_urls=()
    for (( y=1; y<${#bookmarks[@]}; y+=2 )); do
      bookmark_urls+=("${bookmarks[y]}")
    done
    menu=$(printf "%s\n" "${bookmark_names[@]}" |  dmenu -p "Surf" -h 18 )
    for i in "${!bookmark_names[@]}"; do
      if [ ! -z "$menu" ] && [[ "${bookmark_names[$i]}" = $menu ]]; then
        qutebrowser "${bookmark_urls[i]}" && wmctrl -a qutebrowser;
      fi
    done
  elif [ ! -z "$menu" ] && [[ "${search[$i]}" = $menu ]]; then
    submenu=$(echo "$menu home" |  dmenu -p "Surf For " -h 18 );
    if [ ! -z "$submenu" ] && [[ $submenu = "$menu home" ]]; then
      qutebrowser "${homepages[i]}" && wmctrl -a qutebrowser
    elif [ ! -z "$submenu" ]; then
      qutebrowser "${urls[i]}$submenu" && wmctrl -a qutebrowser
    fi
  fi
done
