from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile, Skill
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', "email", "username", 'password1', 'password2']
        labels = {
            'first_name': 'Name',
            'email': 'Email'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "input",
                "placeholder": f"Add {' '.join(name.split('_'))}",
            })


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "username", "email", "short_intro", "bio", "profile_image", "social_github",
                  "social_twitter", "social_linkedin", "social_youtube", "social_website", "social_stackoverflow"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "input",
                "placeholder": f"Add {' '.join(name.split('_'))}",
            })


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "input",
                "placeholder": f"Add {' '.join(name.split('_'))}",
            })
