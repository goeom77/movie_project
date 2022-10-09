# PJT 05

## A. base.html

- 요구 사항 
  
  - 모든 템플릿 파일은 base.html을 상속받아 사용합니다.
  
  - Bootstrap 사용을 위한 코드를 삽입합니다.

- 문제 접근 방법 및 코드 설명

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
  <title>Eom Movie</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&display=swap');

    body {
        font-family: 'Nanum Myeongjo', serif;
        background-color: black;
    }
  </style>
</head>
<body class="bg-dark text-white">
  <nav class="navbar navbar-expand-lg bg-dark">
    <div class="container-fluid">
      <img src="https://images.descentekorea.co.kr/contents/event/about_UMB/2021_renew/ec/about_umbro_renew_topTxt.png" alt="#" width="50px">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active text-white" aria-current="page" href="{% url 'movies:index' %}">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-white" href="{% url 'movies:create' %}">Create</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-white" href="https://www.justwatch.com/kr/%EC%98%81%ED%99%94">Watch</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
    {% block content %}
    {% endblock content %}

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
</body>
</html>
```

+ 이 문제의 포인트
  
  + bootstrap 을 적용하는 것에서 기억나지 않는 부분들이 어려웠습니다.

---

## B. index.html

- 요구 사항
  
  - 데이터베이스에 존재하는 모든 영화의 목록을 표시합니다.
  
  - 적절한 html 요소를 사용하여 영화 제목 및 평점을 표시하며, 제목을 클릭 시 해당 영화의 상세 조회 페이지로 이동합니다.

- 문제 접근 방법 및 코드 설명

![img](C:\Users\SSAFY\Desktop\05_pjt\index.PNG)

```html
{% extends 'base.html' %}

{% block content %}
    <h1 class="d-flex justify-content-center">Movies</h1>
    <hr>
    <div class="d-flex justify-content-center">
        <div class="container row ">
            {% for movie in movies %}
                <div class="card col-4">
                    <img src="{{ movie.poster_url }}" class="card-img-top mt-2" width="100%" alt="#">
                    <div class="card-body">
                        <h5 class="card-title"><a href="{% url 'movies:detail' movie.pk %}" class="text-decoration-none text-dark fs-5">{{ movie.title }}</a></h5>
                        <p class="card-text text-dark"> 💕 {{ movie.score }} </p>
                    </div>
                </div>
            {% endfor %}
            <hr>
        </div>
    </div>
{% endblock content %}
```

- 이 문제의 포인트
  
  - 그림을 넣을 때 img를 이용해서 이미지 주소를 사용

---

## C. detail.html

- 요구 사항
  
  - 해당 영화의 수정 및 삭제 버튼을 표시합니다.
  
  - 전체 영화 목록 조회 페이지로 이동하는 링크를 표시합니다.

- 문제 접근 방법 및 코드 설명

![img](C:\Users\SSAFY\Desktop\05_pjt\detail.PNG)

```html
{% extends 'base.html' %}

{% block content %}
    <h1 class="d-flex justify-content-center">DETAIL</h1>
    <hr>
    <div class="d-flex justify-content-center">
        <div class="card mb-3 col-9 ">
            <div class="row g-0">
            <div class="col-md-4">
                <img src="{{ movie.poster_url }}" class="img-fluid rounded-start" alt="...">
            </div>
            <div class="col-md-8">
                <div class="card-body text-dark">
                <h3 class="card-title">{{ movie.title }}</h3>
                <p class="card-text">Release Dates : {{ movie.release_date }}</p>
                <p class="card-text">Genre : {{ movie.genre }}</p>
                <p class="card-text">Score : {{ movie.score }}</p> 
                <p class="card-text">{{ movie.description }}</p>
                <br>
                <div>
                    <button type="button" class="btn btn-outline-secondary"><a href="{% url 'movies:update' movie.pk %}" class="text-decoration-none text-dark fs-5">UPDATE</a></button>
                    <button type="button" class="btn btn-outline-secondary"><a href="{% url 'movies:delete' movie.pk %}" class="text-decoration-none text-dark fs-5">DELETE</a></button>
                </div>
                <br>
                <a href="{% url 'movies:index' %}" class="text-decoration-none text-dark fs-5">BACK</a>
                </div>
            </div>
            </div>
        </div>
    </div>
{% endblock content %}
```

---

## D. create.html

- 요구 사항
  
  - submit시 단일 영화 데이터를 저장하는 url로 요청과 함께 전송됩니다.
  
  - 전체 영화 목록 조회 페이지로 이동하는 링크를 표시합니다.

- 문제 접근 방법 및 코드 설명
  
  ![loading-ag-253](C:\Users\SSAFY\Desktop\05_pjt\create.PNG)

```html
{% extends 'base.html' %}

{% block content %}
<div class="m-5">
  <h1 class="d-flex justify-content-center">CREATE</h1>
  <form action="{% url 'movies:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" class="btn btn-outline-secondary text-white">
  </form>
  <hr>
  <button type="button" class="btn btn-outline-secondary"><a href="{% url 'movies:index' %}" class="text-decoration-none text-white fs-5">BACK</a></a></button>
</div>
{% endblock content %}  이 문제의 포인트bootstrap 을 적용하는 것에서 기억나지 않는 부분들이 어려웠습니다.
```

---

## E. update.html

- 요구 사항
  
  - 특정영화 수정하기 위한 html form요소를 표시합니다.
  
  - 작성한 정보는 제출 시 단일 영화 데이터를 수정하는 url로 요청과 함께 전송됩니다.

- 문제 접근 방법 및 코드 설명
  
  ![img](C:\Users\SSAFY\Desktop\05_pjt\edit.PNG)

```html
{% extends 'base.html' %}

{% block content %}
    <h1>UPDATE</h1>
    <form action="{% url 'movies:update' movie.pk %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
        <input type="submit" name="cancel" value="Cancel">
    </form>
    <hr>
    <a href="{% url 'movies:index' %}" class="text-decoration-none text-dark fs-5">BACK</a>
{% endblock content %}
```

프로젝트를 하고 느낀 점

- 반복해서 기능들을 추가해가며 연습해야 되는 필요성
- django와 bootstrap을 이용해서 기능들을 적용해가면서 좀 더 다양한 디자인을 바꿀수 있을 것입니다.
- 
