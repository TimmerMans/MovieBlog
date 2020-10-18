from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('Email must be set')

		if not password:
			raise ValueError('Password must be set')

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.password = make_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		extra_fields.setdefault('is_active', True)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True')
		
		if extra_fields.get('is_superuser') is not True:			
			raise ValueError('Superuser must have is_superuser=True')
		
		return self._create_user(email, password, **extra_fields)
