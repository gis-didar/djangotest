from django.urls import path
from .views import home, visual, upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('', home, name ='home'),
path('upload', upload,name='upload'),
path('viewing', visual, name = 'visual' )
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
