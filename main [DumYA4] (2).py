import telebot
from telebot import types
from logic import Translator
from datetime import datetime

d = {'af': "африканский",
     'sq': "албанский",
     'am': "амхарский",
     'ar': "арабский",
     'hy': "армянский",
     'az': "азербайджанский",
     'eu': "баскский",
     'be': "белорусский",
     'bn': "бенгальский",
     'bs': "боснийский",
     'bg': "болгарский",
     'ca': "каталанский",
     'ceb': "кебуано",
     'ny': "чичева",
     'zh-cn': "китайский",
     'zh-tw': "китайский традиционный",
     'co': "корсиканский",
     'hr': "хорватский",
     'cs': "чешский",
     'da': "датский",
     'nl': "голландский",
     'en': "английский",
     'eo': "эсперанто",
     'et': "эстонский",
     'tl': "филиппинский",
     'fi': "финский",
     'fr': "французский",
     'fy': "фризский",
     'gl': "галисийский",
     'ka': "грузинский",
     'de': "немецкий",
     'el': "греческий",
     'gu': "гуджаратский",
     'ht': "гаитянский",
     'ha': "хауса",
     'haw': "гавайский",
     'iw': "иврит",
     'hi': "хинди",
     'hmn': "хмонг",
     'hu': "венгерский",
     'is': "исландский",
     'ig': "игбо",
     'id': "индонезийский",
     'ga': "ирландский",
     'it': "итальянский",
     'ja': "японский",
     'jw': "яванский",
     'kn': "каннада",
     'kk': "казахский",
     'km': "кхмерский",
     'ko': "корейский",
     'ku': "курдский",
     'ky': "киргизский",
     'lo': "лаосский",
     'la': "латинский",
     'lv': "латышский",
     'lt': "литовский",
     'lb': "люксембургский",
     'mk': "македонский",
     'mg': "малагасийский",
     'ms': "малайский",
     'ml': "малаялам",
     'mt': "мальтийский",
     'mi': "маори",
     'mr': "маратхи",
     'mn': "монгольский",
     'my': "мьянманский",
     'ne': "непальский",
     'no': "норвежский",
     'ps': "пушту",
     'fa': "персидский",
     'pl': "польский",
     'pt': "португальский",
     'pa': "панджабский",
     'ro': "румынский",
     'ru': "русский",
     'sm': "самоанский",
     'gd': "шотландско-гэльский",
     'sr': "сербский",
     'st': "сесото",
     'sn': "шона",
     'sd': "синдхи",
     'si': "сингальский",
     'sk': "словацкий",
     'sl': "словенский",
     'so': "сомалийский",
     'es': "испанский",
     'su': "сунданский",
     'sw': "суахили",
     'sv': "шведский",
     'tg': "таджикский",
     'ta': "тамильский",
     'te': "телугу",
     'th': "тайский",
     'tr': "турецкий",
     'uk': "украинский",
     'ur': "урду",
     'uz': "узбекский",
     'vi': "вьетнамский",
     'cy': "валлийский",
     'xh': "хоса",
     'yi': "идиш",
     'yo': "йоруба",
     'zu': "зулу",
     'fil': "филиппинский",
     'he': "иврит"}
tg_token = open('token.txt').readline() # токен бота
codes = list(d.keys())
langs = list(d.values())
bot = telebot.TeleBot(tg_token)
a = []
tr = Translator()


@bot.message_handler(commands=['start'])  # команда старт
def main(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    # item1 = types.InlineKeyboardButton('ENGLISH', callback_data='question1')
    # item2 = types.InlineKeyboardButton('italian', callback_data='question2')
    item1 = types.InlineKeyboardButton('На какой язык переводить?', callback_data='choose')
    item2 = types.InlineKeyboardButton('Чтобы получить перевод, просто отправь текст сообщением', callback_data='a')
    markup.add(item1, row_width=1)
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.first_name}, это бот-переводчик.\n\nЧтобы получить перевод, просто отправь текст сообщением',

                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>help</b>', parse_mode='html')


# Определяем функцию для обработки сообщений
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        # if call.data == 'auto' and tr.autodetect:
        #   bot.send_message(call.message.chat.id, 'Автоопределение отключено.')
        #  tr.change_autodetect(0)
        # if call.data == 'auto' and not tr.autodetect:
        #   bot.send_message(call.message.chat.id, 'Автоопределение включено.')
        #  tr.change_autodetect(1)
        if call.data == 'choose':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Русский 🇷🇺', callback_data='ru')
            item2 = types.InlineKeyboardButton('Английский 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='en')
            item3 = types.InlineKeyboardButton('Французский 🇫🇷', callback_data='fr')
            item4 = types.InlineKeyboardButton('Итальянский 🇮🇹', callback_data='it')
            item5 = types.InlineKeyboardButton('Немецкий 🇩🇪', callback_data='de')
            item6 = types.InlineKeyboardButton('Испанский 🇪🇸', callback_data='es')
            item7 = types.InlineKeyboardButton('Другой 🏳', callback_data='other')
            markup.add(item1, item2, item3, item4, item5, item6, item7, row_width=3)
            bot.send_message(call.message.chat.id,
                             f'Выбери язык для перевода:',
                             reply_markup=markup)
        if call.data in codes:
            tr.change_target_lang(call.data)
            bot.send_message(call.message.chat.id,
                             f'Язык сменен на {langs[codes.index(call.data)]}')
        if call.data == 'other':
            bot.send_message(call.message.chat.id,
                             f'Чтобы выбрать язык, не указанный в списке, напишите /c и название языка (на русском)')


@bot.message_handler(func=lambda call: True)
def translate(message):
    if '/c' in message.text or '/с' in message.text:
        if len(message.text) > 2:
            c = message.text.lower().split()[1]
            if c in langs:
                tr.change_target_lang(codes[langs.index(c)])
                bot.send_message(message.chat.id, f'Язык сменен на {c}', parse_mode='html')
            else:
                bot.send_message(message.chat.id, f'Мы пока не знаем такого языка(', parse_mode='html')
        else:
            bot.send_message(message.chat.id, f'Укажите название языка после /c', parse_mode='html')
    else:
        e = tr.translate(message.text)
        a.append(f'{message.chat.id}, [{datetime.now()}]: {message.text} => {e}\n')
        bot.send_message(message.chat.id, f'<b>{e}</b>', parse_mode='html')
        print(a)
        f = open('query_history.txt', 'a')
        f.write(f'{message.chat.id}, [{datetime.now()}]: {message.text} => {e}\n')
        f.close()


bot.polling(none_stop=True)
