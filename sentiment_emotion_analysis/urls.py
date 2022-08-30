from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentiment/', include('sentiment.urls')),
    path('', include('sentiment_or_emotion.urls')),
    path('emotion/', include('emotion.urls')),
]
