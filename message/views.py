from dj_rest_auth.views import PasswordResetConfirmView,PasswordResetView
from .Serializer import PasswordSerializer


class Password(PasswordResetView):
    serializer_class=PasswordSerializer