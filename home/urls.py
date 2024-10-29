from django.urls import path
from . import views
from .views import signup_view
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='index/', permanent=False), name='home'),  # Home page redirect to index
    path('index/', views.index, name='index'),  # Actual index page
    path('about/', views.about, name='about'),  # About page
    path('signup/', signup_view, name='signup'),  # Sign up page
    path('contact/', views.contact_view, name='contact'),  # Contact page
    path('login/', views.login_view, name='login'),  # Login page
    path('log_out/', views.log_out, name='logout'),  # Logout page
    path('project/', views.project, name='project'),  # Project page
]
