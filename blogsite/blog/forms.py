from django import forms
from .models import Keyword


class SearchForm(forms.Form):
    content = forms.CharField(label="Czego szukasz?", help_text="", required=False, widget=forms.TextInput(attrs={'class': 'form_field'}))
    keyword = forms.ChoiceField(label="W jakim temacie?", help_text="", widget=forms.Select(attrs={'class': 'form_field'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        keywords = Keyword.objects.all().values_list('name', 'name').order_by('name')
        keyword_list = [("-", "-")]
        keyword_list.extend(keywords)
        self.fields['keyword'].choices = keyword_list