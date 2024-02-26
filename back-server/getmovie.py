#############################################################################
################### movies.json을 만드는 코드 입니다 ########################
#############################################################################


import requests
import json

def get_popular_movies():
    api_key = "c376bdf28af008508b9156b102e6baf9"  # 본인의 TMDB API 키로 대체해주세요
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page=1&certification_country=KR&certification.lte=15"
    global cnt
    movies = []

    # 페이지 반복
    for page in range(1, 6):  # 5 페이지까지 가져옵니다. (총 100개)
        url_with_page = url + f"&page={page}"
        response = requests.get(url_with_page)
        
        if response.status_code == 200:
            data = response.json()
            results = data["results"]

            # 필요한 데이터 추출
            for result in results:
                movie = {
                    "model": "movies.movies",
                    "pk":cnt,
                    "fields":{
                        "movie_id": result["id"],
                        "poster_path": result["poster_path"],
                        "title": result["title"]
                    }
                }
                movies.append(movie)
                cnt += 1

        else:
            print("Error occurred on page", page, ":", response.status_code)

    return movies

cnt = 1
# 인기 영화 데이터 가져오기
popular_movies = get_popular_movies()

# 한글 제목을 출력하기 위해 인코딩 방식을 지정합니다
# print("Movies with Korean titles:")
# for movie in popular_movies:
#     print(movie["title"].encode("utf-8").decode("unicode_escape"))

# JSON 파일로 저장하기
with open("movies.json", "w", encoding="utf-8") as file:
    json.dump(popular_movies, file, indent=2, ensure_ascii=False)

print("Movies.json 파일이 생성되었습니다.")
