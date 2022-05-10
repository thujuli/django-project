from django.forms import ModelForm
from .models import Article
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
