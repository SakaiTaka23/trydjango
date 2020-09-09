from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'not raw your title'}))
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'placeholder': 'your description', 'class': 'new-class-name two', 'rows': 20, 'cols': 120, }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'CFE' in title:
            raise forms.ValidationError('this is not a valid title')
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='raw', widget=forms.TextInput(
        attrs={'placeholder': 'your title'}))
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'placeholder': 'your description', 'class': 'new-class-name two', 'rows': 20, 'cols': 120, }))
    price = forms.DecimalField(initial=199.99)
