# 자소AI

![logo4](https://user-images.githubusercontent.com/45377884/84596752-805d0d80-ae9a-11ea-90a2-c40c06d43794.png)

자기소개서 작성 도우미 프로그램 자소AI

제작 기간 : 2020.5 ~ 2020.6.12

<br/>

## 프로젝트 시작 계기

취업 준비생 71만 시대. 취업 준비생이 자기소개서에 소비하는 시간 하루 7시간. ~

이렇게 낭비되는 시간과 자원을 아끼기 위해서 자기소개서 작성을 돕는 프로그램 기획. 마침 4월 말에 SKT에서 한국어 자연어 생성 모델인 KoGPT2 모델을 공개하였고, [gyunggyung](https://github.com/gyunggyung/KoGPT2-FineTuning) 님이 작성한 Finetuning 코드를 변형하여 활용.

<br/>

## 만들고자 하는 솔루션

자소서의 첫 부분, 혹은 키워드를 입력하면 나머지 부분을 인공지능이 작성하도록 한다. 인공지능이 작성한 여러 개의 문장 중에서 하나를 선택. 본인의 경험이 아니거나 문맥 상 어색한 부분 등 수정이 필요한 부분을 고친 뒤 자기소개서를 저장하여 관리할 수 있도록 한다. 

<br/>

## 내부 디렉토리 구조

```python
Aid_self-Introduce
┖ __pycache__
┖ kogpt2			
  ┖ __pycache__
  ┖ model
	┖ __pycache__
    ┖ __init__.py
    ┖ gpt.py
    ┖ sample.py
    ┖ torch_gpt2.py
  ┖ __init__.py 
  ┖ data.py
  ┖ mxnet_kogpt2.py
  ┖ pytorch_kogpt2.py
  ┖ utils.py
┖ static
  ┖ css
  ┖ font-awesome-4.1.0
  ┖ fonts
  ┖ img
  ┖ js
  ┖ php
┖ templates
  ┖ error.html			# 각종 에러 메세지 출력
  ┖ landing.html		# 랜딩 페이지 구성
  ┖ login.html		# 로그인 페이지 구성
  ┖ myresume.html		# '내 자소서' 페이지 구성
  ┖ resumeGen.html	# '자소서 생성' 페이지 구성
  ┖ signup.html		# '회원가입' 페이지 구성
  ┖ writeResume.html	# '자소서 작성' 페이지 구성
LICENSE
app.py		# 플라스크 실행 파일
generator.py
jupyter_generator.py
jupyter_main.py
requirements.txt	# 필요한 라이브러리 모음
```

<br/>

## 사용 언어

- Python : KoGPT2 모델 파인튜닝, 크롤링, 백엔드 프레임워크 구성 등 다양한 용도로 파이썬 사용
- HTML5 : 홈페이지 프레임 제작 (랜딩, 로그인, 회원가입, 내 자소서, 자소서 생성, 자소서 작성 페이지)
- CSS3 : 페이지 내 구성요소 디자인
- Javascript : 각종 버튼의 기능 등 동적인 페이지를 구성
- MySQL : 데이터베이스 구축 및 웹과 연동

<br/>

## 사용 프레임워크, 라이브러리 & 툴

- Bootstrap : Free HTML Template을 구한 뒤 수정하여 사용
- Flask : Back-End 프레임워크로 플라스크를 사용
- Git : 깃허브 Private Repo 를 사용하여 협업
- Notion : 일정과 업무 관리 및 멘토링 피드백 정리

<br/>

## 모델 탐색 및 파인튜닝

**모델 탐색** : 자연어 생성(Natural Language Generation, NLG) 모델 탐색. 여러 모델 중에서 NLG에서 좋은 성능을 보이고 있고 한국어 Pretrained가 되어있는 KoGPT2 모델이 4월 28일에 공개되어 사용하기로 결정



**데이터 수집과 전처리**

- **수집** : 합격자소서 약 22,000건(에듀스 약 17,000건, 사람인 약 5,000건)을 크롤링. 사람인은 `BeautifulSoup` 을 사용하였고 에듀스는 `Selenium` 을 사용하여 동적 크롤링.

- **전처리** : 정규 표현식 및 수작업(Visual Studio Code)으로 진행
  - 모든 자소서에 공통되는 부분은 정규 표현식을 사용하여 제거. 문제와 소제목은 수작업을 통해 최대한 제거. 사람마다 소제목을 표기하는 방법과 자기소개서 내용 내부에 인용문을 표기하는 방법이 달랐기 때문에 수작업으로 제거할 수 밖에 없었음. 한자는 최대한 한글로 대체
  - 프로젝트 기간이 충분하지 않아 맞춤법이나 OOO 등으로 마스킹 처리된 개인정보 부분(작성자 이름, 동아리 이름 등)을 하나하나 처리하지 못한 것이 아쉬움. 또한 형태소 분석기를 사용하여 말뭉치의 토큰 수를 조금 더 낮출 수 있지 않았을까 생각됨. (추후 발전 과제)
  - 불필요한 부분 삭제가 끝난 후에는 한 줄에 하나의 문장만 들어갈 수 있도록 최종 전처리 과정을 진행. 약 563,000 개의 문장으로 분리



**모델 학습 (Fine-Tuning)** : Google Colab Pro를 사용하여 학습하였다. gyunggyung 님의 깃허브로 부터 포크한 원래의 코드에서 data.py를 우리의 데이터에 맞게 수정하였다. 한번에 9개의 문장을 붙여 하나의 배치를 구성하게 되며 배치사이즈는 그래도 8로 두어 1번의 배치학습(count += 1)을 할 때마다 72개의 문장이 인풋되도록 하였다.

약 563,000개의 문장으로 구성되어 있었으므로 약 7,820번의 배치학습 이후에 1에포크가 올라가게 되었다. 1,000번의 배치 학습마다 샘플 문장을 생성하고 18,500번의 배치 학습마다 파라미터를 저장하는 코드는 그대로 두었다. 이틀 내내 학습하여 277,500번의 배치 학습(약 35 Epoch)을 거친 파라미터를 저장하여 사용하였다. 샘플 문장 이외에도 여러 문장을 생성해 본 뒤 적당하다고 생각되어 학습을 중단.

시간 부족으로 인해 learning rate decay 등 추가적인 학습 방법을 사용해보지 못한 것이 아쉬움 (추후 발전 과제)



**학습 결과 생성되는 예시 문장** : Pre-Trained 모델로 문장 생성시 소설체의 문장이 생성되기도 하며 문장 간 문맥이 이어지지 않음. 3,000회 이내(1epoch도 돌지 않은)로 많은 학습을 시키지 않았음에도 자기소개서스러운 문장을 작성해내었다. 하지만 같은 문장에 팀원이라는 말이 2번 등장하는 등의 어색한 부분을 찾아낼 수 있었다. 최종 학습 후 생성된 문장을 보면 문장 길이가 있음에도 불구하고 문맥이 일정하게 유지되고 인과관계를 찾을 수 있었기에 이 단계에서 학습 중단을 결정하였다.

| 모델 학습 정도                     | 생성된 예시 문장                                             |
| ---------------------------------- | ------------------------------------------------------------ |
| 학습 전<br />Pre-Trained 모델      | 성실 너두 잘 자요. 내 사랑 나 내일 일찍 봐. 쪽쪽쪽.<br />즐거운 추석을 맞아 늘 가정에 웃음꽃이 가득하시길 바랍니다. |
| 학습 초기<br />(3,000회 이내 학습) | 성실함과 책임감이 있어야 하는 직무에 대한 이해도 있고,<br />팀원들과의 원만한 대인관계를 통해 팀원들과 원활한 의사소통도 할 수 있습니다. |
| 최종 학습 후<br />(277,500회 학습) | 성실하고 꼼꼼한 성격은 제가 지원한 생산관리에서 꼭 필요한 자질입니다.<br />저는 전공 수업중에 재료역학을 수강하였습니다.<br />이를 통해 생산 시스템의 전반적인 흐름과 제품의 특성에 대한 지식을 습득할 수 있었습니다. |



**문장 생성시 하이퍼 파라미터 튜닝** : temperature 위주로 여러 케이스를 실험해본 뒤 적정하다고 생각되는 값을 사용하였다. 자유도를 낮게 설정하였을 때에는 동일한 토큰을 계속 선택하는 경향을 보였으며 최대치로 높였을 때는 확실히 어색한 문장을 생성하였다.

| 파라미터 조정 정도 | 생성된 예시 문장                                             |
| ------------------ | ------------------------------------------------------------ |
| 자유도 낮음        | 신뢰받는 사람이 되기 위해 항상 노력하고 있습니다. <br /> 저는 항상 제 자신을 믿습니다. 믿기 때문에 모든 일을 믿고 맡길 수 있습니다. <br /> 저는 어떤 일을 할 때 완벽하게 하려고 합니다. 그래서 일처리가 늦어지는 경우가 있습니다. |
| 자유도 적정        | 신뢰받는 리더의 자질 또한 갖추어야 한다고 생각합니다. <br />신뢰를 받는 리더는 항상 구성원들의 의견에 귀 기울이며, <br />구성원의 능력을 최대한 이끌어내도록 하며, <br />이를 바탕으로 팀의 협동과 시너지 효과를 창출해야 하기 때문입니다. |
| 자유도 높음        | 신뢰받는 사람이란 주어진 일이 편하고 어려울지언을 알고<br />주어진 역할에 충실한 인간적이어야 된다고 판단하였습니다. |

<br/>

## 웹 페이지 기획 및 구성

**웹 페이지 기획** : 랜딩 페이지, 회원가입 과 로그인 페이지, 자소서 작성 및 생성 페이지 그리고 내 자소서 관리까지 크게 5개의 페이지로 구성



**랜딩 페이지** ( `landing.html` ) : 사이트 접속 시 가장 먼저 볼 수 있는 페이지

- 상단 탭은 랜딩 페이지 내에서 이동할 수 있는 탭(Feature, About, Contact)과 **로그인**, **내 자소서** 로 구성되어 있으며 화면 왼쪽에 **자소서 작성하기** 버튼을 통해 이동할 수 있도록 구성
- **로그인** 이나 **자소서 작성하기** 버튼 클릭시 구글 로그인(OAuth2.0)을 통해 자동으로 로그인이 되며 자소서 작성 페이지(`writeResume.html`) 로 이동
- 기존에 가입이 되어있지 않은 회원은 구글 계정을 통해 가입을 할 수 있도록 회원가입 페이지로 이동하며 추가 정보를 입력받기 위한 페이지로 이동
- 세션(session)을 활용하여 로그인 후 로그아웃 이전까지 유저의 정보(id, text)를 유지
- 초기 사용자가 서비스 이용에 어려움을 겪지 않도록 랜딩 페이지 중단에 초기 사용자를 위한 설명을 배치



**회원가입 페이지** ( `signup.html` ) : 회원가입시 OAuth 2.0 이 제공하는 정보 이외에 추가정보를 받기 위한 페이지

- 회원의 생년월일과 성별, 전공을 수집하도록 함
- 모든 데이터를 제대로 입력한 후 가입하기 버튼을 누를 경우 회원가입이 완료되고 정보가 DB(user_tb)에 저장



**로그인 페이지** ( `login.html` ) : 기존 사용자 로그인을 위한 페이지

- 가입되어 있는 구글 계정을 클릭하여 인증할 수 있도록 함



**자소서 작성 페이지** ( `writeReusme.html` ) : 고객이 실제로 키워드를 입력하여 문장을 생성할 수 있는 페이지

- 최초 로그인 시에는 아무런 키워드도 입력되어 있지 않으므로 본인이 원하는 키워드를 입력한 후 문장 생성하기 버튼을 눌러 5개의 문장을 생성할 수 있다.
- 이후에는 자소서 생성 페이지에서 선택한 키워드가 session 텍스트에 저장되어 나타나게 된다. 최대 100자 내에서 입력 키워드를 변경할 수 있다.
- 문장 생성시 키워드가 길면 길수록 시간이 오래 걸림. (추후 발전 과제)



**자소서 생성 페이지** ( `resumeGen.html` ) : 모델이 생성한 문장이 보이는 페이지

- 생성된 5개의 문장 중 하나를 선택할 수 있도록 버튼을 Radio로 구성
- 선택한 문장에 추가적으로 더 자소서를 작성하고 싶은 경우에는 **이어쓰기** 버튼을 클릭하여 자소서 작성 페이지( `writeResume.html` )로 이동할 수 있도록 함. 선택한 문장은 session에 저장되어 writeResume의 키워드 입력칸으로 자동입력
- 문장이 충분히 길게 생성된 경우 (혹은 생성된 문장이 100자가 넘는 경우) 이를 활용하여 자소서를 작성할 수 있도록 한다. **클립보드 복사** 버튼을 클릭하면 클립보드에 해당 문장에 복사되며 아래에 있는 **자기소개서 저장**에 붙여넣기하여 수정 및 추가 내용을 작성할 수 있다.
- 수정 및 내용 추가 이후에는 자기소개서 작성 버튼을 활용하여 자기소개서를 저장할 수 있다. **저장하기** 버튼 클릭 시 자기소개서의 제목을 입력할 수 있는 alert 창이 나오게 되며 입력 후 확인을 클릭하면 내 자소서 관리 페이지로 이동하게 된다.



**내 자소서 관리 페이지** ( `myResume.html` ) : 자신이 저장한 자기소개서를 수정 및 삭제할 수 있는 페이지

- 생성한 자기소개서의 **제목을 클릭**하면 자기소개서를 수정할 수 있다. 제목 클릭시 하단에 있는 자기소개서 수정/저장 부분으로 제목과 내용이 나오게 된다. 내용을 수정한 후에는 **수정하기** 버튼을 클릭하여 수정된 내용을 저장할 수 있다.
- **삭제 버튼**을 클릭하면 해당 자기소개서를 삭제할 수 있다.
- 삭제와 수정하기 버튼 클릭 시 바로 페이지가 변경되지 않고 새로고침을 한 번 더 눌러주어야 페이지가 변경되는 문제가 있다. (추후 발전 과제)

<br/>

## 데이터베이스 구축 및 연동

MySQL을 사용하였으며 유저 테이블, 자소서 테이블 2가지로 구성



**유저 테이블** (user_tb)

- idx : PK(Primary Key). auto_increment. 
- email : 구글 계정의 이메일. PK.
- user_id : 구글에서 부여하는 고유 키 값
- gender : 남성, 여성, LGBTQ를 각각 1, 2, 3 의 Int 형태로 저장
- birthdate : 생년월일을 yyyy-mm-dd의 Date 형태로 저장
- major : 회원이 선택한 전공 계열을 저장



**자기소개서 테이블** (resume_tb)

- idx : PK(Primary Key). auto_increment.
- email : 구글 계정의 이메일. FK(Foreign Key)로 user_tb의 동일한 항목에서 저장되어 있다.
- title : 자기소개서의 제목. varchar(string)의 형태로 저장
- texts : 자기소개서의 본문 내용. varchar(string)의 형태로 저장
- actDeact : 활성화 여부. 자기소개서 추가시 default값인 1로 설정되며 해당 자기소개서를 삭제하면 0으로 변경



**웹과 DB 연동하기** : pymysql을 활용하여 연동. 

<br/>

## 추후 발전 과제

**클라우드 서버에 배포하기** : ~~Google Cloud Platform 내부에 있는 Compute Engine을 사용하여 배포하려고 한다. 현재 웹 페이지 코드와 모델 코드는 올라가 있으나 파라미터가 저장된 .tar 파일이 올라가지 않아 시도 중.~~
배포 완료.



**데이터 추가 수집 및 전처리** : 현재 수집한 22,000 건의 데이터 중 오래된 자소서의 비율이 높다는 단점이 있다. 추가적으로 더 많은 최신 자기소개서 데이터를 모아 학습시키면 시대에 맞는 자소서를 작성할 수 있을 것으로 생각한다. 또한 맞춤법이나 OOOOOO 등으로 마스킹된 부분을 조금 더 정교하게 다듬는다면 생성된 문장에서 이런 부분이 등장하지 않을 것으로 생각한다.



**서비스 고도화** : 현재는 데이터가 적어 모든 데이터를 한 번에 학습에 사용하였다. 하지만 학습 데이터가 더 많아진다면 직군별 혹은 질문별로 모델을 따로 학습시켜 다양한 기능을 수행할 수 있도록 서비스를 고도화 하는 방향도 가능하다.

<br/>

## 결과물
### 운영 페이지 : [자소AI](http://resumeai.kro.kr)

**랜딩 페이지 상단부**

![ai_landing1](https://user-images.githubusercontent.com/45377884/84596349-1a6f8680-ae98-11ea-9ce4-67353ae7bafb.png)



**랜딩 페이지 가이드**

![ai_landing_guide](https://user-images.githubusercontent.com/45377884/84596366-3c690900-ae98-11ea-9842-2ec9bd969b47.png)



**자소서 작성 페이지** - `writeResume`

![ai_writeResume](https://user-images.githubusercontent.com/45377884/84596372-5acf0480-ae98-11ea-8396-0522c8bb0506.png)



**자소서 생성 페이지** - `resumeGen`

![ai_resumeGen_1](https://user-images.githubusercontent.com/45377884/84596425-a1bcfa00-ae98-11ea-8f0e-1a0687361c0b.png)

![ai_resumeGen_2](https://user-images.githubusercontent.com/45377884/84596431-a97c9e80-ae98-11ea-944b-8cd670edaf70.png)



**내 자소서 관리** - `myResume`

![ai_myResume_1](https://user-images.githubusercontent.com/45377884/84596546-5d7e2980-ae99-11ea-900d-712d9900924c.png)

![ai_myResume_2](https://user-images.githubusercontent.com/45377884/84596557-6b33af00-ae99-11ea-95b1-b4f0e1cabc00.png)

