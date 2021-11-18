# PJT-Final: 영화 추천 사이트 만들기

>  11/17(수)

### 🌈Goals

- 팀원 간 아이스브레이킹
- 우선순위 설정
- DB 모델링 - ERD 다이어그램
- Django 서버 구축

### 🌈Discussion Items

- 팀명 - 코딩수재(수민 + 재현)

- 컨셉

  - 크리스마스
  - 간지나되, 깔끔하게
  - 로고, 사이트 네이밍

- 기능

  1. 기본 기능 - 기본은 완벽하게!

     

  💡 데이터 수집(API) - **TMDB API**

  💡 관리자 뷰(영화 등록, 수정, 삭제) + 유저 관리 권한

  💡 영화 정보

  - 평점(별점, 한줄평) 등록, 수정, 삭제

  - 메인페이지 - 추천된 영화 목록(간지나게)

  - 상세정보(포스터, 장르, 줄거리, 평점, 예고편)

    

  2. 추천 알고리즘 - 어떻게 하면 취향저격 영화를 추천할 수 있을까!

   ### 🤯브레인스토밍

  재현이의 영화 선택 기준 ) 장르가 젤 중요(애니메이션), 유명한, 어두운 vs 밝은

  수민이의 영화 선택 기준) 외국영화 선호, 장르, 유명한거, 숨겨진 명작

  **협업 필터링 - 비슷한 취향의 유저가 추천한 영화를 추천 - 좋아요 기능**

  비슷한 취향: 회원가입 시 여러개 영화 중 몇개 선택 -> 장르, 배우 등으로 취향 분류

  Collaboraiton Filtering

  → Explict DataSet Neighborhood model

  https://yeomko.tistory.com/6?category=805638

  감독, **장르, 배우,** 내용 등에서 유사한 콘텐츠 추천

  시기별 추천(크리스마스, 여름, 겨울)

  타임머신 → 몇 년전으로 돌아갈까? 그 시기에 맞는 영화 추천

  재밌는 설문을 통한 추천

  검색, 좋아요로 초기 선호 데이터 업데이트

  비슷한 영화추천 →

  Hybrid Filtering(협업 + 콘텐츠 기반)

  - 회원가입 할 때, 좋아하는 영화 픽 & 장르 → 취향 반영

  - 여행가고싶은 나라 - 그 나라 영화 추천

  - 좋아하는 배우 선택 → 비슷한 느낌의 배우 추천, 그 배우의 필모그라피 추천

  - 기분

    

  ### 🎄확정

  컨셉 - 크리스마스

  [박스오피스 기준 TOP 영화들]

  [크리스마스 영화들]

  [추천 영화들]

  회원가입 → 장르&종류별 대표 영화 여러개 선택 → 유저 취향 저장 → 가장 베스트인 장르 기반 추천

  협업 필터링 → 같은 취향의 유저가 좋아요 누른 영화들을 좋아요 순으로 출력

  타임머신 → 해당 연도의 영화 랜덤으로 출력

  영화 상세 정보

  포스터, 장르, 주연배우, 평점, 영화 description, 예고편

  포스터 + 마우스 오버시: 플립되면서 제목, 짧은 줄거리, 평점, 장르 나오고

  클릭하면 줄거리, 한줄평 리뷰, 주연 배우, 예고편

  **프론트엔드**

  주요 컬러 - 빨간색, 진초록

  bgm - 캐롤

  💡 커뮤니티

  - 글 (자유 글)조회, 생성, 삭제

  - 댓글 작성, 삭제(생성 및 수정 시각 포함)

  - 글 작성할때 태그 선택 + 추가 작성

  - 해시태그로 검색 가능하게(시간 되면 2개 이상)

    

  💡 추가기능

  - 소셜로그인, 비밀번호 & 아이디 찾기

  - 페이지네이션

- Youtube API -  영화 예고편

  ### 🌈계획

![](https://i.ibb.co/n3TVG8q/plan.png)





> **11/18(목)**

### 🌈Goals

- Git 레포지토리 만들기 ✔︎
- Django 서버 구축 ✔︎
- Model 작성, Account, Community, Movies 기능 개발 (Model 작성 + Account 기능 개발까지)
- API를 JSON 파일로 불러와 DB에 저장 ✔︎

### 🌈Discussion Items

✅ 재현이의 목표

- tmdb에서 Json파일 받아와서 DB에 저장 ✔︎

- Home 페이지에 server, client 완료 ✔︎

- 영화상세정보는 api ✔︎

- 별점 Modeling ✔︎

✅ 해야할 것

- 영화 상세 페이지 vue에 한줄평 쓸수 있도록

- 배우 정보 추가

- 별점 CRUD

- 좋아요 기능

✅ 수민이의 목표

- 회원가입, 로그인 구현 ✔︎

- 커뮤니티, 유저 정보 모델링 ✔︎

- 회원가입 후 myPage에 장르별 대표영화 고를 수 있는 기능 ✔︎

✅ 해야할 것

- 대표 영화 고르면 유저 db에 저장

- 커뮤니티 CRUD, vue

- 영화추천 알고리즘 시작...........





