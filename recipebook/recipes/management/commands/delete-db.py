from django.core.management.base import BaseCommand, CommandError
from recipes.models import Recipe

class Command(BaseCommand):
    help = 'Delete recipes in the DB'

    def handle(self, *args, **options):
        Recipe.objects.all().delete()
        print(f'Deleted entires in the Django DB.')
