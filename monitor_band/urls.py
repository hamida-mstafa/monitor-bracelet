"""monitor_band URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from monitor_band import settings
from monitor_band.views import index,get_values,get_latest_temp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name="home"),
    url(r"^post_temp$",get_values,name="post_temp"),
    url(r"^get_latest_temp$",get_latest_temp,name="get_latest_temp")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)