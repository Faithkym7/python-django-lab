from django.test import TestCase

# Create your tests here.
def test_register_book_post_creates_data(db, client):
    data = {
        'author_name': 'John Doe',
        'author_email': 'john@example.com',
        'book_title': 'Test Driven Django',
        'book_published_date': '2024-06-01',
        'book_isbn': '1234567890123',
        'book_pages': 250,
    }
    response = client.post('/register/', data)
    
    # Redirect on success
    assert response.status_code == 302

    # Check DB
    from .models import Author, Book
    assert Author.objects.filter(email='john@example.com').exists()
    assert Book.objects.filter(title='Test Driven Django').exists()


def test_register_book_invalid_isbn_fails(db, client):
    data = {
        'author_name': 'Bad ISBN',
        'author_email': 'bad@example.com',
        'book_title': 'Broken Book',
        'book_published_date': '2024-06-01',
        'book_isbn': 'notvalidisbn',
        'book_pages': 100,
    }
    response = client.post('/register/', data)

    # Should re-render form
    assert response.status_code == 200
    assert b'ISBN must be exactly 13 digits.' in response.content
