import csv
import json
import os
import re

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from recipes.models import Recipe, RecipeType


class Command(BaseCommand):
    help = 'Ingest the data from a CSV as recipies'

    def add_arguments(self, parser):
        parser.add_argument('csv_filename', type=str)

    def handle(self, *args, **options):
        csv_path = options['csv_filename']
        if not os.path.exists(csv_path):
            raise CommandError('invalid csv file path')

        count_before_add = Recipe.objects.count()
        with open(csv_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                creator = User.objects.get(username='admin')

                category = row['Category']
                if category == 'Main Course':
                    category = 'Entree'
                elif category == 'Beverage' and 'liquor' in row['Ingredients']:
                    category = 'Mixed Drink'

                try:
                    recipe_type = RecipeType.objects.get(name=category)
                except RecipeType.DoesNotExist as dne:
                    print('category in csv does not exist in ORM')

                ingredients = []
                for part in re.split(r'\n|,', row['Ingredients']):
                    if len(part.strip().rstrip()) > 0:
                        ingredients.append(part.strip().rstrip().capitalize())
                ingredients_json = json.dumps(ingredients)

                steps = []
                for part in re.split(r'\n|\.', row['Description']):
                    if len(part.strip().rstrip()) > 0:
                        steps.append(part.strip().rstrip().capitalize())
                steps_json = json.dumps(steps)

                r = Recipe(
                    creator=creator,
                    name=row['Name'].capitalize(),
                    recipe_type=recipe_type,
                    ingredients_json=ingredients_json,
                    steps_json=steps_json,
                )
                r.save()
        count_after_add = Recipe.objects.count()
        print(f'Added {count_after_add-count_before_add} entires to the Django DB.')
