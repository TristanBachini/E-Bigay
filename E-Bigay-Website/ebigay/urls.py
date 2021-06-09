from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register-ayuda/', views.register_ayuda, name="register-ayuda"),
    path('register-account/', views.register_account, name="register-account"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('ayudadropoff/', views.ayuda_dropoff, name="ayudadropoff"),
    path('dropoff-list/', views.dropoff_list, name="dropoff-list"),
    path('dropoff-list-delete/<str:pk>', views.dropoff_list_delete, name="dropoff-list-delete"),
    path('ayuda-schedule', views.ayuda_schedule, name="ayuda-schedule"),
    path('ayuda-list-delete', views.ayuda_list_delete, name="ayuda-list-delete"),

    path('mission-vision/', views.mission_vision, name="mission-vision"),
    path('story/', views.story, name="story"),
    path('donate/', views.donate, name="donate"),
    path('volounteer/', views.volounteer, name="volounteer"),
    path('terms-of-service/', views.terms_of_service, name="terms-of-service"),
]