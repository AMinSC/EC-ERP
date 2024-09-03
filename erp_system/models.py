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
    authority_name = models.CharField(max_length=255, db_comment="권한 이름")
    authority_menu = models.CharField(max_length=255, db_comment="권한 메뉴")
    authority_level_code = models.CharField(max_length=255, db_comment="권한 단계")

    def __str__(self) -> str:
        return self.authority_name


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True, primary_key=True, db_comment="관리자 이메일")
    Authority_id = models.ForeignKey(Authority, on_delete=models.CASCADE, related_name='authority_id', db_comment="관리자 권한")
    name = models.CharField(max_length=255, db_comment="관리자 이름")
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
    dealer_name = models.CharField(max_length=255, db_comment="딜러 이름")
    dealer_phone = models.CharField(max_length=11, db_comment="딜러 연락처")
    dealer_branch = models.CharField(max_length=255, db_comment="딜러 지점")
    dealer_loc = models.CharField(max_length=255, db_comment="딜러 지역")



class Client(models.Model):
    client_id = models.BigAutoField(unique=True, primary_key=True, db_comment="고객 ID")
    client_name = models.CharField(max_length=255, db_comment="고객 이름")
    building_type = models.CharField(max_length=255, db_comment="고객 건물 형식")
    client_phone = models.CharField(max_length=11, db_comment="고객 연락처")
    client_email = models.CharField(max_length=255, db_comment="고객 이메일")
    client_addr1 = models.CharField(max_length=255, db_comment="고객 주소")
    client_addr2 = models.CharField(max_length=255, db_comment="고객 상세 주소")
    client_state = models.CharField(max_length=255, db_comment="?")


class InstallationRequest(models.Model):
    ist_req_contract_num = models.BigAutoField(unique=True, primary_key=True)
    reception_num = models.CharField(max_length=255)
    user_email = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_email')
    dealer_id = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_id')
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_id')
    ist_req_date = models.DateTimeField(auto_now_add=True)
    ist_req_vehi_num = models.CharField(max_length=10)
    ist_req_type = models.CharField(max_length=255)
    ist_req_visit_date = models.DateTimeField()
    ist_req_cancle_msg = models.TextField()
    ist_req_cancle_reason = models.TextField()
    ist_req_cancle_date = models.DateTimeField()
    ist_req_state = models.CharField(max_length=255)


class History(models.Model):
    pass


class ASRegister(models.Model):
    pass


class Contractor(models.Model):
    pass


class Combo(models.Model):
    pass

