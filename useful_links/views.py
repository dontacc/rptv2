from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet,ReadOnlyModelViewSet
from .models import ContactUsQuestions,Collection
from movies.permission import FullDjangoModelPermissions,IsAuthenticatedOrReadOnly
from . import Serializers
from rest_framework.decorators import action
# Create your views here.

class Questions(ModelViewSet):
    queryset = ContactUsQuestions.objects.select_related('collection').all()
    serializer_class = Serializers.QuestionsSerializers


class CollectionModelViewSet(ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = Serializers.CollectionSerializers
