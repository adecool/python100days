import smtplib
from bs4 import BeautifulSoup
import requests
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Accept-Language':'en-US,en;q=0.9',

}
response = requests.get('https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B01NBKTPTS&psc=1&pd_rd_w=0Fi5r&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=WJ6X1F2T4FB2SFE6K4ZW&pd_rd_wg=Qsdaj&pd_rd_r=c9cbd1ac-7947-440c-8dd6-1030d12b4b2d&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699', headers=header)
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, 'html.parser')
#print(soup)
earbud_price = soup.find(name='span', class_='a-offscreen')
price = earbud_price.getText().split('$')[1]
if float(price)  > 94:
    with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as server:
        server.starttls()
        server.login('gen2proff@yahoo.com', 'gen2;soul')
        server.sendmail(
             'gen2proff@yahoo.com',
            "tobiadebiyi17@gmail.com",
            msg=f'Subject:Amazon Prize Alert!\n\nInstant Pot Duo Plus 6 Quart 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, 15 One-Touch Programs,Stainless Steel/Black' +
f'\n\n This is to alert you that the price is now {price}')
