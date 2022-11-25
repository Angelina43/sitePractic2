# Код модуля пакета приложения

from django.urls import path
from .views import index
from .views import other_page
from .views import BBLoginView
from .views import profile
from .views import BBLogoutView
from .views import ChangeUserInfoView
from .views import BBPasswordChangeView
from .views import RegisterUserView, RegisterDoneView
from .views import user_activate
from .views import DeleteUserView
from .views import new_orders
from .views import doing_orders
from .views import done_orders
from .views import product

app_name = 'main'

urlpatterns = [
    path('new_orders', new_orders, name='new_orders'),
    path('doing_orders', doing_orders, name='doing_orders'),
    path('done_orders', done_orders, name='done_orders'),
    path('product', product, name='product'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index')
]
