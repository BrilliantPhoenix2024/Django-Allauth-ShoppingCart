from django import forms


# This is a Sample Form for Showing Product in cart, and you can change it based on your Project.
class AddToCartProductForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
