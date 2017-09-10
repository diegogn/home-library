from rest_framework import serializers
from libraryapi.models import *

class AuthorSerializer(serializers.ModelSerializer):
    '''
    Author serializer class
    '''
    class Meta:
        '''
        Meta
        '''
        model = Author
        fields = ('id', 'created', 'name', 'surname')

class TagSerializer(serializers.ModelSerializer):
    '''
    Tag serializer class
    '''
    class Meta:
        '''
        Meta
        '''
        model = Tag
        fields = ('id', 'name', 'color')

class WorkSerializer(serializers.ModelSerializer):
    '''
    Work serializer class
    '''
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset = Tag.objects.all())
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset = Author.objects.all())

    class Meta:
        '''
        Meta
        '''
        model = Work
        fields = ('id', 'created', 'title', 'price', 'tags', 'authors')
