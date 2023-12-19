import pandas as pd

# CSV 파일들 읽기
anal_html_text_path = "/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/anal_prep.csv"
assay_text_preprocessing_path = "/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/assay_prep.csv"
trend_text_preprocessing_path = "/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/trend_prep.csv"

# CSV 파일들을 데이터프레임으로 읽기
anal_html_text_df = pd.read_csv(anal_html_text_path)
assay_text_preprocessing_df = pd.read_csv(assay_text_preprocessing_path)
trend_text_preprocessing_df = pd.read_csv(trend_text_preprocessing_path)

# 필요한 컬럼 선택 및 컬럼명 변경
anal_html_text_df.rename(columns={"Anal_text": "Contents"}, inplace=True)
assay_text_preprocessing_df.rename(columns={"Assay_text": "Contents"}, inplace=True)
trend_text_preprocessing_df.rename(columns={"Trend_text": "Contents"}, inplace=True)

# Company 컬럼을 유지하면서 Contents 컬럼만 있는 새로운 데이터프레임 생성
merged_df = pd.concat([anal_html_text_df[['Company', 'Contents']],
                       assay_text_preprocessing_df[['Company', 'Contents']],
                       trend_text_preprocessing_df[['Company', 'Contents']]])

# CSV 파일로 저장
merged_csv_path = "/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/output/crawl_merged_data.csv"
merged_df.to_csv(merged_csv_path, index=False)

print("데이터를 성공적으로 병합하여 저장했습니다.")
