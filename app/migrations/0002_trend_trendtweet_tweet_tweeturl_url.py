# Generated by Django 2.1.3 on 2020-04-26 04:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trendword', models.CharField(max_length=200, verbose_name='トレンドワード')),
                ('syutokuymd', models.DateField(verbose_name='取得日')),
                ('syutokutime', models.TimeField(verbose_name='取得時間')),
                ('tweetvolume', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-1)], verbose_name='ツイート数')),
                ('avetweetsentimentscore', models.FloatField(blank=True, null=True, verbose_name='平均ツイート感情指数')),
            ],
            options={
                'verbose_name': 'アイテムMeta',
                'verbose_name_plural': 'アイテムMetaPlural',
            },
        ),
        migrations.CreateModel(
            name='TrendTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trendid', models.IntegerField(verbose_name='トレンドID')),
                ('tweetid', models.IntegerField(verbose_name='ツイートID')),
            ],
            options={
                'verbose_name': 'アイテムMeta',
                'verbose_name_plural': 'アイテムMetaPlural',
            },
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200, verbose_name='ユーザーID')),
                ('tweettext', models.CharField(max_length=500, verbose_name='ツイートテキスト')),
                ('retweetvolume', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='RT数')),
                ('favoritevolume', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='FV数')),
                ('tweeturl', models.CharField(max_length=200, verbose_name='ツイートURL')),
                ('tweettime', models.DateTimeField(verbose_name='ツイート日時')),
                ('tweetsentimentscore', models.FloatField(blank=True, null=True, verbose_name='ツイート感情指数')),
                ('tweetsentimentsmagnitude', models.FloatField(blank=True, null=True, verbose_name='ツイート感情強度指数')),
                ('tweetvalidstrcount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='ツイート有効文字数')),
            ],
            options={
                'verbose_name': 'アイテムMeta',
                'verbose_name_plural': 'アイテムMetaPlural',
            },
        ),
        migrations.CreateModel(
            name='TweetUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetid', models.IntegerField(verbose_name='ツイートID')),
                ('linkedurlid', models.IntegerField(verbose_name='関連URLID')),
            ],
            options={
                'verbose_name': 'アイテムMeta',
                'verbose_name_plural': 'アイテムMetaPlural',
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlid', models.CharField(max_length=500, verbose_name='関連リンクURL')),
                ('sentimentscore', models.FloatField(blank=True, null=True, verbose_name='感情指数')),
                ('sentimentsmagnitude', models.FloatField(blank=True, null=True, verbose_name='感情強度指数')),
                ('validstrcount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='有効文字数')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('contents', models.CharField(max_length=10000, verbose_name='本文')),
            ],
            options={
                'verbose_name': 'アイテムMeta',
                'verbose_name_plural': 'アイテムMetaPlural',
            },
        ),
    ]
