from django.urls import path
from home import views
from home import views_user
from django.views.generic.base import RedirectView
urlpatterns = [
    path('index', views.index),
    path('reg',views.register),
    path('forum', views.forum),
    path('topic/<int:id>',views.topic),
    path('logout',views_user.logout_view),
    path('login',views_user.login_view)

]