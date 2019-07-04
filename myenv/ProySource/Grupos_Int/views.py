from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Institucion
from .models import Convenio
from .models import PlanDeCapacitacion
from Grupos_Int.forms import InstitucionesForm
from Grupos_Int.forms import ConveniosForm
from Grupos_Int.forms import PlanCapForm
# Create your views here.

# Pagina Principal


def inicio(request):
    return render(request, "inicio.html", {})


def principal(request):
    return render(request, "principal.html", {})

#Instituciones 
# Pagina Principal

def inicioInst(request):
    return render(request, "inicioInst.html", {})
# Listar
class InstitucionList (ListView):
    model = Institucion
    template_name = 'instituciones_List.html'

# Registrar
class InstitucionCreate (CreateView):
    model = Institucion
    form_class = InstitucionesForm
    template_name = "instituciones_Form.html"
    success_url = reverse_lazy ("instituciones")

# Modificar

class InstitucionUpdate (UpdateView):
    model = Institucion
    form_class = InstitucionesForm
    template_name = "instituciones_Form.html"
    success_url = reverse_lazy ("instituciones")

# Eliminar

class InstitucionDelete (DeleteView):
    model = Institucion
    template_name = "instituciones_delete.html"
    success_url = reverse_lazy ("instituciones")

#Conveniones Clases
# Pagina Principal 

def inicioConv(request):
    return render(request, "inicioConv.html", {})
#Listar

class ConvenioList (ListView):
    model = Convenio
    template_name = 'convenios_List.html'
#Registrar

class ConvenioCreate (CreateView):
    model = Convenio
    form_class = ConveniosForm
    template_name = "convenios_Form.html"
    success_url = reverse_lazy ("convenios")
#Modificar

class ConvenioUpdate (UpdateView):
    model = Convenio
    form_class = ConveniosForm
    template_name = "convenios_Form.html"
    success_url = reverse_lazy ("convenios")
#Eliminar

class ConvenioDelete (DeleteView):
    model = Convenio
    template_name = "Convenios_delete.html"
    success_url = reverse_lazy ("convenios")

#Plan de Capacitación 
# Pagina Principal 

def inicioPC(request):
    return render(request, "plan_cap_inicio.html", {})
# Listar
class PlanCapList (ListView):
    model = PlanDeCapacitacion
    template_name = "plan_cap_List.html"

# Registrar
class PlanCapCreate (CreateView):
    model = PlanDeCapacitacion
    form_class = PlanCapForm
    template_name = 'plan_cap_Form.html'
    success_url = reverse_lazy ("plan_cap")

# Modificar

class PlanCapUpdate (UpdateView):
    model = PlanDeCapacitacion
    form_class = PlanCapForm
    template_name = 'plan_cap_Form.html'
    success_url = reverse_lazy ("plan_cap")

# Eliminar

class PlanCapDelete (DeleteView):
    model = PlanDeCapacitacion
    template_name = 'plan_cap_delete.html'
    success_url = reverse_lazy ("plan_cap")
