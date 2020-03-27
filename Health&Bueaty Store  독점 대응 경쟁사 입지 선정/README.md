# Health&Bueaty Store  독점 대응 경쟁사 입지 선정

- 프로젝트 기간 : 2020/01/21 ~ 2020/01/24
- 지역은 서울시에 한함

<br/>



## 분석 배경

#### 1. 국내 H&B 스토어시장 규모

- **H&B 스토어 시장은 점점 확대되어 가고 있음**  

<img src="https://user-images.githubusercontent.com/52812181/77737606-ab7d5100-7051-11ea-8ccd-f27e8944ba73.png" width="400" height="450">

#### 2. 국내 H&B 스토어 매장 수

- **CJ의 올리브영의 H&B Store 업계 독보적인 1위**  

<img src="https://user-images.githubusercontent.com/52812181/77737882-2c3c4d00-7052-11ea-932e-8cda5730e72c.png" width="400" height="250">

#### 3. H&B 스토어브랜드 이용 및 인지도

- **올리브영의 압도적인 이용률에 비해 인지도는 비교적 차이가 적음**  

<img src="https://user-images.githubusercontent.com/52812181/77738137-a40a7780-7052-11ea-9414-16f852bdab28.png" width="600" height="350">

#### 4. H&B 스토어 이용 관련 리포트

- 이용 목적

<img src="https://user-images.githubusercontent.com/52812181/77739110-51ca5600-7054-11ea-8a7a-b8025060c3c4.png" width="420" height="350" display="inline">

- 브랜드별 이용 이유

<img src="https://user-images.githubusercontent.com/52812181/77739232-83432180-7054-11ea-834a-3ea864b4cf98.png" width="620" height="350" display="inline">

- 제품 계획 구매 여부

<img src="https://user-images.githubusercontent.com/52812181/77739773-7541d080-7055-11ea-8d91-805b6b6a2a7b.png" width="300" height="300">



- 성별/연령대 별 H&B 스토어 이용 비교

  ![image](https://user-images.githubusercontent.com/52812181/77768369-bd78e700-7085-11ea-8b6a-c550a4f662f3.png)



### 자료 출처 : [오픈서베이 H&B 스토어 트렌드 2019](https://github.com/dustinkim86/MyProjects/blob/master/Health%26Bueaty%20Store%20%20%EB%8F%85%EC%A0%90%20%EB%8C%80%EC%9D%91%20%EA%B2%BD%EC%9F%81%EC%82%AC%20%EC%9E%85%EC%A7%80%20%EC%84%A0%EC%A0%95/%EC%98%A4%ED%94%88%EC%84%9C%EB%B2%A0%EC%9D%B4%20h%26b%20%EC%8A%A4%ED%86%A0%EC%96%B4%ED%8A%B8%EB%A0%8C%EB%93%9C_2019.pdf)

<br/>



## 예측 결론

- 브랜드 별 매장 수의 차이는 크지만 **인지도**에는 크게 **차이가 없고**, **가까울수록** 이용하는 경우가 많기 때문에 가장 최적의 입지 위치를 분석하여 올리브영에 대응하는 솔루션을 제안할 수 있을 것으로 판단됨

<br/>



## 예측 결론에 따른 분석 목표

![image](https://user-images.githubusercontent.com/52812181/77740468-a7076700-7056-11ea-987c-eb2d8cf85665.png)

<br/>



## 데이터 설명

- 지역 특성 데이터(단위 : 행정동)
  - 총 생활인구
  - 연령별 생활인구
  - 성별 생활인구
  - 지하철역 수
  - 학교 수
  - 올리브영 매장 수
  - 롭스 매장 수
  - 랄라블라 매장 수
- 브랜드 개별 특성 데이터
  - 임대료(단위 : 행정동)
  - 블로그 텍스트마이닝(단위 : 브랜드별)
  - SNS 사진 크롤링(단위 : 브랜드별)

- **자료 : [Datasets](https://github.com/dustinkim86/MyProjects/tree/master/Health%26Bueaty%20Store%20%20%EB%8F%85%EC%A0%90%20%EB%8C%80%EC%9D%91%20%EA%B2%BD%EC%9F%81%EC%82%AC%20%EC%9E%85%EC%A7%80%20%EC%84%A0%EC%A0%95/Datasets)**

<br/>



## 사용 프로그램

- Excel : 데이터 전처리
- R : 데이터 전처리 및 분석
- Python : 이미지 크롤링 및 텍스트마이닝

<br/>



## 데이터 전처리

#### R 이용 [Source](https://github.com/dustinkim86/MyProjects/blob/master/Health%26Bueaty%20Store%20%20%EB%8F%85%EC%A0%90%20%EB%8C%80%EC%9D%91%20%EA%B2%BD%EC%9F%81%EC%82%AC%20%EC%9E%85%EC%A7%80%20%EC%84%A0%EC%A0%95/Scripts/%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A0%84%EC%B2%98%EB%A6%AC.R)

- 각 브랜드별 매장 / 학교 위치 데이터 GIS 변환 및 행정동별 갯수 Count

- 임대료 행정동별 Average

- 행정동 코드를 이용해 생활인구 데이터를 행정동별로 Merge
  - 매장 평균 운영시간에 맞춰 정제

#### Excel 이용

- 위치 데이터 행정동별 갯수 Count 데이터와 생활인구 데이터 행정동별 Merge 데이터 병합
- 올리브영 수 - (랄라블라 수 + 롭스 수) / 전체 매장 수

- 총 매장 수
- 총 생활인구 및 여성15~39세 인구
- 총 생활인구 / 총 매장 수
- id 순번

#### *전처리 후 datasets.csv로 통합*

<br/>

## 데이터 시각화

- 행정동별 생활인구

  <img src="https://user-images.githubusercontent.com/52812181/77780255-0a18ee00-7097-11ea-922b-17fc98996076.png" width="520" height="400">

- 행정동별 여성15~39세 인구

  <img src="https://user-images.githubusercontent.com/52812181/77780357-359bd880-7097-11ea-93cb-6638c434c1f0.png" width="600" height="400">

- 행정동별 지하철역 수

  <img src="https://user-images.githubusercontent.com/52812181/77780536-7e539180-7097-11ea-806b-aba19bdab517.png" width="570" height="400">

- 행정동별 학교 수

  <img src="https://user-images.githubusercontent.com/52812181/77780622-9c20f680-7097-11ea-88d4-0d0e123fc00d.png" width="570" height="400">

- 행정동별 임대료(짙은 회색의 경우 데이터가 없는 동)

  <img src="https://user-images.githubusercontent.com/52812181/77780700-c07cd300-7097-11ea-9d69-19c25651cb57.png" width="570" height="400">

<br/>



## 분석 개요

#### 1. 다중 선형회귀 : 지역적 틍성 변수 추출

- 종속변수
  - 총 매장 수
- 독립변수
  - 학교 수
  - 지하철역 수
  - 임대료
  - 총 인구 수
  - 여성 15~39세 총 인구 수

#### 2. K-means 군집 분석 : 최적의 집단 추출

- 3개의 집단 분류
  - 지역적 틍성이 잘 반영되어 경쟁사가 진입할 수 있는 최적의 행정동 집단 추출

#### 3.1 ANOVA 분산 분석 : 각 브랜드 별 평균 임대료 차이 분석 - ANOVA 검정

#### 3.2 이미지 크롤링 / 텍스트마이닝 : 각 브랜드 이미지 분석

- 추출된 집단에서 각 개별적 특성별로 경쟁사 맞춤 진입 입지 추천

<br/>



## 분석 결과

#### 1. 다중 선형회귀

- 종속 : 총 매장 수 / 독립 : 모든 변수

  - 총 생활인구와 여성15~39세 인구의 다중공선성이 의심됨

    <img src="https://user-images.githubusercontent.com/52812181/77782270-5b76ac80-709a-11ea-9525-409be722d18d.png" width="700" height="650">

  - 다중공선성 확인 : 굉장히 높은 다중공선성이 확인되어 여성15~39세 인구 변수 제외

    ![image](https://user-images.githubusercontent.com/52812181/77782678-fec7c180-709a-11ea-88e7-7ec0e0d216d4.png)

- 종속 : 총 매장 수 / 독립 : 여성15~39세 인구를 제외한 모든 변수

  <img src="https://user-images.githubusercontent.com/52812181/77782804-30d92380-709b-11ea-9627-093424ef45e5.png" wigth="700" height="650">



- **단순 선형회귀**
  
- 총 매장 수와 총 생활인구, 여성인구, 임대료 각각의 상관관계 확인
  
  ![제목 없음](https://user-images.githubusercontent.com/52812181/77783651-97ab0c80-709c-11ea-82a0-a1ff8140d407.png)
  
- 총 매장 수 대비 총 생활인구

  - 회색지역 : H&B 스토어가 없는 행정동

  - 매장이 없는 곳은 분석 범위에서 제외

    - 고려해야 할 다른 변수가 많음(청와대 부근, 서울숲, 북한산 등)

  - 총 매장 수 대비 총 생활인구가 많은 곳이 경쟁사가 들어가기 좋은 곳으로 판단

    ![image](https://user-images.githubusercontent.com/52812181/77785000-d5109980-709e-11ea-986b-b2e07ee832be.png)



#### 2. K-means 군집 분석

- 3집단으로 나누어 최적의 집단 추출
  
  - X축 : 총 매장수 대비 올리브영 매장수 = (올리브영 매장수 - 경쟁사 매장수) / 총 매장수
  
  - Y축 : 매장수 대비 인구수 = 총 생활인구 수 / 총 매장수
  
    <img src="https://user-images.githubusercontent.com/52812181/77789190-ea3cf680-70a5-11ea-9f65-f19a6ee3b1e7.png" width="600" height="500">
  
  - 적색 집단은 생활인구 대비 매장수도 많은 집단이므로 적당하지 않다고 판단되며, 흑색 집단은 생활인구 대비 매장수는 적지만 위험 리스크가 크거나 특수 지역일 가능성이 있으므로 **녹색 집단이 가장 입지가 좋을 것으로 판단됨**
  
    - 녹색 집단 행정동
  
      ![제목 없음](https://user-images.githubusercontent.com/52812181/77789355-35efa000-70a6-11ea-982e-0476df882488.png)



#### 3.1. ANOVA 분산 분석

- 등분산 검정

  - 검정 결과 p-value가 0.05보다 크므로 귀무가설 채택, 임대료와 집단분류는 등분산성을 띄고 있음

    <img src="https://user-images.githubusercontent.com/52812181/77790437-36893600-70a8-11ea-8a9a-66e7c2a364e9.png" width="600" height="150">

- Oneway ANOVA

  - 임대료는 집단분류에 대해 평균의 차이가 통계적으로 유의하나, 높은 상관성을 띄지는 않음

    <img src="https://user-images.githubusercontent.com/52812181/77793868-3855f800-70ae-11ea-8c58-935093a5679a.png" width="700" height="200">

- 사후 검정
  - 1번 그룹 : 올리브영 / 2번 그룹 : 랄라블라 / 3번 그룹 : 롭스
  - 올리브영은 임대료가 가장 높은 행정동을 선호하며, 랄라블라도 비슷하나 올리브영 보다는 상대적으로 낮은 임대료를 선호한다. 롭스는 가장 임대료가 저렴한 곳을 선호

    <img src="https://user-images.githubusercontent.com/52812181/77793951-650a0f80-70ae-11ea-9e5b-b009082030fb.png" width="700" height="600">	



#### 3.2. 이미지 크롤링 / 텍스트마이닝

- 오픈서베이 트렌드 리포트의 브랜드별 이미지

  <img src="https://user-images.githubusercontent.com/52812181/77797630-bd441000-70b4-11ea-9e78-1319e86300e4.png" width="500" height="350">

- SNS 이미지 크롤링 및 블로그 텍스트마이닝 결과

  - 올리브영

    ![image](https://user-images.githubusercontent.com/52812181/77797874-2f1c5980-70b5-11ea-81e1-77a6ec5ca5f3.png)

  - 롭스
    
    ![image](https://user-images.githubusercontent.com/52812181/77797977-5f63f800-70b5-11ea-95d8-17a16674b195.png)

  - 랄라블라

    ![image](https://user-images.githubusercontent.com/52812181/77798030-799dd600-70b5-11ea-8d81-022095f4ebe5.png)

- **결과**

  - 올리브영과 롭스는 이미지가 비슷한 반면 랄라블라의 경우 붉은 컬러가 많은 여성스러운 이미지 크롤링 결과가 나옴
  - 블로그 텍스트마이닝에서는 롭스의 경우 할인에 관련한 키워드가 많이 등장하여 비교적 합리적임을 알 수 있었고, 랄라블라의 경우 뷰티방송 등의 여성들을 대상으로 한 매체와 관련이 많음을 알 수 있음



<br/>



## 결론 및 한계점

#### 1. 입지 추천

- **브랜드 이미지 -  Target 고객별**
  - 롭스 : 전체 연령 대상
    - 1순위 : 동작구 노량진1동
    - 2순위 : 관악구 대학동
    - 3순위 : 강동구 길동
  - 랄라블라 : 15~39세 여성 대상
    - 1순위 : 동작구 노량진1동
    - 2순위 : 강서구 화곡1동
    - 3순위 : 강동구 길동
- **임대료 차이에 따른 선정**
  - 롭스 : 임대료 낮은 순서
    - 1순위 : 성북구 종암동
    - 2순위 : 은평구 역촌동
    - 3순위 : 동대문구 전농1동
  - 랄라블라 : 임대료 높은 순서
    - 1순위 : 서초구 반포3동
    - 2순위 : 동작구 노량진1동
    - 3순위 : 성동구 사근동

#### 2. 분석 차별점

- 단계별로 분석기법을 도입하여 여러 특성과 변수들을 고려할 때 용이
- 지역적 특성과 브랜드의 개별적 특성을 모두 반영하여 해당 산업의 브랜드별 맞춤 분석 가능
- 분석기법이 비교적 쉽고 데이터 품질이 높아 분석을 통해 범할 오류 적음
- 특정 최적 집단을 추출 후 분석을 하여 목적에 부합하는 핀포인트 결과 도출 가능

#### 3. 분석 한계점

- 분석지역 단위를 행정동별로 고정해 실제 매장 반경의 특성을 부여한 분석결과와의 차이
- 데이터 수집하는 데 어려움으로 데이터 다양성이 떨어지고, 실제 영향을 미치는 다른 변수들이 생략될 가능성
- 해당 분석모델은 특정 이해관계자들에게 활용될 수 있어 떨어지는 범용성
- 정적인 데이터들을 반영한 기법이기 때문에 상시 변화하는 값의 변수를 고려한 결과를 반영하지 못함

<br/>



## 분석모델 활용 방안

#### 1. 다른 독점 산업 분석에 활용

- 각 산업에서 매장 수로 독점하는 브랜드 견제 전략 수립에 활용 가능

#### 2. 소상공인 창업 입지 선별시 활용

- 창업 입지 선별에 어려움이 있을 때
- 지역적, 개별적 특성을 고려하여 입지를 선정하고 싶을 때
- 창업 분야의 특성을 이해하고 싶을 때

#### 3. 행정동별 상권 특성 분석에 활용

- 매장들이 많이 밀집되어 있는 지역의 상권을 분석하고 싶을 때
- 생활인구의 특성과 상권의 특성의 관계를 보고 싶을 때

<br/>



## 참고 문헌

- 서울시 열린데이터 광장 : 생활인구, 지하철역, 학교 수
- 우리마을 가게 상권분석 서비스 : 임대료
- 각 브랜드 사이트 : 매장 위치
- 네이버 : 블로그 텍스트 데이터
- 인스타그램 : 이미지 데이터
