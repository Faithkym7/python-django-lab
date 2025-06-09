from django import forms
from .models import Author, Book

class AuthorBookForm(forms.Form):
    author_name = forms.CharField(max_length=100)
    author_email = forms.EmailField()

    book_title = forms.CharField(max_length=200)
    book_published_date = forms.DateField()
    book_isbn = forms.CharField(max_length=13)
    book_pages = forms.IntegerField(min_value=1)