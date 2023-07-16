from django.core.management import BaseCommand

from main.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        product_list = [
            {'name': 'Помидор', 'description': 'Обычный помидор', 'category': 'Овощи', 'price': 10, 'date_create': '2023-07-15',
             'date_edit': '2023-07-15'},
            {'name': 'Огурец', 'description': 'Обычный огурец', 'category': 'Овощи', 'price': 14, 'date_create': '2023-07-15',
             'date_edit': '2023-07-15'},
            {'name': 'Свекла', 'description': 'Необычная свекла', 'category': 'Овощи', 'price': 20, 'date_create': '2023-07-15',
             'date_edit': '2023-07-15'},
            {'name': 'Малина', 'description': 'Обычная малина', 'category': 'Ягоды', 'price': 30, 'date_create': '2023-07-15',
             'date_edit': '2023-07-15'},
            {'name': 'Клубника', 'description': 'Необычная клубника', 'category': 'Ягода', 'price': 88, 'date_create': '2023-07-15',
             'date_edit': '2023-07-15'}
        ]

        add_products = []
        for product_item in product_list:
            add_products.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(add_products)

        category_list = [
            {'name' : 'Овощи', 'description' : 'Овощи. Самые обычные овощи.'},
            {'name': 'Ягод.', 'description': 'Ягоды. Самые обычные ягоды'}
        ]

        add_categories = []
        for category_item in category_list:
            add_categories.append(
                Product(**category_item)
            )

        Category.objects.bulk_create(category_list)
