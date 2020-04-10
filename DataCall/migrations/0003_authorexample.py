# Generated by Django 3.0.3 on 2020-03-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataCall', '0002_auto_20200203_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorExample',
            fields=[
                ('authorid', models.AutoField(db_column='AuthorID', primary_key=True, serialize=False)),
                ('authorfname', models.CharField(db_column='AuthorFName', max_length=50)),
                ('authorlname', models.CharField(db_column='AuthorLName', max_length=50)),
                ('authorage', models.CharField(blank=True, db_column='AuthorAge', max_length=50, null=True)),
                ('authorcountry', models.CharField(blank=True, max_length=50, null=True)),
                ('alive', models.BooleanField()),
                ('sex', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Author',
                'managed': False,
            },
        ),
    ]
