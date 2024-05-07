
from django.urls import path
from .views import BookListCreate,ReadingListRetrieveUpdateDestroy,ReadingListItemCreate,ReadingListCreate, ReadingListItemRetrieveUpdateDestroy,BookRetrieveUpdateDestroy


urlpatterns = [
    path('Books/', BookListCreate.as_view(), name='book-list-create'),
    path('Books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    path('reading-lists/', ReadingListCreate.as_view(), name='reading-list-create'),
    path('reading-lists/<int:pk>/', ReadingListRetrieveUpdateDestroy.as_view(), name='reading-list-retrieve-update-destroy'),
    path('reading-list-items/', ReadingListItemCreate.as_view(), name='reading-list-item-create'),
    path('reading-list-items/<int:pk>/', ReadingListItemRetrieveUpdateDestroy.as_view(), name='reading-list-item-retrieve-update-destroy'),
]
