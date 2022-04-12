from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def is_csv_file(value):
    if not value.name.endswith('.csv'):
        raise ValidationError(_('O arquivo deve ser um arquivo CSV.'))
