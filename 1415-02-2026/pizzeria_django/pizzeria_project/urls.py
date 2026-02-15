from django.urls import include
from django.urls import path
from . import views

# TODO: Dodaj routing do swoich appow w miare ich tworzenia, np:
#   path('menu/', include('menu_app.urls')),
#   path('klienci/', include('customers_app.urls')),
#   path('zamowienia/', include('orders_app.urls')),

urlpatterns = [
    # path('hello/', views.hello),
    # path('books/', views.book_list),
    path('menu/', include('menu_app.urls')),
    path('klienci/', include('customers_app.urls')),
    path('zamowienia/', include('orders_app.urls')),
]
