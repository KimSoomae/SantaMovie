# PJT-Final: 영화 추천 사이트 만들기

>  ## 11/17(수)

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



점심은 든든하게

![](https://i.esdrop.com/d/eae6tqatp81y/u9gXKb0K7o.jpeg.sthumb)

> ## **11/18(목)**

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



점심은 든든하게

![](https://i.esdrop.com/d/eae6tqatp81y/XnDFcXOwtD.jpeg.sthumb)

> ## 11월 22일(월)

월요일 아자아자 화이팅.

# Goals

- Community, 댓글 Vue

- 커뮤니티-유저, 커뮤니티-태그

- My Page Vue, 유저에 선호하는 영화 데이터 저장

- 영화 추천 알고리즘

- 장르연결

  

# Discussion Items

- 

# Action Items



- [x] PickMovie - Genre 연결 

- [x] My Page Vue, 유저에 선호하는 영화 데이터 저장 

- [x] Community, 댓글 Vue 

- [x] 커뮤니티-유저 연결 

- [x] 합치기

- [x] 커뮤니티-태그 

- [x] 태그 검색 

  



> 상대경로시 에러

"attempted relative import beyond top-level package" 에러

```python
import os
from movies.models import Genre
```

..movies 이런식으로 상대 경로를 설정하는 것은 디버깅 설정에 따라 다를 수 있다.

따라서 패키지 이름을 넣어 선언하면 다른 앱에 있는 함수나 모델들 불러올 수 있음.



> ManyToMany Field Serializer 데이터 저장

Create하면서 동시에 ManyToMany 데이터 추가해야되는데, 막막했음. 

Django 공식 문서를 보며 해결.

1. 먼저 serializer.save()를 통해 community 생성
2. 생성한 serializer의 id로 community object 얻어오기
3. 태그 리스트 반복문 돌면서 해당하는 이름의 태그 Object 불러오기
4. 없으면 Tag 테이블에 추가
5. 해당 Tag Object를 Community Object의 ManyToMany Field에 추가

```python
		taglist = request.data['tags'].split('#')[1:]  
    serializer = CommunitySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        community= get_object_or_404(Community, pk =serializer.data['id'])

        for i in range(len(taglist)):
            if not Tag.objects.filter(name=taglist[i]).exists():
                Tag.objects.create(name=taglist[i])
            tag = Tag.objects.get(name=taglist[i])
            community.tags.add(tag)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```



### 중간 결과 사진 - 꾸미기 전!!!

1. Home 화면 - 영화 추천할

![](./images/home.png)

2. 커뮤니티 화면

![](./images/community.png)

3. 커뮤니티 - 태그로 검색

   ![](./images/community_search.png)

   4. 회원가입 - 영화취향 고르기

      ![](./images/mypage.png)

   5. 마이페이지

   ![](./images/mypagelist.png)



오늘은 재현이가 아팠다. 아픈데도 프로젝트를 중단할 수 없는 현실이 참 슬펐다.

수민이는 가슴이 답답하다. 오늘 눈이 온다는 소식이 들린다. 마음이 싱숭생숭하다. 

그래도 스트레스뿐이었던 어제 밤보단 낫다. 어제 밤에는 각자 했기 때문이다.

역시 페어를 만나야 힘이 나는 것 같다. 내일도 화이팅.



> ## 11월 23일(화)

## Goals

- [ ] 영화 추천 알고리즘
- [ ] 데이터 넣어야 될 것: MoviePick, Christmas 영화
- [ ] 꾸미는 거 시작
- [ ] 협업 필터링 



🌟 협업 Filtering

1. 회원가입 시 좋아하는 영화 여러개 선택 - 가장 많은 장르 1, 2순위

- 여러개 어려우면 하나만 선택해서 장르 두개 뽑기

2. 유저가 선택한 좋아하는 영화 장르를 똑같이 좋아하는 유저 뽑기

3. 그 유저가 좋아요 누른 영화들을 좋아요 많은 순으로 추천

   

🎄 크리스마스

1. 좋아하는 장르 먼저 보여주기

2. 데이터는 직접 넣기

   

💡 영화 유명한 순으로