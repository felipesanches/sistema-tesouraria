"""sistema_tesouraria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout

from geral.views import PasswordResetViewSendgrid

urlpatterns = [
    url(r'^admin/', RedirectView.as_view(url='https://www.youtube.com/watch?v=ednKK8GlvwI')),
    url(r'^conselho/', admin.site.urls),
    url(r'^signup/', include('confirmation.urls')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^', include('geral.urls')),

    # Password Reset
    url(r'^password_reset/$', PasswordResetViewSendgrid.as_view(), name='password_reset'),
    url(r'^', include('django.contrib.auth.urls')),

    # Serve Database Files directly
    url(r'', include('database_files.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

# BAD - TODO: Refactor
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
