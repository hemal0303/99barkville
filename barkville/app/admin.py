from django.contrib import admin
from .models import *
from django import forms

admin.site.register(Breed)
admin.site.register(Blog)


class DogForm(forms.ModelForm):
    with_kids = forms.CharField(label="Behavior with Kids")
    with_adults = forms.CharField(label="Behavior with Adults")
    with_other_dogs = forms.CharField(label="Behavior With Other Dogs")

    class Meta:
        model = Dog
        fields = "__all__"
        exclude = ("behavior",)


class DogAdmin(admin.ModelAdmin):
    form = DogForm


admin.site.register(Dog, DogAdmin)
