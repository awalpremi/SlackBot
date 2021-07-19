import pandas as pd
import requests

pd.set_option("display.max_colwidth", None)

g_sheet = 'https://docs.google.com/spreadsheets/d/1yfzBeIvNfTrK93qzM6uGUAUa0hb3zu08cXGsDH-LKNc/edit#gid=0'
g_csv = g_sheet.replace('/edit#gid=', '/export?format=csv&gid=')


WEBHOOK_URL = 'INSERT YOUR URL'

def create_message():
    df = pd.read_csv(g_csv)
    message  = df.iloc[-1].to_string()
    return message

def push_message(message):
    payload = {'text':message}
    requests.post(WEBHOOK_URL, json=payload)

push_message(create_message())

#Cron */5 * * * * /user/bin/python3 /pathtoscript >> /root/alert.log 2>&1