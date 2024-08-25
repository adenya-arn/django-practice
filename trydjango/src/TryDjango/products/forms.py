from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label="", 
                widget=forms.TextInput(attrs={"placeholder":"Your Title"})) 
    email =  forms.EmailField()
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

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")

        if not "CFE" in title:
            raise forms.ValidationError("This Is Not A Valid Title")
        if not "NEWS" in title:
            raise forms.ValidationError("This Is Not A Valid Title")
        else:
            return title 

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")

        if not email.endswith("edu"):
            raise forms.ValidationError("This is not the right email")
        return email 



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
