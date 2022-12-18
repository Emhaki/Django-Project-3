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
> 유저의 accounts, DM의 notes, 문의의 questions 앱을 전체 로직 및 설계 담당

> accounts에서는 소셜로그인과 이메일 인증 기능 적용

> 모든 DB내역을 끌고와 프로필에서 작가의 작품, 좋아요한 작품, 구매내역, 판매내역, 장바구니 목록을 볼 수 있게 연결

> 작가 인증 이메일을 통해 대학생인지 여부 판별 로직설계

> notes앱의 DB로직 설계

> questions앱의 CRUD, request user와 admin만 해당문의 페이지에 들어올 수 있게 설계

## 5.프로젝트 후기
![image](https://user-images.githubusercontent.com/105331868/208282727-e41a88e4-55c5-4041-9ebb-378c19584445.png)
> NES 피그마 계화면설계
- 기획의 중요성을 깨닫게 됐다. 막연하게 이런 앱, 서비스가 아니라 사용자에게 어떤 가치를 제공해주고 싶은지를 먼저 생각해보니 프로젝트의 방향성을 잡기에 더 편했던 것 같다. 피그마를 통해 상세하게 화면설계를 진행해보니 이전 프로젝트보다 훨씬 작업에 속도가 붙었던 것 같다.

- 프론트와 백을 딱 구분지어서 프로젝트를 해 본 경험이 처음이다보니 큰 책임감을 느끼게 됐다. 특히 회원쪽을 맡다보니 서비스의 근간이 되는 회원관리의 중요성을 알게 됐다. 다양한 소셜 로그인과 일반 로그인을 구현할 경우 DB에서 유저 저장값들을 일치시켜주는 것이 중요하다는 것을 깨닫게 됐다.

- 한 페이지에 많은 내용을 담으려고 하다보면 생각치 못한 변수에 부딪히게 된다. 문의 페이지에서 문의 내역과 문의댓글을 연결하려고 하다보니 pk값을 일치시켜야 했고, 여러 댓글 작성폼에서 작성한 value값도 서버로 잘 넘겨줘야 했다. 저장된 댓글 내용도 해당 pk값안에서 보일 수 있게 필터링을 걸어줘야 했다.

- 이번에 Django의 SMTP 이메일 전송기능과 소셜로그인 API, 카카오 지도검색 API를 사용해보면서 새로운 기술을 적용시키는데에 조금이나마 익숙해진 것 같다.

### 문의 views.py 일부분
```py
<!-- 내 문의내역 -->
@login_required
def myquestion(request):

    # 문의 pk를 추적할 수 있도록, 첫번째 문의는 댓글작성이 되나
    # 두번째 문의부터 댓글작성이 안되는 현상 발생.
    my_questions = Question.objects.filter(user_id=request.user.pk)
    context = {
      "questions": my_questions,
    }

    return render(request, "questions/myquestion.html", context)
```
```py
@login_required
def comment_create(request, question_pk):
    question_comment = get_object_or_404(Question, pk=question_pk)
    if request.user.is_authenticated:
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.question = question_comment
            comment.user = request.user
            comment.save()
            if comment.user.test:
                name = comment.user.creater_name
            elif comment.user.creater_name:
                name = comment.user.creater_name
            elif comment.user.username:
                name = comment.user.username
            context = {
              'content': comment.content,
              'userName': name,
              'created_at': comment.created_at
            }
            print(context)
        return JsonResponse(context)
    else:
        return redirect("accounts:login")
```

- 문의 html 일부분
```html
{% for question in questions %}
  <div class="myquestion__list">
    <div class="myquestion__list__title">
      <p>Q. {{ question.title }}</p>
      <button class="myquestion__list__title__button" data-container="myquestion__title__content__{{ question.pk }}">
        <svg class="myquestion__list__title__button__down bi bi-caret-down-fill" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewbox="0 0 16 16">
          <path d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/>
        </svg>
        <svg class="myquestion__list__title__button__cancle bi bi-x-circle" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewbox="0 0 16 16">
          <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
          <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
        </svg> 
      </button>
    </div>
    <div class="myquestion__title__content" id="myquestion__title__content__{{ question.pk }}">
      {% if question.image %}
      <div class="myquestion__title__content__image">
        <img src="{{ question.image.url }}" alt="">
      </div>
      {% else %}
      <div>
        
      </div>
      {% endif %}
      <div class="myquestion__title__content__box">
      <p class="myquestion__title__content__text">{{ question.content }}</p>
      <div class="myquestion__title__content__comment">
        {% comment %} 문의 댓글 {% endcomment %}
        {% if request.user.is_authenticated %}
          <div id="question-comments" class="mt-3">
            <form id="question-comment-form" class="d-flex create-form" data-question-id="{{ question.pk }}">
              {% csrf_token %}
                <input type="text" name="content" class="form-control" placeholder="댓글을 달아주세요">
                <input type="submit" class="btn btn-primary mx-1" value="작성">
            </form>
          </div>          
          {% for comment in question.comment_set.all %}
          {% if comment.question.pk == question.pk %}
            <div class="fw-bold mt-2">
              {% if comment.user.test %}
                {{ comment.user.creater_name }}
              {% elif comment.user.creater_name %}
                {{ comment.user.creater_name }}
              {% elif comment.user.username %}
                {{ comment.user.username }}
              {% endif %}
            </div>
            <div sytle="width:350px;">
              <div class="col-10 d-flex align-items-center">
                {{ comment.content }}
              </div> 
            </div>
            <div style="font-size:12px;" class="text-muted">{{ comment.created_at|date:"o-m-d"}} {{comment.created_at|time:"H:i"}}</div>
            <hr>
          {% endif %}
          {% endfor %}
          <div id="question-commentss-{{ question.pk }}" class="question-commentss">

          </div>
        {% endif %}
        {% comment %} 문의 댓글 끝 {% endcomment %}
      </div>
      </div>
    </div>
  </div>
  {% endfor %}
```
- ajax 비동기 일부분
```js
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    const commentFormSet = document.querySelectorAll('.create-form')
    const commentsSet = document.querySelectorAll(".question-commentss")
      for (j=0; j < commentFormSet.length; j++) {
      let targetDiv = commentsSet[j]
      commentFormSet[j].addEventListener('submit', function(event) {
        event.preventDefault();
        axios({
          method: 'post',
          url: `/questions/${event.target.dataset.questionId}/comment/create/`,
          headers: {'X-CSRFToken': csrftoken},
          data: new FormData(event.target)
        })
        .then(response => {
          const div = document.createElement('div')
          const p = document.createElement('p')
          const small = document.createElement('small')
          div.innerText = `${response.data.userName}`
          div.className = "fw-bold mt-2"
          p.innerText = `${response.data.content}`
          p.className = "text-muted"
          small.innerText = "0분전"
          small.className = "text-muted fs-7"
          const hr = document.createElement('hr')
          targetDiv.append(div, p, small, hr)
        })
      })
    }
```

## 6.팀원들의 후기
백솔비😍
```
우리도 끝이 아닌 시작 👊
```

이명학🐻‍❄️
```
3~4주 동안 프로젝트를 진행하면서 많은 것들을 배울 수 있었습니다.
팀원들 모두 책임감 있게 프로젝트를 진행해주어서 잘 마무리 할 수 있었습니다.
함께 협업해준 팀원들에게 감사합니다 :)
```

최근영🐶
```
벌써 마무리 해야한다는 점이 아쉽고 프론트를 재밌게 만들어 볼 수 있었던 주제였습니다.
```

김예린🐻
```
좋은 팀원들과 끊임없이 소통하며 만족할 수 있는 프로젝트를
경험할 수 있어서 감사하고 뿌듯합니다 :)
⭐️NES 뽀에버⭐️
```
문현동🦔
```
4주동안 마주쳤던 다양한 도전들을 통해 개발자로서 많은 성장을 할 수 있어서 좋았습니다.
```
