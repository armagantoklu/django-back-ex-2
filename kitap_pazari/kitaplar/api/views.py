from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from kitaplar.models import Kitap, Yorum
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, get_object_or_404


class KitaplarCreateApiView(ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer


class KitapDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer


class YorumCreateApiView(CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer

    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        serializer.save(kitap=kitap)


class YorumDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer

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
