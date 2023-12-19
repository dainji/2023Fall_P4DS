import pandas as pd
from bs4 import BeautifulSoup

# CSV 파일 읽기
df = pd.read_csv('/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/assay_html.csv')

# HTML 소스에서 특정 요소의 텍스트 추출하는 함수
def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    target_element = soup.select_one('#company-body > section > div > section.secView > article > div.viewCont')

    if target_element:
        # 특정 태그 제외하고 텍스트 추출
        # 글자수, byte 등 내용과 무관한 내용
        for tag in target_element.find_all(class_='txSpllChk'):
            tag.extract()  # 특정 태그 제거

        return target_element.get_text(separator='\n')
    else:
        return None  # 특정 요소를 찾지 못한 경우

# Trend 컬럼의 HTML 소스를 텍스트로 변환하여 새로운 컬럼에 추가
df['Assay_text'] = df['Assay_html'].apply(extract_text_from_html)


# 새로운 컬럼을 CSV 파일로 저장
df.to_csv('/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/assay_prep.csv', index=False)
