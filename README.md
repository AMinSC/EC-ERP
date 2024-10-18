# EC-ERP
ERP for ElectricCharging with django project


### 기술 스택
[python 3.10.11](https://devguide.python.org/versions/)

[django 4.2](https://docs.djangoproject.com/ko/5.1/faq/install/#what-python-version-can-i-use-with-django)


### 과제 및 고민
- 과제
  - SECRET_KEY 재생성 및 보안상의 이유로 숨기기
- 고민
  - Foreign Key의 경우 related_name 참고해서 컬럼명 수정 고민
  - SQLite의 경우 db_comments 미지원 참고


### [Figjam](https://www.figma.com/board/qfnAYMr465GPgesbUgnaJ2/%EC%A0%84%EA%B8%B0%EC%B6%A9%EC%A0%84%EC%86%8C_ERP?node-id=0-1&t=oOI0q1hnH0WGPg6D-0)
### [ERD](https://www.erdcloud.com/d/x8CkAhn5bPjbQ5Zk2)
- **User** (사용자 테이블)
  - 실질적으로 ERP를 운영 및 관리 하는 사용자의 정보를 저장하는 테이블
- **Authority** (권한 테이블)
  - 사용자의 권한 등급을 저장하는 테이블
- **AuthorityMenu** (권한 메뉴 테이블)
  - 사용자의 권한과 연관된 작업들의 종류들이 저장된 테이블
- **InstallaionRequest** (설치 신청 테이블)
  - 전기충전소를 신청하는 테이블
  - 연관된 테이블(콤보, 사용자, 딜러)
- **ASRegister** (AS 신청 테이블)
  - 설치 신청 테이블 기반으로 AS를 신청하는 정보가 저장된 테이블
- **History** (상태 변경 이력 테이블)
  - 설치, AS 테이블의 변경 이력을 저장하는 테이블
- **Combo** (콤보 테이블)
  - 유동적인 옵션을 저장하는 테이블
- **Contractor** (업체[협력사] 테이블)
  - 협력사 정보가 저장된 테이블
- **Dealer** (딜러 테이블)
  - 딜러 정보가 저장된 테이블
- **Client** (설치 고객 정보 테이블)
  - 설치 고객 정보가 저장된 테이블


### [Django ERP Framework](https://github.com/RamezIssac/django-erp-framework)

해결하기 위해 미비된 라이브러리 재설치, 버전 도 맞춰봤으나 실패.

1. 정확히는 환경 세팅 및 호스팅은 가능하지만, admin 추가 시 에러 발생
2. 해결하기 위해 GitHub 코어 코드를 확인, 모듈 이름이 바뀐것 같아 수정.
3. (2) 메서드 인수 값 2개중 1개가 iterable 한 객체가 오지 않은 에러로 실행 불가..
4. iterable하지 않은 객체는 모델 객체로 확인되었고, 상속받은 클래스 또한 프레임워크 클래스인 것을 확인

장고 핵심 코어의 경우 학습 겸 수정해서 풀어갈 수 있지만, 사용하려는 프레임워크가 계속 발전되지 않을수도 있는점(23년이 마지막 커밋)과 더불어 핵심코어를 수정해가며 풀어가는 번거로움 까지 감안해서 적용하기 보단, 직접 만들어야겠다는 생각으로 중지
