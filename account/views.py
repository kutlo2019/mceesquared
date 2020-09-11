from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate

from account.forms import RegistrationForm, StudentRegistrationForm, TutorRegistrationForm, EditProfileForm

account = get_user_model().objects.filter()

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
			if form.fields == 'STUDENT':
				return redirect('account:student_register')
			else:
				return redirect('account:tutor_register')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'registration/register.html', context)

def student_register(request):
	"""Register as a student"""
	context = {}
	if request.method != 'POST':
		# Display blank registration form
		form = StudentRegistrationForm()
	else:
		# Process the completed form
		form = StudentRegistrationForm(data=request.POST)
		if form.is_valid():
			account = form.save()
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password1')
			account.set_password(password)
			account.save()
			account.account_type = 'STUDENT'
			account = authenticate( email=email, password=password)
			login(request, account.get_user())
			return redirect('student_portals:index')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'registration/student_register.html', context)

def tutor_register(request):
	"""Register as a student"""
	context = {}
	if request.method != 'POST':
		# Display blank registration form
		form = TutorRegistrationForm()
	else:
		# Process the completed form
		form = TutorRegistrationForm(data=request.POST)
		if form.is_valid():
			account = form.save()
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password1')
			account.set_password(password)
			account.save()
			account.account_type = 'TUTOR'
			account = authenticate( email=email, password=password)
			login(request, account)
			return redirect('student_portals:index')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'registration/tutor_register.html', context)

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
