# 날씨에 따른 매개 감염병 확산 예측

- 프로젝트 기간 : 2019/07/01 ~ 2019/07/22
- 2019년 기상청 빅데이터 콘테스트 공모전 참가

<br/>



## 주제 선정 이유

- 기상 기후에 따른 다양한 감염병 발생
  - 말라리아, 쯔쯔가무시, SFTS(중증 열성 혈소판 감소 증후군) 등
- 질병관리 본부의 감염병 관리 시스템 효율성 증대
  - 사전 경보 시스템 구축 및 대책 마련
- 치료 및 대규모 감염 확산의 골든 타임의 중요성
  - 확산 시간 증가시 감염자 수 증폭
- 대규모 감염과 확산 방지 및 치료에 따른 사회적 비용 발생
  - 치료제, 예방 백신, 감시체제 유지 비용 등
- 기상기후와 매개체를 통한 감염병의 상관관계 분석
- 감염병을 옮기는 매개체(모기, 진드기, 쥐 등)의 생태계 특징을 파악하여 기상기후 변화에 증식 지역 예측
  - 감염병 발병시 확산 지역 예측
- 국가 바역체계 효율성 극대화

<br/>



## 감염 매개체별 특징
#### [ 모기 ]
<img src="https://user-images.githubusercontent.com/52812181/78764939-3b13ef80-79c2-11ea-9004-261bb6cae7f6.png" width="600" height="350">  

1. 감염 매개체
   
   - 중국얼룩날개모기, 잿빛얼룩날개모기, 레스터얼룩날개모기, 클레인얼룩날개모기, 벨렌얼룩날개모기, 가중국얼룩날개모기 등
2. 병명 : 삼일열말라리아, 내륙성 브르기아 사상충증 등

3. 숙주 : 사람, 동물

4. 서식 환경

   - 논과 관개수로, 미나리꽝, 호수, 연못, 웅덩이, 늪지, 강가, 고인 물 등

     ![image](https://user-images.githubusercontent.com/52812181/78765522-1704de00-79c3-11ea-967b-f0966740d3db.png)

5. 전파 경로

   - 말라리아 원충에 감염된 매개 모기를 통해 전파
   - 드물게 수혈, 주사기 공동 사용 등에 의하여 감염

6. 발병 시기

   - 5 ~ 10월 집중 발생

   - 단기 잠복기(12~18일), 장기 잠복기(6~12개월) 후 발현

     ![image](https://user-images.githubusercontent.com/52812181/78765679-49aed680-79c3-11ea-9c9b-8e8770131bf7.png)

7. 얼룩날개모기 생태적 특성
   - 계절적 소장 : 이른 봄 ~ 가을, 7월 초,중순에 최고치
   - 분포 : 전국적으로 고루 분포하면서 다른 종에 비해 높은 개체군 밀도를 보임
   - 유충 : 논, 관개수로, 늪, 개울, 빗물 고인 웅덩이, 자동차 바큇자국에 고인 물 등
   - 흡혈 습성 : 주로 동물기호성으로 소, 말, 돼지 등 가축, 사람
   - 활동시간 : 야간을 통해 흡혈 활동하며 밤 2~4시에 정점
   - 흡혈 후 휴식 : 원칙적으로 옥외 휴식습성, 기후에 따라 옥내(특히 축사 내)
   - 월동 : 두터운 갈대, 억새, 수풀, 볏짚단 등에서 성충으로 월동
   - 월동기간 : 보통 10월부터 4월이며, 대부분 2~3월 중 (단, 온도가 높은 날이 많은 경우)
   - 월동 후 활동 : 월동에서 깨어나온 초기에는 밤 기온이 낮기 때문에 상당기간 낮에 흡혈 활동



<br/>

#### [ 살인진드기 ]

1. 감염매개체

   - 작은소참진드기, 개피참진드기, 뭉뚝참진드기, 일본참진드기 등

2. 병명 : SFTS(중증 열성 혈소판 감소 증후군)

3. 숙주 : 사람, 동물 등 포유류, 조류, 파충류

4. 서식 환경 : 수풀, 잔디밭, 야행동물 털 등

   ![image](https://user-images.githubusercontent.com/52812181/78766390-2afd0f80-79c4-11ea-94d1-b6f7a92649bb.png)

5. 전파 경로

   - SFTS에 감염된 매개 진드기를 통해 전파
   - 환자의 혈액 및 체액 노출에 따른 전파 가능성 존재

6. 발병 시기 : 6~10월 집중 발생, 1~2주의 잠복기(6~14일)

   ![image](https://user-images.githubusercontent.com/52812181/78766546-5bdd4480-79c4-11ea-9955-f529244ad979.png)



<br/>



## 감염 매개체 별 감염 지역

- 말라리아 확진 환자 현황

  <img src="https://user-images.githubusercontent.com/52812181/78766870-cf7f5180-79c4-11ea-84cf-67d0d7216cf3.png" width="400" height="500">

- SFTS 확진 환자 현황

  <img src="https://user-images.githubusercontent.com/52812181/78766958-efaf1080-79c4-11ea-9976-5394077aeb6d.png" width="500" height="500">

<br/>



## 기후 변화에 따른 감염병

![image](https://user-images.githubusercontent.com/52812181/78767257-52a0a780-79c5-11ea-9fbc-772a37c66b55.png)



<br/>



## 감염병의 확산

![image](https://user-images.githubusercontent.com/52812181/78767334-6e0bb280-79c5-11ea-98d9-7e1306b409c2.png)

![image](https://user-images.githubusercontent.com/52812181/78767510-a612f580-79c5-11ea-9e2c-1b0e512d6b35.png)



<br/>



## 분석 근거

- 과거 수많은 연구원들에 의하여 기상 기후에 따른 감염병 발생에 대한 연구가 진행되어 왔음
  - 국내 기후변화 관련 감염병과 기상요인간의 상관성
    - 아주대학교 의과대학 예방의학교실
  - 기온과 지역특성이 말라리아 발생에 미치는 영향
    - 한국보건사회연구원(연구보고서 2008-24-4)
  - 기후변화에 따른 매개체 전염병 관리 대책 수립
    - 학술연구용역사업 최종결과보고서(2008-E00180-00) 순천향대학교

- 매개체에 의한 감염병은 기상기후(온도, 습도, 강수량 등)에 따른 영향이 밀접하다는 연구결과가 입증되었음

![image](https://user-images.githubusercontent.com/52812181/78771161-acf03700-79ca-11ea-8906-6d436b1e1696.png)



<br/>

## 데이터 설명

- 수집 데이터 기간 : 2012/01/01 ~ 2018/12/30
- 종관 관측 기상 데이터
  - 기온
  - 습도
  - 강수량
  - 풍속
  - 적설량
- 감염병 발병률
  - 전국 시도 별, 감염병 별 발생 비율

<br/>



## 사용 프로그램

- Python : 데이터 크롤링 및 전처리 & 분석 및 시각화
- R : 데이터 분석

<br/>



## 데이터 크롤링

- Selenium을 이용한 감염병 발병률 데이터 crawling
  - 자동화 순서
    1. 감염병명 선택 : 군
    2. 감염병명 선택 : 병명
    3. 발병률 체크박스 클릭
    4. 설정한 날짜부터 7일 단위로 크롤링 시작
  - 자동화 종료 후 csv file로 저장
- [Source 바로가기](https://github.com/dustinkim86/MyProjects/blob/master/%EB%82%A0%EC%94%A8%EC%97%90%20%EB%94%B0%EB%A5%B8%20%EB%A7%A4%EA%B0%9C%20%EA%B0%90%EC%97%BC%EB%B3%91%20%ED%99%95%EC%82%B0%20%EC%98%88%EC%B8%A1/Scripts/incidence_rate_selenium.py)

<br/>



## 데이터 전처리

1. 날씨 Dataset은 감염병 Dataset과 다르게 지역별이 아닌 관측소별로 나누어져 있어 지역별로 통합

2. 날씨 Dataset은 일별 데이터이지만 감염병 Dataset은 주별 데이터이므로 날씨 Dataset을 주별로 변경(평균)

3. 감염병 Dataset과 날씨 Dataset 통합

- [Source 바로가기](https://github.com/dustinkim86/MyProjects/blob/master/%EB%82%A0%EC%94%A8%EC%97%90%20%EB%94%B0%EB%A5%B8%20%EB%A7%A4%EA%B0%9C%20%EA%B0%90%EC%97%BC%EB%B3%91%20%ED%99%95%EC%82%B0%20%EC%98%88%EC%B8%A1/Scripts/for_tot_weather_disease.py)

<br/>



## 데이터 시각화

- 전국 발병률 추이

  ![전국발병률추이](https://user-images.githubusercontent.com/52812181/78795371-ec7d4a00-79ef-11ea-8940-81c3526bb199.png)


- 서울 / 강원 발병률 추이

  ![서울강원발병률추이](https://user-images.githubusercontent.com/52812181/78795581-20f10600-79f0-11ea-858e-864488953261.png)

- 지역별 발병률 평균 비교

  ![지역별발병률평균비교](https://user-images.githubusercontent.com/52812181/78795648-3108e580-79f0-11ea-811c-7b10a894952f.png)
  
  
    - 발병률 추이 및 평균 비교 [Source 바로가기](https://github.com/dustinkim86/MyProjects/blob/master/%EB%82%A0%EC%94%A8%EC%97%90%20%EB%94%B0%EB%A5%B8%20%EB%A7%A4%EA%B0%9C%20%EA%B0%90%EC%97%BC%EB%B3%91%20%ED%99%95%EC%82%B0%20%EC%98%88%EC%B8%A1/Scripts/EDA.py)

<br/>


- 서울 기상기후 변수 중요도 in python

  ![기상기후변수중요도](https://user-images.githubusercontent.com/52812181/78851334-81199380-7a54-11ea-8f4d-df21931d79a6.png)
  
  
    - [Source 바로가기](https://github.com/dustinkim86/MyProjects/blob/master/%EB%82%A0%EC%94%A8%EC%97%90%20%EB%94%B0%EB%A5%B8%20%EB%A7%A4%EA%B0%9C%20%EA%B0%90%EC%97%BC%EB%B3%91%20%ED%99%95%EC%82%B0%20%EC%98%88%EC%B8%A1/Scripts/x_importance.py)

- 변수 상관관계 분석(Random Forest) in r

  - 말라리아 / 쯔쯔가무시증 / SFTS

    ![[image]](https://user-images.githubusercontent.com/52812181/78870529-3c582180-7a81-11ea-93ab-b9746d09f6fc.png)

  - [Source 바로가기](https://github.com/dustinkim86/MyProjects/blob/master/%EB%82%A0%EC%94%A8%EC%97%90%20%EB%94%B0%EB%A5%B8%20%EB%A7%A4%EA%B0%9C%20%EA%B0%90%EC%97%BC%EB%B3%91%20%ED%99%95%EC%82%B0%20%EC%98%88%EC%B8%A1/Scripts/randomforest.R)

<br/>



## 분석 개요

- Keras를 이용한 시계열 분석

  1. GRU와 LSTM 비교
2. Optimizer 비교 : Adam, AdaDelta, RMSprop
     1. 날씨 API를 이용한 향후(D+2일 까지) 지역 감염병 발병률 예측 / 시각화

<br/>



## 분석 결과

#### GRU

- Optimizer : *Adam*

  ![image](https://user-images.githubusercontent.com/52812181/78904183-22d1cc80-7ab7-11ea-8ad3-41731f7d75d5.png)

- Optimizer : *AdaDelta*

  ![image](https://user-images.githubusercontent.com/52812181/78904251-354c0600-7ab7-11ea-8717-cc8af58d55d4.png)

- Optimizer : RMSprop

  ![image](https://user-images.githubusercontent.com/52812181/78904329-4bf25d00-7ab7-11ea-9eae-3ab2094bafbc.png)

#### LSTM

- Optimizer : Adam

  ![image](https://user-images.githubusercontent.com/52812181/78904401-6f1d0c80-7ab7-11ea-9fab-79676c961a88.png)

- Optimizer : AdaDelta

  ![image](https://user-images.githubusercontent.com/52812181/78904451-81974600-7ab7-11ea-84e0-9b31b641791f.png)

- Optimizer : RMSprop

  ![image](https://user-images.githubusercontent.com/52812181/78904498-98d63380-7ab7-11ea-9f27-43b86c7746e2.png)

- [GRU Source 바로가기](https://github.com/dustinkim86/MyProjects/blob/master/%EB%82%A0%EC%94%A8%EC%97%90%20%EB%94%B0%EB%A5%B8%20%EB%A7%A4%EA%B0%9C%20%EA%B0%90%EC%97%BC%EB%B3%91%20%ED%99%95%EC%82%B0%20%EC%98%88%EC%B8%A1/Scripts/GRU.py)

- [LSTM Source 바로가기](https://github.com/dustinkim86/MyProjects/blob/master/%EB%82%A0%EC%94%A8%EC%97%90%20%EB%94%B0%EB%A5%B8%20%EB%A7%A4%EA%B0%9C%20%EA%B0%90%EC%97%BC%EB%B3%91%20%ED%99%95%EC%82%B0%20%EC%98%88%EC%B8%A1/Scripts/LSTM.py)

<br/>



## 결론 및 한계점

- Optimizer의 경우 RMSprop가 Adam이나 AdaDelta에 비해 높은 적중률을 보였으며, GRU와 LSTM의 차이는 거의 없었음

- 발병일 ~ +2일 확산지역 확률 결과

  ![image](https://user-images.githubusercontent.com/52812181/78905298-bbb51780-7ab8-11ea-812f-54ce0d71d3f4.png)

  - 타 지역은 감소세에 이를 것으로 예측되나 충남과 경남의 경우 그 경우가 덜한 것으로 나타남

- [Source 바로가기](https://github.com/dustinkim86/MyProjects/blob/14085250970e2218fd14f87a8100d9f4c15af3a7/%EB%82%A0%EC%94%A8%EC%97%90%20%EB%94%B0%EB%A5%B8%20%EB%A7%A4%EA%B0%9C%20%EA%B0%90%EC%97%BC%EB%B3%91%20%ED%99%95%EC%82%B0%20%EC%98%88%EC%B8%A1/Scripts/GRU.py#L452)

<br/>



## 사업성 / 활용 방안

- 활용 방안

  - 감염병 및 방역 관리 대책 수립의 기초자료로 활용
  - 대국민 감염지역 주의 문자 알림 서비스
  - 날씨와 다양한 빅데이터를 활용하여 가축 전염병 확산 지역 예측 서비스
  - 해외 유입 감염병 확산 지역 예측

- 사업성

  - 감염병 예방관리 강화
  - 감염병 R&D 사업 추진
  - 감염병 관리 체계 구축에 필요한 예산 절감
  - 국가 방역 체계 및 감염병 관리 사업에 필요한 시스템

- 확장성

  - 지구 온난화에 따른 전염병이 확산되고, 한반도의 기후가 열대기후화 됨으로써 열대 기후에서 발병하는 지카, 에볼라 등 새로운 전염병이 유입되어 확산될 가능성이 높아짐
  - 따라서, **새로운 감염병의 확산을 예측할 수 있는 시스템**의 필요가 절대적

  ![image](https://user-images.githubusercontent.com/52812181/78906623-8c070f00-7aba-11ea-926c-da3ff1b6504b.png)

  ![image](https://user-images.githubusercontent.com/52812181/78906691-a214cf80-7aba-11ea-8cf2-1b2cd52e7e02.png)

<br/>



## 참고 문헌

- 감염병의 예방 및 관리에 관한 기본계획(2013~2017) - 보건복지부, 질병관리본부
- 기온과 지역특성이 말라리아 발생에 미치는 영향 - 한국보건사회연구원
- 기후변화에 따른 매개체 전염병 관리 대책 수립 - 학술연구용역사업 최종 결과 보고서(2008-E00180-00) 순천향대학교
- 말라리아 우선방역 후보지 선정을 위한 GIS 활용 빅데이터 분석 결과 - 김포시 정보통신과
- 감염병 관리 사업 지침(2016, 2018) - 보건복지부, 질병관리본부
- 한국의 사회동향 2016(11-1240245-000014-10) - 통계청 통계개발원
- 감염병 매개체의 분류 및 생태 - 국립고건연구원 질병매개곤충과
