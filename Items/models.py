from django.db import models
from Users.models import User
# Create your models here.

class CategoriesMaster(models.Model):
    categoryId = models.AutoField(primary_key=True, db_index=True, db_column='category_id')
    catName = models.CharField(max_length=255, db_column='cat_name')
    status = models.CharField(max_length=1, db_column='status', default='A')

    REQUIRED_FIELDS = [ 'catName']

    class Meta:
        db_table = 'categories_master'

class ItemsTable(models.Model):
    itemId = models.AutoField(primary_key=True, db_column='item_id')
    categoryId = models.ForeignKey(CategoriesMaster, on_delete=models.CASCADE, db_column='category_id', db_index=True)
    brandName = models.CharField(max_length=255, db_column='brand_name',null=True)
    description = models.TextField(db_column='description',null=True)
    price = models.DecimalField(db_column='price', max_digits=10, decimal_places=2)
    avgRating = models.FloatField(db_column='avg_rating',default=0)
    quantity = models.IntegerField(db_column='quantity')
    userCount = models.IntegerField(db_column='user_count')
    created_at = models.DateTimeField(auto_now_add=True,db_column='created_at')
    updated_at = models.DateTimeField(auto_now_add=True,db_column='updated_at')
    status = models.CharField(max_length=1, db_column='status', default='A')

    REQUIRED_FIELDS = ['categoryId', 'brandName','price']

    class Meta:
        db_table = 'item_table'


class RatingTable(models.Model):
    Id = models.AutoField(primary_key=True, db_index=True, db_column='id')
    itemId = models.ForeignKey(ItemsTable, on_delete=models.CASCADE, db_column='item_id', db_index=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', db_index=True)
    userName = models.CharField(max_length=255,db_column='user_name',null=True)
    rating = models.FloatField(db_column='save_rating',default=0)
    review = models.TextField(db_column='review')
    created_at = models.DateTimeField(auto_now_add=True,db_column='created_at')
    updated_at = models.DateTimeField(auto_now_add=True,db_column='updated_at')


    class Meta:
        db_table = 'rating_table'