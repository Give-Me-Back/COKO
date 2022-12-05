# Generated by Django 4.1.3 on 2022-12-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deathcnt', models.IntegerField(blank=True, db_column='deathCnt', null=True)),
                ('defcnt', models.TextField(blank=True, db_column='defCnt', null=True)),
                ('gubun', models.TextField(blank=True, null=True)),
                ('gubuncn', models.TextField(blank=True, db_column='gubunCn', null=True)),
                ('gubunen', models.TextField(blank=True, db_column='gubunEn', null=True)),
                ('incdec', models.TextField(blank=True, db_column='incDec', null=True)),
                ('isolclearcnt', models.IntegerField(blank=True, db_column='isolClearCnt', null=True)),
                ('isolingcnt', models.TextField(blank=True, db_column='isolIngCnt', null=True)),
                ('localocccnt', models.IntegerField(blank=True, db_column='localOccCnt', null=True)),
                ('overflowcnt', models.IntegerField(blank=True, db_column='overFlowCnt', null=True)),
                ('qurrate', models.TextField(blank=True, db_column='qurRate', null=True)),
                ('stdday', models.DateTimeField(blank=True, db_column='stdDay', null=True)),
            ],
            options={
                'db_table': 'corona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CoronaCon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jcg_dt', models.DateTimeField(blank=True, db_column='JCG_DT', null=True)),
                ('variable', models.TextField(blank=True, null=True)),
                ('con', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'corona_con',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('originallink', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('pubdate', models.DateTimeField(blank=True, db_column='pubDate', null=True)),
            ],
            options={
                'db_table': 'news',
                'managed': False,
            },
        ),
    ]
