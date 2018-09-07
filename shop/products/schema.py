import graphene

from graphene_django.types import DjangoObjectType

from products import models



class ProductType(DjangoObjectType):
    class Meta:
        model = models.Products


class CategoryType(DjangoObjectType):
    class Meta:
        model = models.Category


class Query(graphene.AbstractType):
    products = graphene.List(ProductType)
    category = graphene.List(CategoryType)


    def resolve_products(self, info, **kwargs):
        return models.Products.objects.all()

    def resolve_category(self, info, **kwargs):
        return models.Category.objects.all()


