from django.contrib import admin
from .models import User, Author, Book, Loan

# Register each model with the admin site
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Loan)