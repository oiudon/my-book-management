from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from my_book_management.models import Category, ReadingList, Review


class CategorySerializer(serializers.ModelSerializer):
    """3.カテゴリモデル用のシリアライザ"""

    class Meta:
        # 対象のモデルクラスを指定
        model = Category
        # 利用するモデルのフィールドを指定
        fields = "__all__"
        # シリアライザのバリデーションメッセージをカスタマイズ
        extra_kwargs = {
            "category_nm": {
                "error_messages": {
                    "blank": "カテゴリ名が入力されていません。",
                }
            },
        }


class CategoryListSerializer(serializers.ListSerializer):
    """複数の3.カテゴリモデルを扱うためのシリアライザ"""

    # 対象のシリアライザを設定
    child = CategorySerializer()


class ReadingListSerializer(serializers.ModelSerializer):
    """1.読書リストモデル用のシリアライザ"""

    # 関連先モデルのシリアライザを取得
    # しかし、これを定義すると中間テーブルの登録ができない（カテゴリモデルの登録になってしまう）
    # category = CategoryListSerializer()

    class Meta:
        # 対象のモデルクラスを指定
        model = ReadingList
        # 利用するモデルのフィールドを指定
        fields = [
            "id",
            "book_id",
            "title",
            "authors",
            "price",
            "publisher",
            "published_date",
            "image_link",
            "created_by",
            "category",
            "order_num",
            "created_at",
            "completed_fg",
            "completed_at",
        ]
        # シリアライザのバリデーションメッセージをカスタマイズ
        extra_kwargs = {
            "title": {
                "error_messages": {
                    "blank": "タイトルは空にできません。",
                }
            },
            "price": {
                "error_messages": {
                    "invalid": "価格には有効な整数を入力してください。",
                }
            },
        }


class ReadingListListSerializer(serializers.ListSerializer):
    """複数の1.読書リストモデルを扱うためのシリアライザ"""

    # 対象のシリアライザを設定
    child = ReadingListSerializer()


class ReviewSerializer(WritableNestedModelSerializer):
    """2.レビューモデル用のシリアライザ"""

    # 関連先モデルのシリアライザを取得（多対多のフィールドは不可）
    reading_list_title = serializers.ReadOnlyField(source="reading_list.title")
    reading_list_price = serializers.ReadOnlyField(source="reading_list.price")
    reading_list_publisher = serializers.ReadOnlyField(source="reading_list.publisher")
    reading_list_published_date = serializers.ReadOnlyField(
        source="reading_list.published_date"
    )
    reading_list_completed_fg = serializers.ReadOnlyField(
        source="reading_list.completed_fg"
    )

    class Meta:
        # 対象のモデルクラスを指定
        model = Review
        # 利用するモデルのフィールドを指定
        fields = [
            "id",
            "reading_list",
            "reading_list_title",
            "reading_list_price",
            "reading_list_publisher",
            "reading_list_published_date",
            "reading_list_completed_fg",
            "text",
            "rating",
            "created_at",
            "updated_at",
        ]
