from django.urls import path
from .views import Register, CreateProduct, CategoryView, SavatView



urlpatterns = [
    path('signup/', Register.as_view()),
    path('product/', CreateProduct.as_view()),
    path('category/', CategoryView.as_view()),
    path('savat/', SavatView.as_view()),
]