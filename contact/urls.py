
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<int:contact_id>/', views.Contact, name='contact'),
    path('', views.index, name='index' ),
]

