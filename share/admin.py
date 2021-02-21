from django.contrib import admin
from .models import Image
from .models import Friend
from .models import Post

admin.site.register(Image)
admin.site.register(Friend)
admin.site.register(Post)