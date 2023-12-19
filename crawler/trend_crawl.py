from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


# 셀레니움으로 파싱하면 시간이 오래걸리기 때문에 html 소스만 가져오기
def get_trend_html(url):
    # Safari 드라이버를 이용하여 웹 페이지에 접속
    driver = webdriver.Safari()
    driver.get(url)

    # 현재 페이지의 HTML 내용을 가져오기
    # BeautifulSoup을 사용하여 HTML을 파싱
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    driver.quit()  # 작업이 끝나면 드라이버 종료

    # 파싱된 HTML을 반환
    return soup


# html에서 텍스트만 추출하기
#br 태그를 기준으로 텍스트가 존재하는 것을 파악
def trend_extract_text(soup):
    br_tags = soup.find_all('br')  # 모든 <br> 태그 찾기
    # 추출된 텍스트를 저장할 리스트 초기화
    text_br_tag = []
    # 모든 <br> 태그에 대해 반복
    for br in br_tags:
        next_s = br.nextSibling  # 다음 sibling 탐색
        # 텍스트 추출 후 공백 제거
        if next_s and hasattr(next_s, 'strip') and callable(getattr(next_s, 'strip')):
            text = next_s.strip()
            # 추출된 텍스트가 비어있지 않은 경우 리스트에 추가
            if text:
                text_br_tag.append(text)

    # 추출된 텍스트 리스트 반환
    return text_br_tag


# 각 기업의 정보 페이지 번호와 이름 설정
# 기업 트렌드 보고서 url에 나와있는 기업 고유 id 번호
enterprises = {
    '우아한 형제들': 15982,
    '네이버': 11459,
    '라인': 12317,
    '쿠팡': 18350,
    '카카오': 12807
}

data = []

# 각 기업 번호를 변경해가며 기업트렌드보고서 텍스트 추출
for enter in enterprises:
    url = f'https://www.jobkorea.co.kr/starter/companyreport/view?Inside_No={enterprises[enter]}&schCtgr=101012&schGrpCtgr=101&schTxt=%EA%B5%90%EB%B3%B4%EB%AC%B8%EA%B3%A0&Page=1'
    parsed_html = get_trend_html(url)

    text_between_br = trend_extract_text(parsed_html)
    data.append({'Company': enter, 'Trend_text': '\n'.join(text_between_br)})  # 각 기업의 텍스트를 리스트에 추가

# 데이터프레임 생성
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv('/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/trend_html_text.csv', index=False)
