from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render
from .models import Expense, ExpenseParticipant, User
from django.db.models import Sum
import json

def create_expense(request):
    # Implement expense creation logic here
    return JsonResponse({'message': 'Expense created successfully'})

def get_balances(request, user_id):
    # Calculate balances for the user
    user = User.objects.get(user_id=user_id)
    balances = ExpenseParticipant.objects.filter(user=user).values('expense__payer__user_id').annotate(balance=Sum('share'))
    return JsonResponse(list(balances), safe=False)

def home(request):
    if request.method == 'POST':
        payer = request.POST['payer']
        amount = float(request.POST.get("amount"))
        # participants = request.POST['participants']
        expense_type = request.POST['expense_type']
        users = User.objects.exclude(name=payer).values()
        userl = User.objects.all().values()
        sep_amount = amount / len(userl)
        
        for user in users:
            user['owe'] = sep_amount
            
            
        
        
        for user in users:
                user['owe'] = sep_amount
                print(user)
        
        
    return render(request,'home.html')
        
      
        # expense = Expense.objects.create(payer_id_id=payer, amount=amount, expense_type=expense_type,participants=participants)
    # return JsonResponse(list(user), safe=False)

