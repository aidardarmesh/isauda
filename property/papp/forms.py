# encoding: utf-8
from django import forms
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

class UserLoginForm(forms.Form):
	username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Электронный адрес/логин*'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			if not User.objects.filter(username=username).exists():
				raise forms.ValidationError('Такого пользователя не существует')
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError('Неправильный пароль')
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия, имя*'}), 
		required=True)
	username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Электронный адрес/логин*'}),
		max_length=150)
	last_name = forms.CharField(
		widget=forms.TextInput(attrs={
			'placeholder': 'Номер телефона*',
			'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57' + 
							' || event.charCode == 43' + 
							' || event.charCode == 32' + 
							' || event.charCode == 40' + 
							' || event.charCode == 41' + 
							' || event.charCode == 45'}), 
		required=True)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля'}))
	
	class Meta:
		model = User
		fields = [
			'first_name',
			'username',
			'last_name',
			'password',
			'password2',
		]

	def clean(self):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError('Пароли должны совпадать')
		if User.objects.filter(username=self.cleaned_data['username']).exists():
			raise forms.ValidationError('Такой пользователь существует')

class UpdateProfileForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Новые фамилия, имя*'}), 
		required=False)
	username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Новый электронный адрес/логин*'}),
		max_length=150, required=False)
	last_name = forms.CharField(
		widget=forms.TextInput(attrs={
			'placeholder': 'Новый номер телефона*',
			'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57' + 
							' || event.charCode == 43' + 
							' || event.charCode == 32' + 
							' || event.charCode == 40' + 
							' || event.charCode == 41' + 
							' || event.charCode == 45'}), required=False)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите новый пароль'}),
		required=False)
	
	class Meta:
		model = User
		fields = [
			'first_name',
			'username',
			'last_name',
			'password',
		]

	def clean(self):
		username = self.cleaned_data.get('username')
		if username:
			if User.objects.filter(username=self.cleaned_data['username']).exists():
				raise forms.ValidationError('Такой email уже используется')