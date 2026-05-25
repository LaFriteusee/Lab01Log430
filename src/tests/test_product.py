from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert isinstance(product_list, list)

def test_product_insert():
    product = Product(None, 'Laptop Test', 'TestBrand', 999.99)
    dao.insert(product)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, 'Old Name', 'BrandX', 10.00)
    assigned_id = dao.insert(product)

    product.id = assigned_id
    product.name = 'New Name'
    product.price = 20.00
    dao.update(product)

    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert 'New Name' in names

    # cleanup
    dao.delete(assigned_id)

def test_product_delete():
    product = Product(None, 'To Delete', 'BrandY', 5.00)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)

    new_dao = ProductDAO()
    product_list = new_dao.select_all()
    ids = [p.id for p in product_list]
    assert assigned_id not in ids
