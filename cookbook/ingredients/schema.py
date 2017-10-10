import graphene
from graphene_django.types import DjangoObjectType
from cookbook.ingredients.models import *

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class Query(graphene.AbstractType):
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)
    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()
