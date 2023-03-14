from django.urls import path, include

from users.views import Register, Account

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('account/', Account.as_view(), name='account'),
]