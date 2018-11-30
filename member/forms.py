from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['username', 'password']
        fields_placeholder = {
            'username': '이름',
            'password': '비밀번호'
        }
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': fields_placeholder[field_name]
            })

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['password1', 'password2']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })
        class_update_fields = ['username', 'password1', 'password2']
        fields_placeholder = {
            'username': '이름',
            'password1': '비밀번호',
            'password2': '비밀번호 확인'
        }
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'placeholder': fields_placeholder[field_name]
            })

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
