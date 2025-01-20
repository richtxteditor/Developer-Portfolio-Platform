from django.core.exceptions import ValidationError

def validate_file_size(value):
    max_size = 10 * 1024 * 1024  # 10MB limit
    if value.size > max_size:
        raise ValidationError('The maximum file size that can be uploaded is 10MB')
    else:
        return value

