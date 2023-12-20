from django.urls import path
from .views import get_about_item, get_stripe_session_id, index, success, cancel

urlpatterns = [
    path('', index, name='index'),
    path('buy/<int:id>', get_stripe_session_id, name='create-checkout-session'),
    path('item/<int:id>', get_about_item, name='item'),
    path('cancel/', cancel, name='cancel'),
    path('success/', success, name='success'),
]
