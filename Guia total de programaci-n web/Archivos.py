'''
   Se asumira de antemano que se tiene instalado el ambiente virtual y la version de python/Django que prefieran.
   Todo lo que esta entre <> (signos de mayor, menor que) se tiene que reemplazar.
'''

# ==========================================================================
# 01.-Crear el proyecto:
# ==========================================================================

(ambiente_virtual)$django-admin.py startproject nombreProyecto

# ==========================================================================
# 02.-Crear la aplicación:
# ==========================================================================

(ambiente_virtual)$python manage.py starapp nombreApp

# ==========================================================================
# 03.-Configurar el archvio settings.py:
# ==========================================================================

setting.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ------------------------------------------------------
        # Agregar la ruta en donde esta la carpeta de templates:
        # ------------------------------------------------------
        'DIRS': ["<ruta>"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALED_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  # ------------------------------------------------------
  # Agregar la app:
  # ------------------------------------------------------
  '<nombreApp>',
)

# ==========================================================================
# 04.- Crear una vista:
# ==========================================================================

views.py

from django.shortcuts import render

def <nombreVista>(request):
  return render(request, '<nombreArchivo>.html', {})
  
# ==========================================================================
# 05.- Modificar el archivo del proyecto urls.py:
# ==========================================================================

urls.py

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('<nombreApp>.urls')),
]

# ==========================================================================
# 06.- Craar y configurar el archivo de la aplicacin urls.py:
# ==========================================================================

urls.py

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.<urlBase>), # Esta esla url que se abrira por defecto en el servidor:
    url(r'^<Url>/$', views.<nombreVista>, name="<nombreUrl>"), # Esta es una url normal
]
