from django.db import models
from django.contrib.auth.models import User 

class Product(models.Model):

	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	#image = 
	brand = models.CharField(max_length=200, null=True, blank=True)
	category = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	rating = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
	numReviews = models.IntegerField(default=0, blank=True, null=True)
	price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
	countInStock = models.IntegerField(default=0, blank=True, null=True)
	createdAt = models.DateTimeField(auto_now_add=True)
	_id = models.AutoField(primary_key=True, editable=False)

	def __str__(self):
		return f'{self.name}'

class Review(models.Model):

	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	rating = models.IntegerField(null=True, blank=True, default=0)
	comment = models.TextField(null=True, blank=True)
	_id = models.AutoField(primary_key=True, editable=False)

	def __str__(self):
		return str(self.rating)

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	paymentMethod = models.CharField(max_length=200, null=True, blank=True)
	taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	totalPrice = models.
	isPaid =
	paidAt =
	isDelivered =
	deliveredAt =
	created_at =
	_id = models.AutoField(primary_key=True, editable=False)

