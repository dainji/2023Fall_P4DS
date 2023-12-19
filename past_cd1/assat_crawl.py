import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.jobkorea.co.kr/starter/passassay/View/240007?Page=1&OrderBy=0&FavorCo_Stat=0&Pass_An_Stat=0')

soup = BeautifulSoup(response.text, 'html.parser')

f = open('Essay1.txt', 'w')

text01 = soup.find('div', class_='stContainer')

print(text01.get_text().strip(), file=f)

f.close()
# 합격자소서 크롤링 