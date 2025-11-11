from django.shortcuts import render
from rest_framework.filters import SearchFilter,OrderingFilter
from books.models import Book,Category,Review,BookImages
from books.serializers import BookSerializers,CategorySerializer,ReviewSerilizers,BookImageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from books.filters import BookFilter
from books.paginations import DefaultPagination
from rest_framework.permissions import IsAdminUser
from api.permissions import IsAdminOrReadOnly,FullDjangoModelPermission
from books.permissions import IsReviewAuthorOrReadonly
from drf_yasg.utils import swagger_auto_schema
# Create your views here.



class BookViewSet(ModelViewSet):
    """API endPint for managing in the E-book Store
    - ALLows Authenticated admin to create update, and delete books
    - Allows users to browse and filter book
    """
    queryset=Book.objects.all()
    serializer_class=BookSerializers
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class=BookFilter
    pagination_class=DefaultPagination
    search_fields=['name','description']
    ordering_fields=['price','updated_at']
    permission_classes=[IsAdminOrReadOnly]

    @swagger_auto_schema(operation_summary='Every on can saw the book and Read')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary='create a book by Admin',
            responses={
                201 :BookSerializers,
                400: "Bad Request"
            }
            )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_summary='Admin can delate')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can update that books')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='normal user can see book id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can update the books')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class BookImageViewSet(ModelViewSet):
    serializer_class=BookImageSerializer
    permission_classes=[IsAdminOrReadOnly]
    def get_queryset(self):
        return BookImages.objects.filter(book_id=self.kwargs.get('book_pk'))
    
    def perform_create(self, serializer):
        serializer.save(book_id=self.kwargs.get('book_pk'))

    @swagger_auto_schema(operation_summary='every user can see the images') 
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can Post and Edit the books')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='user can see the Images')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin Can PUT in images')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can PATCH the images')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can DELETE ')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    


class CategoryViewSet(ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    queryset=Category.objects.annotate(book_count=Count('bookes')).all()
    serializer_class=CategorySerializer
    
    @swagger_auto_schema(operation_summary='every user can see the Category') 
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can Post and Edit the Category')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='User can go the id Category')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can PUT Category')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can PATCH the Category')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can DELETE ')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    

class ReviewViewSet(ModelViewSet):
    serializer_class=ReviewSerilizers
    permission_classes=[IsReviewAuthorOrReadonly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs.get('book_pk'))

    def get_serializer_context(self):
        return {'book_id':self.kwargs.get('book_pk')}
    
    @swagger_auto_schema(operation_summary='User can saw the Reviews')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can POST and Edit Reviews')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='User can go the id reviews')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can PUT Reveiws ')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin can PATCH')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Admin Can DELETE')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
