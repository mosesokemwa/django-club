from django import forms


# this is the context('form': form)
class follow(forms.Form):
    user_text = forms.CharField(label="Enter Text", min_length=1, max_length=100)
    key = forms.IntegerField(label="Enter Key")


class Ceaser(forms.Form):
    user_text = forms.CharField(label="Enter Text", min_length=1, max_length=100)
    key = forms.IntegerField(label="Enter Key")
