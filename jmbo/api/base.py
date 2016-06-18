from rest_framework import viewsets
from rest_framework_extras.serializers import FormMixin
from rest_framework.serializers import HyperlinkedModelSerializer, \
    ReadOnlyField, Serializer

from jmbo.models import ModelBase
from jmbo.admin import ModelBaseAdmin


class PropertiesMixin(Serializer):
    image_detail_url = ReadOnlyField()

    class Meta:
        fields = ("image_detail_url",)


class HyperlinkedModelBaseSerializer(
    FormMixin, PropertiesMixin, HyperlinkedModelSerializer
    ):

    class Meta:
        model = ModelBase
        queryset = ModelBase.objects.all()
        admin = ModelBaseAdmin


class ModelBaseViewSet(viewsets.ModelViewSet):
    queryset = ModelBase.objects.all()
    serializer_class = HyperlinkedModelBaseSerializer
