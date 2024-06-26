# Generated by Django 2.2.20 on 2021-04-25 13:58
import phonenumbers
from django.db import migrations

def fix_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for number in Flat.objects.all():
        checked_number = phonenumbers.parse(number.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(checked_number):
            number.owners_pure_phone = phonenumbers.format_number(checked_number, phonenumbers.PhoneNumberFormat.E164)
            number.save()

def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for number in Flat.objects.all():
        number.owners_pure_phone = ''
        number.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owners_pure_phone'),
    ]

    operations = [migrations.RunPython(fix_numbers, move_backward)
    ]
