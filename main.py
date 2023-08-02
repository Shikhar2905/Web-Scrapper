import requests
from bs4 import BeautifulSoup
import smtplib
import time

# while True :
re = requests.get('https://www.amazon.in/s?k=rs+agarwal+quantitative+aptitude+book&crid=HVC8MMZ1T0EX&sprefix=rs+a%2Caps%2C307&ref=nb_sb_ss_ts-doa-p_1_4')
res = re.content

soup = BeautifulSoup(res,'html.parser')
price = float(soup.find( 'span' , class_='a-price-whole').text)

if price<560 :
    print(price)
    smt = smtplib.SMTP('smtp.gmail.com', 587)
    smt.ehlo()
    smt.starttls()
    smt.login('mr.shikhar29@gmail.com','amgigkyubehcotdd')
    smt.sendmail('mr.shikhar29@gmail.com' ,
                'mr.shikhar29@gmail.com' ,
                f"Subject : Alert! Price is below 560" )
    smt.quit()
        
    time.sleep(2)