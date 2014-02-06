from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from coffees.forms import CreateCoffee
from coffees.models import Coffee


def coffee_details(request, coffee_id):
    """
    Details of a coffee
    """
    coffee = get_object_or_404(Coffee, pk=coffee_id)
    return render(request, "coffees/details.html", {"coffee": coffee})


def coffees_list(request):
    """
    List of available coffess
    """
    coffees = Coffee.objects.all().order_by("-created_at")
    return render(request, "coffees/list.html", {"coffees": coffees})


def coffee_create(request):
    """
    Creates new type of coffee.
    """
    if request.method == "GET":
        form = CreateCoffee()
    else:
        form = CreateCoffee(request.POST, request.FILES)
        if form.is_valid():
            coffee = form.save()
            return redirect(reverse('coffee_details', kwargs={'coffee_id': coffee.pk}))
    return render(request, "coffees/new.html", {"form": form})