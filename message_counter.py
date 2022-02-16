from config import API_ID, API_HASH
from pyrogram import Client


def chat_message_rating(chat_id: int):
    with Client("my_account", API_ID, API_HASH) as app:
        users_dict = {}
        count_all_messages = 0
        chat_title = app.get_chat(chat_id).title
        for message in app.iter_history(chat_id):
            if message.from_user and message.from_user.is_bot is False:
                count_all_messages += 1
                username = "Нет логина"
                if message.from_user.username:
                    username = f"@{message.from_user.username}"

                key = f"{message.from_user.first_name} ({username})"
                if key in users_dict:
                    users_dict[f"{message.from_user.first_name} ({username})"] += 1
                else:
                    users_dict[f"{message.from_user.first_name} ({username})"] = 1

        sorted_users_dict = {
            key: value for key, value in sorted(users_dict.items(), key=lambda item: item[1])
        }

        message = (
            f"**Статистика сообщений и пользователей в этом чате "
            f"({chat_title})**\n"
            "\n"
            f"Всего сообщений в чате: **{count_all_messages}**\n"
            "\n"
            "**Топ 10 пользователей:**\n"
        )
        count = 0
        sorted_dict_length = len(sorted_users_dict)

        for key in sorted_users_dict:
            place = sorted_dict_length - count
            count += 1
            if place == 1:
                percent = round(sorted_users_dict[key] / count_all_messages * 100, 2)
                message += (
                    "\n"
                    "<i><strong>И наш победитель!</strong></i>\n"
                    "\n"
                    f"<i><strong>{place}. {key}: {sorted_users_dict[key]}"
                    f" ({percent}%)</strong></i>\n"
                )
            elif place <= 10:
                percent = round(sorted_users_dict[key] / count_all_messages * 100, 2)
                message += (f"**{place}**. {key}: **{sorted_users_dict[key]}"
                            f" ({percent}%)**\n")
        app.send_message(chat_id, message)
        print(message)


if __name__ == "__main__":
    id_chat = int(input("Enter chat_id where count messages:"))
    chat_message_rating(id_chat)
