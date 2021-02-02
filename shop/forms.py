from django import forms

class SearchForm(forms.Form):

    search_fiel = forms.CharField()