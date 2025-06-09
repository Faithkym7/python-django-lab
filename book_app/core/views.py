# views.py
from django.shortcuts import render, redirect
from .forms import AuthorBookForm
from .models import Author, Book
from django.core.exceptions import ValidationError

def register_book(request):
    if request.method == 'POST':
        form = AuthorBookForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            author_name = form.cleaned_data['author_name']
            author_email = form.cleaned_data['author_email']
            book_title = form.cleaned_data['book_title']
            book_published_date = form.cleaned_data['book_published_date']
            book_isbn = form.cleaned_data['book_isbn']
            book_pages = form.cleaned_data['book_pages']

            # Create or get Author
            author, created = Author.objects.get_or_create(
                email=author_email,
                defaults={'name': author_name}
            )

            # Create Book instance
            book = Book(
                title=book_title,
                author=author,
                published_date=book_published_date,
                isbn=book_isbn,
                pages=book_pages
            )

            try:
                book.full_clean()  # Runs model validations
                book.save()
                return redirect('success')  # Replace with your success URL
            except ValidationError as e:
                form.add_error(None, e)

    else:
        form = AuthorBookForm()
    
    return render(request, 'register_book.html', {'form': form})
