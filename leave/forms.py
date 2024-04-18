from django import forms
from .models import Movement, MovementReason
from .models import LEAVE_STATUS, REQUESTED
from master.models import User
class MovementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        leave_type = kwargs.pop('leave_type', None)  # Get the leave_type value
        super(MovementForm, self).__init__(*args, **kwargs)
        # Set default values for the dropdown fields
        # self.fields['status'].initial = REQUESTED
        # If you have predefined categories, you can set a default like this:
        # self.fields['mv_reason'].initial = MovementCategory.objects.get(id=default_id)

        # Modify the queryset for the user field based on leave_type
        if leave_type == 0:
            self.fields['user'].queryset = User.objects.filter(teacher__isnull=False)
        elif leave_type == 1:
            self.fields['user'].queryset = User.objects.filter(student__isnull=False)
        else:
            self.fields['user'].queryset = User.objects.all()

    class Meta:
        model = Movement
        fields = ['user', 'mv_reason', 'destination', 'leave_permitted_from', 'leave_permitted_to', 'returned_on', 'remarks']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control dt-full-name dt-user',
                                      'placeholder': '',
                                      'aria-label': 'Select User',
                                      'aria-describedby': 'user2'}),
            'mv_reason': forms.Select(attrs={'class': 'form-control dt-post dt-mv_reason',
                                    'placeholder': 'Reason',
                                    'aria-label': 'Reason',
                                    'aria-describedby': 'mv_reason2'}),
            'destination': forms.TextInput(attrs={'class': 'form-control dt-email dt-destination',
                                      'placeholder': 'Destination',
                                      'aria-label': 'Destination'}),
            # 'leave_permitted_from': forms.DateTimeInput(attrs={'class': 'form-control'}),
            # 'leave_permitted_to': forms.DateTimeInput(attrs={'class': 'form-control'}),
            # 'returned_on': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'leave_permitted_from': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'leave_permitted_to': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'returned_on': forms.DateTimeInput(attrs={'class': 'form-control'}),
            # 'status': forms.Select(attrs={'class': 'form-control dt-salary dt-status',
            #                        'placeholder': 'Status',
            #                        'aria-label': 'Status',
            #                        'aria-describedby': 'status2'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control'}),
        }
