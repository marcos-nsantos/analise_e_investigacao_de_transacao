from django.core.exceptions import ValidationError


def validate_csv(file):
    """Validates the CSV file"""
    if not file.name.endswith('.csv'):
        raise ValidationError('O arquivo deve ser do tipo CSV.')
    if not file.size < 10485760:
        raise ValidationError('O arquivo deve ter no máximo 10MB.')
    if file.size == 0:
        raise ValidationError('O arquivo não pode estar vazio.')
