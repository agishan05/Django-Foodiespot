from django.shortcuts import render, get_object_or_404, redirect
from .models import Food, Order


def intro(request):
    return render(request, 'intro.html')


def home(request):

    foods = Food.objects.all()

    return render(request, 'index.html', {
        'foods': foods
    })


def order_food(request, id):

    food = get_object_or_404(Food, id=id)

    if request.method == "POST":

        name = request.POST.get('name')

        if name:  

            Order.objects.create(
                food=food,
                customer_name=name
            )

            return redirect('success')

    return render(request, 'order.html', {
        'food': food
    })


def success(request):

    return render(request, 'success.html')