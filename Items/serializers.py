from rest_framework import serializers

from Items.models import ItemsTable,RatingTable


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemsTable
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RatingTable
        fields = '__all__'

class ItemRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemsTable
        fields = ['avgRating']