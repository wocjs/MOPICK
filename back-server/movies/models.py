from django.db import models
from django.conf import settings

'''
    {
      "adult": false,
      "backdrop_path": "/m8JTwHFwX7I7JY5fPe4SjqejWag.jpg",
      "genre_ids": [
        28,
        12,
        878
      ],
      "id": 640146,
      "original_language": "en",
      "original_title": "Ant-Man and the Wasp: Quantumania",
      "overview": "슈퍼히어로 파트너인 스캇 랭과 호프 반 다인, 호프의 부모 재닛 반 다인과 행크 핌, 그리고 스캇의 딸 캐시 랭까지 미지의 양자 영역 세계 속에 빠져버린 앤트맨 패밀리. 그 곳에서 새로운 존재들과 무한한 우주를 다스리는 정복자 캉을 만나며, 그 누구도 예상 못 한 모든 것의 한계를 뛰어넘는 모험을 시작하게 되는데…",
      "popularity": 3294.76,
      "poster_path": "/sz6mTIDDQmR3DYgJudiTmoW2gR5.jpg",
      "release_date": "2023-02-15",
      "title": "앤트맨과 와스프: 퀀텀매니아",
      "video": false,
      "vote_average": 6.5,
      "vote_count": 2650
    },
'''
# Create your models here.
class Movies(models.Model):
    movie_id = models.IntegerField()
    poster_path = models.CharField(max_length=500)
    title = models.CharField(max_length=100)