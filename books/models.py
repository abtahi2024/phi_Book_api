from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator
from books.validators import validate_file_size
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveBigIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='bookes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class BookImages(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to='Books/images',validators=[validate_file_size])

class Review(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ratings=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.user.first_name} on {self.book.name}'
    
