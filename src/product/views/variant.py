from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from product.forms import VariantForm
from product.models import Variant


class BaseVariantView(generic.View):
    form_class = VariantForm
    model = Variant
    template_name = 'variants/create.html'
    success_url = '/product/variants'


class VariantView(BaseVariantView, ListView):
    template_name = 'variants/list.html'
    paginate_by = 10

    def get_queryset(self):
        filter_string = {}
        # print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return Variant.objects.filter(**filter_string)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = True
        context['request'] = ''
        if self.request.GET:
            context['request'] = self.request.GET['title__icontains']
        return context


class VariantCreateView(BaseVariantView, CreateView):
    pk_url_kwarg = 'id'
    context_object_name = 'variant_create'
    fields = ['title', 'description', 'active']
    success_url = reverse_lazy('variants')

class VariantEditView(BaseVariantView, UpdateView):
    pk_url_kwarg = 'id'
    template_name = 'variants/create.html'
    fields = ['title', 'description', 'active']
    success_url = reverse_lazy('variants')


class VariantDeleteView(BaseVariantView, DeleteView):
    template_name = 'variants/delete_confirm.html'
    context_object_name = 'variant_delete'
    success_url = reverse_lazy('variants')