import customtkinter
import requests
from PIL import Image, ImageTk
from io import BytesIO
from data import app_data
import creds
class app_ui:
    def __init__(self):
        self.user_email = ""  
        self.username = ""    
        self.ticker = ""
        self.lowValue = ""
        self.highValue = ""
        self.updates = ""
        self.window = customtkinter.CTk()
        self.window.geometry("350x600")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.window_bg_color = self.window.cget("bg")
        self.window.title("Jai's Stock Tracking Program")
        self.welcomePage = customtkinter.CTkFrame(self.window, width=350, height=600)
        self.stockInputPage = customtkinter.CTkFrame(self.window, width=350, height=600)
        self.stockOutputPage = customtkinter.CTkFrame(self.window, width=350, height=600)
        self.generalPage = customtkinter.CTkFrame(self.window, width=350, height=600)
        self.cName = ""
        self.index = 0
        self.my_data = app_data()
        self.nameList = []
        self.tickerList = []
        self.welcomePage.tkraise()
        self.openList = []
        self.highList = []
        self.closeList = []
        self.lowList = []
        self.userHigh = ""
        self.userLow = ""
        self.usernameList = []
        self.emailList = []
        self.userHighList = []
        self.userLowList = []
        #---Page 1---

        self.custom_font_app_title = customtkinter.CTkFont("Times", 30)
        self.custom_slogan_font = customtkinter.CTkFont("Times", 25, slant="italic")
        self.custom_name_font = customtkinter.CTkFont("Times", 20)
        self.custom_warning_font = customtkinter.CTkFont("Times", 15)
        self.welcomePage.tkraise()
        self.welcomePage.grid(column=0, row=0, sticky="nsew")
        self.welcomePage.configure(fg_color=self.window_bg_color)
        self.appNameLabel = customtkinter.CTkLabel(self.welcomePage, text="Jai's Stock Market Tracker", font=self.custom_font_app_title)
        self.appNameLabel.place(x=16, y=30)
        self.sloganLabel = customtkinter.CTkLabel(self.welcomePage, text="Your Personal Stocket Market Tracking Program", font=self.custom_slogan_font)
        self.sloganLabel.configure(wraplength=350)
        self.sloganLabel.place(x=22, y=75)
        self.nameLabel = customtkinter.CTkLabel(self.welcomePage, text="Enter your full legal name", font=self.custom_name_font)
        self.nameLabel.place(x=71, y=175)
        self.nameEntry = customtkinter.CTkEntry(self.welcomePage, placeholder_text="Enter name", border_color=self.window_bg_color, width=207)
        self.nameEntry.place(x=71, y=210)
        self.emailLabel = customtkinter.CTkLabel(self.welcomePage, text="Enter your email address", font=self.custom_name_font)
        self.emailLabel.place(x=74, y=260)
        self.emailEntry = customtkinter.CTkEntry(self.welcomePage, placeholder_text="Enter email", border_color=self.window_bg_color, width=207)
        self.emailEntry.place(x=71, y=290)
        self.startInfoButton = customtkinter.CTkButton(self.welcomePage, text="Get Started", command=self.combined_function_1)
        self.startInfoButton.place(x=104, y=340)
        self.startImage = customtkinter.CTkImage(dark_image=Image.open("starting.png"), size=(300, 200))
        self.startingLabel = customtkinter.CTkLabel(self.welcomePage, text="", image=self.startImage)
        self.startingLabel.place(x=25, y=380)

        #---Page 2---

        self.tickers = []
        self.titleFontCustom = customtkinter.CTkFont("Times", 24)
        self.tickerFontCustom = customtkinter.CTkFont("Times", 22)
        self.lowFontCustom = customtkinter.CTkFont("Times", 22)
        self.stockFont = customtkinter.CTkFont("Times", 28)
        self.stockInputPage.grid(column=0, row=0, sticky="nsew")
        self.stockInputPage.configure(fg_color=self.window_bg_color)
        self.inputTitleLabel = customtkinter.CTkLabel(self.stockInputPage, text="Enter Tracking Information", font=self.titleFontCustom)
        self.inputTitleLabel.place(x=35, y=30)
        self.companyInputLabel = customtkinter.CTkLabel(self.stockInputPage, text="Enter Stock Name", font=self.tickerFontCustom)
        self.companyInputLabel.place(x=90, y=80)
        self.companyEntry = customtkinter.CTkEntry(self.stockInputPage, placeholder_text="Enter Name", border_color=self.window_bg_color, width=187)
        self.companyEntry.place(x=83, y=130)
        self.tickerInputLabel = customtkinter.CTkLabel(self.stockInputPage, text="Enter Stock Ticker", font=self.tickerFontCustom)
        self.tickerInputLabel.place(x=90, y=180)
        self.tickerEntry = customtkinter.CTkEntry(self.stockInputPage, placeholder_text="Enter Ticker", border_color=self.window_bg_color, width=187)
        self.tickerEntry.place(x = 83, y = 230)
        self.lowInputLabel = customtkinter.CTkLabel(self.stockInputPage, text="How low should the stock price go to trigger an alert?", font=self.lowFontCustom)
        self.lowInputLabel.place(x=30, y=280)
        self.lowInputLabel.configure(wraplength=280)
        self.lowPriceEntry = customtkinter.CTkEntry(self.stockInputPage, placeholder_text="Enter Price", border_color=self.window_bg_color, width=187)
        self.lowPriceEntry.place(x=83, y=355)
        self.highInputLabel = customtkinter.CTkLabel(self.stockInputPage, text="How high should the stock price go to trigger an alert?", font=self.lowFontCustom)
        self.highInputLabel.place(x=30, y=400)
        self.highInputLabel.configure(wraplength=300)
        self.highPriceEntry = customtkinter.CTkEntry(self.stockInputPage, placeholder_text="Enter Price", border_color=self.window_bg_color, width=187)
        self.highPriceEntry.place(x=83, y=470)
        self.stockInputButton = customtkinter.CTkButton(self.stockInputPage, text="Add stock", command=self.addButtonStuff)
        self.stockInputButton.place(x=108, y=520)
        self.next1 = customtkinter.CTkButton(self.stockInputPage, text="Next", command=self.goToOutputPage)
        self.next1.place(x=197, y=563)
        self.back1 = customtkinter.CTkButton(self.stockInputPage, text="Previous", command=self.welcomePage.tkraise)
        self.back1.place(x=13, y=563)

        #---Page 3---

        self.domain = "ibm.com"
        self.size = 200
        self.greyscale = False
        self.url = f'https://logo.clearbit.com/{self.domain}?size={self.size}&greyscale={self.greyscale}'
        self.response = requests.get(url = self.url)
        self.image_data = BytesIO(self.response.content)
        self.img = Image.open(self.image_data)
        self.logo = ImageTk.PhotoImage(self.img)
        self.titleFontCustom = customtkinter.CTkFont("Times", 24)
        self.stockOutputPage.configure(fg_color=self.window_bg_color)
        self.stockOutputPage.grid(column=0, row=0, sticky="nsew")
        self.companyLogo = customtkinter.CTkLabel(self.stockOutputPage, image=self.logo, text="")
        self.companyLogo.place(x=75, y=15)
        self.stockTickerLabel = customtkinter.CTkLabel(self.stockOutputPage, text=f"Stock Ticker: ", font=self.titleFontCustom)
        self.stockTickerLabel.place(x=30, y=270)
        self.stockNameLabel = customtkinter.CTkLabel(self.stockOutputPage, text=f"Stock Name:", font=self.titleFontCustom)
        self.stockNameLabel.place(x=30, y=220)
        self.lowOutputLabel = customtkinter.CTkLabel(self.stockOutputPage, text=f"Daily Low:", font=self.titleFontCustom)
        self.lowOutputLabel.place(x=30, y=320)
        self.highOutputLabel = customtkinter.CTkLabel(self.stockOutputPage, text=f"Daily High:", font=self.titleFontCustom)
        self.highOutputLabel.place(x=30, y=370)
        self.openOutputLabel = customtkinter.CTkLabel(self.stockOutputPage, text=f"Daily Open:", font=self.titleFontCustom)
        self.openOutputLabel.place(x=30, y=420)
        self.closeOutputLabel = customtkinter.CTkLabel(self.stockOutputPage, text=f"Daily Close:", font=self.titleFontCustom)
        self.closeOutputLabel.place(x=30, y=470)
        self.nextStock = customtkinter.CTkButton(self.stockOutputPage, text="Next stock", command= self.seeNextStock)
        self.nextStock.place(x=197, y=520)
        self.previousStock = customtkinter.CTkButton(self.stockOutputPage, text="Previous stock", command= self.seePreviousStock)
        self.previousStock.place(x=13, y=520)
        next2 = customtkinter.CTkButton(self.stockOutputPage, text="Next", command= self.generalPage.tkraise)
        next2.place(x=197, y=560)
        self.back2 = customtkinter.CTkButton(self.stockOutputPage, text="Previous", command=self.stockInputPage.tkraise)
        self.back2.place(x=13, y=560)

        #---Page 4---
        self.custom_title_font = customtkinter.CTkFont("Times", 24)
        self.custom_subtitle_font = customtkinter.CTkFont("Times", 22)
        self.custom_point_font = customtkinter.CTkFont("Times", 19)
        self.generalPage.grid(column=0, row=0, sticky="nsew")
        self.overviewLabel = customtkinter.CTkLabel(self.generalPage, text="Top Gainers & Losers", font=self.custom_title_font)
        self.overviewLabel.place(x=60, y=25)
        self.gainersLabel = customtkinter.CTkLabel(self.generalPage, text="Gainers (Name: Change Percentage)", font=self.custom_subtitle_font)
        self.gainersLabel.place(x=20, y=65)
        self.gainer1Label = customtkinter.CTkLabel(self.generalPage, text="1. Stock name - Percent Increase", font=self.custom_point_font)
        self.gainer1Label.place(x=20, y=105)
        self.gainer2Label = customtkinter.CTkLabel(self.generalPage, text="2. Stock name - Percent Increase", font=self.custom_point_font)
        self.gainer2Label.place(x=20, y=145)
        self.gainer3Label = customtkinter.CTkLabel(self.generalPage, text="3. Stock name - Percent Increase", font=self.custom_point_font)
        self.gainer3Label.place(x=20, y=185)
        self.gainer4Label = customtkinter.CTkLabel(self.generalPage, text="4. Stock name - Percent Increase", font=self.custom_point_font)
        self.gainer4Label.place(x=20, y=225)
        self.gainer5Label = customtkinter.CTkLabel(self.generalPage, text="5. Stock name - Percent Increase", font=self.custom_point_font)
        self.gainer5Label.place(x=20, y=265)
        self.losersLabel = customtkinter.CTkLabel(self.generalPage, text="Losers (Name: Change Percentage)", font=self.custom_subtitle_font)
        self.losersLabel.place(x=20, y=305)
        self.loser1Label = customtkinter.CTkLabel(self.generalPage, text="1. Stock name - Percent Decrease", font=self.custom_point_font)
        self.loser1Label.place(x=20, y=345)
        self.loser2Label = customtkinter.CTkLabel(self.generalPage, text="2. Stock name - Percent Decrease", font=self.custom_point_font)
        self.loser2Label.place(x=20, y=385)
        self.loser3Label = customtkinter.CTkLabel(self.generalPage, text="3. Stock name - Percent Decrease", font=self.custom_point_font)
        self.loser3Label.place(x=20, y=425)
        self.loser4Label = customtkinter.CTkLabel(self.generalPage, text="4. Stock name - Percent Decrease", font=self.custom_point_font)
        self.loser4Label.place(x=20, y=465)
        self.loser5Label = customtkinter.CTkLabel(self.generalPage, text="5. Stock name - Percent Decrease", font=self.custom_point_font)
        self.loser5Label.place(x=20, y=505)
        self.back3 = customtkinter.CTkButton(self.generalPage, text="Previous", command=self.stockOutputPage.tkraise)
        self.back3.place(x=13, y=560)
        gainers_labels_list = [self.gainer1Label, self.gainer2Label, self.gainer3Label, self.gainer4Label, self.gainer5Label] 
        for i in range(0, 5):  
            companyName = self.my_data.getgainCompanyList()[i]
            changeValue = self.my_data.getgainChangeList()[i]
            gainers_labels_list[i].configure(text=f"{companyName}: {changeValue}%")
        losers_labels_list = [self.loser1Label, self.loser2Label, self.loser3Label, self.loser4Label, self.loser5Label]
        for i in range(0,5):
            companyName = self.my_data.getloseCompanyList()[i]
            changeValue = self.my_data.getloseChangeList()[i]
            losers_labels_list[i].configure(text = f"{companyName}: {changeValue}%")


        #--Other Configurations--
        self.welcomePage.tkraise()
        self.window.after(1800000, lambda: self.window.destroy())
        self.window.mainloop()
    
    def combined_function_1(self):
        self.username =  self.nameEntry.get()
        self.user_email = self.emailEntry.get()
        self.usernameList.append(self.username)
        self.emailList.append(self.user_email)
        self.stockInputPage.tkraise()     
    def getName(self):
        return self.username    
    def getEmail(self):
        return self.user_email
    def setTicker(self):
        self.ticker = self.tickerEntry.get()
        return self.ticker
    def getcName(self):
        self.cName = self.companyEntry.get()
        return self.cName


    def setImage(self, theName):
        API_KEY = creds.image_key
        url = f'https://logo.clearbit.com/{theName.lower()}.com'
        headers = {'Authorization': f'Bearer {API_KEY}'}

        response = requests.get(url, headers=headers)

        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img = img.resize((200, 200), Image.ANTIALIAS)  
        img_tk = ImageTk.PhotoImage(img)
        self.companyLogo.configure(image=img_tk)

        
    def seeNextStock(self):
        self.ticker = self.setTicker()
        self.openList = self.my_data.returnOpen()
        self.highList = self.my_data.returnHigh()
        self.closeList = self.my_data.returnClose()
        self.lowList = self.my_data.returnLow()
        self.index += 1
        if self.index < len(self.openList):
            self.openOutputLabel.configure(text=f"Daily Open: ${self.openList[self.index]}")
            self.highOutputLabel.configure(text=f"Daily High: ${self.highList[self.index]}")
            self.lowOutputLabel.configure(text=f"Daily Low: ${self.lowList[self.index]}")
            self.closeOutputLabel.configure(text=f"Daily Close: ${self.closeList[self.index]}")
            self.stockNameLabel.configure(text = f"Stock Name: {self.nameList[self.index]}")
            self.stockTickerLabel.configure(text = f"Stock Ticker: {self.tickerList[self.index]}")
            self.setImage(self.nameList[self.index])
    def seePreviousStock(self):
        self.ticker = self.setTicker()
        self.openList = self.my_data.returnOpen()
        self.highList = self.my_data.returnHigh()
        self.closeList = self.my_data.returnClose()
        self.lowList = self.my_data.returnLow()
        self.index -= 1
        if self.index >= 0:
            self.setImage(self.nameList[self.index])
            self.openOutputLabel.configure(text=f"Daily Open: ${self.openList[self.index]}")
            self.highOutputLabel.configure(text=f"Daily High: ${self.highList[self.index]}")
            self.lowOutputLabel.configure(text=f"Daily Low: ${self.lowList[self.index]}")
            self.closeOutputLabel.configure(text=f"Daily Close: ${self.closeList[self.index]}")
            self.stockNameLabel.configure(text = f"Stock Name: {self.nameList[self.index]}")
            self.stockTickerLabel.configure(text = f"Stock Ticker: {self.tickerList[self.index]}")
            self.setImage(self.nameList[self.index])
    def addButtonStuff(self):
        self.ticker = self.tickerEntry.get()
        self.tickerList.append(self.ticker)
        self.cName = self.companyEntry.get()
        self.nameList.append(self.cName)
        self.my_data.addOpen(self.ticker) 
        self.my_data.addHigh()  
        self.my_data.addLow()  
        self.my_data.addClose() 
        self.lowValue = self.lowPriceEntry.get()
        self.highValue = self.highPriceEntry.get()
        self.userHighList.append(self.highValue)
        self.userLowList.append(self.lowValue)


    def goToOutputPage(self):
        
        self.ticker = self.tickerEntry.get()
        self.tickerList.append(self.ticker)
        self.cName = self.companyEntry.get()
        self.nameList.append(self.cName)
        self.my_data.addOpen(self.ticker) 
        self.my_data.addHigh()  
        self.my_data.addLow()   
        self.my_data.addClose() 
        self.ticker = self.setTicker()
        self.openList = self.my_data.returnOpen()
        self.highList = self.my_data.returnHigh()
        self.closeList = self.my_data.returnClose()
        self.lowList = self.my_data.returnLow()
        self.openOutputLabel.configure(text=f"Daily Open: ${self.openList[0]}")
        self.highOutputLabel.configure(text=f"Daily High: ${self.highList[0]}")
        self.closeOutputLabel.configure(text = f"Daily Close: ${self.closeList[0]}")
        self.lowOutputLabel.configure(text = f"Daily Low: ${self.lowList[0]}")
        self.setImage(self.nameList[0])
        self.stockNameLabel.configure(text = f"Stock Name: {self.nameList[0]}")
        self.stockTickerLabel.configure(text = f"Stock Ticker: {self.tickerList[0]}")
        self.index = 0
        self.openList.pop()
        self.highList.pop()
        self.closeList.pop()
        self.lowList.pop()
        self.nameList.pop()
        self.tickerList.pop()
        self.stockOutputPage.tkraise()
    def getName(self):
        return self.username
    def getEmail(self):
        return self.user_email
    def getOpenList(self):
        return self.openList
    def getCloseList(self):
        return self.closeList
    def getHighList(self):
        return self.highList   
    def getLowList(self):
        return self.lowList
    def getTickerList(self):
        return self.tickerList
    def getNameList(self):
        return self.nameList
    def getHigh(self):
        return self.userHighList
    def getLow(self):
        return self.userLowList
    def getUsername(self):
        return self.usernameList
    def getEmail(self):
        return self.emailList