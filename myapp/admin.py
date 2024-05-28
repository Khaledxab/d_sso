# To fix the AlreadyRegistered error, modify the file `myapp/admin.py` as follows:

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

# Unregister the default User model and then register the custom User model
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
