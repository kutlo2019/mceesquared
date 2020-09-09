from django import forms
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import Account, Student

class RegistrationForm(forms.ModelForm):
	"""docstring for RegistrationForm"""
	class Meta:
		model = Account
		fields = ("account_type")
	

class TutorRegistrationForm(forms.ModelForm):
	"""Tutor Registration form"""
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')
	username = forms.CharField(max_length=60, help_text='Required. Add a valid email username.')

	class Meta:
		model = Account
		fields = ("email", "username", "date_of_birth", "password1", "password2")

		def clean_password2(self):
			# Check that the two password entries match
			password1 = self.cleaned_data.get("password1")
			password2 = self.cleaned_data.get("password2")
			if password1 and password2 and password1 != password2:
				raise forms.ValidationError("Passwords don't match")
			return password2

		def save(self, commit=True):
			# Save the provided password in hashed format
			user = super(UserCreationForm, self).save(commit=False)
			user.set_password(self.cleaned_data["password1"])
			if commit:
				user.save()
			return user

class StudentRegistrationForm(TutorRegistrationForm):
	"""Tutor Registration form"""
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')
	username = forms.CharField(max_length=60, help_text='Required. Add a valid email username.')

	class Meta:
		model = Account
		fields = ("email", "username", "date_of_birth", "school_attending", "password1", "password2")

		def clean_password2(self):
			# Check that the two password entries match
			password1 = self.cleaned_data.get("password1")
			password2 = self.cleaned_data.get("password2")
			if password1 and password2 and password1 != password2:
				raise forms.ValidationError("Passwords don't match")
			return password2

		def save(self, commit=True):
			# Save the provided password in hashed format
			user = super(UserCreationForm, self).save(commit=False)
			user.set_password(self.cleaned_data["password1"])
			if commit:
				user.save()
			return user


class EditProfileForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email', 'username', 'password', 'date_of_birth')

	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
			except Account.DoesNotExist:
				return email
			raise forms.ValidationError('Email "%s" is already in use.' % account.email)

	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
			except Account.DoesNotExist:
				return username
			raise forms.ValidationError('Username "%s" is already in use.' % account.username)

	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		# This is done here, rather than on the field, because the
		# field does not have access to the initial value
		return self.initial["password"]


class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances
	form = RegistrationForm
	add_form = EditProfileForm

	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('email', 'is_admin')
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('date_of_birth',)}),
		('Permissions', {'fields': ('is_admin',)}),
)
	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'date_of_birth', 'password1', 'password2')}
	),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

# Now register the new UserAdmin...
#admin.site.register(StudentAccount, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)