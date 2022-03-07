from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

# Create your views here.
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import PyViSerializer
from rest_framework.exceptions import APIException
from .ViTokenizer import ViTokenizer
import time


class Success(APIException):
    status_code = status.HTTP_202_ACCEPTED
    default_detail = 'Success .'
    default_code = 'success'


class PiViView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = PyViSerializer



    def update(self, request, *args, **kwargs):
        text = request.data['text']
        start_time = time.time()
        k2 = [y.replace("_", ' ') if "_" in y else y for y in ViTokenizer.tokenize(text).split()]
        endtime = time.time() - start_time
        data = {'words': k2, 'time': endtime}
        raise Success(data)
    

    def get(self, request, *args, **kwargs):
        raise Success('a')

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
