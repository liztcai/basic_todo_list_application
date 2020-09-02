from django import forms

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task', 'class':'mdc-text-field__input'}))
