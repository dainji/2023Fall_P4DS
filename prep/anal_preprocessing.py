import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('/content/anal_html_text.csv')

# 각 기업의 Trend 컬럼의 9번째 원소까지 삭제
df['Anal_html_text'] = df['Anal_html_text'].apply(lambda x: '\n'.join(x.split('\n')[9:]))

# 끝에서 -1부터 -21까지의 원소 삭제
df['Anal_html_text'] = df['Anal_html_text'].apply(lambda x: '\n'.join(x.split('\n')[:-21]))

# #으로 시작하는 원소 삭제
df['Anal_html_text'] = df['Anal_html_text'].apply(lambda x: '\n'.join([line for line in x.split('\n') if not line.startswith('#')]))

# '필진'으로 시작하는 원소 삭제
df['Anal_html_text'] = df['Anal_html_text'].apply(lambda x: '\n'.join([line for line in x.split('\n') if not line.startswith('필진ㅣ')]))



# 수정된 데이터프레임을 새로운 CSV 파일로 저장
df.to_csv('/content/anal_prep.csv', index=False)
