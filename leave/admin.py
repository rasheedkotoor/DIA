from django.contrib import admin
from .models import Movement, MovementReason


class MovementReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'reason',)
    list_filter = ('reason',)
    search_fields = ('reason', 'description')

    class Meta:
        model = MovementReason
        fields = "__all__"


class MovementAdmin(admin.ModelAdmin):
    list_display = ('id', 'mv_reason', 'destination', 'leave_permitted_from', 'leave_permitted_to', 'status')
    list_filter = ('mv_reason', 'destination', 'leave_permitted_from', 'leave_permitted_to', 'status')
    search_fields = ('mv_reason', 'destination')

    class Meta:
        model = Movement
        fields = "__all__"


admin.site.register(MovementReason, MovementReasonAdmin)
admin.site.register(Movement, MovementAdmin)