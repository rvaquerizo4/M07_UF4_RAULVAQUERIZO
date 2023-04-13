from django.forms import ModelForm
from .models import Alum, Prof

class AlumForm(ModelForm):
    class Meta:
        model = Alum
        fields = '__all__'

class ProfForm(ModelForm):
    class Meta:
        model = Prof
        fields = '__all__'