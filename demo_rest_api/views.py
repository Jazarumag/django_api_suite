#guia 20
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid

data_list = []

data_list.append({'id': str(uuid.uuid4()), 'name': 'User01', 'email': 'user01@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User02', 'email': 'user02@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User03', 'email': 'user03@example.com', 'is_active': False})

#GET y POST
class DemoRestApi(APIView):
    def get(self, request):
        active_items = [item for item in data_list if item.get('is_active', False)]
        return Response(active_items, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        if 'name' not in data or 'email' not in data:
            return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

        data['id'] = str(uuid.uuid4())
        data['is_active'] = True
        data_list.append(data)

        return Response({'message': 'Dato guardado exitosamente.', 'data': data}, status=status.HTTP_201_CREATED)

#PUT, PATCH y DELETE
class DemoRestApiItem(APIView):
    def get_object(self, item_id):
        for item in data_list:
            if item['id'] == item_id:
                return item
        return None

    def put(self, request, item_id):
        item = self.get_object(item_id)
        if item is None:
            return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        if 'name' not in data or 'email' not in data:
            return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

        item['name'] = data['name']
        item['email'] = data['email']
        item['is_active'] = data.get('is_active', item['is_active'])

        return Response({'message': 'Elemento actualizado completamente.', 'data': item}, status=status.HTTP_200_OK)

    def patch(self, request, item_id):
        item = self.get_object(item_id)
        if item is None:
            return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        item.update({k: v for k, v in data.items() if k in item})
        return Response({'message': 'Elemento actualizado parcialmente.', 'data': item}, status=status.HTTP_200_OK)

    def delete(self, request, item_id):
        item = self.get_object(item_id)
        if item is None:
            return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        item['is_active'] = False
        return Response({'message': 'Elemento eliminado lógicamente.'}, status=status.HTTP_200_OK)