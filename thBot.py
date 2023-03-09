
import pandas as pd
from datetime import datetime
import requests
import re

today = datetime.now()

#Read the excel into a dataframe
#df = pd.read_excel('TrailBlazers_Birthdays.xlsx')
df = pd.read_excel('/home/ec2-user/south-west/south-west/TrailBlazers_Birthdays.xlsx')

#Gets the system date - Month and day
month = today.month
day = today.day

#You need both the token and chat id to send the message
TOKEN = "Hidde"

#group chat id
chat_id = "-idden"

#Boolean variable to be updated to True if there is someone with a birthday
someone_has = 0;

#loop through the df, if you get a date matching today; send a message
for tuple in df.itertuples():
    if ((month == tuple.Month) & (day == tuple.Date)):
        someone_has = 1;
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={'Happy Birthday' +' '+tuple.Name}"
        print(requests.get(url).json()) # this sends the message


if(someone_has == 0):
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'Very Hidden'})
    if response.status_code == requests.codes.ok:
        data = response.text
        new_string = re.sub(r'[^\w\s]', '', data)
        final_string = new_string.replace('fact', '')
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={'No Trailblazer has a birthday today, did you know :'+' '+final_string}"
        print(requests.get(url).json()) # this sends the message
