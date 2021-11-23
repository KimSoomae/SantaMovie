# 영화정보를 API를 이용해서 가져오기

# 홈페이지  https://www.themoviedb.org/
# Document  https://developers.themoviedb.org/3

import json
# pip install requests
import requests
#from api_key import URLMaker

# # url 가져오기
# url_maker = URLMaker(URLMaker.key)
# url = url_maker.get_url()

# # url 요청
# r = requests.get(url)
# movie_dict = r.json()

# result = [movie_dict]

# with open('movies.json', 'w', encoding='UTF-8') as file:
#     file.write(json.dumps(result, ensure_ascii=False))


### fixtures, loaddata로 처리


#####################################################################################

## 1. movie 정보
result = []
url = 'https://api.themoviedb.org/3/keyword/207317/movies'
key = '408e6526da70264082bc4ae31ffbbe3e'
for page in range(1, 5):
    URL = f'{url}?api_key={key}&language=ko-Kr&include_adult=true&page={page}'

    raw_data = requests.get(URL).json()
    data = raw_data.get('results')
    for movie in data:
        movie_dict = {
            "model" : "movies.christmasmovie",
            "pk" : movie.get("id"),
            "fields" : {
                "title" : movie.get("title"),
                "popularity" : movie.get("popularity"),
                "genre_ids" : movie.get("genre_ids"),
                "release_date" : movie.get("release_date"),
                "overview" : movie.get("overview"),
                "poster_path" : movie.get("poster_path")
            }
        }
        result.append(movie_dict)

with open('christmasmovies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(result, ensure_ascii=False))
