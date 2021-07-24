from django import forms
from .models import Post, Keyword

keywords = Keyword.objects.all().values_list('name', 'name')
keyword_list = [("-", "-")]
keyword_list.extend([item for item in keywords])


class SearchForm(forms.Form):
    content = forms.CharField(label="Czego szukasz?", help_text="", widget=forms.TextInput(attrs={'class': 'form_field'}))
    keyword = forms.ChoiceField(label="W jakim temacie?", choices=keyword_list, help_text="", widget=forms.Select(attrs={'class': 'form_field'}))

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 3:
            raise forms.ValidationError("Podaj więcej szczegółów!")