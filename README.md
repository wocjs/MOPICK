# Final Project

## **Contributors**

- **[JaeChun Hwang](https://github.com/wocjs)** (wocjs602@gmail.com)
- **[SeHoon Ko](https://github.com/Gobro-s)** (govelopper@gmail.com)

## **프로젝트 개요**

### **What**

- 본 프로젝트는 [MOPICK]이라는 영화 추천 및 조회 기능을 포함하는 웹 서비스를 개발하는 것을 목표로 합니다.
- MOPICK은 사용자들에게 다양한 영화 정보를 제공하고 개인의 취향에 맞는 영화를 추천하여 영화 관람 경험을 향상시키는 플랫폼입니다.

### **For Who?**

- 이 프로젝트는 다양한 영화를 탐색하고자 하는 영화 애호가들을 위해 개발되었습니다. 영화를 찾아보고 싶은 사람들이나 랜덤으로 영화 추천을 받고 싶은 사람들을 대상으로 합니다. 또한, 영화에 관심이 있는 사람들이 영화에 대한 정보를 얻고, 자신의 의견을 공유하며 영화 커뮤니티와 소통할 수 있는 기회를 제공합니다.

### **How?**

- 본 프로젝트는 웹 사이트로 구현될 예정입니다. 사용자들은 MOPICK 웹 사이트를 방문하여 영화 검색, 추천, 리뷰 작성 등의 기능을 이용할 수 있습니다. 이를 위해 영화 데이터베이스를 구축하고, 추천 알고리즘을 개발하여 사용자들에게 맞춤 영화 추천을 제공합니다. 또한, 사용자들은 회원가입을 통해 개인화된 경험을 할 수 있으며, 소셜 기능을 통해 다른 사용자들과 소통할 수 있습니다.

### **프로젝트 기반**

- 기술 스택
    - 백엔드 개발에는 Python과 Django REST 프레임워크를 사용하여 개발되었습니다.
    - 프론트엔드 개발에는 JavaScript와 Vue.js를 활용하였습니다.
    - 데이터베이스로는 SQLite3를 사용합니다.
- 프로젝트 활용 도구: Git을 통해 협업하고 버전 관리를 진행하며, 프로젝트 관리 도구로는 Notion을 활용했습니다.
- ERD (Entity-Relationship Diagram): 데이터베이스 구조를 시각적으로 표현한 ERD를 사용하여 데이터베이스 설계를 합니다.
    
    ![MOPICK.png](/ERD.png)
    

## **기능 구현**

- 본 프로젝트의 구현된 기능은 다음과 같습니다:
    - **영화 검색**
        - 사용자는 특정 영화를 검색할 수 있습니다.
    - **배우 검색**
        - 사용자는 원하는 배우를 검색하여 해당 배우의 정보를 확인할 수 있습니다.
    - **TMDB 사이트에서 선정된 추천**
        - 프로젝트는 TMDB 사이트에서 제공하는 인기 있는 영화, 최신 영화, 사용자의 취향에 맞는 비슷한 영화, 추천 영화 등을 선정하여 사용자에게 추천해줍니다.
    - **영화 정보 상세 제공**
        - 사용자는 선택한 영화에 대한 상세 정보, 줄거리, 출연 배우 등을 확인할 수 있습니다.
    - **배우 정보 상세 제공**
        - 사용자는 선택한 배우에 대한 상세 정보, 출연한 영화 목록 등을 확인할 수 있습니다.
    - **소통을 위한 게시판**
        - 사용자들은 게시판을 통해 서로 소통할 수 있습니다. 이 게시판에는 영화나 배우에 관한 이야기, 추천 등 다양한 주제의 게시글이 작성될 수 있습니다.
    - **게시글 좋아요**
        - 사용자는 게시글에 좋아요를 표시하여 관심을 표현할 수 있습니다.
    - **게시글에 댓글**
        - 사용자는 게시글에 댓글을 작성하여 의견을 공유하거나 답글을 남길 수 있습니다.
    - **댓글 좋아요**
        - 사용자는 댓글에 좋아요를 표시하여 해당 댓글에 대한 관심을 표현할 수 있습니다.
    - **좋아하는 영화 선택**
        - 사용자는 자신이 좋아하는 영화를 선택하고, 이를 기반으로 새로운 영화 추천을 받을 수 있습니다.

## **설치 및 실행 방법**

### **서버 실행**

1. **가상 환경 설정**
    
    ```
    cd back-server
    python -m venv venv
    ```
    
2. **가상 환경 활성화**
    
    ```
    source venv/Scripts/activate
    ```
    
3. **의존성 설치**
    
    ```
    pip install -r requirements.txt
    ```
    
4. **데이터베이스 마이그레이션**
    
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata movies.json
    ```
    
5. **서버 실행**
    
    ```
    python manage.py runserver
    ```
    
6. **접속**: 웹 브라우저에서 `http://localhost:8000`으로 접속

### **Vue 실행**

1. 의존성 설치
 - bash 새로 열고
    ```
    cd front-server
    npm install
    ```
    
2. 서버 실행
    
    ```
    npm run serve
    ```
    

## **Router 정보**

| View | URL | 액션 또는 뮤테이션 |
| --- | --- | --- |
| ArticleView | /article | 자유게시판 url로 이동 |
| ArticleCreateView | /article/create | 게시물 업로드 url로 이동 |
| SignUpView | /signup | 회원가입 url로 이동 |
| LogInView | / | 로그인 url로 이동 |
| ArticleDetailView | /article/:id | 게시물 상세 페이지 url로 이동 |
| ArticleUpdateView | /article/:id/update | 게시물 업데이트 페이지 url로 이동 |
| BaseView | /base | 회원가입 또는 개인 선호 영화가 추천되지 않은 경우 해당 url로 이동 |
| MovieView | /movie | 메인페이지 url로 이동 |
| MovieDetailView | /movie/:id | 영화 상세 페이지 url로 이동 |
| SearchView | /search | 영화 또는 배우 검색 url로 이동 |
| UpdateView | /update | 개인정보 수정 url로 이동 |
| ProfileView | /profile/:id | 배우 상세 페이지 url로 이동 |
| RecoView | /reco | 개인 선호 영화 목록 페이지 url로 이동 |

## **팀원 정보 및 업무 분담 내역**

프로젝트의 업무는 기능단위로 분배했으며 다음과 같이 이루어졌습니다:

- 황재천
    - TMDB 사이트에서 선정된 추천 영화들 표시
    - 영화 또는 배우 검색
    - 영화 정보 상세 제공
    - 배우 정보 상세 제공
    - 좋아하는 영화 선택
- 고세훈:
    - 전체 게시글 목록 페이지 제작
    - 게시글 생성, 수정, 삭제, 조회 제작
    - 댓글 생성, 삭제, 조회 제작
    - 게시글, 댓글 좋아요 기능 구현

## **목표 서비스 구현 및 실제 구현 정도**

프로젝트의 목표는 MOPICK이라는 영화 추천 및 조회 기능을 포함하는 웹 서비스를 개발하는 것입니다. 아래는 목표 서비스와 실제 구현 정도에 대한 설명입니다:

1. **영화 검색**: 실제로 영화 검색 기능을 구현했습니다. 사용자는 원하는 영화를 검색할 수 있습니다.
2. **배우 검색**: 배우 검색 기능을 구현했습니다. 사용자는 원하는 배우를 검색하여 해당 배우의 정보를 확인할 수 있습니다.
3. **TMDB 사이트에서 선정된 추천**: 실제로 TMDB 사이트에서 제공하는 인기 있는 영화, 최신 영화, 사용자의 취향에 맞는 비슷한 영화, 추천 영화 등을 선정하여 사용자에게 추천해줍니다.
4. **영화 정보 상세 제공**: 영화에 대한 상세 정보, 줄거리, 출연 배우 등을 확인할 수 있는 기능을 구현했습니다.
5. **배우 정보 상세 제공**: 배우에 대한 상세 정보, 출연한 영화 목록 등을 확인할 수 있는 기능을 구현했습니다.
6. **소통을 위한 게시판**: 사용자들은 게시판을 통해 서로 소통할 수 있습니다. 이 게시판에는 영화나 배우에 관한 이야기, 추천 등 다양한 주제의 게시글이 작성될 수 있습니다.
7. **게시글 좋아요**: 사용자는 게시글에 좋아요를 표시하여 관심을 표현할 수 있습니다.
8. **게시글에 댓글**: 사용자는 게시글에 댓글을 작성하여 의견을 공유하거나 답글을 남길 수 있습니다.
9. **댓글 좋아요**: 사용자는 댓글에 좋아요를 표시하여 해당 댓글에 대한 관심을 표현할 수 있습니다.
10. **좋아하는 영화 고르고 새로 추천 받기**: 사용자는 자신이 좋아하는 영화를 선택하고, 이를 기반으로 새로운 영화 추천을 받을 수 있습니다.
11. 개인 프로필 및 팔로우 기능 : 구현하지 못하였습니다

## 느낀점, 후기

황재천

- 영화 추천 웹사이트를 제작했는데 정말 만족스러운 결과물이었습니다. 사용자들에게 맞춤형 영화 추천을 제공하고, 다양한 장르와 평점 기준으로 검색할 수 있는 기능을 구현했습니다. 또한, 사용자들의 리뷰와 평가를 수집하여 영화 추천에 반영하는 시스템을 구축했습니다. 사용자 친화적인 UI와 빠른 응답 속도로 웹사이트의 사용성을 높였습니다. 피드백을 통해 지속적으로 개선하고 발전시킬 예정입니다.

고세훈

- 제 첫 협업 프로젝트로 영화 추천 웹사이트를 만들어 보았습니다. 5개월 동안 개발을 배우고 프로젝트에 참여하면서 많은 것을 경험하고 배울 수 있었습니다. 그 경험은 매우 값진 것으로 생각됩니다.

- 프로젝트를 시작할 때는 많은 시행착오가 있을 것이라 예상했습니다. 개발 과정에서 문제가 발생하고, 어떤 기능을 구현해야 할지에 대한 고민이 있었습니다. 하지만 저희 팀은 함께 협력하여 이러한 에러에 대한 고민을 극복했습니다. 서로의 아이디어와 의견을 나누고, 문제를 해결하기 위해 적극적으로 노력했습니다. 그 결과로 저희는 그래도 만족할만한 영화 추천 웹사이트를 만들어냈습니다.

- 이 프로젝트를 통해 개발에 대한 실전 경험을 쌓을 수 있었습니다. 이론적인 개념을 배웠던 것을 실제로 적용해보면서 개발의 과정과 흐름을 이해할 수 있었습니다. 또한, 협업에 대한 중요성을 깨달았습니다. 팀원들과의 의사소통과 협력을 통해 프로젝트를 성공적으로 완료할 수 있었습니다.

- 이번 프로젝트에서 저희 팀은 영화 추천 웹사이트를 만들기 위해 다양한 기술과 도구를 사용했습니다. django와 vue, sqlite3, 등을 활용하여 웹사이트를 구축했습니다. 또한, 사용자들의 취향을 분석하여 개인 맞춤형 추천 기능을 구현했습니다. 이러한 기술들을 배우고 응용함으로써 저희는 만족스러운 웹사이트를 만들 수 있었습니다.

- 이 프로젝트를 통해 제 개인적인 성장을 많이 느낄 수 있었습니다. 처음에는 개발에 대한 자신감이 없었고, 협업에 대한 두려움도 있었습니다. 하지만 팀원과의 소통과 지속적인 노력 덕분에 이러한 부분들을 극복할 수 있었습니다. 개발 과정에서 발생한 문제들을 해결해 나가는 과정에서 새로운 도전에 대한 자신감을 갖게 되었고, 협업의 가치와 중요성을 깨달을 수 있었습니다. 뭐가 문제인지 몰라 막연히 어려움만 있었던 처음에 비해 서로 도움을 주고 받으며 발생한 버그를 디버깅해가며 한층 성장한 것 같습니다.

- 마지막으로, 이 프로젝트에 참여한 재천님에게 감사의 말씀을 전하고 싶습니다. 함께 노력하고 협력하여 우리가 만든 영화 추천 웹사이트에 자부심을 가질 수 있었습니다. 앞으로도 더 많은 협업 프로젝트에 참여하여 함께 성장해 나가고 싶습니다.