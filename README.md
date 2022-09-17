# IMDB API Clone with DRF
https://www.imdb.com/


## API Documentation

### 1. 어드민
* 요청 방식: get
* 기능: 어드민 페이지로 이동한다.
* url: http://127.0.0.1:8000/dashboard/

예시 
```
http://127.0.0.1:8000/dashboard/
```

<br>

---

<br>

### 2. 계정
#### registration_view(request)
* 요청 방식: post
* 기능: 회원 가입
* url: http://127.0.0.1:8000/api/account/register/

예시
```
http://127.0.0.1:8000/api/account/register/
```

Body
```
{
    "username": "dbstn6477",
    "email": "dbstn6477@gmail.com",
    "password": 1234,
    "password2": 1234,
}
```

Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

{
    "response": "유저 등록 성공!!",
    "username": "dbstn6477",
    "email": "dbstn6477@gmail.com",
    "token": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzUyNjAyNiwiaWF0IjoxNjYzNDM5NjI2LCJqdGkiOiJkMzY4YjAxODQyNWU0OWViODRjMzk5NWY4ZmEwZjg5OSIsInVzZXJfaWQiOjEyfQ.fj-dRaaOPgw-00F-H88Nt5Khno3N9noA7EbJFXPcT50",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNDM5OTI2LCJpYXQiOjE2NjM0Mzk2MjYsImp0aSI6IjljMWEwYzhlNDdlNzQ5YmY4ZmYyMDQxODc0OTc0ZjgyIiwidXNlcl9pZCI6MTJ9.VgI3oji2QPIsgVTrbsDnA-N_rA1tKzD0N8L9ob0Riyo"
    }
}
```
#### obtain_auth_token
* 요청 방식: post
* 기능: 로그인
* url: http://127.0.0.1:8000/api/account/login/


예시
```
http://127.0.0.1:8000/api/account/login/
```

Body
```
{
    "username": "dbstn6477",
    "password": 1234,
}
```

Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzUyNjA1OCwiaWF0IjoxNjYzNDM5NjU4LCJqdGkiOiI1MjE3ODJlMDIwNWI0ZjU5YTZiYTNmZTRhMGEwNGFhOCIsInVzZXJfaWQiOjEyfQ.5ok229Fw1z-bTttbfi3dDs1uZAwKqFzf0CKaZPlk6Ks",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNDM5OTU4LCJpYXQiOjE2NjM0Mzk2NTgsImp0aSI6IjgzZmE4MGZjODg5NjRjYmNiNjJkYjlmOWU5MDY5NmJjIiwidXNlcl9pZCI6MTJ9.fxRT0btTJP6uNUjth5-_Rb_ihhh7Sk5QdCdrdaknWfY"
}
```

#### logout_view(request)
* 요청 방식: post
* 기능: 로그아웃
* url: http://127.0.0.1:8000/api/account/logout/

예시
```
http://127.0.0.1:8000/api/account/logout/
```

Headers
```
{
    "Authorization": "Bearer" + [access_token],
}
```
Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept
```
<br>

---

<br>

### 3. 스트리밍 플랫폼
#### StreamPlatformAV(APIView)
* 요청 방식: get
* 기능: 스트리밍 플랫폼 목록 확인
* 권한: 관리자외 read만 가능
* url: http://127.0.0.1:8000/api/watch/stream/


예시
```
http://127.0.0.1:8000/api/watch/stream/
```

Response
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 4,
        "watchlist": [
            {
                "id": 1,
                "platform": "Netflix",
                "title": "공조",
                "storyline": "공조2 개봉기념 무료 출시!",
                "active": true,
                "avg_rating": 4.25,
                "number_rating": 4,
                "created_at": "2022-09-14T05:06:04.543877Z"
            },
            {
                "id": 3,
                "platform": "Netflix",
                "title": "범죄도시2",
                "storyline": "손석구와 마동석의 만남",
                "active": true,
                "avg_rating": 5.0,
                "number_rating": 1,
                "created_at": "2022-09-15T04:41:57.110388Z"
            }
        ],
        "name": "Netflix",
        "about": "since 2012",
        "website": "https://www.netflix.com/kr/"
    },
    {
        "id": 5,
        "watchlist": [],
        "name": "Youtube",
        "about": "since 2009",
        "website": "https://www.youtube.com/"
    },
    {
        "id": 6,
        "watchlist": [
            {
                "id": 2,
                "platform": "tvN",
                "title": "신서유기2",
                "storyline": "강호동과 이수근 그리고 새로운 맴버들까지!!",
                "active": true,
                "avg_rating": 5.0,
                "number_rating": 3,
                "created_at": "2022-09-14T05:32:42.368068Z"
            }
        ],
        "name": "tvN",
        "about": "since 2020",
        "website": "https://www.tvn.com/"
    },
```

#### StreamPlatformVS(viewsets.ModelViewSet)
* 요청 방식: get
* 기능: 특정 스트리밍 플랫폼 조회
* 권한: 관리자외 read만 가능
* url: http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>


예시
```
http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/
```

Response
```
HTTP 200 OK
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 4,
    "watchlist": [
        {
            "id": 1,
            "platform": "Netflix",
            "title": "공조",
            "storyline": "공조2 개봉기념 무료 출시!",
            "active": true,
            "avg_rating": 4.25,
            "number_rating": 4,
            "created_at": "2022-09-14T05:06:04.543877Z"
        },
        {
            "id": 3,
            "platform": "Netflix",
            "title": "범죄도시2",
            "storyline": "손석구와 마동석의 만남",
            "active": true,
            "avg_rating": 5.0,
            "number_rating": 1,
            "created_at": "2022-09-15T04:41:57.110388Z"
        }
    ],
    "name": "Netflix",
    "about": "since 2012",
    "website": "https://www.netflix.com/kr/"
}
```

#### StreamPlatformVS(viewsets.ModelViewSet)
* 요청 방식: put
* 기능: 특정 스트리밍 플랫폼 수정
* 권한: 관리자외 read만 가능
* url: http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>


예시
```
http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/
```

Headers
```
"Authorization": "Bearer" + [admin_access_token],
```

Body
```
{
    "name": "Netflix - Updated",
    "about": "since 2012",
    "website": "https://www.netflix.com/kr/"
}
```

Response
```
HTTP 200 OK
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 4,
    "watchlist": [
        {
            "id": 1,
            "platform": "Netflix - Updated",
            "title": "공조",
            "storyline": "공조2 개봉기념 무료 출시!",
            "active": true,
            "avg_rating": 4.25,
            "number_rating": 4,
            "created_at": "2022-09-14T05:06:04.543877Z"
        },
        {
            "id": 3,
            "platform": "Netflix - Updated",
            "title": "범죄도시2",
            "storyline": "손석구와 마동석의 만남",
            "active": true,
            "avg_rating": 5.0,
            "number_rating": 1,
            "created_at": "2022-09-15T04:41:57.110388Z"
        }
    ],
    "name": "Netflix - Updated",
    "about": "since 2012",
    "website": "https://www.netflix.com/kr/"
}
```

#### StreamPlatformVS(viewsets.ModelViewSet)
* 요청 방식: delete
* 기능: 특정 스트리밍 플랫폼 삭제
* 권한: 관리자외 read만 가능
* url: http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>


예시
```
http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/
```

Headers
```
"Authorization": "Bearer" + [admin_access_token],
```

Response
```
HTTP 204 NO_CONTENT
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

<br>

---

<br>


### 4. 영화 리스트
#### WatchListAV(APIView)
* 요청 방식: get
* 기능: 모든 영화 리스트 조회
* 권한: 관리자외 read만 가능
* url: http://127.0.0.1:8000/api/watch/

예시
```
http://127.0.0.1:8000/api/watch/
```

Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "platform": "Netflix - Updated",
        "title": "공조",
        "storyline": "공조2 개봉기념 무료 출시!",
        "active": true,
        "avg_rating": 4.25,
        "number_rating": 4,
        "created_at": "2022-09-14T05:06:04.543877Z"
    },
    {
        "id": 2,
        "platform": "tvN",
        "title": "신서유기2",
        "storyline": "강호동과 이수근 그리고 새로운 맴버들까지!!",
        "active": true,
        "avg_rating": 5.0,
        "number_rating": 3,
        "created_at": "2022-09-14T05:32:42.368068Z"
    },
    {
        "id": 3,
        "platform": "Netflix - Updated",
        "title": "범죄도시2",
        "storyline": "손석구와 마동석의 만남",
        "active": true,
        "avg_rating": 5.0,
        "number_rating": 1,
        "created_at": "2022-09-15T04:41:57.110388Z"
    }
]
```

#### WatchListAV(APIView)
* 요청 방식: post
* 기능: 영화 리스트 생성
* 권한: 관리자외 read만 가능
* url: http://127.0.0.1:8000/api/watch/

예시
```
http://127.0.0.1:8000/api/watch/
```

Response

#### WatchDetailAV(APIView)
* 요청 방식: get
* 기능: 특정 영화 조회
* 권한: 관리자외 read만 가능
* url: http://127.0.0.1:8000/api/watch/<int:movie_id>/

예시
```
http://127.0.0.1:8000/api/watch/<int:movie_id>/
```

Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

{
    "id": 3,
    "platform": "Netflix - Updated",
    "title": "범죄도시2",
    "storyline": "손석구와 마동석의 만남",
    "active": true,
    "avg_rating": 5.0,
    "number_rating": 1,
    "created_at": "2022-09-15T04:41:57.110388Z"
}
```

#### WatchDetailAV(APIView)
* 요청 방식: put
* 기능: 특정 영화 수정
* 권한: 관리자외 read만 가능
* url: http://127.0.0.1:8000/api/watch/<int:movie_id>/

예시
```
http://127.0.0.1:8000/api/watch/<int:movie_id>/
```

Headers
```
"Authorization": "Bearer" + [admin_access_token],
```

Body
```
{
    "title": "범죄도시3",
    "storyline": "손석구와 마동석의 만남",
    "active": true
}
```

Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

{
    "id": 3,
    "platform": "Netflix - Updated",
    "title": "범죄도시3",
    "storyline": "손석구와 마동석의 만남",
    "active": true,
    "avg_rating": 5.0,
    "number_rating": 1,
    "created_at": "2022-09-15T04:41:57.110388Z"
}
```

#### WatchDetailAV(APIView)
* 요청 방식: delete
* 기능: 특정 영화 삭제
* 권한: 관리자외 read만 가능
* url: http://127.0.0.1:8000/api/watch/<int:movie_id>/


예시
```
http://127.0.0.1:8000/api/watch/<int:movie_id>/
```

Headers
```
"Authorization": "Bearer" + [admin_access_token],
```

Response
```
HTTP 204 NO_CONTENT
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```


<br>

---

<br>


### 5. 리뷰
#### class ReviewList(generics.ListCreateAPIView)
* 요청 방식: get
* 기능: 특정 영화에 대한 리뷰 생성
* 권한: 로그인 한 유저만 가능
* url: http://127.0.0.1:8000/api/watch/<int:pk>/reviews/create/


예시
```
http://127.0.0.1:8000/api/watch/2/reviews/create/
```

Headers
```
"Authorization": "Bearer" + [access_token],
```

Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

{
    "id": 12,
    "review_user": "yoonsu",
    "rating": 5,
    "description": "너무 재밌어요ㅜㅠ",
    "active": true,
    "created_at": "2022-09-17T20:10:59.991297Z",
    "updated_at": "2022-09-17T20:10:59.991342Z"
}
```

#### class ReviewList(generics.ListCreateAPIView)
* 요청 방식: get
* 기능: 특정 영화의 리뷰 조회
* 권한: 로그인 한 유저만 가능
* url: http://127.0.0.1:8000/api/watch/</int:movie_id>/reviews


예시
```
http://127.0.0.1:8000/api/watch/3/reviews/
```

Headers
```
"Authorization": "Bearer" + [access_token],
```

Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

[
    {
        "id": 9,
        "review_user": "dbstn023",
        "rating": 5,
        "description": "요근래 젤많이 웃은듯ㅋㅌㅋㅋㅋ",
        "active": false,
        "created_at": "2022-09-16T14:02:51.798302Z",
        "updated_at": "2022-09-16T14:02:51.798347Z"
    },
    {
        "id": 12,
        "review_user": "yoonsu",
        "rating": 5,
        "description": "너무 재밌어요ㅜㅠ",
        "active": true,
        "created_at": "2022-09-17T20:10:59.991297Z",
        "updated_at": "2022-09-17T20:10:59.991342Z"
    }
]
```

#### class ReviewDetail(generics.RetrieveUpdateDestroyAPIView)
* 요청 방식: get
* 기능: 특정 영화의 리뷰 조회
* 권한: 리뷰 작성자외 읽기만 가능
* url: http://127.0.0.1:8000/api/watch/reviews/<int:pk>/


예시
```
http://127.0.0.1:8000/api/watch/3/reviews/
```

Headers
```
"Authorization": "Bearer" + [access_token],
```

Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "review_user": "yoonsu",
    "rating": 5,
    "description": "마동석 드립 개웃김ㅋㅋㅋ",
    "active": true,
    "created_at": "2022-09-15T06:02:31.162792Z",
    "updated_at": "2022-09-15T06:02:31.162838Z"
}
```

#### class ReviewDetail(generics.RetrieveUpdateDestroyAPIView)
* 요청 방식: put
* 기능: 특정 영화의 리뷰 수정
* 권한: 리뷰 작성자외 읽기만 가능
* url: http://127.0.0.1:8000/api/watch/reviews/<int:pk>/


예시
```
http://127.0.0.1:8000/api/watch/3/reviews/
```

Headers
```
"Authorization": "Bearer" + [review_writer_access_token],
```

Body
```
{
    "rating": 3,
    "description": "이번편 재미없어용ㅜㅠㅠㅜㅠ",
    "active": "True"
}
```

Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "review_user": "yoonsu",
    "rating": 3,
    "description": "이번편 재미없어용ㅜㅠㅠㅜㅠ",
    "active": true,
    "created_at": "2022-09-15T06:02:31.162792Z",
    "updated_at": "2022-09-17T20:16:41.174710Z"
}
```

#### class ReviewDetail(generics.RetrieveUpdateDestroyAPIView)
* 요청 방식: delete
* 기능: 특정 영화의 리뷰 삭제
* 권한: 리뷰 작성자외 읽기만 가능
* url: http://127.0.0.1:8000/api/watch/reviews/<int:pk>/


예시
```
http://127.0.0.1:8000/api/watch/3/reviews/
```

Headers
```
"Authorization": "Bearer" + [review_writer_access_token],
```

Response
```
HTTP 204 NO_CONTENT
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```


<br>

---

<br>


### 6. 유저 리뷰

#### class UserReview(generics.ListAPIView):
* 요청 방식: get
* 기능: 특정 유저의 모든 리뷰 조회
* 권한: 로그인 한 유저만 가능
* url: http://127.0.0.1:8000/api/watch/user-reviews/?username=example


예시
```
http://127.0.0.1:8000/api/watch/user-reviews/?username=yoonsu
```

Headers
```
"Authorization": "Bearer" + [review_writer_access_token],
```

Response
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "review_user": "yoonsu",
        "rating": 3,
        "description": "이번편 재미없어용ㅜㅠㅠㅜㅠ",
        "active": true,
        "created_at": "2022-09-15T06:02:31.162792Z",
        "updated_at": "2022-09-17T20:16:41.174710Z"
    },
    {
        "id": 4,
        "review_user": "yoonsu",
        "rating": 5,
        "description": "진짜재밌다ㅋㅋ 2편 언제나와요ㅜㅠ",
        "active": false,
        "created_at": "2022-09-15T09:15:31.281556Z",
        "updated_at": "2022-09-15T09:15:31.281590Z"
    },
    {
        "id": 12,
        "review_user": "yoonsu",
        "rating": 5,
        "description": "너무 재밌어요ㅜㅠ",
        "active": true,
        "created_at": "2022-09-17T20:10:59.991297Z",
        "updated_at": "2022-09-17T20:10:59.991342Z"
    }
]
```
