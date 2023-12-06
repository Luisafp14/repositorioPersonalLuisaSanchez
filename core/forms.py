from django import forms
from .models import Cita
from django.utils import timezone

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'hora', 'taller']
    
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = timezone.localdate()
        max_date = today + timezone.timedelta(days=60) 
        self.fields['fecha'].widget.attrs['min'] = today
        self.fields['fecha'].widget.attrs['max'] = max_date
        
    

    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M']
    )

    def clean_hora(self):
        hora = self.cleaned_data.get('hora')
        if hora:
            if hora >= timezone.datetime.today().time().replace(hour=16, minute=0) or hora < timezone.datetime.today().time().replace(hour=8, minute=0):
                raise forms.ValidationError("Las citas solo están disponibles entre las 8:00 AM y las 6:00 PM.")
        return hora