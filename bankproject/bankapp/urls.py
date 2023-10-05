# from . import views
# from django.urls import path
# app_name='bankapp'
# urlpatterns = [
#     path('', views.base, name='base'),
#     path('register/',views.register,name='register'),
#     path('login/',views.login,name='login'),
    # path('logout/',views.logout,name='logout')
# ]
# from django.urls import path
# from django.views.generic import RedirectView
#
# urlpatterns = [
#     path('', RedirectView.as_view(url='/base'),
#     path('register/', RedirectView.as_view(url='/register')),
#     path('login/', RedirectView.as_view(url='/login')),
#     path('logout/', RedirectView.as_view(url='/logout'))
# ]
# from django.urls import path
# from . import views
#
# urlpatterns = [
#
#     path('register/', views.register, name='register'),  # Add a trailing slash here
#     path('login/', views.login, name='login'),  # Add a trailing slash here as well
#      # Add a trailing slash here as well
# ]
from . import views
from django.urls import path


urlpatterns = [
    path('', views.base,name='base'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('new',views.new,name='new'),
    path('logout',views.logout,name='logout'),
    path('newpage',views.newpage,name='newpage'),
    path('message',views.msg,name='msg'),


]

