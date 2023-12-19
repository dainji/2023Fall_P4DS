import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.jobkorea.co.kr/starter/companyreport/view?Inside_No=19389&schCtgr=101012&schGrpCtgr=101&schTxt=%EA%B5%90%EB%B3%B4%EB%AC%B8%EA%B3%A0&Page=1')

soup = BeautifulSoup(response.text, 'html.parser')

f = open('stdout2.txt', 'w')

for p in soup.select('p'):
    print(p.text, file=f)

f.close()

#기업정보 보고서,트렌드 보고서 크롤링