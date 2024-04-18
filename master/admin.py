from django.contrib import admin
from .models import User, Teacher, Parent, Standard, Student
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from .utils import create_user_import



class StudentResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        create_user_import(row)
        short_form = row["standard__short_form"]
        full_form = row["standard__full_form"]
        std, created = Standard.objects.get_or_create(short_form=short_form, full_form=full_form, defaults={"short_form": short_form})

    class Meta:
        model = Student
        # skip_unchanged = True
        # report_skipped = False

        fields = (
            'id', 'user', 'user__username', 'user__password', 'user__user_id', 'user__full_name', 'user__email', 'user__phone', 'user__whatsapp',
            'standard', 'standard__short_form', 'standard__full_form'
        )
        # export_order = (
        #     'id', 'user', 'user__username', 'user__password', 'user__user_id', 'user__full_name', 'user__email', 'user__phone', 'user__whatsapp',
        #     'standard', 'standard__short_form', 'standard__full_form'
        # )


class TeacherResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        create_user_import(row)

    class Meta:
        model = Teacher
        fields = (
            'id', 'user', 'designation', 
            'user__username', 'user__password', 'user__user_id', 'user__full_name', 'user__email', 'user__phone', 'user__whatsapp',
        )


class ParentResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        create_user_import(row)

    class Meta:
        model = Parent
        fields = (
            'id', 'user', 'user__username', 'user__password', 'user__user_id', 'user__full_name', 'user__email', 'user__phone', 'user__whatsapp',
            'relation', 'occupation'
        )


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email')
    list_filter = ('full_name',)
    search_fields = ('full_name', 'phone', 'email')

    class Meta:
        model = User
        fields = "__all__"


class TeacherAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'user', 'designation')
    list_filter = ('user', 'designation')
    search_fields = ('user', 'designation')
    resource_classes = [TeacherResource]

    class Meta:
        model = Teacher
        fields = "__all__"


class ParentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'user', 'relation')
    list_filter = ('user', 'relation')
    search_fields = ('user', 'relation')
    resource_classes = [ParentResource]

    class Meta:
        model = Parent
        fields = "__all__"


class StandardAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'short_form', 'full_form', 'category', 'in_charge')
    list_filter = ('short_form', 'full_form', 'category', 'in_charge')
    search_fields = ('short_form', 'full_form', 'category', 'in_charge')

    class Meta:
        model = Standard
        fields = "__all__"


class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'user', 'standard')
    list_filter = ('user', 'standard')
    search_fields = ('user', 'standard')
    resource_classes = [StudentResource]


    class Meta:
        model = Student
        fields = "__all__"

admin.site.register(User, UserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Standard, StandardAdmin)
admin.site.register(Student, StudentAdmin)
