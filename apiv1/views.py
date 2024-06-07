from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from my_book_management.models import Category, ReadingList, Review

from .serializers import CategorySerializer, ReadingListSerializer, ReviewSerializer


class ReadingListViewSet(viewsets.ModelViewSet):
    """1.読書リストモデルのCRUD用APIクラス"""

    # 1.読書リストモデルの一覧を取得
    queryset = ReadingList.objects.all()
    # シリアライザクラスを指定する
    serializer_class = ReadingListSerializer
    # 一覧・詳細以外のAPI利用時の認証情報を必須化
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # フィルタリング設定
    filter_backends = [filters.DjangoFilterBackend]
    # フィルタリング対象のフィールドを指定(ArrayField型は指定不可)
    filterset_fields = ["title"]

    def create(self, request, *args, **kwargs):
        # request.data を変更可能な辞書に変換
        data = request.data.copy()
        # order_num をデータの個数 + 1 に設定
        data["order_num"] = ReadingList.objects.count() + 1

        # 修正したデータでシリアライザを初期化
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class ReviewViewSet(viewsets.ModelViewSet):
    """2.レビューモデルのCRUD用APIクラス"""

    # 2.レビューモデルの一覧を取得
    queryset = Review.objects.all()
    # シリアライザクラスを指定する
    serializer_class = ReviewSerializer
    # 一覧・詳細以外のAPI利用時の認証情報を必須化
    # permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    """3.カテゴリモデルのCRUD用APIクラス"""

    # 3.カテゴリモデルの一覧を取得
    queryset = Category.objects.all()
    # シリアライザクラスを指定する
    serializer_class = CategorySerializer
    # 一覧・詳細以外のAPI利用時の認証情報を必須化
    # permission_classes = [IsAuthenticatedOrReadOnly]
