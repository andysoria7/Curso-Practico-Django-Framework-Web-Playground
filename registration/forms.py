from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    # Valida si existe ya un email en el sistema, devuelve un error.
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}), # Este widget nos permitira limpiar el campo con el checkbox "limpiar".
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografia'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")
    
    class Meta:
        model = User
        fields = ['email']
    
    # Valida si existe ya un email en el sistema, devuelve un error.
    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Valida si el campo email ha cambiado.
        if 'email' in self.changed_data: # Es una lista que almacena todos los campos que se han editado en el formulario (self.changed_data)
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email
    
    