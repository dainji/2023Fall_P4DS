# 2023Fall_P4DS
# 취업포털 사이트 합불 예측 서비스 🐚

이 프로젝트는 2022년에 기획 된 프로젝트이며, 코로나 사태로 인해 취업난을 겪고 있는 취업 준비생들의 어려움을 덜어주고자 취업 합격 예측 및 피드백 제공 서비스를 실시하였습니다.
자세한 프로젝트는 내용은 아래 참조한 링크를 확인해주세요.

[https://www.notion.so/Capstone-Design-1-f8600d9ba28a43658a6a7a7270467aaf?pvs=4](https://www.notion.so/Capstone-Design-1-f8600d9ba28a43658a6a7a7270467aaf?pvs=21)

---

# 목차
[1. 개요](#개요)
[2. 프로젝트 폴더 설명](#프로젝트-폴더-설명)
[3. 기존 코드 대비 발전한 점](#기존-코드-대비-발전한-점)
[4. 버전 및 업데이트 정보](#버전-및-업데이트-정보)
[5. 주의 사항](#주의-사항)
[6. 참고 사항](#참고-사항)
[7. 향후 계획](#향후-계획)


## 개요


프로젝트명: 취업포털 사이트 합불 예측 서비스

프로젝트 기간: 2022.09 - 2023. 12

개발 엔진 및 언어: Python 

멤버: 지다인, 이다검, 한채원

---

## 프로젝트 폴더 설명


- crawler
    - 본 프로젝트에 사용하기 위하여 잡코리아 데이터 크롤링 진행
    - 잡코리아 사이트에서 제공하는 데이터인 기업분석보고서, 기업트렌드보고서, 합격자소서로 총 3분야의 데이터 활용
    - 기업은 네이버, 카카오, 라인, 쿠팡, 배달의민족(우아한형제들)의 데이터를 활용하여 진행
    - 기업분석보고서는 enterprises_anal_crawl.py
    - 기업트렌드보고서는 trend_crawl.py
    - 합격자소서는 assay_crawl.py
- prep
    - 앞서 수집한 크롤링 데이터는 불필요한 텍스트들이 섞여 있어 정제가 필요
    - 각 csv의 특성에 맞게 코드 작성하여 진행하였음
    - 기업분석보고서는 anal_prep.py
    - 기업트렌드보고서는 trend_prep.py
    - 합격자소서는 assay_prep.py
- modeling
    - 지원자에게 각 기업별 합격 확률을 제공하기 위해 토큰화 및 임베딩 진행
    - 또한, 지원자에게 각 기업에서 중요시 여기는 5가지 특징에 대해 본인 역량을 레이더 차트로 표기하여 역량 채울 수 있는 방법을 제공
- run
    - 앞서 전처리된 데이터들을 한 csv로 merge하기 위함
    - anal_prep.csv, trend_prep.csv, assay_prep.csv를 merge하여 crawl_merged_data.csv
- past_cd1
    - 기존 2022년에 실행하였던 코드를 넣어둔 폴더
    - 기업분석보고서, 기업트렌드보고서, 면접질문, 면접후기, 인적성검사결과 등의 분야의 데이터를 크롤링하는 코드
    - 전처리는 수기로 진행하여 코드가 따로 존재하지 않음
    - 모델링까지 이뤄지지 않아 크롤링 코드만 존재
---

## 기존 코드 대비 발전한 점

- 기존 코드의 경우 크롤링 시 for문을 돌지 않고 일일이 url을 기입하여 진행했음
    - 현재는 for문을 활용하여 기업 리스트와 페이지, 리스트를 돌고 있음
    - 또한, csv로 한 번에 저장
- 전처리를 수기로 진행
    - 현재는 인덱스값과 rule을 기반하여 코드를 작성하고 빠르게 전처리 진행
- 모델링 진행하지 않음
    - 현재는 지원자의 합격 예측 확률 벡터값을 출력하기 위해 토큰화 및 임베딩 진행하여 출력
    - 또한, 각 기업별 주요 포인트 5가지를 출력하여 지원자의 레이더 차트를 그려 부족한 부분을 시각화로 제공

---

## 버전 및 업데이트 정보

- Matplotlib 버전: 3.7.1
- KoNLPy 버전: 0.6.0
- Numpy 버전: 1.23.5
- Scikit-learn 버전: 1.2.2
- Pandas 버전: 1.5.3
- beautifulsoup4 버전: 4.12.2
- selenium 버전: 4.12.0

---

## 주의 사항

- konlpy 코랩에서 사용 시 설치 필수
- matplotlib 사용 시 한글 깨질 수 있어 반드시 아래와 같은 코드 설치 필수
    
    ```python
    !sudo apt-get install -y fonts-nanum
    !sudo fc-cache -fv
    !rm ~/.cache/matplotlib -rf
    ```
    
    ### **반드시 설치 후 세션 다시 시작 하기 (시작하지 않을 경우 한글 오류 발생할 수 있음)**
    
- mac 유저가 아닌 경우 driver 설정 필요
    - chrome driver 참고 사항 확인
    - https://chromedriver.chromium.org/downloads
---

## 참고사항


실제 모델의 예측과 예측 피드백을 살펴보기 위해 삼성전자에 근무하는 합격자의 지원서로 실행하였고 이 지원서는 output/new_resume.csv에 저장되어 있음

---

## 향후 계획


- 현재 기업을 제한하여 5개의 기업에 대해서 만 예측과 피드백을 제공하였음
    - 향후 다양한 기업들을 추가하여 더 많은 기업 정보들을 취업준비생들에게 제공해주고자 함
- 기업 모집 분야와 년도에 관계없이 각 기업의 특징을 보았음
    - 향후에 기업 모집 분야와 년도를 구별하여 분야에 맞는 더 적절한 피드백을 제공해주고자 함
---
