from django.contrib import admin
from django.urls import path
from first_app.views import index
from first_app.views import riddle
from first_app.views import answer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('riddle/',riddle,name = 'rid'),
    path('answer/',answer,name='ans')
]
