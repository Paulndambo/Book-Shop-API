from django.shortcuts import get_object_or_404, render
from .serializers import BurgainSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Burgain
from .utils import send_burgain_notification
# Create your views here.

class BookBurgainAPIView(generics.ListCreateAPIView):
    queryset = Burgain.objects.all()
    serializer_class = BurgainSerializer

    #incase you decide to use GenericAPIView, uncomment this block
    """
    def get(self, request):
        burgains = Burgain.objects.all()
        serializer = self.serializer_class(instance=burgains, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """

class BookBurgainUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Burgain.objects.all()
    serializer_class = BurgainSerializer

    lookup_field = "pk"

    def partial_update(self, request, *args, **kwargs):
        burgain_id = kwargs['pk']
        burgain = get_object_or_404(Burgain, pk=burgain_id)
        email = burgain.customer.email
        name = burgain.customer.name
        book = burgain.book.title
        decision = ""
        if request.data['is_approved']:
            decision = "Accepted"
        else:
            decision = "Declined"
        try:
            send_burgain_notification(email, name, book, decision)
        except Exception as e:
            raise e
        return Response({"message": "Burgain Updated"})