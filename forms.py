from django.forms import forms

# then I change as below field:

from django import forms


from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','sexo','data_nascimento','email','profissao']