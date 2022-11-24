from django import forms
from . import models


# class jkkForm(forms.ModelForm):
#     class Meta:
#         model = models.Jkk
#         fields = '__all__'
#         # widgets = {
#         #     'x': forms.HiddenInput(),
            
#         # }

class jkks8Form(forms.ModelForm):
    class Meta:
        model = models.Jkks8
        fields = '__all__'
    

# class periodjkkForm(forms.ModelForm):
#     class Meta:
#         model = models.periodJkk
#         fields = ['jkk_tm','auditor']

# class checkjkkForm(forms.ModelForm):
#     class Meta:
#         model = models.checkJkk
#         fields = ['timecheck']

# class stopwatchForm(forms.ModelForm):
#     class Meta:
#         model = models.stopwatch
#         fields = ['timeelement']