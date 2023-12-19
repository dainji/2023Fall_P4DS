import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.jobkorea.co.kr/starter/review/view?C_Idx=489&Ctgr_Code=3&FavorCo_Stat=0&schTxt=%EA%B5%90%EB%B3%B4%EB%AC%B8%EA%B3%A0&G_ID=0&Page=1')
soup = BeautifulSoup(response.text, 'html.parser')

f = open('review1.txt', 'w')

text01 = soup.find('dl', class_='qnaLists')
print(text01.get_text().strip(), file=f)

f.close()

#면접후기 크롤링


import requests
from bs4 import BeautifulSoup
import sys

response = requests.get('https://www.jobkorea.co.kr/starter/review/view?C_Idx=489&Ctgr_Code=3&FavorCo_Stat=0&schTxt=%EA%B5%90%EB%B3%B4%EB%AC%B8%EA%B3%A0&G_ID=0&Page=1')
soup = BeautifulSoup(response.text, 'html.parser')

f = open('review1.txt', 'w')

text01 = soup.find('div', class_='reviewQnaWrap')
print(text01.get_text().strip(), file=f)

f.close()

#면접후기 크롤링 수정본

import requests
from bs4 import BeautifulSoup
import sys

response = requests.get('https://www.jobkorea.co.kr/starter/review/view?C_Idx=489&Half_Year_Type_Code=0&Ctgr_Code=3&FavorCo_Stat=0&schTxt=%EA%B5%90%EB%B3%B4%EB%AC%B8%EA%B3%A0&G_ID=0&Page=1')
soup = BeautifulSoup(response.text, 'html.parser')

f = open('review1.txt', 'w')

text01 = soup.find('div', class_='stContainer')
print(text01.get_text().strip(), file=f)

f.close()

#면접후기 크롤링 최종 수정본