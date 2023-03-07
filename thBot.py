
import pandas as pd
from datetime import datetime
import requests

today = datetime.now()

#Read the excal into a dataframe
df = pd.read_excel('TrailBlazers_Birthdays.xlsx')

#Gets the system date - Month and day
month = 3 #today.month
day = 8 #today.day

#You need both the token and chat id to send the message
TOKEN = "I have hidden my token"
chat_id = "I have hidden my chat id too"

#loop through the df, if you get a date matching today; send a message
for tuple in df.itertuples():
    if ((month == tuple.Month) & (day == tuple.Date)):
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={'Happy Birthday' +' '+tuple.Name}"
        print(requests.get(url).json()) # this sends the message
