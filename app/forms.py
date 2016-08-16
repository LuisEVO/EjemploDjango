from django.forms import ModelForm
from .models import *


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('__all__')

    def __init__(self, **kwargs):
        super(AuthorForm, self).__init__(**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})