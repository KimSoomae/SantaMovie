genre_dict = {'로맨스': 2, '액션': 3, '서부': 1, '코미디':1, '공포':4}
a = sorted(genre_dict.items(), reverse=True, key=lambda item:item[1])
genre, v = a[0]
print(genre)
print(a[0][0])
print(a[1][0])
