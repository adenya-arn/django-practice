from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]


class RawProductionForm(forms.Form):
    title =forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
    description = forms.CharField(required= False,
        widget=forms.Textarea(
            attrs={
                "placeholder":"Your Description",
                "class":"new-class-name-two",
                "rows":20,
                "cols":120,
                "id":"my-id-for-textarea",

                }
            ),
        )
    price = forms.DecimalField(initial = 12.99)

 