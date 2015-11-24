from django.utils.translation import ugettext_lazy as _
q = [
    {
        'question': _('What country are you from?'),
        'answers': [
            _('Iraq'),
            _('Syria'),
            _('Afghanistan'),
            _('Pakistan'),
            _('other')
        ]
    },
    {
        'question': _('What is your destination?'),
        'answers': [
            _('I want to stay in Austria'),
            _('Germany'),
            _('Sweden'),
            _('United Kingdom'),
            _('other European country'),
        ]
    },
    {
        'question': _('Do you need a doctor?'),
        'answers': [
            _('No'),
            _('Yes')
         ]
    },
]