class Ecommerce:
  def add_product(self,product_name, price, quantity):
    product = {
        'product_name': product_name,
        'price': price,
        'quantity': quantity
    }
    return product

  def update_price(self,product, new_price):
    product['price'] = new_price
    return product

  def update_quantity(self,product, quantity_change):
    product['quantity'] += quantity_change
    return product
ecommerce=Ecommerce()
 # Adding a new product
product1 = ecommerce.add_product('iPhone', 999, 10)
print(product1)

# Updating the price of a product
updated_product =ecommerce.update_price(product1, 899.99)
print(updated_product)

# Updating the quantity of a product
updated_product = ecommerce.update_quantity(product1, -5)
print(updated_product)