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

## 3. 주요 기능

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

### 3-6. 가격 문의
![2022-12-17 00;32;06](https://user-images.githubusercontent.com/105331868/208133059-8be9cb8f-56a7-466a-9de3-745b32fedb74.gif)
> 구매자가 구매를 원하는 가격보다 높을 경우 가격을 문의 할 수 있겠끔 기능 추가

### 3-7. 가격 문의 수락
![2022-12-17 00;34;53](https://user-images.githubusercontent.com/105331868/208133592-de29b0b7-d7ad-427f-b6bb-dfbf4c6fcff9.gif)
> 판매자는 가격문의 탭에서 가격제안을 수락할 수 있음. 수락시 제안가격으로 변동

### 3-8 작품 구매
![2022-12-17 00;41;12](https://user-images.githubusercontent.com/105331868/208134960-0b446af8-9d4b-4877-93fa-613e803b7355.gif)
> 이니시스API를 통해 결제 기능 연결

### 3-9 결제 완료
![image](https://user-images.githubusercontent.com/105331868/208135499-a8e5cad1-5fd4-4570-bbdb-4fb9a9db8020.png)

### 4-1 프로필
![2022-12-17 00;48;20](https://user-images.githubusercontent.com/105331868/208136349-59757f3c-4c70-4f3b-968c-9c578fdbf24c.gif)

### 4-2 작가인
