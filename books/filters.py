from django_filters.rest_framework import FilterSet
from books.models import Book

class BookFilter(FilterSet):
    class Meta:
        model=Book
        fields={
            'category_id':['exact'],
            'price':['gt','lt']
        }