from django.core.exceptions import ValidationError

def validate_file_size(file):
    """this validate if file size is less then 50 mb"""
    max_size=50
    max_size_in_bytes=max_size*1024*1024

    if file.size>max_size_in_bytes:
        raise ValidationError(f'file can not be larger than {max_size}MB')