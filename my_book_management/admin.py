from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, ReadingList, Review


# ReadingListモデルに統合する為にModelResourceを継承したクラスを作成
class ReadingListResource(resources.ModelResource):
    class Meta:
        model = ReadingList


# Reviewモデルに統合する為にModelResourceを継承したクラスを作成
class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review


# Categoryモデルに統合する為にModelResourceを継承したクラスを作成
class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


@admin.register(ReadingList)
class ReadingListAdmin(ImportExportModelAdmin):
    list_display = (
        "id",  # 1.レコードID
        "book_id",  # 2.書籍ID
        "title",  # 3.タイトル
        "authors",  # 4.著者
        "format_price",  # 5.価格
        "publisher",  # 6.出版社
        "published_date",  # 7.発行日
        "image_link",  # 8.イメージ画像
        "created_by",  # 9.登録者ID
        "_category",  # 10.カテゴリ
        "order_num",  # 11.並び順
        "created_at",  # 12.登録日時
        "completed_fg",  # 13.読了フラグ
        "completed_at",  # 14.読了日時
    )
    list_display_links = ("id", "book_id", "title")

    def format_price(self, obj):
        """価格フィールドのフォーマットを変更する"""
        if obj.price is not None:
            return "{:,d} 円".format(obj.price)

    # 価格フィールドのカラム名を指定
    format_price.short_description = "価格"
    # カラム名を押下時のソートを有効化
    format_price.admin_order_field = "price"

    def _category(self, obj):
        """多対多のカテゴリフィールドを表示"""
        if obj.category is not None:
            return ",".join([x.category_nm for x in obj.category.all()])

    # カテゴリフィールドのカラム名を指定
    _category.short_description = "カテゴリ名"
    # カラム名を押下時のソートを有効化
    _category.admin_order_field = "category"
    # カテゴリフィールドの追加画面の表示をカスタマイズ
    filter_horizontal = ("category",)

    # 初期表示時のソート項目を指定
    ordering = ("id",)

    # 簡易検索に使用するフィールドを指定
    search_fields = ("id", "title", "created_by__username")

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = ReadingListResource


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = (
        "id",  # 1.レコードID
        "reading_list",  # 2.読書リストID
        "text",  # 3.感想
        "rating",  # 4.五つ星評価
        "created_at",  # 5.登録日時
        "updated_at",  # 6.更新日時
    )

    # 初期表示時のソート項目を指定
    ordering = ("id",)

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = ReviewResource


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = (
        "id",  # 1.レコードID
        "category_nm",  # 2.カテゴリ名
        "created_by",  # 3.登録者ID
    )

    # 初期表示時のソート項目を指定
    ordering = ("id",)

    # 簡易検索に使用するフィールドを指定
    search_fields = ("id", "category_nm", "created_by__username")

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = CategoryResource
