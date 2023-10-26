from django.core.management.base import BaseCommand
from user_groups.factory import create_test_db
import os

class Command(BaseCommand):
    help = 'Create test data for the application'

    def handle(self, *args, **options):
        flag_path = 'initialized.flag'  

        if not os.path.exists(flag_path):
            create_test_db()
            self.stdout.write(self.style.SUCCESS('Successfully created test data'))
            with open(flag_path, 'w') as flag_file:
                flag_file.write('initialized')
        else:
            self.stdout.write(self.style.SUCCESS('Test data already created'))
