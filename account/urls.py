"""Define URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'account'
urlpatterns = [
	# Include default auth urls.
	path('accounts/', include('django.contrib.auth.urls')),
	# Registration page
	path('register/', views.register, name='register'),
	# Edit profile
	path('edit_profile/', views.edit_profile, name='edit_profile')
]