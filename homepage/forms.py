from django import forms

class QueryForm(forms.Form):
    statefp = forms.CharField(max_length=2, label='State FIPS Code')
    cd116fp = forms.CharField(max_length=5, label='Congressional District Code')