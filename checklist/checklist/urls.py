from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('create/',views.CreateView, name='create'),
    path('all_data/',views.HomeView, name='all_data'),
    path('detail/<int:id>',views.DetailView, name='detail'),
    path('update/<int:id>',views.UpdateView, name='update'),
    path('delete/<int:id>',views.DeleteView, name='delete'),



]
