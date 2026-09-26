from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create initial admin"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = "mohoria"
        email = "magaiwamohoria@gmail.com"
        password = "#40400#"

        if User.objects.filter(username=username).exists():
            self.stdout.write("Admin already exists.")
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        self.stdout.write("Admin created successfully.")