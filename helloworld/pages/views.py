from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.

#Nota:
#TemplateView: GET y POST implementados. Útil para renderizar plantillas sin más.
#View: Hay que incluir GET y POST. Flexibilidad en la lógica de estos métodos.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 
     
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Juan Miguel", 
        }) 
 
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV", "price":100}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":200}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":20}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":15} 
    ] 
 
class ProductIndexView(View): 
    template_name = 'products/index.html' 
 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
 
        return render(request, self.template_name, viewData) 
 
class ProductShowView(View): 
    template_name = 'products/show.html' 
 
 
    def get(self, request, id):

        try: 
            viewData = {} 
            product = Product.products[int(id)-1] 
            viewData["title"] = product["name"] + " - Online Store" 
            viewData["subtitle"] =  product["name"] + " - Product information" 
            viewData["product"] = product
 
            return render(request, self.template_name, viewData)
        
        except (IndexError, ValueError):
            return HttpResponseRedirect(reverse('home')) #Si el id de la URL no existe vuelve a home

class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True)

    def clean_price(self): #clean_<fieldname>
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('The price must be greater than zero.')
        return price
 
class ProductCreateView(View): 
    template_name = 'products/create.html' 
 
    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 
 
    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid(): 
             
            return redirect('created')  
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)

class ProductCreatedView(TemplateView):
    template_name = 'products/created.html'