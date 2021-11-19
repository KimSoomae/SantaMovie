import json
import requests

result = []
url = 'https://api.themoviedb.org/3/movie'
key = 'f9acc36e1794da31c1fa05368571a14c'
with open('movies.json', 'r') as f:
    json_data = json.load(f)

for movie in json_data:
    movie_id  = movie["pk"]
    print(movie_id)
    URL = f'{url}/{movie_id}/credits?api_key={key}&language=en-US'
    raw_data = requests.get(URL).json()
    data = raw_data.get('cast')
    if not data:
        continue
    n = 3
    if len(data) < 3:
        n = len(data)
    for i in range(n):
        actor = data[i]
        actor_dict = {
            "model" : "movies.actor",
            #"pk" : actor.get("id"),
            "fields" : {
                "actor_id" : actor.get("id"),
                "name" : actor.get("name"),
                "profile_path" : actor.get("profile_path"),
                "movie" : movie_id,
            }
        }
        result.append(actor_dict)

with open('actors.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(result, ensure_ascii=False))
