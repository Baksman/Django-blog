
from django.contrib import admin
from users import views as user_views
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("blog.urls")),
    path("register/",user_views.register, name="register")   
]
