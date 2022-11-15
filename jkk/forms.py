from django import forms
from . import models


# class jkkForm(forms.ModelForm):
#     class Meta:
#         model = models.Jkk
#         fields = '__all__'
#         # widgets = {
#         #     'x': forms.HiddenInput(),
            
#         # }

class dailyjkkForm(forms.ModelForm):
    class Meta:
        model = models.dailyJkk
        fields = ['dailyprocess']
    

class periodjkkForm(forms.ModelForm):
    class Meta:
        model = models.periodJkk
        fields = ['jkk_dayly_tm','auditor']

# class checkjkkForm(forms.ModelForm):
#     class Meta:
#         model = models.checkJkk
#         fields = ['timecheck']

class stopwatchForm(forms.ModelForm):
    class Meta:
        model = models.stopwatch
        fields = ['timeelement']