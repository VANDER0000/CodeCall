
from django.contrib import admin
from django.urls import path
from rooms.views import home, room_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('room/<str:room_code>/', room_detail, name='room'),
]