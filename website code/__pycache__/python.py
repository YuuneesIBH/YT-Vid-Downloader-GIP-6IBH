import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

url = "https://www.amazon.de/-/nl/dp/B00IL0ORMI/ref=sr_1_4?crid=2LBO7VN3AGBKC&keywords=eierkocher&qid=1678224561&sprefix=eierk%2Caps%2C76&sr=8-4&th=1"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find(id='productTitle').get_text().strip()
delivery_time = soup.find(id='ddmDeliveryMessage').get_text().strip()

subject = "Leveringstijd van " + title
message = "De leveringstijd van " + title + " is " + delivery_time
sender_email = "sales@staypowered.be"
receiver_email = "norayounes650@gmail.com"

msg = MIMEText(message)
msg['Subject'] = subject
msg['From'] = sender_email
