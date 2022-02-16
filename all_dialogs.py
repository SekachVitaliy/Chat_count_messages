from config import API_ID, API_HASH
from pyrogram import Client


def get_dialogs():
    with Client("my_account", API_ID, API_HASH) as app:
        for dialog in app.iter_dialogs():
            name_data = [dialog.chat.first_name, dialog.chat.last_name,
                         dialog.chat.username, dialog.chat.title]
            name = ' '.join([i for i in name_data if i is not None])
            print(f"{name=}, {dialog.chat.id=}")


if __name__ == "__main__":
    get_dialogs()
