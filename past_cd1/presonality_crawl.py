import requests
from bs4 import BeautifulSoup
import sys

response = requests.get('https://www.jobkorea.co.kr/starter/review/view?C_Idx=377&Ctgr_Code=2&FavorCo_Stat=0&G_ID=0&Page=1')
soup = BeautifulSoup(response.text, 'html.parser')

f = open('intel1.txt', 'w')

text01 = soup.find('dd', class_='show')
text02 = soup.find('span', class_='tx')

for dd in soup.find('dd', class_='show'):
    print(text01, file=f)

for span in soup.find('span', class_='tx'):
    print(text02, file=f)

f.close()

#인적성 후기 크롤링

import requests
from bs4 import BeautifulSoup
import sys

response = requests.get('https://www.jobkorea.co.kr/starter/review/view?C_Idx=489&Ctgr_Code=3&FavorCo_Stat=0&schTxt=%EA%B5%90%EB%B3%B4%EB%AC%B8%EA%B3%A0&G_ID=0&Page=1')
soup = BeautifulSoup(response.text, 'html.parser')

f = open('intel1.txt', 'w')

text01 = soup.find('div', class_='reviewQnaWrap')
print(text01.get_text().strip(), file=f)

f.close()

#인적성후기 크롤링 수정본

import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.jobkorea.co.kr/starter/review/view?C_Idx=2270&Ctgr_Code=2&FavorCo_Stat=0&schTxt=%EB%84%A5%EC%8A%A8%EB%84%A4%ED%8A%B8%EC%9B%8D%EC%8A%A4&G_ID=0&Page=1')

soup = BeautifulSoup(response.text, 'html.parser')

f = open('intel2.txt', 'w')

text01 = soup.find('div', class_='stContainer')

print(text01.get_text().strip(), file=f)

f.close()

#인적성후기 크롤링 최종수정본