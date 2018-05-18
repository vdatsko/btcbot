import requests
import misc
from yobit import get_btc
from time import sleep


token = misc.token

#https://api.telegram.org/bot452411746:AAHgzxq5wW8bVP8sad3m4ghbL8j10P-piJo/sendmessage?chat_id=199954027&text=hi%20Victor
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0







def get_updates():
    url = URL +'getupdates'
    #print(url)
    req = requests.get(url)
    return req.json()

def get_message():
    data = get_updates()

    last_object = data['result'][-1]
    currant_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != currant_update_id:
        last_update_id = currant_update_id

        chat_id = last_object ['message']['chat']['id']

        message_text = last_object['message']['text']

        message = {'chat_id': chat_id,
                   'text': message_text
                   }
        return message
    return None

def send_message(chat_id, text="Dont stop cryind..."):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)








def main():
    #d = get_updates()
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/btc':
                send_message(chat_id, get_btc())
            else:
                continue

        sleep(2)




if __name__ == '__main__':
    main()