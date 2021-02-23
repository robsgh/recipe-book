from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group


class RecipeType(models.Model):
    """ A type of recipe which can be held in the recipe book """
    name = models.CharField(max_length=64)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT, related_name='children')

    class Meta:
        ordering = ['name']
        unique_together = ('slug', 'parent')

    def __str__(self):
        p = [self.name]
        node = self.parent
        while node:
            p.append(node.name)
            node = node.parent
        return '/'.join(p[::-1])

class Recipe(models.Model):
    """ A recipe entry in the recipe book """
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=64, verbose_name='Recipe Name')
    recipe_type = models.ForeignKey(
        RecipeType, 
        null=True, blank=True, 
        on_delete=models.SET_NULL, 
        related_name='type', 
        verbose_name='Recipe Type'
    )

    ingredients_json = models.TextField(verbose_name='Recipe Ingredients')
    steps_json = models.TextField(verbose_name='Recipe Steps')

    created_at = models.DateField(auto_now_add=True, verbose_name='Recipe Creation Date')
    last_modified = models.DateField(auto_now=True, verbose_name='Date of Last Recipe Modification')

    class Meta:
        """ Recipe Metadata """
        ordering = ['-name', '-last_modified']
        get_latest_by = ['-last_modified', '-created_at']

    @property
    def ingredients(self):
        """ Return the list of ingredients in the recipe """
        import json
        return json.loads(self.ingredients_json)

    @ingredients.setter
    def ingredients(self, val):
        """ Set the ingredients in the recipe """
        import json
        self.ingredients_json = json.dumps(val, separators=(',',':'))

    @property
    def steps(self):
        """ Return the list of steps in the recipe """
        import json
        return json.loads(self.steps_json)

    @steps.setter
    def steps(self, val):
        """ Set the steps in the recipe """
        import json
        self.steps_json = json.dumps(val, separators=(',',':'))

    def __str__(self):
        """ Display the model name as a string """
        return f'{self.recipe_type.name} - {self.name}'
