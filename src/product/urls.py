from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView, ProductCreate, ProductEditView
from product.views.variant import VariantView, VariantCreateView, VariantEditView, VariantDeleteView

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create/', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit/', VariantEditView.as_view(), name='update.variant'),
    path('variant/<int:id>/', VariantDeleteView.as_view(), name='delete.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
        'product': True
    }), name='list.product'),
    path('create-product/', ProductCreate.as_view(), name='create-product'),
    path('edit-product/<int:id>/', ProductEditView.as_view(), name='edit-product')
]
