from django import forms

#create form class here
class NewsLetterForm(forms.Form):
  your_name = forms.CharField(label= 'First Name', max_length=30)
  email = forms.EmailField(label='Email')
  