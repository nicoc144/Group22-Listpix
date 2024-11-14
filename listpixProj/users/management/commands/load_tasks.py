# users/management/commands/load_tasks.py
from django.core.management.base import BaseCommand
from users.models import BucketListItem
import csv

class Command(BaseCommand):
    help = 'Loads bucket list tasks from a CSV file, replacing the existing list'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The CSV file path')

    def handle(self, *args, **options):
        file_path = options['file_path']

        try:
            # Clear the existing tasks
            BucketListItem.objects.all().delete()
            
            # Load new tasks from CSV
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    BucketListItem.objects.create(
                        task_name=row['task_name']
                    )

            self.stdout.write(self.style.SUCCESS(f'Successfully replaced tasks with contents from {file_path}'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File {file_path} not found.'))
        except KeyError:
            self.stdout.write(self.style.ERROR('CSV file is missing the expected "task_name" column.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
