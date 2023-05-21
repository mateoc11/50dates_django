from django import forms  

class photoForm(forms.Form):
    image_id = forms.CharField(label="",max_length=10)  
    user_id = forms.CharField(label="",max_length=10) 
    file = forms.FileField()