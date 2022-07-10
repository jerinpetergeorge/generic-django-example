from allauth.account.utils import user_field
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        first_name: str = data.get("first_name", "")
        last_name: str = data.get("last_name", "")
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}".strip()
        user = super().populate_user(
            request=request,
            sociallogin=sociallogin,
            data=data,
        )
        user_field(user, "full_name", full_name)
        return user
