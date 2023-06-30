from telethon import TelegramClient, sync
from telethon import events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.types import InputPeerEmpty, PeerUser, PeerChat, PeerChannel
import requests
import time
import random

# Данные аккаунтов
api_id1 = '12588062'
api_hash1 = 'd0f061c565991d6ed274285c0d032f7a'
phone1 = '+79816661471'

api_id2 = '13123883'
api_hash2 = 'f1fab12098570c2bf8848ad6ea23c62f'
phone2 = '+79676939873'

api_id3 = '19334807'
api_hash3 = '4b4edde7a9d46172399f0ac4cb98ae63'
phone3 = '+79842549006'

api_id4 = ''
api_hash4 = ''
phone4 = ''

api_id5 = ''
api_hash5 = ''
phone5 = ''

api_id6 = ''
api_hash6 = ''
phone6 = ''

api_id7 = ''
api_hash7 = ''
phone7 = ''

api_id8 = ''
api_hash8 = ''
phone8 = ''

api_id9 = ''
api_hash9 = ''
phone9 = ''

api_id10 = ''
api_hash10 = ''
phone10 = ''

api_id11 = ''
api_hash11 = ''
phone11 = ''

api_id12 = ''
api_hash12 = ''
phone12 = ''

api_id13 = ''
api_hash13 = ''
phone13 = ''

api_id14 = ''
api_hash14 = ''
phone14 = ''

api_id15 = ''
api_hash15 = ''
phone15 = ''

api_id16 = ''
api_hash16 = ''
phone16 = ''

api_id17 = ''
api_hash17 = ''
phone17 = ''

# Создание клиентов 
client1 = TelegramClient('session1', api_id1, api_hash1)
client2 = TelegramClient('session2', api_id2, api_hash2)
client3 = TelegramClient('session3', api_id3, api_hash3)
client4 = TelegramClient('session4', api_id4, api_hash4)
client5 = TelegramClient('session5', api_id5, api_hash5)
client6 = TelegramClient('session6', api_id6, api_hash6)
client7 = TelegramClient('session7', api_id7, api_hash7)
client8 = TelegramClient('session8', api_id8, api_hash8)
client9 = TelegramClient('session9', api_id9, api_hash9)
client10 = TelegramClient('session10', api_id10, api_hash10)
client11 = TelegramClient('session11', api_id11, api_hash11)
client12 = TelegramClient('session12', api_id12, api_hash12)
client13 = TelegramClient('session13', api_id13, api_hash13)
client14 = TelegramClient('session14', api_id14, api_hash14)
client15 = TelegramClient('session15', api_id15, api_hash15)
client16 = TelegramClient('session16', api_id16, api_hash16)
client17 = TelegramClient('session17', api_id17, api_hash17)

# Авторизация
client1.connect()
if not client1.is_user_authorized():
    client1.send_code_request(phone1)
    client1.sign_in(phone1, input('1 Введите код подтверждения: '))
client2.connect()
if not client2.is_user_authorized():
    client2.send_code_request(phone2)
    client2.sign_in(phone2, input('2 Введите код подтверждения: '))
client3.connect()
if not client3.is_user_authorized():
    client3.send_code_request(phone3)
    client3.sign_in(phone3, input('3 Введите код подтверждения: '))
# Команда для отправки нескольких сообщений с задержкой
@client1.on(events.NewMessage(pattern='/send_multiple'))
async def send_multiple_messages(event):
    chat_id = event.chat_id
# Извлечение сообщений после команды
messages = event.raw_text.split(' ')[1:]
for i in range(10):
        for message in messages:
            await client1(SendMessageRequest(chat_id, me
ssage))
            time.sleep(2)
@client2.on(events.NewMessage(pattern='/send_multiple'))
async def send_multiple_messages(event):
    chat_id = event.chat_id
    messages = event.raw_text.split(' ')[1:]
    for i in range(10):
        for message in messages:
            await client2(SendMessageRequest(chat_id, message))
            time.sleep(2)
# Запуск клиентов
client1.start()
client2.start()
client1.run_until_disconnected()
client2.run_until_disconnected()
