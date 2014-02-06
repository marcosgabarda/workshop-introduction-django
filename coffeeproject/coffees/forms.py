from django.forms import ModelForm
from coffees.models import Coffee


class CreateCoffee(ModelForm):

    class Meta:
        model = Coffee
        fields = ['name', 'picture']