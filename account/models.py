from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, date_of_birth, password=None):
		"""
		Creates and saves an account with the given email, password
		and username
		"""
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			date_of_birth=date_of_birth,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		"""
		Creates and saves a superuser with the given email and password
		"""
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):

	class Types(models.TextChoices):
		STUDENT = "STUDENT", "Student"
		TUTOR = "TUTOR", "Tutor"

	class StudentClass(models.TextChoices):
		STD1  = '1', "Standard 1"
		STD2  = '2', "Standard 2"
		STD3  = '3', "Standard 3"
		STD4  = '4', "Standard 4"
		STD5  = '5', "Standard 5"
		STD6  = '6', "Standard 6"
		STD7  = '7', "Standard 7"
		STD8  = '8', "Form 1"
		STD9  = '9', "Form 2"
		STD10 = '10', "Form 3"
		STD11 = '11', "Form 4"
		STD12 = '12', "Form 5"

	account_type 			= models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.STUDENT)

	email 					= models.EmailField(verbose_name="email", max_length=200, unique=True)
	username				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	date_of_birth			= models.DateField()
	school_attending		= models.CharField(max_length=100)
	current_class 			= models.CharField(_('Type'), max_length=50, choices=StudentClass.choices)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	objects = MyAccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'date_of_birth', 'account_type' ]

	def __str__(self):
		return self.email 

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True

class StudentManager(models.Manager):
	def get_query_set(self, *args, **kwargs):
		return super().get_query_set(*args, **kwargs).filter(type=Account.Types.STUDENT)

class TutorManager(models.Manager):
	def get_query_set(self, *args, **kwargs):
		return super().get_query_set(*args, **kwargs).filter(type=Account.Types.TUTOR)

class Student(Account):
	"""docstring for Student"""
	objects = StudentManager()

	class Meta:
		proxy = True

	def save(self, *args, **kwargs):
		if not self.pk:
			self.type = Account.Types.STUDENT
		return super().save(*args, **kwargs)

	REQUIRED_FIELDS = ['username', 'date_of_birth', 'school_attending', 'current_class' ]

class Tutor(Account):
	"""docstring for Student"""
	objects = TutorManager()
	#students = models.ManyToManyField(Student)

	class Meta:
		proxy = True

	#is_staff				= models.BooleanField(default=True)
	def save(self, *args, **kwargs):
		if not self.pk:
			self.type = Account.Types.STUDENT
		return super().save(*args, **kwargs)
		return True