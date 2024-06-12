from django import forms

class InputForm(forms.Form):
    input_word = forms.CharField(max_length=3, min_length=3, label="Enter a three-letter word")

