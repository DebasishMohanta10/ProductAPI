from rest_framework import serializers
from .models import Category,Product
import bleach

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(lookup_field="slug",view_name="category-details",read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    stock = serializers.IntegerField(source="inventory",read_only=True)
    class Meta:
        model=Product
        fields = ["name","slug","price","stock","category","category_id","url","inventory"]
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "product-detail"
            }
        }
    def validate(self, attrs):
        attrs["name"] = bleach.clean(attrs["name"])
        if attrs["inventory"] < 0:
            serializers.ValidationError("No of items in Stock must be greater than zero.")
        if attrs["price"] < 10:
            serializers.ValidationError("Price must be Greater than or equal to 10")
        return super().validate(attrs)

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["name","slug","url"]
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "category-details"
            }
        }

        
        