from django.urls import path
from kitaplar.api.views import KitaplarCreateApiView, KitapDetailApiView, YorumCreateApiView,YorumDetailApiView

# classi viewa ceviriyoz
urlpatterns = [
    path('kitaplar', KitaplarCreateApiView.as_view(), name='kitap-listesi'),
    path('kitaplar/<int:pk>', KitapDetailApiView.as_view(), name='kitap-bilgileri'),
    path('kitaplar/<int:kitap_pk>/yorum-yap', YorumCreateApiView.as_view(), name='yorum-yap'),
    path('yorum/<int:pk>', YorumDetailApiView.as_view(), name='yorum-detay'),

]
