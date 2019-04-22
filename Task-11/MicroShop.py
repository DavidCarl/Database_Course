class Customer:
	def __init__(self, name, Order):
		self.name = name
		self.Order = Order

class Order:
	def __init__(self, date, total, customer, OrderLine):
		self.date = date
		self.total = total
		self.customer = customer
		self.OrderLine = OrderLine

class OrderLine:
	def __init__(self, order, product, count, total):
		self.order = order
		self.product = product
		self.count = count
		self.total = total

class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

