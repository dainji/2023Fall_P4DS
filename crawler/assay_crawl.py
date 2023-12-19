from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


# 자소서 html url 가져오는 코드
def get_assay_html_url(url):
    driver = webdriver.Safari()
    # Safari 드라이버를 이용하여 주어진 URL의 웹 페이지에 접속
    driver.get(url)
    # 웹 페이지의 HTML 내용을 가져오기
    html_content = driver.page_source
    # BeautifulSoup을 사용하여 HTML을 파싱
    soup = BeautifulSoup(html_content, 'html.parser')
    # 드라이버 종료
    driver.quit()
    # 파싱된 HTML을 반환
    return soup


# 자소서 URL을 추출하는 함수
def assay_extract_url(soup):
    # class가 'assay'인 <li> 태그들을 찾기
    assay_tags = soup.find_all('li', class_='assay')
    # 자소서의 URL을 저장할 리스트 초기화
    href_list = []
    # 각 <li> 태그에서 <a> 태그를 찾아 URL 추출
    for tag in assay_tags:
        a_tag = tag.find('a')
        if a_tag and 'href' in a_tag.attrs:
            href = a_tag['href']
            href_list.append(href)
    # 자소서 URL을 담은 리스트를 반환
    return href_list


# 마지막 페이지 번호를 가져오는 함수
def get_last_page_number(soup):
    # class가 'tplPagination'인 <div> 태그 찾기
    pagination_div = soup.find('div', class_='tplPagination')
    # <div> 태그 내부의 <ul> 태그 찾기
    if pagination_div:
        # <ul> 태그 내부의 <li> 태그들 찾기
        ul_tag = pagination_div.find('ul')
        if ul_tag:
            # <li> 태그의 개수가 페이지 번호의 마지막 숫자
            li_tags = ul_tag.find_all('li')
            last_page_number = len(li_tags)
            # 마지막 페이지 번호를 반환
            return last_page_number


# 자소서 HTML을 가져오는 함수
def get_assay_html(href):
    # Safari 드라이버를 이용하여 주어진 URL의 웹 페이지에 접속
    driver = webdriver.Safari()
    driver.get(href)
    # 웹 페이지의 HTML 내용을 가져오기
    html_content = driver.page_source
    # BeautifulSoup을 사용하여 HTML을 파싱
    soup = BeautifulSoup(html_content, 'html.parser')
    # 드라이버 종료
    driver.quit()
    # 파싱된 HTML을 반환
    return soup


# 각 기업의 정보 페이지 번호와 이름 설정
# 합격자소서 url에 나와있는 기업 고유 id 번호
enterprises = {
    '우아한 형제들': 1450187,
    '네이버': 1402025,
    '라인': 1435513,
    '쿠팡': 1532033,
    '카카오': 1976007
}

# 기업 정보와 자소서 데이터를 저장할 리스트 초기화
data = []
#기업을 돌면서 기업의 페이지 번호 가져오기
for enter in enterprises:
    last_page_number = get_last_page_number(get_assay_html_url(
        f'https://www.jobkorea.co.kr/company/{enterprises[enter]}/PassAssay?C_IDX=215&Part_Code=0&Search_Order=1&Part_Btn_Stat=0&Page=1'))
    print(enter, last_page_number)
    #기업별 합격자소서 url 가져오기
    for p in range(1, last_page_number + 1):
        url = f'https://www.jobkorea.co.kr/company/{enterprises[enter]}/PassAssay?C_IDX=215&Part_Code=0&Search_Order=1&Part_Btn_Stat=0&Page={p}'
        parsed_html = get_assay_html_url(url)
        href_list = assay_extract_url(parsed_html)

        # URL 앞에 'https://www.jobkorea.co.kr'을 붙여준다.
        href_list = [f'https://www.jobkorea.co.kr{href}' for href in href_list]

        #url을 돌면서 html 가져오기
        for href in href_list:
            # 자소서 페이지의 HTML을 파싱
            assay_html = get_assay_html_url(href)
            # 자소서 텍스트 추출
            texts = get_assay_html(href)
            # 데이터에 추가
            data.append({'Company': enter, 'Assay_html': texts})

# 데이터프레임 생성
df = pd.DataFrame(data)
# CSV 파일로 저장
df.to_csv('/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/assay_html.csv', index=False)