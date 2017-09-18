#Extender modelos de usuarios en jango:

#1.- Generar un modelo en django:

from django.contrib.auth.models import User

class Ususarios(model.Model):
  name = models.OneToOneField(User)
  phone = models.IntegerField()
  email = models.CharField(max_length=48)
  aaddress = models.CharField(max_length=256)
  
#2.- Importar el modelo (archivo admin site):


#3.- Crear el formulario:

from django.contrib.auth.fomrs import UserCreationForm

class Users_Form(UserCreationForm):
  phone = forms.IntegerField()
  email = forms.CharField(max_length=48)
  addres = forms.CharField(max_legth=256)
  
#4.- Crear la vista:

from django.views.generic

class SignUp(FormView):
  template_name = 'home/signup.html'
  form_class = UsersForm
  success_url = reverse_lazy('login')
  
  def form_valid(self, form)
    user = form.svae()
    p = Usuarios()
    p.name = user
    p.phone = form.cleaned_data['phone']
    p.email = form.cleaned_data['email']
    p.address = form.cleaned_data['address']
    p.save()
    return super(SignUp, self).form_valid(form)

#5.-Generar el template:

{% extends 'base.html' %}
{% block title %}SignUp{% endblock %}
{% block content %}
<form method="POST"
  {%csrf_token %}
  {{ form.as_p }}
  <input tupe="submit" value="SignUp">
  <input tupe="reset" value="Cancel">
  
{% endblock %}

#6.-Crear la url:
url(r'^signup/$', views.SignUp.as_view(), naame="SingUp_view")

#7.-Realizar la migracion:
#En la terminal: colocarse en la carpeta del proyecto:

python manage.py make migration
python manage.py migrate
