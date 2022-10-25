from rest_framework import serializers
from .models import Collection,ContactUsQuestions

class CollectionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields=['id','title','explanation']

class QuestionsSerializers(serializers.ModelSerializer):
    collection=serializers.HyperlinkedRelatedField(
        # queryset=Collection.objects.all(),
        # many=True,
        view_name='collection-detail',
        read_only=True
    )
    class Meta:
        model=ContactUsQuestions
        fields=['id','title','explanation','stars','collection']





