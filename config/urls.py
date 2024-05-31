from django.contrib import admin
from django.urls import path

admin.site.site_header = "管理サイト"
admin.site.site_title = "書籍管理プロジェクト"
admin.site.index_title = "ホーム"

urlpatterns = [
    path("admin/", admin.site.urls),
]
