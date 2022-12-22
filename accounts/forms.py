from django import  forms
from .models import Account, UserProfile

#formulario  para registro de usuario
#froms son formas que django crea cosas en html  como ejemplo caja de texto
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'placeholder': 'Ingrese Password',
                'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'placeholder':'Confirmar Password',
                'class': 'form-control',
    }))
    class Meta:
        model= Account
        fields = ['first_name', 'last_name', 'phone_nuber', 'email', 'password']
    #se crear esta funcion con el proposito de  poder  mostrar  los campos que se requieren 
    def __init__(self, *args, **kwargs):

        super(RegistrationForm, self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Ingrese nombre'
        self.fields['last_name'].widget.attrs['placeholder']='Ingrese apellidos'
        self.fields['phone_nuber'].widget.attrs['placeholder']='Ingrese telefono'
        self.fields['email'].widget.attrs['placeholder']='Ingrese email'
        #los fiels representan cada  caja de texto que se a registrado
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "El password no coincide"
            )

class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_nuber')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid': ('Solo archivos de imagen')}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
