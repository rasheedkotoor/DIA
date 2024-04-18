from django.db import models
from master.models import User

# Create your models here.
REQUESTED = 0
ON_HOLD = 1
APPROVED = 2
ON_LEAVE = 3
RETURNED = 4
LEAVE_STATUS = (
    (REQUESTED, 'Requested'),
    (ON_HOLD, 'On Hold'),
    (APPROVED, 'Approved'),
    (ON_LEAVE, 'On Leave'),
    (RETURNED, 'Returned'),
)


class MovementReason(models.Model):
    reason = models.CharField(max_length=50, blank=True, null=True) 
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.reason


class Movement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mv_reason = models.ForeignKey(MovementReason, on_delete=models.SET_NULL, blank=True, null=True)
    destination = models.CharField(max_length=150, blank=True, null=True)
    leave_permitted_from = models.DateTimeField(blank=True, null=True)
    leave_permitted_to = models.DateTimeField(blank=True, null=True)
    returned_on = models.DateTimeField(blank=True, null=True)
    # allowed_duration = # set property from - to
    # total_duration = # set property from - returned
    # extra_duration = # set property from - returned
    status = models.IntegerField(choices=LEAVE_STATUS, default=REQUESTED)
    remarks = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    @property
    def allowed_duration(self):
        return self.leave_permitted_from - self.leave_permitted_to

    @property
    def total_duration(self):
        return self.leave_permitted_from - self.returned_on

    @property
    def total_duration(self):
        return self.allowed_duration - self.total_duration