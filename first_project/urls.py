from django.contrib import admin
from django.urls import path
from first_app.views import index
#abcd
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index)
]
