from itertools import product
from pydantic import BaseModel

# TODO: Create Product model with id, name, price, in_stock

class Product(BaseModel):
    id: int
    name: str
    price : float
    in_stock : bool = True


product_data = {
    "id": 1,
    "name": "Product 1",
    "price": '10.99',
    "in_stock": 'false'
}

product = Product(**product_data)
print(product)