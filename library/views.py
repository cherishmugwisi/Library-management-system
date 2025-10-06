from django.shortcuts import render
from.models import Book, Author
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def book_list(request):
    books=Book.objects.all()#retrieve all books
    context={
        'books':books,
    }
    return render(request,'library/book_list.html',context)
def index(request):
    total_books=Book.objects.count()
    available_books=Book.objects.filter(available=True).count()
    total_authors=Author.objects.count()

    context={
        'total_books':total_books,
        'available_books':available_books,
        'total_authors':total_authors,
    }
    return render(request, 'library/index.html', context)

def book_detail(request, book_id):
    book=get_object_or_404(Book,id=book_id)
    context={
        'book':book,
    }
    return render(request,'library/book_detail.html',context)
    

    
