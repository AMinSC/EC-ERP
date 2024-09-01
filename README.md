# EC-ERP
ERP for ElectricCharging

[Django ERP Framework](https://django-erp-framework.readthedocs.io/en/latest/index.html) 를 사용해보려고 했으나,
Sample Tutorial에서 안내하는 메서드 미구현

## 스택
Python 3.12.4

Django 5.1


## 기간
08.26 ~ 08.30 : 기획 및 DB 정의

09.02 ~ 09.06 : 기술 선정

09.11 ~ : 구현 예정



#### [Figjam](https://www.figma.com/board/qfnAYMr465GPgesbUgnaJ2/%EC%A0%84%EA%B8%B0%EC%B6%A9%EC%A0%84%EC%86%8C_ERP?node-id=0-1&t=oOI0q1hnH0WGPg6D-0)
#### [ERD](https://www.erdcloud.com/d/x8CkAhn5bPjbQ5Zk2)
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
