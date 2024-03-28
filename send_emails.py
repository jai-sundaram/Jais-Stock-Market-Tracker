from ui import app_ui
import requests
import smtplib
import pandas
import creds
data = pandas.read_csv("user_info_stocks.csv")
def sendEmails():
    for index, row in data.iterrows():
        current = requests.get(url =f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={row['Stock Ticker']}&apikey={creds.api_key}").json()
        currentHigh = current['Global Quote']['03. high']
        currentLow = current["Global Quote"]["04. low"]
        currentOpen = current["Global Quote"]["02. open"]
        currentClose = current["Global Quote"]["08. previous close"]
        users_email = row['Email']
        if float(currentHigh) > float(row['User High']):
            with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
                connection.starttls()
                my_email = "jaisstockmarkettracker@gmail.com"   
                my_password = "hksz pswq fbre yisz"
                connection.login(user = my_email, password = my_password)
                connection.sendmail(from_addr = my_email, to_addrs= users_email, 
                msg = 
                f"Subject: Your Stock Information - {row['Stock Name']}\n\n" +
                f"Hello, {row['Name']}!\n\n" +
                f"Thank you for using Jai's Stock Market Tracker. This email contains informating about one of the stocks you added, the {row['Stock Name']} ({row['Stock Ticker']}) stock.\n\n"+
                f"Here are some datapoints: \n \n" +
                f"Opening Value: ${currentOpen} \n"+
                f"Lowest Value: ${currentLow} \n"+
                f"Highest Value: ${currentHigh}\n"
                f"Close Value: ${currentClose}\n\n"+
                f"NOTIFICATION: USER HIGH EXCEEDED\n"
                f"The stock currently has a value of ${currentHigh}, which is greater than high value threshold of ${row['User High']}.\n\n"
                f"Thank you for using my program. \n\nSincerely, \n Jai Sundaram"
                )
        elif float(currentLow) < float(row['User Low']):
            with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
                connection.starttls()
                my_email = "jaisstockmarkettracker@gmail.com"   
                my_password = "hksz pswq fbre yisz"
                connection.login(user = my_email, password = my_password)
                connection.sendmail(from_addr = my_email, to_addrs= users_email, 
                msg = 
                f"Subject: Your Stock Information - {row['Stock Name']}\n\n" +
                f"Hello, {row['Name']}!\n\n" +
                f"Thank you for using Jai's Stock Market Tracker. This email contains informating about one of the stocks you added, the {row['Stock Name']} ({row['Stock Ticker']}) stock.\n\n"+
                f"Here are some datapoints: \n \n" +
                f"Opening Value: ${currentOpen} \n"+
                f"Lowest Value: ${currentLow} \n"+
                f"Highest Value: ${currentHigh}\n"
                f"Close Value: ${currentClose}\n\n"+
                f"NOTIFICATION: USER Low EXCEEDED\n"
                f"The stock currently has a value of ${currentLow}, which is lower than lowest value threshold of ${row['User Low']}.\n\n"
                f"Thank you for using my program. \n\nSincerely, \n Jai Sundaram"
                )
        else:
            with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
                connection.starttls()
                my_email = "jaisstockmarkettracker@gmail.com"   
                my_password = creds.email_pass
                connection.login(user = my_email, password = my_password)
                connection.sendmail(from_addr = my_email, to_addrs= users_email, 
                msg = 
                f"Subject: Your Stock Information - {row['Stock Name']}\n\n" +
                f"Hello, {row['Name']}!\n\n" +
                f"Thank you for using Jai's Stock Market Tracker. This email contains informating about one of the stocks you added, the {row['Stock Name']} ({row['Stock Ticker']}) stock.\n\n"+
                f"Here are some datapoints: \n \n" +
                f"Opening Value: ${currentOpen} \n"+
                f"Lowest Value: ${currentLow} \n"+
                f"Highest Value: ${currentHigh}\n"
                f"Close Value: ${currentClose}\n\n"+
                f"Thank you for using my program. \n\nSincerely, \n Jai Sundaram")
sendEmails()