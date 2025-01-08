from django.urls import path
from rent_house import views

urlpatterns = [
    path('',views.Index.as_view(),name = 'home'),
    path('about/',views.about,name = 'about'),
    path('post/<slug:post_slug>/',views.ShowPost.as_view(),name='post'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('add_apartment/',views.add_apartment.as_view(),name='apart'),
    path('contact/',views.contact,name='contact'),
    path('profile/',views.profile,name='profile'),
    path('edit/<slug:slug>/',views.edit_page.as_view(),name='edit'),
]
