from django.db import models
from django.contrib.auth.models import AbstractUser

# -------------------------------
# Custom User Model
# -------------------------------
class User(AbstractUser):
    """
    Extends Django's built-in User model to add user_type.
    user_type: 'admin' or 'member'
    """
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='member',
        help_text="Type of user: Admin or Member"
    )

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

# -------------------------------
# Author Model
# -------------------------------
class Author(models.Model):
    """
    Stores author information.
    """
    name = models.CharField(max_length=100, help_text="Full name of the author")
    bio = models.TextField(blank=True, help_text="Short biography of the author")

    def __str__(self):
        return self.name

# -------------------------------
# Book Model
# -------------------------------
class Book(models.Model):
    """
    Stores book information.
    """
    title = models.CharField(max_length=200, help_text="Title of the book")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.CharField(max_length=50, help_text="Genre of the book")
    isbn = models.CharField(max_length=13, unique=True, help_text="ISBN number")
    available_copies = models.PositiveIntegerField(default=1, help_text="Number of available copies")

    def __str__(self):
        return f"{self.title} by {self.author.name}"

# -------------------------------
# Loan Model
# -------------------------------
class Loan(models.Model):
    """
    Tracks which users have borrowed which books and due dates.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    borrowed_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when the book was borrowed")
    due_date = models.DateField(help_text="Due date for returning the book")
    returned = models.BooleanField(default=False, help_text="Has the book been returned?")

    def __str__(self):
        return f"{self.book.title} loaned to {self.user.username}"

    class Meta:
        unique_together = ('user', 'book', 'returned')  # Prevent duplicate active loans

# --------------------------------
# End of models.py
# --------------------------------

"""
Multi-line comment:
- Each model is documented with docstrings and help_text for clarity.
- Relationships are set up using ForeignKey.
- User model is customized for user_type.
- Use 'python manage.py makemigrations' and 'python manage.py migrate' to create the database tables.
- If you change the User model, update AUTH_USER_MODEL in settings.py.
"""