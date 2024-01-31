"""
URL configuration for contactacontractor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from accounts.views import register, user_dashboard, user_profile
from app.views import submit_dispute

app_name = "accounts"
urlpatterns = [
    path('register/', register, name='register'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('profile/', user_profile, name='user_profile'),
    path('dashboard/submit-dispute/<str:user>/<int:job_id>/', submit_dispute, name='submit_dispute'),
]

