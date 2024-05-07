from django.contrib import admin
from .models import Book, ReadingList, ReadingListItem

admin.site.register(Book)
admin.site.register(ReadingList)
admin.site.register(ReadingListItem)
