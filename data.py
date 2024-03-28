import requests 
import yfinance
import creds
class app_data:
    def __init__(self):
        self.response_wn = requests.get(url = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={creds.api_key}").json()
        self.latest = ""
        self.gaincompanyList = []
        self.gainchangeList = []
        self.losecompanyList = []
        self.losechangeList = []
        self.inputLowPrice = ""
        self.inputHighPrice = ""
        self.low = ""
        self.high = ""
        self.open = ""
        self.close = ""
        self.highList = []
        self.lowList = []
        self.openList = []
        self.closeList = []
        for i in range(0,5):    
            self.theTicker = yfinance.Ticker(self.response_wn["top_gainers"][i]["ticker"])
            try:
                self.companyName = self.theTicker.info['longName']
            except:
                self.companyName = self.response_wn["top_gainers"][i]["ticker"]
            else:
                self.companyName = self.theTicker.info['longName']
            finally:
                self.gaincompanyList.append(self.companyName)
                self.value = self.response_wn["top_gainers"][i]["change_percentage"]
                self.value = self.value.strip('%')
                self.value = float(self.value)
                self.value = round(self.value, 0)
                self.gainchangeList.append(self.value)
        for i in range(0,5):    
            self.theTicker = yfinance.Ticker(self.response_wn["top_losers"][i]["ticker"])
            try:
                self.companyName = self.theTicker.info['longName']
            except:
                self.companyName = self.response_wn["top_losers"][i]["ticker"]
            else:
                self.companyName = self.theTicker.info['longName']
            finally:
                self.losecompanyList.append(self.companyName)
                self.value = self.response_wn["top_losers"][i]["change_percentage"]
                self.value = self.value.strip('%')
                self.value = float(self.value)
                self.value = round(self.value, 0)
                self.losechangeList.append(self.value)
        
    def getgainCompanyList(self): 
        return self.gaincompanyList

    def getgainChangeList(self):
        return self.gainchangeList

    def getloseCompanyList(self): 
        return self.losecompanyList

    def getloseChangeList(self):
        return self.losechangeList 

    def saveTicker(self, tickerName):
        self.ticker = tickerName 

    
    def addOpen(self, tickerName):
        self.latest = requests.get(url =f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={tickerName}&apikey={creds.api_key}").json()
        self.open = self.latest['Global Quote']['02. open']
        self.openList.append(self.open)
    def addHigh(self):
        self.high = self.latest['Global Quote']['03. high']
        self.highList.append(self.high)
    def addLow(self):
        self.low = self.latest["Global Quote"]["04. low"]
        self.lowList.append(self.low)
    def addClose(self):
        self.close = self.latest["Global Quote"]["08. previous close"]
        self.closeList.append(self.close)
    def returnOpen(self):
        return self.openList

    def returnHigh(self):
        return self.highList

    def returnLow(self):
        return self.lowList

    def returnClose(self):
        return self.closeList
    def returnCurrentHigh(self):
        return self.high
    def returnCurrentLow(self):
        return self.low
    def getHello(self):
        return "hello"