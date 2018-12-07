from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import *
from django.contrib.admin.widgets import AdminDateWidget


class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)


class TeacherRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'UserName'}))
    first_name = forms.CharField(max_length=30, required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'FirstName'}))
    last_name = forms.CharField(max_length=30, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'LastName'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))
    admin_id = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'college code'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'admin_id'
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        admin_id = cleaned_data.get('admin_id')

        print('did clean run?')

        if password != confirm_password:
            print('are password not equal?')
            self.add_error('password', 'Password Did Not Match')

        if admin_id != '12345':
            print('Yes it is right')
            self.add_error('admin_id', 'Admin id does not match')


class StudentRegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'UserName'}))
    first_name = forms.CharField(max_length=30, required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'FirstName'}))
    last_name = forms.CharField(max_length=30, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'LastName'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        print('did clean run?')

        if password != confirm_password:
            print('are password not equal?')
            self.add_error('password', 'Password Did Not Match')



class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields= ('first_name' , 'last_name' ,'password')

class passwordchange(PasswordChangeForm):
    class Meta:
        model=User
        fields =('old_password','new_password1','new_password2')

class ProfileUpdateForm(forms.ModelForm):
    #dob = forms.DateField(widget=DatePicker(options={"format": "YYYY-MM-DD"}, fontawesome=True))
    photo=forms.ImageField()
    class Meta:
        model = Student
        fields= ('dob' , 'photo')
    ''' def save(self, user=None):
        user_profile = super(ProfileUpdateForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile'''


class TeacherProUpdateForm(forms.ModelForm):
    #dob = forms.DateField(widget=DatePicker(options={"format": "YYYY-MM-DD"}, fontawesome=True))
    class Meta:
        model = Teacher
        fields= ('dob' , 'photo')