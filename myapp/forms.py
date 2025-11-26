# from django import forms
# from .models import BillingDetails

# class DeliveryDetailsForm(forms.ModelForm):
#     class Meta:
#         model=BillingDetails
#         fields=['full_name','email','phone','country','address','city','postal_code','created_at']


from django import forms
from .models import BillingDetails

class DeliveryDetailsForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        fields = [
            'full_name',
            'email',
            'phone',
            'country',
            'address',
            'city',
            'postal_code'
        ]
