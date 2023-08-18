from django import forms

class cohorte1Validacion (forms.Form):
        CI = forms.CharField(label = 'numero de cedula', max_length = 50)

