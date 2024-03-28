
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect,render
from django.views.generic import CreateView, DetailView, ListView, UpdateView



from .forms import *
from .models import *
from django.views import View



class AddClothesView(CreateView):
    modal = Clothes
    form_class = ClothesForm
    template_name = 'create_clothes.html'
    success_url = '/clothes/'

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            clothes = form.save(commit=False)
            clothes.author = self.request.user
            clothes.save()
        return redirect('clothes_list')


def clothes_view(request):
    object_list = Clothes.objects.all()
    return render(request, 'clothes.html', {'items': object_list})


class ClothesDetailsView(DetailView):
    modal = Clothes
    template_name = 'clothes_list.html'

    def get_queryset(self):
        return Clothes.objects.filter(id=self.kwargs['pk'])


class ClothesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    modal = Clothes
    form_class = ClothesForm
    template_name = 'update_clothes.html'
    success_url = '/clothes/'

    def get_queryset(self):
        return Clothes.objects.filter(id=self.kwargs['pk'])

    def test_func(self):
        clothes = self.get_object()
        if self.request.user == clothes.author:
            return True
        return False


@login_required
def delete_product(request, clothes_id: int):
    clothes = Clothes.objects.get(id=clothes_id)
    clothes.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('clothes_list')


def add_to_cart(request, clothes_id):
    clothes = Clothes.objects.get(id=clothes_id)

    # Initialize the cart in the session if it doesn't exist
    if 'cart' not in request.session:
        request.session['cart'] = []

    # Add the clothes ID to the cart
    request.session['cart'].append(clothes.id)
    request.session.modified = True  # To save the changes to the session

    return redirect('view_cart')

def view_cart(request):
    clothes_ids = request.session.get('cart', [])
    cart_items = Clothes.objects.filter(id__in=clothes_ids)

    # Calculate total amount, etc., based on your requirements

    total_amount = sum(item.price for item in cart_items)

    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_amount': total_amount})


def remove_from_cart(request, clothes_id):
    # Ensure 'cart' key exists in the session
    if 'cart' not in request.session:
        request.session['cart'] = []

    # Remove the item with the specified item_id from the cart
    if clothes_id in request.session['cart']:
        request.session['cart'].remove(clothes_id)
        request.session.modified = True  # Save changes to the session

    return redirect('view_cart')

