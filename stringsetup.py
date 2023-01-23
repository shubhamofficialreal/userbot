#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details"""
)
APP_ID = int(input("27899654"))
API_HASH = input("644a291c69677a2fd785c43455b1df08")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.sendmessage("me", client.session.save())
