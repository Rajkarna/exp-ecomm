from django.db import models

# Create your models here.
from Users.models import User

from Items.models import ItemsTable


class CartItem(models.Model):
    cartItemId = models.AutoField( db_column='cart_item_id',primary_key=True)
    userId = models.ForeignKey(User,db_column='user_id',on_delete=models.CASCADE)
    itemId = models.ForeignKey(ItemsTable, db_column='item_id',on_delete=models.CASCADE)
    quantity = models.IntegerField( db_column='quantity')
    price = models.IntegerField(db_column='price')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createBy = models.IntegerField(db_column='create_by')
    modifyBy = models.IntegerField(db_column='modify_by')

    class Meta:
        db_table = 'cart_item'

class Orders(models.Model):
    orderId = models.AutoField(db_column='order_id',primary_key=True)
    userId = models.ForeignKey(User,db_column='user_id',null=False,on_delete=models.CASCADE)
    itemId = models.ForeignKey(ItemsTable, db_column='item_id',on_delete=models.CASCADE)
    invoiceId = models.IntegerField(db_column='invoice_id')
    discountId = models.IntegerField(db_column='discount_id',null=False)
    amount = models.IntegerField(db_column='amount',null=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Orders'
