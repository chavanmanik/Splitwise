# expenses/models.py
from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)

class Expense (models.Model):

    # EQUAL = 'EQUAL'
    # EXACT = 'EXACT'
    # PERCENT = 'PERCENT'

    # EXPENSE_TYPE_CHOICES = [
    #     (EQUAL, 'Equal'),
    #     (EXACT, 'Exact'),   
    #     (PERCENT, 'Percent'),
    # ]

    payer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # participants = models.ManyToManyField(User, related_name="participants")
    # description = models.TextField()
    expense_type = models.CharField(max_length=10)

class ExpenseParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    share = models.DecimalField(max_digits=10, decimal_places=2)
