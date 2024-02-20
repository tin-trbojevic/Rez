from django.core.management.base import BaseCommand
from sportovi.models import *  

class Command(BaseCommand):
    help = 'Delete all data from specified models'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleting all data...'))
        Sport.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All data deleted successfully.'))