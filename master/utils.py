from .models import User


def create_user_import(row):
    user_id = row["user__user_id"]
    username = row["user__username"]
    password = row["user__password"]
    user, created = User.objects.get_or_create(user_id=user_id, username=username, defaults={"user_id": user_id})
    if created:
        user.full_name = row["user__full_name"]
        user.email = row["user__email"]
        user.phone = row["user__phone"]
        user.whatsapp = row["user__whatsapp"]
        user.set_password(password)
        user.save()
