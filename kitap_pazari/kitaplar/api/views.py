from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from kitaplar.models import Kitap, Yorum
from kitaplar.api.permissions import IsAdminUserOrReadOnly, IsYorumSahibiOrReadOnly
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, get_object_or_404
from kitaplar.api.pagination import SmallPagination,LargePagination

class KitaplarCreateApiView(ListCreateAPIView):
    # queryset = Kitap.objects.all().order_by('-id')  #tersten sirala
    queryset = Kitap.objects.all().order_by('id')

    serializer_class = KitapSerializer
    # permission_classes = [permissions.IsAdminUser] #eger adminse bu servisi calistir
    permission_classes = [IsAdminUserOrReadOnly]
    # pagination_class = LargePagination
    # pagination_class = SmallPagination
    #Global olarak settingsde ayarladik rest_framework arrayi icerisinde
class KitapDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all().order_by('id')
    serializer_class = KitapSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class YorumCreateApiView(CreateAPIView):
    queryset = Yorum.objects.all().order_by('id')
    serializer_class = YorumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)

        kullanici = self.request.user
        yorum = Yorum.objects.filter(kitap=kitap, yorum_sahibi=kullanici)
        if yorum.exists():
            raise ValidationError('zaten yorum yaptiniz')
        serializer.save(kitap=kitap, yorum_sahibi=kullanici)


class YorumDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsYorumSahibiOrReadOnly]
# class KitaplarCreateApiView(CreateModelMixin, ListModelMixin, GenericAPIView):
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer
#
#     # lookup_field = 'id'
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class YorumlarCreateApiView(GenericAPIView):
#     queryset = Yorum.objects.all()
#     serializer_class = YorumSerializer
#     lookup_field = 'id'
