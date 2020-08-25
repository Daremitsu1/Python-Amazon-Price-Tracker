import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Samsung-Galaxy-10-1-Wi-Fi-Black/dp/B07SVZ86KS/ref=asc_df_B07SVZ86KS/?tag=googleshopdes-21&linkCode=df0&hvadid=397082359880&hvpos=&hvnetw=g&hvrand=11287654645532331634&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007828&hvtargid=pla-836035476407&psc=1&ext_vrnc=hi'

#Add User Agent
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

page=requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[:3])

print(converted_price)
print(title.strip())
