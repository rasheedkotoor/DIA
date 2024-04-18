from django.contrib import admin
from .models import Account, AccountCategory


class AccountCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)
    list_filter = ('category',)
    search_fields = ('category', 'description')

    class Meta:
        model = AccountCategory
        fields = "__all__"


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'ac_category', 'amount', 'account_type', 'transaction_type')
    list_filter = ('ac_category', 'amount', 'account_type', 'transaction_type')
    search_fields = ('ac_category', 'amount')

    class Meta:
        model = Account
        fields = "__all__"


admin.site.register(AccountCategory, AccountCategoryAdmin)
admin.site.register(Account, AccountAdmin)