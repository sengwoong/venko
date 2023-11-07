

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

# ERD

![스크린샷 2023-11-07 오후 4.41.12.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_4.41.12.png)

# 기술스택

- Git 🐙
- Django 🎸
- 템플릿 📄
- SQLite 🗄️

---

## **요구사항 명세**

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
5. **관리자 권한 기능**
    - 관리자는 게시물 및 사용자를 관리할 수 있어야 합니다.
6. **히스토리 관리 기능**
    - 시스템은 게시물의 히스토리를 관리할 수 있어야 합니다.

---

## **기능 요구사항 명세**

1. **게시물 관련 기능**
    - 게시물 작성 및 조회 기능을 구현해야 합니다.
2. **댓글 관련 기능**
    - 사용자가 게시물에 댓글을 작성할 수 있어야 합니다.
3. **파일 관련 기능**
    - 첨부 파일을 열람및 저장을 할 수 있는 기능을 추가해야 합니다.
4. **태그 관련 기능**
    - 사용자가 게시물에 태그를 추가하거나 검색할 수 있어야 합니다.
5. 로그인 **관련 기능**
    - 로그인을 한 사람만 사용이 가능 해야합니다. 기능을 가져야 합니다.
6. **히스토리 관련 기능**
    - 게시물의 변경 이력을 관리할 수 있는 기능을 추가해야 합니다.

## **이벤트 스토밍**

### **1. 게시물 관리 기능**

- **이벤트**:
    - 게시물 작성 요청 (🟩)
    - 게시물 조회 요청 (🟦)
    - 파일 첨부 요청 (🟨)
- **액터**:
    - 사용자 (🟧)
    - 시스템 (🟥)
- **명령**:
    - 게시물 작성 (🟩)
    - 게시물 조회 (🟦)
    - 파일 첨부 (🟨)

### **2. 댓글 관리 기능**

- **이벤트**:
    - 댓글 작성 요청 (🟪)
- **액터**:
    - 사용자 (🟧)
    - 시스템 (🟥)
- **명령**:
    - 댓글 작성 (🟪)

### **3. 태그 관리 기능**

- **이벤트**:
    - 태그 추가 요청 (🟫)
    - 태그 검색 요청 (🟬)
- **액터**:
    - 사용자 (🟧)
    - 시스템 (🟥)
- **명령**:
    - 태그 추가 (🟫)
    - 태그 검색 (🟬)

### 4**. 히스토리 관리 기능**

- **이벤트**:
    - 히스토리 관리 요청 (🟭)
- **액터**:
    - 시스템 (🟥)
- **명령**:
    - 게시물 변경 이력 관리 (🟭)
- 🟩 : 게시물 작성 및 관리와 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 게시물과 관련된 주요 기능을 나타냅니다.
- 🟦 : 관리자와 관리 권한과 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 관리자와 관련된 주요 기능을 나타냅니다.
- 🟨 : 파일 첨부와 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 파일 관련 주요 기능을 나타냅니다.
- 🟪 : 댓글 작성과 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 댓글 관련 주요 기능을 나타냅니다.
- 🟫 : 태그 추가와 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 태그 관련 주요 기능을 나타냅니다.
- 🟬 : 태그 검색과 히스토리 관리 의 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 태그 관련 주요 기능을 나타냅니다.
- 🔴 : 관리자 권한 요청과 관련된 이벤트와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 관리자 권한 관련 주요 기능을 나타냅니다.
- 🟥 : 시스템과 관련된 액터와 명령을 나타냅니다. 이벤트 스토밍에서 이 색상은 시스템과 관련된 주요 기능을 나타냅니다.
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

### **Accounts App URLs**

| URL 패턴 | 뷰 이름 | URL 역전시 이름 | 설명 |
| --- | --- | --- | --- |
| signup/ | signup | signup | 사용자 회원가입을 처리하는 페이지입니다. |
| login/ | login | login | 사용자 로그인을 처리하는 페이지입니다. |
| logout/ | logout | logout | 사용자 로그아웃을 처리하는 페이지입니다. |
| profile/ | profile | profile | 사용자 프로필 정보를 보여주는 페이지입니다. |
| profile_change/ | post_file_update | profile_change | 사용자 프로필 정보를 업데이트하는 페이지입니다. |
| profile_change/pass/ | change_password | profile_change_pass | 사용자 비밀번호를 변경하는 페이지입니다. |

![스크린샷 2023-11-07 오후 5.27.50.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.27.50.png)

페이지만들기 + 페이지 내용물 넣기

![스크린샷 2023-11-07 오후 5.19.31.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.19.31.png)

![스크린샷 2023-11-07 오후 5.22.31.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.22.31.png)

전체 페이지 및 카테고리및 태그검색

![스크린샷 2023-11-07 오후 5.28.49.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.28.49.png)

![스크린샷 2023-11-07 오후 5.30.12.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.30.12.png)

![스크린샷 2023-11-07 오후 5.30.27.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.30.27.png)

상세 페이지 포스팅 모습 (여러 이미지 업로드 가능)

![스크린샷 2023-11-07 오후 5.16.40.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.16.40.png)

![스크린샷 2023-11-07 오후 5.36.17.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.36.17.png)

태그 및 상세 상세 페이지 대댓글 및 처리상태변경

![스크린샷 2023-11-07 오후 5.16.55.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.16.55.png)

![스크린샷 2023-11-07 오후 5.46.58.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.46.58.png)

![스크린샷 2023-11-07 오후 5.18.30.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.18.30.png)

완료 목록

![스크린샷 2023-11-07 오후 5.37.23.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.37.23.png)

내용 지우기(변경) 이후에 상세 페이지 보기(변경불가)
진짜로 삭제 하기 

![스크린샷 2023-11-07 오후 5.44.26.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.44.26.png)

![스크린샷 2023-11-07 오후 5.44.48.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.44.48.png)

![스크린샷 2023-11-07 오후 5.45.40.png](%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%B7%202860a4badbf3451fbd59a5c894ee8bc7/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_5.45.40.png)