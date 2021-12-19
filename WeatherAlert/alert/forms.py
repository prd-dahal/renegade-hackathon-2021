from .models import MembersModels, AlertModel
from django import forms


class MembersForm(forms.ModelForm):
    class Meta:
        model = MembersModels
        fields = '__all__'


class AlertForm(forms.ModelForm):

    class Meta:
        model = AlertModel
        fields = ['location', 'river_level']
