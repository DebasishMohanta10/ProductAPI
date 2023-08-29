from .serializers import CategorySerializer,ProductSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .models import Category,Product
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ["inventory","price"]
    search_fields = ["name","category__name"]
    filterset_fields = ["category"]
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle,AnonRateThrottle]

class CategoryProductView(generics.ListAPIView):
    query_set = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["name"]
    ordering_fields = ["inventory","price"]
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    
    def get_queryset(self):
        slug = self.kwargs["slug"]
        return Product.objects.all().filter(category__slug=slug)
    
        
        
    
