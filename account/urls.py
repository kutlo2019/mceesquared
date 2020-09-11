"""Define URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'account'
urlpatterns = [
	# Include default auth urls.
	path('accounts/', include('django.contrib.auth.urls')),
	# Registration page
	path('register/', views.register, name='register'),
	# Student register
	path('register/student_register', views.student_register, name='student_register'),
	# Tutor register
	path('register/tutor_register', views.tutor_register, name='tutor_register'),
	# Edit profile
	path('edit_profile/', views.edit_profile, name='edit_profile'),
]