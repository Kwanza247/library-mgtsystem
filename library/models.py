from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Custom User model
class User(AbstractUser):
    date_of_membership = models.DateField(default=timezone.now)
    active_status = models.BooleanField(default=True)

    ROLE_CHOICES = (
        ('librarian', 'Librarian'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} ({self.role})"


# Category model
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"  # ✅ fixes admin name and filter issue



# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField(null=True, blank=True)
    available_copies = models.PositiveIntegerField(default=1)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books'
    )

    def __str__(self):
        return f"{self.title} by {self.author}"


# Transaction model (Borrow/Return)
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transactions')
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} -- {self.book.title} ({'Returned' if self.is_returned else 'Borrowed'})"
