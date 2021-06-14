from django.contrib import admin
from .models import Place, Tag, User, UserPlace

admin.site.register(Place)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(UserPlace)

