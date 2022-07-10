from allauth.account.utils import perform_login
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.models import SocialLogin
from allauth.socialaccount.signals import pre_social_login
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.shortcuts import redirect

User = get_user_model()


@receiver(pre_social_login)
def link_to_local_user(sender, request, sociallogin: SocialLogin, **kwargs):
    """
    This signal is used to connect the local user with social-user.
    Ref: https://github.com/pennersr/django-allauth/issues/215
    """
    email = sociallogin.user.email.lower()
    try:
        user = User.objects.get(email=email)
        perform_login(request, user, email_verification="none")
        raise ImmediateHttpResponse(redirect("/"))
    except User.DoesNotExist:
        pass
