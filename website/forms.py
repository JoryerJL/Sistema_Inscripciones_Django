from django import forms

class InscripcionAlumnoCursoForm(forms.Form):
    comprobante_domicilio = forms.FileField()
    curp = forms.FileField()
    identificacion_oficial = forms.FileField()
    comprobante_pago = forms.FileField()
    comprobante_estudios = forms.FileField()
    acta_nacimiento = forms.FileField()