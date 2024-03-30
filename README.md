A program designed for users to easily view information related to and receive updates about stocks they favor.

Program features:
- Add stocks of your choosing, along with maximum and minimum stock values that should be crossed to receive notifications
- View the stock's opening, closing, high, and low value
- View the top gainers and losers (stocks that increased and decreased the most) using the percent change metric
- Receive daily updates that contain the opening, closing, high and low value and a notification if the thresholds set are crossed

Technical details: 
- Utillized CTk (CustomTkinter) to design an appealing and easy to navigate user interface
- Utillized Alpha Vantage's API to extract stock information and the top gainers and losers
- Used the Clearbit API to get company logos
- Used the Yahoo Finance API to find company logo given ticker, to display the names of the top gainers and losers
- Used the io and Pillow modules to perform operations with image data 
- Used the pandas module to save and read user preferences
- Used the smtplib to send emails to users
- Used the schedule and time modules to automatically send users emails everyday

IMPORTANT - Program functionality:
  - Please get an API key for the Alpha Vantage and Clearbit API's to seamlessly use my program
  - Get the Alpha Vantage API key here: https://www.alphavantage.co/support/#api-key
  - Get the Cleabit API key here by following the steps: https://help.clearbit.com/hc/en-us/articles/6045527495191-Access-your-Clearbit-API-key
  - Run the 'run_program.py' file to interact with the program
  - If you would like the email mechanism to function, please email me at je.sundaram@gmail.com and I will provide the password for the email account
  - To automatically receive emails everyday, ensure that you leave the send_emails.py file running 
