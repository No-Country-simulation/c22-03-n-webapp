from django.forms import *

from users.models import Users

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class']='form-control'
        #     form.field.widget.attrs['autocomplete']='off'
        self.fields['dni'].widget.attrs['autofocus']=True


    class Meta:
        model = Users
        fields = '__all__'
        widgets = {
            'dni': NumberInput(
                attrs={
                    'placeholder' : 'Ingrese su dni',
                }
            ),
            'name': TextInput(
                attrs={
                    'placeholder' : 'Ingrese su nombre',
                }
            ),
             'surname': TextInput(
                attrs={
                    'placeholder' : 'Ingrese su apellido',
                }
            ),
            'phone_number': TextInput(
                attrs={
                    'placeholder' : 'Ingrese su número de teléfono',
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder' : 'Ingrese su email',
                }
            ),
            'direction': Textarea(
                attrs={
                    'placeholder' : 'Ingrese su dirección',
                }
            ),
            'birthdate': NumberInput(
                attrs={
                    'placeholder' : 'Ingrese su fecha de nacimiento',
                }
            )
        }
       