from rest_framework import viewsets, status
from .models import Book, Transaction, Category
from .serializers import (
    UserSerializer,
    BookSerializer,
    TransactionSerializer,
    CategorySerializer,
)
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from django.utils import timezone
from .permissions import IsLibrarian

User = get_user_model()

# ---------------------------
# USER CRUD
# ---------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ---------------------------
# BOOK VIEWSET
# ---------------------------
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only librarians can add, edit, or delete books
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsLibrarian]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


# ---------------------------
# TRANSACTION VIEWSET (BORROW/RETURN)
# ---------------------------
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "librarian":
            return Transaction.objects.all()
        return Transaction.objects.filter(user=user)

    # Student borrows a book
    @action(detail=True, methods=["post"])
    def borrow(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        user = request.user

        if user.role != "student":
            return Response(
                {"error": "Only students can borrow books."},
                status=status.HTTP_403_FORBIDDEN,
            )

        if book.available_copies <= 0:
            return Response(
                {"error": "No copies available for borrowing."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        transaction = Transaction.objects.create(user=user, book=book)
        book.available_copies -= 1
        book.save()

        return Response(
            {"message": f"{book.title} borrowed successfully!"},
            status=status.HTTP_201_CREATED,
        )

    # Student returns a book
    @action(detail=True, methods=["post"])
    def return_book(self, request, pk=None):
        try:
            transaction = Transaction.objects.get(
                user=request.user, book_id=pk, is_returned=False
            )
        except Transaction.DoesNotExist:
            return Response(
                {"error": "No active borrow record found for this book."},
                status=status.HTTP_404_NOT_FOUND,
            )

        transaction.is_returned = True
        transaction.return_date = timezone.now()
        transaction.save()

        book = transaction.book
        book.available_copies += 1
        book.save()

        return Response(
            {"message": f"{book.title} returned successfully!"},
            status=status.HTTP_200_OK,
        )


# ---------------------------
# CATEGORY VIEWSET
# ---------------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ---------------------------
# AUTHENTICATION VIEWS
# ---------------------------
@api_view(["POST"])
@permission_classes([AllowAny])  # anyone can register
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])  # anyone can login
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])  # only logged-in users can logout
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
