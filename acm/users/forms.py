from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ACMUser


class ACMUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = ACMUser
        fields = ('username', 'sid', )


class ACMUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = ACMUser
        fields = ('first_name', 'last_name', 'email', )
