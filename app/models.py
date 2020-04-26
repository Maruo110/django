from django.db import models
from django.core import validators


class Trend(models.Model):

    trendword = models.CharField(
        verbose_name = 'トレンドワード',
        max_length = 200,
    )

    syutokuymd = models.DateField(
        verbose_name='取得日',
    )

    syutokutime = models.TimeField(
        verbose_name='取得時間',
    )

    tweetvolume = models.IntegerField(
        verbose_name='ツイート数',
        validators=[validators.MinValueValidator(-1)],
        blank=True,
        null=True,
    )

    avetweetsentimentscore = models.FloatField(
        verbose_name='平均ツイート感情指数',
        blank=True,
        null=True,
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテムMeta'
        verbose_name_plural = 'アイテムMetaPlural'

class Tweet(models.Model):

    userid = models.CharField(
        verbose_name = 'ユーザーID',
        max_length = 200,
    )

    tweettext = models.CharField(
        verbose_name = 'ツイートテキスト',
        max_length = 500,
    )

    retweetvolume = models.IntegerField(
        verbose_name='RT数',
        validators=[validators.MinValueValidator(0)],
    )

    favoritevolume = models.IntegerField(
        verbose_name='FV数',
        validators=[validators.MinValueValidator(0)],
    )

    tweeturl = models.CharField(
        verbose_name = 'ツイートURL',
        max_length = 200,
    )

    tweettime = models.DateTimeField(
        verbose_name='ツイート日時',
    )

    tweetsentimentscore = models.FloatField(
        verbose_name='ツイート感情指数',
        blank=True,
        null=True,
    )

    tweetsentimentsmagnitude = models.FloatField(
        verbose_name='ツイート感情強度指数',
        blank=True,
        null=True,
    )

    tweetvalidstrcount = models.IntegerField(
        verbose_name='ツイート有効文字数',
        validators=[validators.MinValueValidator(0)],
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテムMeta'
        verbose_name_plural = 'アイテムMetaPlural'


class TrendTweet(models.Model):

    trendid = models.IntegerField(
        verbose_name='トレンドID',
    )

    tweetid = models.IntegerField(
        verbose_name='ツイートID',
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテムMeta'
        verbose_name_plural = 'アイテムMetaPlural'

class TweetUrl(models.Model):

    tweetid = models.IntegerField(
        verbose_name='ツイートID',
    )

    linkedurlid = models.IntegerField(
        verbose_name='関連URLID',
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテムMeta'
        verbose_name_plural = 'アイテムMetaPlural'


class Url(models.Model):

    urlid = models.CharField(
        verbose_name = '関連リンクURL',
        max_length = 500,
    )

    sentimentscore = models.FloatField(
        verbose_name='感情指数',
        blank=True,
        null=True,
    )

    sentimentsmagnitude = models.FloatField(
        verbose_name='感情強度指数',
        blank=True,
        null=True,
    )

    validstrcount = models.IntegerField(
        verbose_name='有効文字数',
        validators=[validators.MinValueValidator(0)],
    )

    title = models.CharField(
        verbose_name = 'タイトル',
        max_length = 200,
    )

    contents = models.CharField(
        verbose_name = '本文',
        max_length = 10000,
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテムMeta'
        verbose_name_plural = 'アイテムMetaPlural'



#**************************************************************************************************
# 以下、ひな形
#**************************************************************************************************


class Item(models.Model):

    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )

    name = models.CharField(
        verbose_name='名前',
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name='年齢',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'