from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from libraryapi.models import *
from libraryapi.serializers import *


class AuthorList(generics.ListCreateAPIView):
    '''
    Author List/Create view
    '''
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
    '''
    Author Put/Retrieve/Delete view
    '''
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class WorkList(generics.ListCreateAPIView):
    '''
    Work List/Create view
    '''
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class WorkDetails(generics.RetrieveUpdateDestroyAPIView):
    '''
    Work Put/Retrieve/Delete view
    '''
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class TagList(generics.ListCreateAPIView):
    '''
    Tag List/Create view
    '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetails(generics.RetrieveUpdateDestroyAPIView):
    '''
    Tag Put/Retrieve/Delete view
    '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer