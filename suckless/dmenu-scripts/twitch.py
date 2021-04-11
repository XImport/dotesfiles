import requests
import json
import dmenu
import os
ACESS_TOKEN = "pd6tbsj76qavsgpc5dyry32u52gtpj"
CLIENT_ID = "ahr7oa929qwfos91n3p4h12webx6u2"

headers = {"Client-ID": CLIENT_ID,
           "Accept": "application/vnd.twitchtv.v5+json",
           "Authorization": f"Bearer {ACESS_TOKEN}"}

ids = []
GET = requests.get(
    "https://api.twitch.tv/kraken/users/428714354/follows/channels", headers=headers)
for user in GET.json().get("follows"):
    ids.append(user.get("channel").get("_id"))

online_users = []
for id_ in ids:
    CHECK = requests.get(
        f"https://api.twitch.tv/helix/streams?user_id={id_}", headers=headers)
    for online in CHECK.json().get("data"):
        online_users.append(online.get("user_name"))

prompte = dmenu.show(
    online_users, prompt="Current Online Stremears:", lines=50)

os.system(f"qutebrowser https://www.twitch.tv/{prompte}")
