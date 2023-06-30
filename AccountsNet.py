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
    client1.sign_in(phone1, input('Session-1 Введите код подтверждения: '))
client2.connect()
if not client2.is_user_authorized():
    client2.send_code_request(phone2)
    client2.sign_in(phone2, input('Session-2 Введите код подтверждения: '))
client3.connect()
if not client3.is_user_authorized():
    client3.send_code_request(phone3)
    client3.sign_in(phone3, input('Session-3 Введите код подтверждения: '))
client4.connect()
if not client4.is_user_authorized():
    client4.send_code_request(phone4)
    client4.sign_in(phone4, input('Session-4 Введите код подтверждения: '))
client5.connect()
if not client5.is_user_authorized():
    client5.send_code_request(phone5)
    client5.sign_in(phone5, input('Session-5 Введите код подтверждения: '))
client6.connect()
if not client6.is_user_authorized():
    client6.send_code_request(phone6)
    client6.sign_in(phone6, input('Session-6 Введите код подтверждения: '))
client7.connect()
if not client7.is_user_authorized():
    client7.send_code_request(phone7)
    client7.sign_in(phone7, input('Session-7 Введите код подтверждения: '))
client8.connect()
if not client8.is_user_authorized():
    client8.send_code_request(phone8)
    client8.sign_in(phone8, input('Session-8 Введите код подтверждения: '))
client9.connect()
if not client9.is_user_authorized():
    client9.send_code_request(phone9)
    client9.sign_in(phone9, input('Session-9 Введите код подтверждения: '))
client10.connect()
if not client10.is_user_authorized():
    client10.send_code_request(phone10)
    client10.sign_in(phone10, input('Session-10 Введите код подтверждения: '))
client11.connect()
if not client11.is_user_authorized():
    client11.send_code_request(phone11)
    client11.sign_in(phone11, input('Session-11 Введите код подтверждения: '))
client12.connect()
if not client12.is_user_authorized():
    client12.send_code_request(phone12)
    client12.sign_in(phone12, input('Session-12 Введите код подтверждения: '))
client13.connect()
if not client13.is_user_authorized():
    client13.send_code_request(phone13)
    client13.sign_in(phone13, input('Session-13 Введите код подтверждения: '))
client14.connect()
if not client14.is_user_authorized():
    client14.send_code_request(phone14)
    client14.sign_in(phone14, input('Session-14 Введите код подтверждения: '))
client15.connect()
if not client15.is_user_authorized():
    client15.send_code_request(phone15)
    client15.sign_in(phone15, input('Session-15 Введите код подтверждения: '))
client16.connect()
if not client16.is_user_authorized():
    client16.send_code_request(phone16)
    client16.sign_in(phone16, input('Session-16 Введите код подтверждения: '))
client17.connect()
if not client17.is_user_authorized():
    client17.send_code_request(phone17)
    client17.sign_in(phone17, input('Session-17 Введите код подтверждения: '))

# Команда для отправки нескольких сообщений с задержкой
@client1.on(events.NewMessage(pattern='/s'))
async def send_multiple_messages(event):
    chat_id = event.chat_id
# Извлечение сообщений после команды
messages = event.raw_text.split(' ')[1:]
for i in range(1000000):
        for message in messages:
            await client1(SendMessageRequest(chat_id, message))
            await client2(SendMessageRequest(chat_id, message))
            await client3(SendMessageRequest(chat_id, message))
            await client4(SendMessageRequest(chat_id, message))
            await client5(SendMessageRequest(chat_id, message))
            await client6(SendMessageRequest(chat_id, message))
            await client7(SendMessageRequest(chat_id, message))
            await client8(SendMessageRequest(chat_id, message))
            await client9(SendMessageRequest(chat_id, message))
            await client10(SendMessageRequest(chat_id, message))
            await client11(SendMessageRequest(chat_id, message))
            await client12(SendMessageRequest(chat_id, message))
            await client13(SendMessageRequest(chat_id, message))
            await client14(SendMessageRequest(chat_id, message))
            await client15(SendMessageRequest(chat_id, message))
            await client16(SendMessageRequest(chat_id, message))
            await client17(SendMessageRequest(chat_id, message))
            time.sleep(2)
            
# Запуск клиентов
client1.start()
client2.start()
client3.start()
client4.start()
client5.start()
client6.start()
client7.start()
client8.start()
client9.start()
client10.start()
client11.start()
client12.start()
client13.start()
client14.start()
client15.start()
client16.start()
client17.start()
client1.run_until_disconnected()
client2.run_until_disconnected()
client3.run_until_disconnected()
client4.run_until_disconnected()
client5.run_until_disconnected()
client6.run_until_disconnected()
client7.run_until_disconnected()
client8.run_until_disconnected()
client9.run_until_disconnected()
client10.run_until_disconnected()
client11.run_until_disconnected()
client12.run_until_disconnected()
client13.run_until_disconnected()
client14.run_until_disconnected()
client15.run_until_disconnected()
client16.run_until_disconnected()
client17.run_until_disconnected()
