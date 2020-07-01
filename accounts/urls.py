from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
      path('', views.home, name="home"),
      path('customers/<str:pk_text>/', views.customer, name="customers" ),
      path('products/', views.products, name= "products"),
      path('create_order/<str:pk>/', views.createOrder, name='create_order'),
      path('edit_order/<str:pk>/', views.updateOrder, name='edit_order'),
      path('delete_order/<str:pk>/', views.deleteOrder, name='delete'),
      path('login/', views.loginUser, name='login'),
      path('register/', views.register, name='register'),
      path('logout/', views.logoutUser, name='logout'),
      path('user/', views.user, name='user'),
      path('settings/', views.settings, name='settings'),

      path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='reset_password'),
      path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
      path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
      path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]