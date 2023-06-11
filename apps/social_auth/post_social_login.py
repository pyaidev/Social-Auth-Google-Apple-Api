""" Grab user information from social account """

from urllib.request import urlopen

from allauth.socialaccount.models import SocialAccount
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db.models.signals import post_save
from django.utils import timezone


class BaseUserInfoSetter:
    def __init__(self, social_account):
        self.social_account = social_account
        self._is_user_signed_up = (
            social_account.last_login - social_account.date_joined
        ).total_seconds() < timezone.timedelta(
            milliseconds=100
        ).total_seconds()  # silly hack to check if user is signed up or logged in

    def set_data(self):
        # check if user is signed up. we don't want to override data if user logged in
        if self._is_user_signed_up:
            provider_setter = getattr(self, self.social_account.provider, None)
            if provider_setter:
                self._set_image()
                if self._is_user_signed_up:
                    self.social_account.user.password_set = False
                provider_setter(self.social_account.user, self.social_account.extra_data)
                self.social_account.user.save()
            else:
                raise Exception("No setter for provider {}".format(self.social_account.provider))

    def _set_image(self):
        img_temp = NamedTemporaryFile(delete=True)
        image_url = self.social_account.get_profile_url() or self.social_account.get_avatar_url()  # noqa
        if image_url:
            img_temp.write(urlopen(image_url).read())
            img_temp.flush()
            self.social_account.user.avatar.save(f"avatar_{self.social_account.user.pk}.jpg", File(img_temp))


class UserInfoSetter(BaseUserInfoSetter):
    """
    Add more providers here to extract and set data.
    But don't save user as it will be controlled by set_data()
    """

    @staticmethod
    def facebook(user, extra_data):
        user.full_name = extra_data.get("name")

    @staticmethod
    def apple(user, extra_data):
        user.email = extra_data.get("email")

    @staticmethod
    def google(user, extra_data):
        user.full_name = extra_data.get("name")
        user.first_name = extra_data.get("given_name")
        user.last_name = extra_data.get("family_name")
        user.email = extra_data.get("email")
        user.username = extra_data.get("email")


def set_user_info(sender, instance: SocialAccount, created, **kwargs):
    UserInfoSetter(instance).set_data()


def register_signals():
    post_save.connect(set_user_info, sender=SocialAccount)
