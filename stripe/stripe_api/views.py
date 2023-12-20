from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import stripe

import stripe.settings
from .models import Item

stripe.api_key = stripe.settings.STRIPE_SECRET_KEY
publick_key = stripe.settings.STRIPE_SECRET_KEY


def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'stripe_api/index.html', context=context)


def get_stripe_session_id(request, id):
    item = get_object_or_404(Item, id=id)

    session = stripe.checkout.Session.create(
        line_item=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': item.name},
                    'unit_amount': item.price,
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        succes_url=stripe.settings.DOMAIN + '/success/',
        cancel_url=stripe.settings.DOMAIN + '/cancel/'
    )

    return JsonResponse({'sessionID': session.id})


def get_about_item(request, id):
    item = get_object_or_404(Item, id=id)
    context = {'item': item, 'publick_key': publick_key}
    return render(request, 'stripe_api/checkout.html', context=context)


def success(request):
    return HttpResponse('Ok!')


def cancel(request):
    return HttpResponse('No!')
