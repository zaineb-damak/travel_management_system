from django.urls import path
from payment import views

urlpatterns = [
path('payments/', views.PaymentList.as_view(), name='payment-list'),
path('payments/<int:pk>/', views.PaymentDetail.as_view(), name='payment-detail'),
path('bookings/<int:pk>/pay/', views.PaymentCreate.as_view(), name='pay-booking'),
]