from django.contrib import admin
from osb.models import User, Group, Topics, Comments

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Topics)
admin.site.register(Comments)
