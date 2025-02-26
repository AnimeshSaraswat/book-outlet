from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating")
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_number_of_books": len(books),
            "average_rating": round(
                (sum(book.rating for book in books) / len(books)), 2
            ),
        },
    )


def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "book_outlet/book_details.html",
        {
            "title": book.title,
            "rating": book.rating,
            "author": book.author,
            "is_bestseller": book.is_bestselling,
        },
    )
