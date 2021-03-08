from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"
    
    def get(self, request, **kwargs):
        return super().get(request, **kwargs)
    
class DashboardView(generic.TemplateView):
    template_name = "app/dashboard.html"
    
    def get(self, request, **kwargs):
        return super().get(request, **kwargs)
    
class SigninView(generic.TemplateView):
    template_name = "app/sign-in.html"
    
    def get(self, request, **kwargs):
        return super().get(request, **kwargs)
    
class SignupView(generic.TemplateView):
    template_name = "app/sign-up.html"
    
    def get(self, request, **kwargs):
        return super().get(request, **kwargs)

class TableView(generic.TemplateView):
    template_name = "app/table.html"
    
    def get(self, request, **kwargs):
        return super().get(request, **kwargs)
    
class FormView(generic.TemplateView):
    template_name = "app/form.html"
    
    def get(self, request, **kwargs):
        return super().get(request, **kwargs)
    
class NotFoundView(generic.TemplateView):
    template_name = "app/404.html"
    
    def get(self, request, **kwargs):
        return super().get(request, **kwargs)