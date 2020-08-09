from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate

from account.forms import RegistrationForm, EditProfileForm
from .admin import UserCreationForm

user = get_user_model().objects.filter()

#queryset = get_user_model().objects.all()

def register(request):
	"""Register a new user."""
	context = {}
	if request.method != 'POST':
		# Display blank registration form
		form = RegistrationForm()
	else:
		# Process the completed form
		form = RegistrationForm(data=request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password1')
			user = authenticate( email=email, password=password)
			login(request, user)
			return redirect('student_portals:index')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'registration/register.html', context)

def edit_profile(request):

	if not request.user.is_authenticated:
		return redirect("account:login")

	context = {}

	if request.method =='POST':
		form = EditProfileForm(data=request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('student_portals:index')

	else:
		form = EditProfileForm(
				initial = {
					"email": request.user.email,
					"username": request.user.username,
				}
			)
	context = {'form': form}
	return render(request, 'account/edit_profile.html', context)
