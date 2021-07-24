from django import forms
from .models import Post, Keyword


class SearchForm(forms.Form):
    content = forms.CharField(label="Czego szukasz?", help_text="", widget=forms.TextInput(attrs={'class': 'form_field'}))
    keyword = forms.ChoiceField(label="W jakim temacie?", help_text="", widget=forms.Select(attrs={'class': 'form_field'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        keywords = Keyword.objects.all().values_list('name', 'name')
        keyword_list = [("-", "-")]
        keyword_list.extend([item for item in keywords])
        self.fields['keyword'].choices = keyword_list

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 3:
            raise forms.ValidationError("Podaj więcej szczegółów!")