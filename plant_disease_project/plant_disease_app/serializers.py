from rest_framework import serializers
from .models import UploadImage

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ['image', 'uploaded_at']