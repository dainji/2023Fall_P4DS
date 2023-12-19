from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import sys
from urllib.parse import quote

# 추가된 코드: 프로젝트 경로를 sys.path에 추가
sys.path.append('/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/')


# 셀레니움으로 파싱하면 시간이 오래걸리기 때문에 html 소스만 가져오기
def get_anal_html(url):
    # 웹 드라이버 초기화
    driver = webdriver.Safari()
    # 주어진 URL 열기
    driver.get(url)
    # 페이지 소스코드 가져오기
    html_content = driver.page_source
    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(html_content, 'html.parser')
    # 작업이 끝나면 드라이버 종료
    driver.quit()
    # 파싱된 HTML 반환
    return soup

# HTML에서 텍스트 추출하는 함수
def anal_extract_text(soup):
    # 모든 <p> 태그 찾기
    paragraphs = soup.find_all('p')
    # 텍스트를 저장할 리스트 초기화
    texts = []

    # 모든 <p> 태그에 대해 반복
    for paragraph in paragraphs:
        # 태그에서 텍스트 추출하고 리스트에 추가
        text = paragraph.get_text(strip=True)
        texts.append(text)

    # 추출된 텍스트 리스트 출력 (디버깅 용도)
    print(texts)
    # 추출된 텍스트 리스트 반환
    return texts

# 각 기업의 정보 페이지 번호와 이름 설정
# 기업분석보고서 url에 나와있는 기업 고유 id 번호
enterprises = {
    '우아한 형제들': 15981,
    '네이버': 11458,
    '라인': 12316,
    '쿠팡': 18349,
    '카카오': 12806
}

# 데이터를 저장할 리스트 초기화
data = []

# 각 기업 번호를 변경해가며 기업분석보고서 텍스트 추출
for enter in enterprises:
    encoded_query = quote(enter)  # 기업명을 URL 인코딩
    url = f'https://www.jobkorea.co.kr/starter/companyreport/view?Inside_No={enterprises[enter]}&schCtgr=101012&schGrpCtgr=101&schTxt={encoded_query}&Page=1'
    # HTML 가져오기
    parsed_html = get_anal_html(url)

    # 텍스트 추출
    text_between_br = anal_extract_text(parsed_html)
    # 각 기업의 텍스트를 리스트에 추가
    data.append({'Company': enter, 'Anal_text': '\n'.join(text_between_br)})  # 각 기업의 텍스트를 리스트에 추가

# 데이터프레임 생성
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv('/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/anal_html_text.csv', index=False)
