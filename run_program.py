import pandas
from data import app_data
from datetime import datetime
import schedule 
import time as tm
import creds
from ui import app_ui
import requests
my_screen = app_ui()
now = datetime.now()
my_username = my_screen.getName()
users_email = ""
openList = my_screen.getOpenList()
highList = my_screen.getHighList()
lowList = my_screen.getLowList()
closeList = my_screen.getCloseList()
tickerList = my_screen.getTickerList()
nameList = my_screen.getNameList()
userHighList = my_screen.getHigh()
userLowList = my_screen.getLow()
usersList = my_screen.getUsername()
emailsList = my_screen.getEmail()
data = pandas.read_csv("user_info_stocks.csv")

for i in range(0, len(openList)):
    data.loc[len(data.index)] = [usersList[i], emailsList[i], nameList[i], tickerList[i], userHighList[i], userLowList[i]]
data.to_csv('user_info_stocks.csv', index=False, mode='w')