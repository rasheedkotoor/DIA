from django.db import models
from master.models import User

PTA = 0
STUDENT = 1
ACCOUNT_TYPE = (
    (PTA, 'PTA Fund'),
    (STUDENT, 'Student Account'),
)
CREDIT = 0
DEBIT = 1
TRANSACTION_TYPE = (
    (CREDIT, 'Credit'),
    (DEBIT, 'Debit'),
)


class AccountCategory(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True) 
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.category

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ac_category = models.ForeignKey(AccountCategory, on_delete=models.SET_NULL, blank=True, null=True)
    account_type = models.IntegerField(choices=ACCOUNT_TYPE, blank=True, null=True)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    voucher_no = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    # received_by = models.CharField(max_length=50, blank=True, null=True)
    # paid_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        t = "+" if self.transaction_type == CREDIT else "-"
        return f"{self.user}: {t}"