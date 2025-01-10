from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomUserCreationForm, TransactionForm
from .models import CustomUser, Transaction
from django.db.models import Sum
from django.contrib.contenttypes.models import ContentType

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")  
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  
            user.save()
            return redirect("login")
        else:
            print("Form errors:", form.errors)  
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid credentials"})

    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    total_income = transactions.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = transactions.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expenses

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
    }
    return render(request, "accounts/dashboard.html", context)

@login_required
def add_transaction_view(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("dashboard")
    else:
        form = TransactionForm()

    return render(request, "accounts/add_transaction.html", {"form": form})


@login_required
def manage_permissions_view(request):
    if not request.user.is_superuser:
        return redirect("dashboard")  # Only superuser can access this page

    # Fetch all users excluding the superuser themselves
    users = CustomUser.objects.exclude(is_superuser=True)

    # Handle form submission
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        permission_codename = request.POST.get("permission_codename")
        action = request.POST.get("action")

        # Get user and permission objects
        user = get_object_or_404(CustomUser, id=user_id)
        permission = get_object_or_404(Permission, codename=permission_codename)

        if action == "assign":
            user.user_permissions.add(permission)  # Assign permission
        elif action == "revoke":
            user.user_permissions.remove(permission)  # Revoke permission

        return redirect("manage_permissions")  # Redirect back to the permissions page

    # Fetch all permissions
    permissions = Permission.objects.all()

    return render(
        request,
        "accounts/manage_permissions.html",
        {"users": users, "permissions": permissions},
    )


@login_required
@permission_required("accounts.add_transaction", raise_exception=True)
def add_transaction_view(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("dashboard")
    else:
        form = TransactionForm()

    return render(request, "accounts/add_transaction.html", {"form": form})