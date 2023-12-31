

# **버그 브로핑 포스트 미니서버**

### **소개:**

버그 브로핑 포스트 미니서버는 회사 내에서 발생하는 다양한 버그들에 대해 소통하고 해결 방법을 공유하는 블로그 플랫폼입니다. 사용자는 간편하게 버그에 대한 정보를 작성하고, 태그를 통해 관련된 다른 버그들과 연결할 수 있습니다. 또한, 사용자들은 공유 대화 플랫폼을 통해 실시간으로 의견을 교환하고 해결 방법에 대해 토론할 수 있습니다.

## **요구사항 명세**

### **1. 버그 브로핑 포스트 미니서버**

- 사용자는 버그에 대한 정보를 블로그 형식으로 작성할 수 있어야 합니다.
- 작성된 포스트는 태그를 통해 관련된 버그들과 연결될 수 있어야 합니다.

### **2. 공유 대화 플랫폼**

- 사용자는 버그에 대해 논의하고 의견을 공유할 수 있는 대화 플랫폼을 사용할 수 있어야 합니다.

- 사용자는 채팅이나 댓글을 통해 다른 사용자와 소통할 수 있어야 합니다.
# WBS 
<br>

![스크린샷 2023-11-08 오전 9 15 18](https://github.com/sengwoong/venko/assets/92924243/52f4418e-506c-474f-8a7c-6e64f56b4b35)

<br>
# ERD

<img src="https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122683&authkey=%21ALDgiVxAOIGl1Nc&width=803&height=554" width="803" height="554" />

# 기술스택

- Git 🐙
- Django 🎸
- 템플릿 📄
- SQLite 🗄️

---

## **기능 및 요구사항 명세**

1. **게시물 관리 기능**
    - 사용자는 게시물을 작성할 수 있어야 합니다.
    - 작성된 게시물은 조회할 수 있어야 합니다.
2. **댓글 관리 기능**
    - 사용자는 게시물에 댓글을 작성할 수 있어야 합니다.
3. **파일 첨부 기능**
    - 게시물에는 파일을 첨부할 수 있어야 합니다.
    - 사용자는 첨부된 파일을 열람할 수 있어야 합니다.
4. **태그 관리 기능**
    - 사용자는 게시물에 태그를 추가하거나 검색할 수 있어야 합니다.
5. **로그인 권한 기능**
    - 로그인 한 유자만 게시물을 관리할 수 있어야 합니다.
6. **히스토리 관리 기능**
    - 시스템은 게시물의 히스토리를 관리할 수 있어야 합니다.


## **이벤트 스토밍**

### **1. 게시물 관리 기능**

- **이벤트**:
    - 게시물 작성 요청 (🟩)
    - 게시물 조회 요청 (🟦)
    - 파일 첨부 요청 (🟨)
- **액터**:
    - 사용자 (🟧)
- **명령**:
    - 게시물 작성 (🟩)
    - 게시물 조회 (🟦)
    - 파일 첨부 (🟨)

### **2. 댓글 및 대댓글 관리 기능**

- **이벤트**:
    - 댓글 작성 요청 (🟪)
- **액터**:
    - 사용자 (🟧)
- **명령**:
    - 댓글 작성 (🟪)

### **3.1 태그 관리 기능**

- **이벤트**:
    - 태그 추가 요청 (🟫)
    - 태그 검색 요청 (🟬)
- **액터**:
    - 사용자 (🟧)
- **명령**:
    - 태그 추가 (🟫)
    - 태그 검색 (🟬)

### **3.2 카테고리 관리 기능**

- **이벤트**:
    - 카테고리 추가 요청 (🟫)
    - 카테고리 검색 요청 (🟬)
- **액터**:
    - 사용자 (🟧)
- **명령**:
    - 카테고리 추가 (🟫)
    - 카테고리 검색 (🟬)

### **4. 히스토리 관리 기능**

- **이벤트**:
    - 히스토리 관리 요청 (🟭)
- **명령**:
    - 게시물 변경 이력 관리 (🟭)
- 🟩 : 게시물 작성 및 관리와 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 게시물과 관련된 주요 기능을 나타냅니다.
- 🟦 : 관리자와 관리 권한과 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 관리자와 관련된 주요 기능을 나타냅니다.
- 🟨 : 파일 첨부와 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 파일 관련 주요 기능을 나타냅니다.
- 🟪 : 댓글 작성과 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 댓글 관련 주요 기능을 나타냅니다.
- 🟫 : 카테고리 및 태그 추가와 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 태그 관련 주요 기능을 나타냅니다.
- 🟬 : 카테고리 및 태그 검색과 히스토리 관리 의 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 태그 관련 주요 기능을 나타냅니다.
- 🔴 : 관리자 권한 요청과 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 관리자 권한 관련 주요 기능을 나타냅니다.
- 🟧 : 사용자와 관련된 액터와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 사용자와 관련된 주요 기능을 나타냅니다.

### **Tube App URLs**

| URL 패턴 | 뷰 이름 | URL 역전시 이름 | 설명 |
| --- | --- | --- | --- |
| list/ | post_list | post_list | 포스트 목록을 보여주는 페이지입니다. |
| new/ | post_createView | post_create | 새로운 포스트를 생성하는 페이지입니다. |
| new/<int:pk>/ | post_create_detailView | post_create_detail | 포스트 게시글 생성하는 페이지입니다. |
| history_list/ | history_list | history_list | 포스트 히스토리 목록을 보여주는 페이지입니다. |
| detail/<int:pk>/ | post_detail | post_detail | 특정 포스트의 세부 정보를 보여주는 페이지입니다. |
| historydetail/<int:pk>/ | posthistory_detail | post_historydetail | 특정 포스트의 히스토리 세부 정보를 보여주는 페이지입니다. |
| delete-history/<int:pk>/ | post_delete_history | post_delete_history | 특정 포스트의 히스토리를 삭제하는 페이지입니다. |
| fine/<int:pk>/ | post_fine | post_fine | 포스트를 삭제하고 히스토리에 산입 |
| <int:pk>/comment | comment_new | comment_new | 포스트에 새로운 댓글을 작성하는 페이지입니다. |
| <int:pk>/comment/<int:parent_pk> | comment_reply_new | comment_reply_new | 특정 댓글에 대댓글을 작성하는 페이지입니다. |
| post/<int:pk>/delete/<int:tag_id> | delete_tag | tag_delete | 특정 태그를 삭제하는 페이지입니다. |
| <int:pk>/add_tag | add_tag | add_tag | 포스트에 태그를 추가하는 페이지입니다. |
| <int:pk>/post_new | add_post | add_post | 새로운 포스트를 추가하는 페이지입니다. |
| <int:pk>/edit/ | post_edit | post_edit | 포스트를 수정하는 페이지입니다. |
| <int:pk>/content_delete/ | content_delete | content_delete | 포스트의 내용을 삭제하는 페이지입니다. |
| comment/<int:pk>/edit/<int:commentpk> | comment_edit | comment_edit | 댓글을 수정하는 페이지입니다. |
| comment/<int:pk>/delete/<int:commentpk> | comment_delete | comment_delete | 댓글을 삭제하는 페이지입니다. |
 <br>
<br>
이 로직을 설계할 때는 유연성과 모듈화가 주요 고려 사항이었으며, 특히 항후 시스템이 확장 할경우를 대비하여 생각하였습니다<br>
에씨로 카프카를 사용할 때는 인설트 부분만 삭제하면 쉽게 구현할 수 있도록 만들었습니다.<br>
또한 삭제는 업데이트와 인설트와 달리 페이지 단위가 아닌 컴포넌트 단위로 발생하기 때문에 간단히 함수형으로 분리하여 만들었습니다.
 <br><br><br>
장점: <br>
모듈화: 함수를 분리함으로써 코드를 모듈화하여 유지 보수 및 관리를 용이하게 할 수 있습니다. <br>
가독성: 각 컴포넌트가 명확한 역할을 가지므로 코드를 이해하기 쉽고 가독성이 좋아집니다.<br>
유연성: 클래스와 함수를 분리함으로써 기능이 변경되거나 추가될 때 다른 부분에 영향을 덜 받고 수정이 용이합니다.<br>
<br><br>
단점:<br>
복잡성: 클래스와 함수를 분리하면서 프로젝트의 복잡성이 증가할 수 있습니다.<br>
관리의 어려움: 너무 많은 세분화가 있으면 관리하기가 어려워질 수 있습니다.<br>
오버엔지니어링: 일부 상황에서는 너무 많은 모듈화가 필요하지 않을 수 있으며, 이는 오버엔지니어링의 문제로 이어질 수 있습니다.<br><br>

###   **Accounts App URLs**

| URL 패턴 | 뷰 이름 | URL 역전시 이름 | 설명 |
| --- | --- | --- | --- |
| signup/ | signup | signup | 사용자 회원가입을 처리하는 페이지입니다. |
| login/ | login | login | 사용자 로그인을 처리하는 페이지입니다. |
| logout/ | logout | logout | 사용자 로그아웃을 처리하는 페이지입니다. |
| profile/ | profile | profile | 사용자 프로필 정보를 보여주는 페이지입니다. |
| profile_change/ | post_file_update | profile_change | 사용자 프로필 정보를 업데이트하는 페이지입니다. |
| profile_change/pass/ | change_password | profile_change_pass | 사용자 비밀번호를 변경하는 페이지입니다. |


---
## 고민
### 셀렉트 최적화 post 와 postHistory
![스크린샷 2023-11-08 오전 2 19 04](https://github.com/sengwoong/venko/assets/92924243/8aca3083-ef6d-4155-84a4-0bb592db0f4e)
<br><br><br>

id로 연결되어 있는 Post는 디비튜닝이 어렵다.
<br><br>
삽입이 많이 일어나는 로직이라 모듈화해서 조인하는 것이 맞는데,처음에는 id 값으로  스칼라 hash 힌트를 사용하여 아이디가 같음을 표현하여 효율적이게 조인하려 하였다.
<br><br>
하지만 그렇다고 하여도, 성능이 문제가 있을 것으로 판단하였다. 몽고디비를 사용하여 분리하는 것 또한 방법 이라고 생각하였으나, 현재 프로젝트는 sqllite 라는 디비기술이 확정된 상태였다.
<br><br>
그래서 마지막으로 "인데싱을 방해하며 수정이 불가능 한데 조인되는 로직"을 비즈니스 단계에서 생각해 보니 그러한 것들을 "postHistory"로 만들면 되겠다고 생각하였다.
postHistory란 Post에서 완료된 함수를 가지고 있는 모델이다. post에서 delect를 하면 자동으로 postHistory로 넘기기 위하여 다음과 같은 코드를 사용하였다.
아래 코드는 per_delete로 지워지기 전에 적절하게 로직을 넣을 수 있었다.<br><br><br><br>
```

@receiver(pre_delete, sender=Post)
def pre_delete_post(sender, instance, **kwargs):
    print("postsender")

    post_contents = []
    for content in instance.postcontents.all():
        content_description = f"{content.order}: {content.content}"
        if content.file_upload:
            content_description += f", {content.file_upload.path}"
        post_contents.append(content_description)
    print(post_contents)

    commentAllid = {}
    for comment in instance.comments.all():
        commentAllid[comment.id] = {
            "Front": comment.front_idx,
            "Back": comment.back_idx,
            "Context": comment.message,
            "Author": comment.author.username
        }

    print("commentFrontid")
    print(commentAllid)

    tags = ", ".join([tag.tag_name for tag in instance.tags.all()])

    post_history = PostHistory.objects.create(
        post_contents=json.dumps(post_contents),
        category=instance.category,
        title=instance.title,
        author=instance.author,
        view_count=instance.view_count,
        tags=tags,
        post_comments=json.dumps(commentAllid),
    )
    for content in instance.postcontents.all():
        if content.file_upload:
            image_instance = Image.objects.create(
            image=content.file_upload,  # 이미지 파일 자체를 저장
            post=post_history
        )
        post_history.images.add(image_instance)

```
<br><br><br>
---
## 기능

<br><br>
### 대댓글 (8시간 소유)
대댓글을 만들기 위해서 여러가지 방법을 생각하였다. 
<br>
<br>
연결 리스트로 만들기<br>
![스크린샷 2023-11-08 오전 8 26 14](https://github.com/sengwoong/venko/assets/92924243/b3f68fb7-b567-4f3b-bca1-1bda9c95d3f6)<br>
이중으로 연결된 리스트와 단순 연결 리스트가 있다. 그런데 단순 연결 시스템으로 만들었을 때 누가 부모인지 정하기 힘들어진다.<br>
그래서 이중 연결 시스템으로 자식 값이 지워지고, 그 자식에서 다시 자식을 지우는 작업을 Null이 나올 때까지 반복할 생각이었다.<br>
<br><br><br>
graph lookup 형태<br>
![스크린샷 2023-11-08 오전 8 32 21](https://github.com/sengwoong/venko/assets/92924243/db4ad15d-fe2d-4b9f-af13-306ac035adaa)<br>
위는 카테고리 데이터베이스이다. 연결 리스트로 만들다보니 자식을 검색하지 않으면 지워야 하는 목록이 무엇인지 조차 모를 수가 있다. 직계 자손(1단계 아래 자손)이 100만 개 있다면 검색을 100만 번 해야한다.<br>
단순히 배열에서 셀렉트와 딜리트를 한꺼번에 처리할 수 있는 선택지가 없어지는 것이다.<br>
그래서 필자는 부모 키 + 자손 키를 삽입하여 한 번에 자손을 전부 선택하고 지우는 것이 확장성 있고 좋은 아키텍처라고 생각하였다.<br>
만일 시스템이 확장된다면 몽고디비의 graph lookup을 사용하면 좋을 것 같다.<br>

```
data = {
    46: {'Front': None, 'Back': '48,49', 'Context': '46wagawg', 'Author': '<CustomUser: asdasd>'},
    47: {'Front': None, 'Back': None, 'Context': '47awegweag', 'Author': '<CustomUser: asdasd>'},
    48: {'Front': '46', 'Back': None, 'Context': '48awegwage', 'Author': '<CustomUser: asdasd>'},
    49: {'Front': '46', 'Back': '50', 'Context': '49awegaweg', 'Author': '<CustomUser: asdasd>'},
    50: {'Front': '49', 'Back': None, 'Context': '50ㅁㅈㅎㅁㅈㄷㅎ', 'Author': '<CustomUser: asdasd>'}
}



def extract_author_name(author):
    author_string =str(author)
    author_string = author_string.replace(" ", "")
    return author_string.replace(" ", "")



def print_structure(key, data):
    node = {
        "id": key,
        "Context": data[key]['Context'],
        "Author":extract_author_name( data[key]['Author']),
        "replies": []
    }
    if data[key]['Back'] is not None:
        print(key)
        back_values = data[key]['Back'].split(',')
        for back in back_values:
            node["replies"].append(print_structure(int(back), data))
    return node

final_result = [print_structure(key, data) for key, value in data.items() if value['Front'] is None]
print(final_result)


for comment in final_result:
    print(f"Replies for comment with id {comment['id']}:")
    for reply in comment['replies']:
        print(reply)
    print('\n')


```

<br><br><br>
---

---
## 트러블 슈팅<br>
get_object 가 여러번 발생하는 경우가 생겼다 그리고 새로고침하면 어뷰징으로 뷰수를 올리는 것이 가능했다.<br>
그래서 아래와 같이 캐쉬를 사용하여서 여러번 불러도 카운터가 오르지 않게 수정하였다. <br>
<br>
```
def get_object(self, queryset=None):
        print(queryset)
        print(self)
        pk = self.kwargs.get('pk')
        
        post = get_object_or_404(PostHistory, pk=pk)
        # Increment the view_count and save
        post.view_count += 1
        post.save()
        return post
```

---
## 블로그 프로젝트 화면 

### 블로그 리스트
![블로그 리스트](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122688&authkey=%21AJtpFQyXH8m2OQw&width=641&height=609)

### 블로그생성 및 컨텐츠 작성
![블로그생성 및 컨텐츠 작성](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122689&authkey=%21AHxHN4ykWHCuZb0&width=722&height=351)

### 블로그 검색 기능
![블로그 검색 기능](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122691&authkey=%21AOGIZH69ERBj9bk&width=713&height=433)<br>
카테고리< 테그 = 타이틀 
### 블로그 내용
![블로그 내용](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122685&authkey=%21AGRin2bITWBEvpE&width=1345&height=573)

### 블로그 이미지 두개이상 포스트
![블로그 이미지 두개이상 포스트](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122686&authkey=%21ALI_Bww27A_ndDc&width=604&height=651)

### 수정기능
![스크린샷 2023-11-08 오전 9 26 38](https://github.com/sengwoong/venko/assets/92924243/a74fc282-5d90-4701-ad2e-fdb597ddaf54)
![스크린샷 2023-11-08 오전 9 26 52](https://github.com/sengwoong/venko/assets/92924243/ef40b82f-170e-4172-b194-701b6ca0d269)

### 히스토리 페이지 리스트
![히스토리 페이지 리스트](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122684&authkey=%21AAdiZBvUJhwzUnw&width=626&height=503)

태그 와 타이틀 이너조인씨 성능문제 발생

### 히스토리 페이지 블로그 (삭제 가능)
![히스토리 페이지 블로그 (삭제 가능)](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122692&authkey=%21APKuS8vs_OEC68g&width=713&height=559)

### 메인페이지
![메인페이지](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122695&authkey=%21AEGSYXgzxwMB82I&width=560&height=365)

### 프로필 페이지
![프로필 페이지](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122696&authkey=%21AIoZ3CU2n3gdlfc&width=774&height=496)

### 로그인
![로그인](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122697&authkey=%21AHAU93OpFDxSe1g&width=742&height=223)

### 유저정보수정
![유저정보수정](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122698&authkey=%21AOVXoZEty75YWMc&width=1293&height=636)

### 비밀번호 변경
![비밀번호 변경](https://onedrive.live.com/embed?resid=9F97455DC8826EA7%2122699&authkey=%21ANjE63ccAUVp1Pc&width=1310&height=543)

<br><br>
```
.
├── aa.md
├── accounts
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── forms.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── views.cpython-311.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20231102_1123.py
│   │   ├── 0003_auto_20231102_1132.py
│   │   ├── 0004_alter_customuser_permission.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       ├── 0002_auto_20231102_1123.cpython-311.pyc
│   │       ├── 0003_auto_20231102_1132.cpython-311.pyc
│   │       ├── 0004_alter_customuser_permission.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── home
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── views.cpython-311.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── media
│   ├── awegawge.png
│   ├── awegawge_DkwS91a.png
│   ├── awegawge_ElESYrL.png
│   ├── awegawge_KHP4SDR.png
│   ├── awegawge_LlmCOoJ.png
│   ├── awegawge_W96QVvr.png
│   ├── awegawge_Xx5u6MS.png
│   ├── media
│   │   ├── 스크린샷_2023-11-07_오후_5.07.19.png
│   │   ├── 스크린샷_2023-11-07_시간_07.16.50_2.png
│   │   ├── 스크린샷_2023-11-07_시간_08.15.49_2.png
│   │   ├── 스크린샷_2023-11-07_시간_08.15.49_2_Dh5Xl1s.png
│   │   ├── 스크린샷_2023-11-07_시간_09.06.35_1.png
│   │   ├── 스크린샷_2023-11-07_시간_09.06.35_2.png
│   │   ├── 스크린샷_2023-11-07_시간_09.06.35_2_JjNZuAN.png
│   │   ├── 스크린샷_2023-11-07_시간_09.11.56_2.png
│   │   ├── 스크린샷_2023-11-07_시간_09.11.56_2_1RETx63.png
│   │   ├── 스크린샷_2023-11-07_시간_09.11.56_2_DwW69IV.png
│   │   ├── 스크린샷_2023-11-07_시간_09.11.56_2_Q1gSRYJ.png
│   │   ├── 스크린샷_2023-11-07_시간_09.11.56_2_m8PbEDc.png
│   │   ├── 스크린샷_2023-11-07_시간_10.11.47_1.png
│   │   └── 스크린샷_2023-11-07_시간_10.13.32_1.png
│   ├── tube
│   │   ├── files
│   │   │   └── 2023
│   │   │       └── 10
│   │   │           └── 27
│   │   │               └── 그림1.png
│   │   └── images
│   │       └── 2023
│   │           └── 10
│   │               ├── 26
│   │               │   └── 그림1.png
│   │               └── 27
│   │                   └── 그림1.png
│   ├── 스크린샷 2023-11-07 시간: 09.06.35 [2].png
│   └── 스크린샷 2023-11-07 시간: 09.11.56 [1].png
├── readme.md
├── static
│   └── media
│       ├── 스크린샷 2023-11-07 시간: 08.15.49 [1].png
│       ├── 스크린샷 2023-11-07 시간: 09.06.35 [2].png
│       ├── 스크린샷 2023-11-07 시간: 09.11.56 [2].png
│       └── 스크린샷 2023-11-07 시간: 10.11.47 [2].png
├── templates
│   ├── accounts
│   │   ├── change_password.html
│   │   ├── edit_profile.html
│   │   ├── form.html
│   │   └── profile.html
│   ├── home
│   │   └── index.html
│   └── tube
│       ├── form.html
│       ├── form_detail.html
│       ├── post_confirm_delete.html
│       ├── post_detail.html
│       ├── post_history_list.html
│       ├── post_list.html
│       └── posthistory_detail.html
├── tube
│   ├── Delect.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── admin.cpython-311.pyc
│   │   ├── af.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── forms.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── postHistory.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── views.cpython-311.pyc
│   ├── admin.py
│   ├── af.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20231102_1338.py
│   │   ├── 0003_auto_20231102_1415.py
│   │   ├── 0004_auto_20231102_1441.py
│   │   ├── 0005_rename_name_tag_tag_name.py
│   │   ├── 0006_auto_20231102_1536.py
│   │   ├── 0007_auto_20231102_1650.py
│   │   ├── 0008_auto_20231102_1651.py
│   │   ├── 0009_auto_20231102_1813.py
│   │   ├── 0010_auto_20231102_1840.py
│   │   ├── 0011_post_post_contents.py
│   │   ├── 0012_auto_20231102_1849.py
│   │   ├── 0013_auto_20231102_1912.py
│   │   ├── 0014_auto_20231102_1917.py
│   │   ├── 0015_auto_20231102_2253.py
│   │   ├── 0016_auto_20231106_1421.py
│   │   ├── 0017_remove_post_read_author.py
│   │   ├── 0018_alter_posthistory_tags.py
│   │   ├── 0019_auto_20231107_0616.py
│   │   ├── 0020_posthistory_post_comments.py
│   │   ├── 0021_alter_postcontent_file_upload.py
│   │   ├── 0022_alter_postcontent_file_upload.py
│   │   ├── 0023_auto_20231107_1542.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       ├── 0002_auto_20231102_1338.cpython-311.pyc
│   │       ├── 0003_auto_20231102_1415.cpython-311.pyc
│   │       ├── 0004_auto_20231102_1441.cpython-311.pyc
│   │       ├── 0005_rename_name_tag_tag_name.cpython-311.pyc
│   │       ├── 0006_auto_20231102_1536.cpython-311.pyc
│   │       ├── 0007_auto_20231102_1650.cpython-311.pyc
│   │       ├── 0008_auto_20231102_1651.cpython-311.pyc
│   │       ├── 0009_auto_20231102_1813.cpython-311.pyc
│   │       ├── 0010_auto_20231102_1840.cpython-311.pyc
│   │       ├── 0011_post_post_contents.cpython-311.pyc
│   │       ├── 0012_auto_20231102_1849.cpython-311.pyc
│   │       ├── 0013_auto_20231102_1912.cpython-311.pyc
│   │       ├── 0014_auto_20231102_1917.cpython-311.pyc
│   │       ├── 0015_auto_20231102_2253.cpython-311.pyc
│   │       ├── 0016_auto_20231106_1421.cpython-311.pyc
│   │       ├── 0017_remove_post_read_author.cpython-311.pyc
│   │       ├── 0018_alter_posthistory_tags.cpython-311.pyc
│   │       ├── 0019_auto_20231107_0616.cpython-311.pyc
│   │       ├── 0020_posthistory_post_comments.cpython-311.pyc
│   │       ├── 0021_alter_postcontent_file_upload.cpython-311.pyc
│   │       ├── 0022_alter_postcontent_file_upload.cpython-311.pyc
│   │       ├── 0023_auto_20231107_1542.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── postHistory.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── tutorialdjango
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   ├── settings.cpython-311.pyc
    │   ├── urls.cpython-311.pyc
    │   └── wsgi.cpython-311.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
