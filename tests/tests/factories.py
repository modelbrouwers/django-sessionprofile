import factory
import factory.fuzzy

from django.contrib.auth import get_user_model

from sessionprofile.models import SessionProfile

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    username = 'JohnDoe'
    password = factory.PostGenerationMethodCall('set_password', 'secret')

    class Meta:
        model = User


class SuperUserFactory(UserFactory):
    is_staff = True
    is_superuser = True


class SessionProfileFactory(factory.django.DjangoModelFactory):
    session_key = factory.fuzzy.FuzzyText(length=40)

    class Meta:
        model = SessionProfile
