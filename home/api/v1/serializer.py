from rest_framework import serializers
from home.models import FormAList, FormBList, FormFields


class FormAListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAList
        fields = '__all__'


class FormBListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormBList
        fields = '__all__'


class FormFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFields
        fields = '__all__'


class UnhideFieldsSerializer(serializers.Serializer):
    fields = serializers.ListField(child=serializers.CharField())


class DeleteDataListSerializer(serializers.Serializer):
    type = serializers.CharField()
    ids = serializers.ListField(child=serializers.CharField())


class UpdateDataListSerializer(serializers.Serializer):
    type = serializers.CharField()
    list = serializers.ListField(child=serializers.DictField(child=serializers.CharField()))


class GetDataListSerializer(serializers.Serializer):
    type = serializers.CharField()
    fields = serializers.ListField(child=serializers.DictField(child=serializers.ListField()))

