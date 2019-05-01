from bootstrap_datepicker_plus import DatePickerInput
from django import forms


class ToDoForm(forms.Form):
    todo = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control"})
    )

    date = forms.DateField(
        widget=DatePickerInput(format='%d-%m-%Y')
    )


class CommentForm(forms.Form):
    name = forms.CharField(label='Your name')
    url = forms.URLField(label='Your website', required=False)
    comment = forms.CharField()




