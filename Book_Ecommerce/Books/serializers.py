from rest_framework import serializers
from .models import Book, ReadingList, ReadingListItem

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingList
        fields = '__all__'

class ReadingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingListItem
        fields = '__all__'
