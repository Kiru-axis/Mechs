from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path("mechanic/<int:pk>/",views.mechanic, name='mechanic'),
    path('services/', views.services, name='services'),
    path('mechanic/<int:pk>/add-comment', views.add_comment, name='add-comment'),
    path('contact/', views.contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
