from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='admin@gmail.com',
            first_name='admin',
            last_name='admin',
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('admin')
        user.save()