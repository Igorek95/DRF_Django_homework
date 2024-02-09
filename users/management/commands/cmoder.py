from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='moder@mail.ru',
            first_name='moder',
            last_name='moder',
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )

        user.set_password('moder')
        group, _ = Group.objects.get_or_create(name='Модератор')
        group.user_set.add(user)
        user.save()