from parler.forms import TranslatableModelForm, TranslatedField
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django import forms
from .models import ContentNode

class ContentNodeForm(TranslatableModelForm):

    def __init__(self, *args, **kwargs):
        super(ContentNodeForm, self).__init__(*args, **kwargs)
        print(self.Meta.exclude)
        for lang_code, lang_name in settings.LANGUAGES:
            #I have no clue why this doesn't work without the try/except.
            try:
                self.instance.set_current_language(lang_code)
                self.fields["name_"+lang_code] = forms.CharField(label=_("Name ")+" ("+lang_code+")", max_length=100, required=True, initial=self.instance.name)
            except:
                self.instance.set_current_language(lang_code)

    def save(self, commit=True):
        instance = super(ContentNodeForm, self).save(commit=False)
        instance.save()
        for lang_code, lang_name in settings.LANGUAGES:
            instance.set_current_language(lang_code)
            instance.name = self.cleaned_data['name_'+lang_code]
            instance.save()
        return instance

    class Meta:
        model = ContentNode
        fields = '__all__'
        exclude = ("name", "content")