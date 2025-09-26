from rest_framework import serializers
from .models import Yangiliklar


class YangiliklarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = '__all__'















