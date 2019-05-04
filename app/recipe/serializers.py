from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects
    https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    """

    class Meta:
        model = Tag
        fields = ('id', 'name',)
        read_only_fields = ('id',)
