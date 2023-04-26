from django import forms

from django.core import validators

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name should not with a')
    
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,validators.MaxLengthValidator(5)])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    '''def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('data did not matched')'''

    '''def clean_age(self):
        a=self.cleaned_data['age']
        if a<18:
            raise forms.ValidationError('age is less then 18')'''

    '''def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('data is not entered by human')'''
        
    

