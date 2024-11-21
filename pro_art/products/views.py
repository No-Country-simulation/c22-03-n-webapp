from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer

# Obtencion y creacion de un producto.
class ProductList(APIView):
    
    """Ejecuta el servidor y prueba los endpoints

    - GET /api/products/
    Devuelve todos los productos.
    
    - POST /api/products/
    Crear un producto nuevo con JSON como:
    
        {
            "provider_id": 1,
            "categories_ids": [1, 2],
            "name": "Laptop",
            "quantities": 10,
            "price_product": 1200.123,
            "description_product": "A high-performance laptop",
            "status": "available"
        }
    
    """
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer = ProductSerializer(data=request.data)
            quantities = serializer.validated_data.get("quantities")
            
            if quantities > 0:
                serializer.validated_data['STATUS'] = 'AVAILABLE'
            elif quantities == 0:
                serializer.validated_data['STATUS'] = 'DICONTINUED'
                
            Product = serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtencion, actualizacion y eliminacion de un producto.
class ProductDetail(RetrieveUpdateDestroyAPIView):
    """Ejecuta el servidor y prueba los endpoints
    
    - GET /api/products/<id>/
    Detalle de un producto.
    
    - PUT/PATCH /api/products/<id>/
    Actualización de un producto.
    
    - DELETE /api/products/<id>/
    Eliminación de un producto.

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_update(self, serializer):
        # Lógica para actualizar el estado del producto
        quantities = serializer.validated_data.get('quantities', self.get_object().quantities)
        if quantities > 0:
            serializer.validated_data['status'] = 'AVAILABLE'
        else:
            serializer.validated_data['status'] = 'DISCONTINUED'
        
        # Guardar el producto con el nuevo estado
        serializer.save()
    
    
    