# wardrobe/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import WardrobeItem
from .forms import WardrobeItemForm

class WardrobeItemListView(ListView):
    model = WardrobeItem
    template_name = 'wardrobe/wardrobe_list.html'
    context_object_name = 'items'

class WardrobeItemDetailView(DetailView):
    model = WardrobeItem
    template_name = 'wardrobe/wardrobe_detail.html'
    context_object_name = 'item'

class WardrobeItemCreateView(CreateView):
    model = WardrobeItem
    form_class = WardrobeItemForm
    template_name = 'wardrobe/wardrobe_form.html'
    success_url = reverse_lazy('wardrobe:list')
    

class WardrobeItemUpdateView(UpdateView):
    model = WardrobeItem
    form_class = WardrobeItemForm
    template_name = 'wardrobe/wardrobe_form.html'
    success_url = reverse_lazy('wardrobe:list')

class WardrobeItemDeleteView(DeleteView):
    model = WardrobeItem
    template_name = 'wardrobe/wardrobe_confirm_delete.html'
    success_url = reverse_lazy('wardrobe:list')
