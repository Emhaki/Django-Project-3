# 예술대학 작품 중개 서비스(NES)

![IMG_2017](https://user-images.githubusercontent.com/105331868/208124555-953e4216-3825-4456-b9dd-dd6ba9a2a3c5.jpg)

배포 주소: http://nes-env.eba-9ycvw3yi.ap-northeast-2.elasticbeanstalk.com/

# 목차

[1. 프로젝트 소개](#1프로젝트-소개)

[2. 서비스 소개](#2프로젝트-소개)

[3. 주요 기능](#3주요-기능)

[4. 기여한 부분](#4기여한-부분)

[5. 프로젝트 후기](#5프로젝트-후기)

[6. 팀원들의 후기](#6팀원들의-후기)

<br>

## 1.프로젝트 소개

### 프로젝트 일정

| 날짜 | 내용 |
| --- | --- |
| 11.24 (목) ~ 12.14 (수) | 프로젝트 개발 |
| 12.15 (목) | (오전) 프로젝트 발표회
(오후) 프로젝트 발표회 & 정리 |

## 2.프로젝트 소개

![글자 로딩](https://user-images.githubusercontent.com/105331868/208124365-8c4e0c36-a86c-4134-9ae3-6a5a028c8d16.gif)

> `NES(Never Ending Story)`는 젊은 예술가들이 직면할 수 밖에 없는 작품의 전시와 그에 따른 비용에 관한 문제를 어떻게 해소시켜 줄 수 있을까?를 고민했습니다. `끝나지 않는 이야기`라는 뜻을 담고 있는 NES는 젊은 예술가들의 어려움에 공감하며 그들의 꿈을 이루는 것을 돕고자 졸업 작품 중개 서비스를 기획하였습니다.

## 3.주요 기능

### 3-1. 로그인 페이지
![image](https://user-images.githubusercontent.com/105331868/208125670-fd573a76-5a3a-4f60-ad5f-21b350d6354e.png)
![image](https://user-images.githubusercontent.com/105331868/208126653-1ccf821c-39b4-4327-9928-5dfb697c13dd.png)


> 회원가입은 일반 로그인과 카카오 소셜로그인 두 개로 분류

### 3-2. 일반 회원가입
![image](https://user-images.githubusercontent.com/105331868/208125951-e8b53e5c-bd12-4931-8e68-7b9b69b2a90e.png)

> `아이디 중복검사`, Django SMTP 기능을 활용해 `이메일 유효성 검사`, `카카오 주소검색 API`를 활용해 주소검색

### 3-3. 입장

![티켓 출력](https://user-images.githubusercontent.com/105331868/208125243-e166d1d4-51a9-43b3-b185-f169503a2187.gif)
> 로그인을 후 티켓 출력 페이지로 이동

### 3-4. 카테고리

![2022-12-17 00;22;28](https://user-images.githubusercontent.com/105331868/208130991-b13fd60c-823d-45e1-94ac-b41a4836d212.gif)

![2022-12-17 00;26;39](https://user-images.githubusercontent.com/105331868/208131530-7c112c4d-4083-453d-a081-fc15233ff449.gif)
> 7개 카테고리별로 8개씩 작품을 출력

### 3-5. 작품 디테일
![2022-12-17 00;29;43](https://user-images.githubusercontent.com/105331868/208132553-313b9423-e7cf-4966-a39e-8b99833c1b01.gif)
> 좋아요, 댓글 작성, 삭제 비동기 처리

### 3-6. 최근 본 작품
![2022-12-18 11;49;57](https://user-images.githubusercontent.com/105331868/208278980-34c1a2f4-1d62-454c-8eef-bf9218ea147b.gif)
> 작품 디테일 페이지로 접속하면 최근 본 작품에 해당 작품이됨기록됨

### 3-7. 가격 문의
![2022-12-17 00;32;06](https://user-images.githubusercontent.com/105331868/208133059-8be9cb8f-56a7-466a-9de3-745b32fedb74.gif)
> 구매자가 구매를 원하는 가격보다 높을 경우 가격을 문의 할 수 있겠끔 기능 추가

### 3-8. 가격 문의 수락
![2022-12-17 00;34;53](https://user-images.githubusercontent.com/105331868/208133592-de29b0b7-d7ad-427f-b6bb-dfbf4c6fcff9.gif)
> 판매자는 가격문의 탭에서 가격제안을 수락할 수 있음. 수락시 제안가격으로 변동

### 3-9 작품 구매
![2022-12-17 00;41;12](https://user-images.githubusercontent.com/105331868/208134960-0b446af8-9d4b-4877-93fa-613e803b7355.gif)
> 이니시스API를 통해 결제 기능 연결

### 3-10 결제 완료
![image](https://user-images.githubusercontent.com/105331868/208135499-a8e5cad1-5fd4-4570-bbdb-4fb9a9db8020.png)

### 3-11 프로필
![2022-12-17 00;48;20](https://user-images.githubusercontent.com/105331868/208136349-59757f3c-4c70-4f3b-968c-9c578fdbf24c.gif)

### 3-12 작가인증
![2022-12-18 11;39;06](https://user-images.githubusercontent.com/105331868/208278744-c14b069b-e9e1-4e76-afcb-aa69aede319e.gif)
> 작품을 등록하기 위해서 작가인증 기능을 추가. 대학교 이메일이 아닌경우 메일이 전송되지 않으며, 대학교 이메일로 인증번호를 보내 이메일 인증

### 3-13 작품등록
![2022-12-18 11;44;16](https://user-images.githubusercontent.com/105331868/208278855-65f192ca-98f4-4b2b-b46e-1c1cc7754793.gif)
> 입력한 카테고리별로 DB저장

### 3-14 다이렉트 메시지
![2022-12-18 11;46;21](https://user-images.githubusercontent.com/105331868/208278909-8cf47bf0-70ae-4702-a82a-c4ac70e10e1a.gif)
> 유저에게 DM을 보내면 받은 사람은 받은 편지함에 보낸 사람은 보낸 편지함에 기록

### 3-15 문의등록
![2022-12-18 11;53;50](https://user-images.githubusercontent.com/105331868/208279076-6d47e794-2414-4c73-8aa0-d66190a99952.gif)
![2022-12-18 11;54;29](https://user-images.githubusercontent.com/105331868/208279086-af5c0d8c-bb3f-4920-bcf5-55cfa7013855.gif)

### 3-16 문의답변
![2022-12-18 11;56;36](https://user-images.githubusercontent.com/105331868/208279191-bb2e86ff-1c60-4f7c-b1df-dff8484c9370.gif)
![2022-12-18 11;58;37](https://user-images.githubusercontent.com/105331868/208279195-13cc02ff-41a5-4196-9039-582c24357e32.gif)
> 문의에 대한 내역은 질문자, 관리자만 볼 수 있음. 관리자로 로그인시에는 유저들이 문의한 모든 내역을 볼 수 있게 설계

## 4.기여한 부분
> 유저의 accounts, DM의 notes, 문의의 questions 앱을 담당
> accounts에서는 소셜로그인과 이메일 인증 기능 적용
> 모든 DB내역을 끌고와 프로필에서 작가의 작품, 좋아요한 작품, 구매내역, 판매내역, 장바구니 목록을 볼 수 있게 연결
> 작가 인증 이메일을 통해 대학생인지 여부 판별 로직설계
> notes앱의 DB로직 설계
> questions앱의 CRUD, request user와 admin만 해당문의 페이지에 들어올 수 있게 설계

## 5.프로젝트 후기
