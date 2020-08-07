from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate


from .admin import UserCreationForm

user = get_user_model().objects.filter()

#queryset = get_user_model().objects.all()

def register(request):
	"""Register a new user."""
	if request.method != 'POST':
		# Display blank registration form
		form = UserCreationForm()
	else:
		# Process the completed form
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			#new_user = form.save()
			email = request.POST['email']
			password = request.POST['password1']
			form = authenticate(request, email=email, password=password)
			login(request, form)
			return redirect('student_portals:index')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'registration/register.html', context)