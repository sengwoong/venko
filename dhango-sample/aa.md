믹스인 정리
공식 문서: https://docs.djangoproject.com/en/4.2/ref/class-based-views/mixins/

인증 관련 믹스인:
LoginRequiredMixin: 사용자가 로그인 되어 있을 경우에만 뷰에 접근을 허용합니다.
PermissionRequiredMixin: 사용자에게 특정 권한이 있을 경우에만 뷰에 접근을 허용합니다.
UserPassesTestMixin: test_func() 메서드를 오버라이드하여 사용자가 특정 테스트를 통과할 경우에만 뷰에 접근을 허용합니다.

폼 관련 믹스인:
FormMixin: 폼과 관련된 기본 기능 (폼 인스턴스 생성, 폼 데이터 저장 등)을 제공합니다.
ModelFormMixin: 모델 폼과 관련된 작업에 필요한 메서드를 제공합니다.

리스트 뷰 관련 믹스인:
MultipleObjectMixin: 여러 객체를 처리하는 뷰 (예: 리스트 뷰)에 공통적으로 사용되는 메서드나 속성을 제공합니다.
SingleObjectMixin: 단일 객체를 처리하는 뷰에 필요한 메서드나 속성을 제공합니다.

페이징 관련 믹스인:
MultipleObjectPaginationMixin: 여러 객체를 페이지 단위로 표시하기 위한 페이징 처리 기능을 제공합니다.

상세 뷰 관련 믹스인:
SingleObjectMixin: 단일 객체에 대한 상세 정보를 제공하는 뷰에서 사용되는 메서드와 속성을 제공합니다.

기타 믹스인:
ContextMixin: 컨텍스트 데이터를 뷰에 추가하는 메서드를 제공합니다.
TemplateResponseMixin: 템플릿을 사용하여 응답을 생성하는 메서드를 제공합니다.
RedirectView: 뷰를 다른 URL로 리다이렉트하는 기능을 제공합니다.

sqlite3 db.sqlite3      