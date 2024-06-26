# Generated by Django 2.2.20 on 2021-04-25 14:14

from django.db import migrations


def transfer_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for number in Flat.objects.all():
        Owner.objects.get_or_create(owner=number.owner,
                                    phone_number=number.owners_phonenumber,
                                    clear_phone_number=number.owners_pure_phone
                                    )

def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner, owners_phonenumber, owners_pure_phone in Flat.objects.all():
        Owner.objects.get_or_create(owner = owner,
                                    phone_number=owner.phonenumber,
                                    clear_phone_number=owner.owners_pure_phone
                                    )

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [migrations.RunPython(transfer_owners, move_backward)
    ]
