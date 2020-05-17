from django import forms
from .models import Subscription

class SubsForm(forms.ModelForm):
	class Meta:
		model = Subscription
		fields = ['name', 'email'] 