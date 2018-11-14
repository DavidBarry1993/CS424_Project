from django import forms

from laochragael.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model=Player
        exclude=[]
