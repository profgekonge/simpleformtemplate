from django import forms
from . models import ModelA, ModelB

class FormA(forms.ModelForm):
    
    class Meta:
        model = ModelA
        fields = ['field1', 'field2']

class FormB(forms.ModelForm):
    
    class Meta:
        model = ModelB
        fields = ['field1', 'field2']
