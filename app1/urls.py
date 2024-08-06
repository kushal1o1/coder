from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home')
]

admin.site.site_header='CODE SHARE'
admin.site.site_title='ADMIN PANNEL'