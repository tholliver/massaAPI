from django.urls import path
from .views import LogOutView, PostList, PostDetail, RegisterView, LoginView, UserView

urlpatterns = [
    
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogOutView.as_view()),
    path('user', UserView.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]