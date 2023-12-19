import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/anal_html_text.csv')

# 각 기업의 Trend 컬럼의 9번째 원소까지 삭제
df['Anal_text'] = df['Anal_text'].apply(lambda x: '\n'.join(x.split('\n')[9:]))

# 수정된 데이터프레임을 새로운 CSV 파일로 저장
df.to_csv('/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/anal_prep.csv', index=False)
