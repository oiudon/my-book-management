from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category(models.Model):
    """3.カテゴリ"""

    class Meta:
        # テーブル名
        db_table = "category"
        # 管理サイトで使用するテーブル名
        verbose_name = verbose_name_plural = "3.カテゴリ"

    # 1.レコードID
    id = models.AutoField(verbose_name="レコードID", primary_key=True)
    # 2.カテゴリ名
    category_nm = models.CharField(
        verbose_name="カテゴリ名", max_length=20, unique=True
    )
    # 3.登録者ID
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="登録者ID", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.category_nm


class ReadingList(models.Model):
    """1.読書リスト"""

    class Meta:
        # テーブル名
        db_table = "reading_list"
        # 管理サイトで使用するテーブル名
        verbose_name = verbose_name_plural = "1.読書リスト"

    # 1.レコードID
    id = models.AutoField(verbose_name="レコードID", primary_key=True)
    # 2.書籍ID
    book_id = models.CharField(verbose_name="書籍ID", max_length=30, unique=True)
    # 3.タイトル
    title = models.CharField(verbose_name="タイトル", max_length=120, unique=True)
    # 4.著者
    authors = ArrayField(
        models.CharField(max_length=30, null=True, blank=True),
        size=50,
        verbose_name="著者",
    )
    # 5.価格
    price = models.IntegerField(verbose_name="価格", null=True, blank=True)
    # 6.出版社
    publisher = models.CharField(
        verbose_name="出版社", max_length=30, null=True, blank=True
    )
    # 7.発行日
    published_date = models.DateField(verbose_name="発行日", null=True, blank=True)
    # 8.イメージ画像
    image_link = models.CharField(
        verbose_name="イメージ画像", max_length=100, null=True, blank=True
    )
    # 9.登録者ID
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="登録者ID", on_delete=models.CASCADE
    )
    # 10.カテゴリ
    category = models.ManyToManyField(Category, verbose_name="カテゴリ", blank=True)
    # 11.並び順
    order_num = models.IntegerField(verbose_name="並び順")
    # 12.登録日時
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    # 13.読了フラグ
    completed_fg = models.BooleanField(verbose_name="読了フラグ", default=False)
    # 14.読了日時
    completed_at = models.DateTimeField(verbose_name="読了日時", null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    """2.レビュー"""

    class Meta:
        # テーブル名
        db_table = "review"
        # 管理サイトで使用するテーブル名
        verbose_name = verbose_name_plural = "2.レビュー"

    # 1.レコードID
    id = models.AutoField(verbose_name="レコードID", primary_key=True)
    # 2.読書リストID
    reading_list = models.OneToOneField(
        ReadingList, verbose_name="読書リストID", on_delete=models.CASCADE
    )
    # 3.感想
    text = models.TextField(verbose_name="感想", blank=False)
    # 4.五つ星評価
    rating = models.IntegerField(verbose_name="五つ星評価", null=True, blank=True)
    # 5.登録日時
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    # 6.更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.text
