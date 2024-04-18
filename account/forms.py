from django import forms
from .models import Account, AccountCategory
from master.models import User
from .models import PTA, STUDENT, CREDIT


class AccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        account_type1 = kwargs.pop('account_type', None)  # Get the account_type value
        super(AccountForm, self).__init__(*args, **kwargs)
        # Set default values for the dropdown fields
        # if self.fields['account_type'] == STUDENT:
        print('account_type1', account_type1)
        if account_type1 == STUDENT:
            self.fields['user'].queryset = User.objects.filter(student__isnull=False) #students only
            self.fields['account_type'].initial = STUDENT
        else:
            self.fields['user'].queryset = User.objects.all()
            self.fields['account_type'].initial = PTA

        # self.fields['account_type'].initial = STUDENT
        self.fields['transaction_type'].initial = CREDIT
        # If you have predefined categories, you can set a default like this:
        # self.fields['ac_category'].initial = AccountCategory.objects.get(id=default_id)
        # self.fields['user'].queryset = User.objects.filter(student__isnull=False) #students only


    class Meta:
        model = Account
        fields = ['user', 'ac_category', 'account_type', 'transaction_type', 'amount', 'voucher_no', 'remarks']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control dt-full-name dt-user',
                                      'placeholder': '',
                                      'aria-label': 'Select User',
                                      'aria-describedby': 'user2'}),
            'ac_category': forms.Select(attrs={'class': 'form-control dt-post dt-ac_category',
                                    'placeholder': 'Account category',
                                    'aria-label': 'Account category',
                                    'aria-describedby': 'ac_category2'}),
            'account_type': forms.Select(attrs={'class': 'form-control dt-post dt-account_type',
                                    'placeholder': 'Account Type',
                                    'aria-label': 'Account Type',
                                    'aria-describedby': 'account_type2'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control dt-post dt-transaction_type',
                                    'placeholder': 'Transaction Type',
                                    'aria-label': 'Transaction Type',
                                    'aria-describedby': 'transaction_type2'}),
            'amount': forms.NumberInput({'class': 'form-control dt-email dt-amount',
                                      'placeholder': 'Amount',
                                      'aria-label': 'Amount'}),
            'voucher_no': forms.TextInput(attrs={'class': 'form-control dt-email dt-voucher_no',
                                      'placeholder': 'Voucher No',
                                      'aria-label': 'Voucher No'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control'}),
        }
