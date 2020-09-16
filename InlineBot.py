import telebot
import random
import re
from telebot import types
from time import sleep

bot = telebot.TeleBot('1255962759:AAH9w0KAiju8a-7ZD9MONEDtvDDRA5Qlx6w')

# Обычный режим

Privet = ['привет','хай','хеллоу','хелоу','нихао','коничива','конничива','прив',]
Poka = ['пока','гудбай','аривидерчи','сайонара',]
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboardstart = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Пока','Подбрось монету')
keyboardstart.row('Привет')
def main():
    @bot.message_handler(commands=['start'])


    def start_message(message):
        bot.send_message(message.chat.id, 'Хули ты меня запустил', reply_markup=keyboardstart)


    @bot.message_handler(content_types=['text'])

    def send_text(message):

        if message.text.lower() in Privet:
            bot.send_message(message.chat.id, 'Ну привет Хуйло', reply_markup=keyboard1)
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIMwF52Fkx5TvIYNJzsa0cmm1BGVmPYAAJLAgACWuaOEbe4qFscZwg-GAQ')
        elif message.text.lower() in Poka:
            bot.send_message(message.chat.id, 'Прощай, надеюсь тебя больше  не увижу', reply_markup=keyboard1)
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIMvl52FXMKkg7zbRpGjOUz4a5MCYIRAAJXAgACWuaOEc5zAAF7jyseFBgE')

        elif message.text == 'Doctor_Jackill':
            bot.send_message(message.chat.id, 'Здарова босс!', reply_markup=keyboard1)
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANfXpWsLME90zcxyYGz4FhKyeta-s4AAl0CAAJa5o4RTTxInX8bvdYYBA')



#Кейбордина в меседжаг

        elif message.text.lower() == 'подбрось монету':

            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Подбросить", callback_data="norm")
            keyboard.add(callback_button)
            bot.send_message(message.chat.id, "Так, ща, подожди", reply_markup=keyboard1)
            bot.send_message(message.chat.id, "Монета готова", reply_markup=keyboard)

        else:
            bot.send_message(message.chat.id, 'Дибил,я тебя не понимаю', reply_markup=keyboard1)



# Инлайн-режим с непустым запросом
    @bot.inline_handler(lambda query: len(query.query) > 0)
    def query_text(query):
        kb = types.InlineKeyboardMarkup()
        # Добавляем колбэк-кнопку с содержимым "test"
        kb.add(types.InlineKeyboardButton(text="Подбросить", callback_data="coin"))
        results = []
        single_msg = types.InlineQueryResultArticle(
            id="1", title="Приготовить монету",
            input_message_content=types.InputTextMessageContent(message_text="Монета готова"),
            reply_markup=kb)
        results.append(single_msg)
        bot.answer_inline_query(query.id, results)


# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        # Если сообщение из чата с ботом
        if call.message:
            if call.data == "norm":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=random.choice(["Орёл","Решка"]))

    # Если сообщение из инлайн-режима
        elif call.inline_message_id:
            if call.data == "coin":
                bot.edit_message_text(inline_message_id=call.inline_message_id, text=random.choice(["Орёл","Решка"]))

if __name__ == '__main__':
    main()
    try:
        bot.polling(none_stop=True, interval=3)
    except Exception:
        pass
