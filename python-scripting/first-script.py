def release(movie):
    if(movie["release_year"] < 2000):
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie['name']
    return None

recent_movies = []
favorite_movies =[
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    },
    {
        "name": "Tenet",
        "release_year": 2020
    }
]
for movie in favorite_movies:
    if(release(movie)):
        recent_movies.append(movie)
print(recent_movies)