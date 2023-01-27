import json

from product.models import Variant
from product.models import Variant, Product, ProductVariant, ProductVariantPrice

from django.views import generic
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
    

@method_decorator(csrf_exempt, name='dispatch')
class ProductCreate(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)

        product_data = {
            'title': data.get('title'),
            'sku': data.get('sku'),
            'description': data.get('description'),
        }
        new_product = Product.objects.create(**product_data)
        
        return redirect('list.product')


@method_decorator(csrf_exempt, name='dispatch')
class ProductEditView(View):
    def get(self, request, id, *args, **kwargs):
        data = json.loads(request.body)
        product = Product.objects.prefetch_related('product_set').filter(id=id)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        product = Product.objects.prefetch_related('product_set').filter(id=id)
        product_data = {
            "title": data.get("title"),
            "sku": data.get("sku"),
            "description": data.get("description"),
        }
        product.title = product_data['title']
        product.sku = product_data['sku']
        product.description = product_data['description']
        product.save()

        return redirect('list.product')