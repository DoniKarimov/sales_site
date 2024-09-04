from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from .models import CustomUser, Product, Category

from .serialzer import CustomUserSer, ProductSer, CategorySer


class Register(ListCreateAPIView):
    queryset  = CustomUser.objects.all()
    serializer_class  = CustomUserSer
    # parser_classes = [MultiPartParser, FormParser]



class CategoryView(ListCreateAPIView):
    queryset  = Category.objects.all()
    serializer_class  = CategorySer


class CreateProduct(APIView):
    def post(self, request):
        serializer  = ProductSer(data=request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def get(self, request):
        all_products = Product.objects.all()
        ser = ProductSer(all_products, many=True)
        return Response(ser.data)
    

class SavatView(APIView):
    def get(self, request):
        # id = request.user.id
        # print(dir(request.session))
        # request.session.set_expiry(60) # during a minute
        # request.session.set_expiry(0) # until closing browser
        # request.session.set_expiry(None) # never die

        # request.session[f'{id}'] = [1,2,3,5]
        if 'some' in request.session:
            print(request.session['some'])
        else:
            print('yoq')
        return Response({
            'message': 'Some message'
        })
    def post(self, request):
        request.session.set_expiry(60) # during a minute
        
        request.session['some'] = [1,2,3,5]
        print(request.session['some'])
        del request.session['some']
        return Response({
            'message': 'Some message'
        })