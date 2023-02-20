"""Wishlist views"""
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist


@login_required
def get_wishlist(request):
    """
    A view to render the users wishlist
    """
    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user.userprofile)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    print(wishlist)
    return render(request, 'wishlist/wishlist.html', context=context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product from the store to the
    wishlist for the logged in user
    """
    product = get_object_or_404(Product, pk=product_id)

    user = get_object_or_404(UserProfile, user=request.user)

    wishlist, created = Wishlist.objects.get_or_create(user=user)
    print(created)
    # Add product to the wishlist
    wishlist.products.add(product)

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def remove_from_wishlist(request, product_id):
    """ Remove product from user wishlist """

    # get current product
    product = get_object_or_404(Product, pk=product_id)

    # get user wishlist
    wishlist = Wishlist.objects.get(user=request.user.userprofile)

    # remove product from the wishlist
    wishlist.products.remove(product)
    messages.success(
        request, f'{product.name} was removed from your wishlist.')

    return redirect(reverse('wishlist'))
