from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    def clean(self):
        if self.published_date > timezone.now().date():
            raise ValidationError("Published date cannot be in the future.")
        if not self.isbn.isdigit() or len(self.isbn) != 13:
            raise ValidationError("ISBN must be exactly 13 digits.")
        if self.author is None:
            raise ValidationError("Book must have an author.")


    class Meta:
        ordering = ['published_date']
