from django import forms
from .models import members

class memberForm(forms.ModelForm):
    class Meta:
        model = members
        fields = ['name',
                 'enrollment_number',
                 'email',
                 'course',
                 'semester',
                 'club'
                 ]
        
        widgets = {
            'name' : forms.TextInput(attrs = {'class':'form-control', 'label': 'name', 'autofocus': True}),
            'enrollment_number' : forms.NumberInput(attrs = {'class':'form-control','label': 'enrollment_number'}),
            'email' : forms.TextInput(attrs = {'class':'form-control', 'label': 'email'}),
            'course' : forms.Select(attrs = {'class':'form-control', 'label': 'course'}),
            'semester' : forms.Select(attrs = {'class':'form-control', 'label': 'semester'}),
            'club' : forms.Select(attrs = {'class':'form-control', 'label': 'club'}),
        }

        labels = {
            'name' : "name",
            'enrollment_number' : "enrollment_number",
            'email'  : "email",  
            'course'  : "course",  
            'semester'  : "semester",  
            'club' : "club"
        }