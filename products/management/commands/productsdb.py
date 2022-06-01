from django.core.management.base import BaseCommand
from products.models import Category, Product
from products.utils import AddProduct


class Command(BaseCommand):
    help = 'adds categories and products to database'

    def handle(self, *args, **options):
        api_access = AddProduct()
        for category in api_access.categorylist:
            if Category.objects.filter(category_name=api_access.value_cleaner(category)).exists() is True:
                continue
            else:
                Category.objects.create(category_name=api_access.value_cleaner(category))
        try:
            for one_product in api_access.products_query():
                p = Product.objects.filter(off_url=one_product['url'])
                if p.exists():
                    continue
                else:
                    Product.objects.create(category=Category.objects.get(category_name=one_product['category']),
                                                                          product_name=one_product['product_name'],
                                                                          nutriscore=one_product['nutriscore_grade'],
                                                                          nutri_values=one_product['nutriments'],
                                                                          off_url=one_product['url'],
                                                                          img_url=one_product['image_url'])
        except Exception as e:
            print(e)
