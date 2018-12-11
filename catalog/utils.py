from csv import DictReader
from django.db import transaction
from pprint import pprint
from json import dumps
# from catalog.models import Category

file_data = DictReader(open('test.csv'))


product_list = []

for row in file_data:
    product_dict = {}
    try:
        product_dict['product_id'] = int(row.get('product_id', None))
    except:
        break
    product_dict['product_name'] = row.get('product_name', None)
    product_dict['brand_name'] = row.get('brand_name', None)
    product_dict['description'] = row.get('description', None)
    product_dict['video_url'] = row.get('video_url', None)

    image_iter = 1
    image_list_url = []
    while True:
        try:
            url = row[f'image_url/{image_iter}']
        except:
            break

        if url is not None:
            image_list_url.append(url)
        image_iter += 1
    product_dict['image_url_list'] = image_list_url

    try:
        brand_id = int(row.get('brand_id', None))
    except:
        brand_id = None

    product_dict['brand_id'] = brand_id

    try:
        partner_id = int(row.get('partner_id', None))
    except:
        partner_id = None
    product_dict['partner_id'] = partner_id

    try:
        price = float(row.get('price'))
    except:
        price = 0
    product_dict['price'] = price

    try:
        price_with_discount = float(row.get('price_with_discount', None))
    except:
        price_with_discount = price

    product_dict['price_with_discount'] = price_with_discount

    try:
        category_id = int(row.get('category_id', None))
    except:
        category_id = None

    product_dict['category_id'] = category_id
    category_iter = 1
    category_id_path_view = []

    if category_id is None:
        category_path_list = [row.get(f'category/{i}', None) for i in range(1, 4)]
        product_dict['category_path_list'] = category_path_list

    characteristic_iter = 1
    characteristics = {}
    characteristics_by_type = []

    while True:
        try:
            _characteristic_type = row[f'characteristic/{characteristic_iter}/type']
        except:
            break
        try:
            _characteristic_name = row[f'characteristic/{characteristic_iter}/name']
        except:
            break
        try:
            _characteristic_value = row[f'characteristic/{characteristic_iter}/value']
        except:
            break

        # characteristics = (_characteristic_type, _characteristic_name, _characteristic_value)

        characteristics['type'] = _characteristic_type
        characteristics['name'] = _characteristic_name
        characteristics['value'] = _characteristic_value
        characteristics_by_type.append(characteristics)

        product_dict['characteristics_by_type'] = characteristics_by_type

        characteristic_iter += 1
    product_list.append(product_dict)

    print(characteristics_by_type)


def import_product_from_csv(file):
    pass