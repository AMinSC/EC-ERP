from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """
    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Create a new superuser profile """
        user = self.create_user(email,name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class AuthorityMenu(models.Model):
    authority_menu_code = models.BigAutoField(unique=True, primary_key=True, db_comment="권한 메뉴 ID")
    authority_menu_name = models.CharField(max_length=255, db_comment="권한 메뉴 이름")

    def __str__(self) -> str:
        return self.authority_menu_name


class Authority(models.Model):
    authority_id = models.CharField(max_length=255, unique=True, primary_key=True, db_comment="권한 ID")
    authority_name = models.CharField(max_length=20, db_comment="권한 이름")
    authority_menu = models.CharField(max_length=255, db_comment="권한 메뉴")
    authority_level_code = models.CharField(max_length=255, db_comment="권한 단계")

    def __str__(self) -> str:
        return self.authority_name


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True, primary_key=True, db_comment="관리자 이메일")
    Authority_id = models.ForeignKey(Authority, on_delete=models.CASCADE, related_name='authority_id', db_comment="관리자 권한")
    name = models.CharField(max_length=20, db_comment="관리자 이름")
    addr = models.CharField(max_length=255, db_comment="관리자 주소")
    addr2 = models.CharField(max_length=255, db_comment="관리자 상세 주소")
    phone = models.CharField(max_length=11, db_comment="관리자 연락처")
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dormant = models.BooleanField(default=False, db_comment="휴면계정 여부")


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self) -> str:
        """ Return string representation of our user """
        return self.email


class Dealer(models.Model):
    dealer_id = models.BigAutoField(unique=True, primary_key=True, db_comment="딜러 ID")
    dealer_name = models.CharField(max_length=20, db_comment="딜러 이름")
    dealer_phone = models.CharField(max_length=11, db_comment="딜러 연락처")
    dealer_branch = models.CharField(max_length=255, db_comment="딜러 지점")
    dealer_loc = models.CharField(max_length=255, db_comment="딜러 지역")



class Client(models.Model):
    client_id = models.BigAutoField(unique=True, primary_key=True, db_comment="고객 ID")
    client_name = models.CharField(max_length=20, db_comment="고객 이름")
    building_type = models.CharField(max_length=255, db_comment="고객 건물 형식")
    client_phone = models.CharField(max_length=11, db_comment="고객 연락처")
    client_email = models.CharField(max_length=40, db_comment="고객 이메일")
    client_addr1 = models.CharField(max_length=255, db_comment="고객 주소")
    client_addr2 = models.CharField(max_length=255, db_comment="고객 상세 주소")
    client_state = models.CharField(max_length=10, db_comment="?")


class InstallationRequest(models.Model):
    ist_req_contract_num = models.BigAutoField(unique=True, primary_key=True, db_comment="계약 번호")
    reception_num = models.CharField(max_length=20, db_comment="접수 번호")
    user_email = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_email', db_comment="이메일(담당자)")
    dealer_id = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_id', db_comment="딜러 번호")
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_id', db_comment="고객 번호")
    ist_req_date = models.DateTimeField(auto_now_add=True, db_comment="접수일")
    ist_req_vehi_num = models.CharField(max_length=10, db_comment="신청 대수")
    ist_req_type = models.CharField(max_length=20, db_comment="구분 (개인, 법인)")
    ist_req_visit_date = models.DateTimeField(db_comment="실사 희망일시")
    ist_req_cancel_msg = models.TextField(db_comment="메세지")
    ist_req_cancel_reason = models.TextField(db_comment="취소 사유")
    ist_req_cancel_date = models.DateTimeField(db_comment="취소 일시")
    ist_req_state = models.CharField(max_length=10, db_comment="진행 상태")


class ASRegister(models.Model):
    as_register_num = models.BigAutoField(unique=True, primary_key=True, db_comment="AS 접수번호")
    ist_req_contract_num = models.ForeignKey(InstallationRequest, on_delete=models.CASCADE, related_name="ist_id", db_comment="계약 번호")
    as_engineer = models.CharField(max_length=20, db_comment="AS 설치기사")
    as_date = models.DateTimeField(db_comment="AS 방문 희망일")
    as_detail = models.TextField(db_comment="AS 내용")
    as_cancellation = models.TextField(db_comment="AS 취소 사유")
    as_cancellation_date = models.DateTimeField(db_comment="AS 취소일자")
    as_state = models.CharField(max_length=10, db_comment="AS 상태값")


class History(models.Model):
    ist_req_contract_num = models.ForeignKey(InstallationRequest, on_delete=models.CASCADE, related_name="ist_id", db_comment="설치 계약 번호")
    sqno_num = models.BigAutoField(unique=True, primary_key=True, db_comment="상태변경 ID")
    history_update_name = models.CharField(max_length=20, db_comment="변경자")
    history_update_date = models.DateTimeField(db_comment="변경 일시")
    history_before_state = models.CharField(max_length=10, db_comment="변경 전 상태")
    history_after_state = models.CharField(max_length=10, db_comment="변경 후 상태")
    history_asir = models.CharField(max_length=255, db_comment="설치 AS 구분")


class Contractor(models.Model):
    contractor_id = models.CharField(max_length=20, unique=True, primary_key=True, db_comment="업체 아이디")
    contractor_name = models.CharField(max_length=20, db_comment="업체명")
    contractor_email = models.CharField(max_length=40, db_comment="업체 이메일")
    contractor_tel = models.CharField(max_length=11, db_comment="업체 전화번호")
    contractor_business_info = models.CharField(max_length=255, db_comment="사업정보")
    contractor_state = models.CharField(max_length=10, db_comment="상태값")
    business_name = models.CharField(max_length=255, db_comment="사업명")


class Combo(models.Model):
    combo_code = models.CharField(max_length=8, unique=True, primary_key=True, db_comment="콤보 코드")
    combo_name = models.CharField(max_length=20, db_comment="콤보 이름")
    combo_title = models.CharField(max_length=20, db_comment="콤보 제목")
    combo_state = models.CharField(max_length=10, db_comment="상태값")
