import json
import requests
from django.http import JsonResponse
from django.views import View
from .models import Users, RandomUser

class UsersView(View):
    def get(self, request, *args, **kwargs):
        api_url = 'https://randomuser.me/api/?results=10'

        # Obtener la lista de UUIDs almacenados en la sesión
        stored_uuids = request.session.get('stored_uuids', [])

        # Obtener el parámetro 'limit' de la URL
        limit = int(request.GET.get('limit', 10))

        response = requests.get(api_url)

        if response.status_code == 200:
            user_data = response.json()['results']

            # Filtrar usuarios que ya han sido mostrados
            unique_users = [user for user in user_data if user['login']['uuid'] not in stored_uuids]

            # Agregar nuevos UUIDs a la lista
            stored_uuids.extend(user['login']['uuid'] for user in unique_users)

            # Actualizar la lista de UUIDs almacenados en la sesión
            request.session['stored_uuids'] = stored_uuids

            # Obtener el parámetro 'categorize' de la URL
            categorize = request.GET.get('categorize', None)

            if categorize == 'gender':
                # Organizar por género si el parámetro 'categorize' es 'gender'
                female = [user for user in unique_users if user['gender'] == 'female']
                male = [user for user in unique_users if user['gender'] == 'male']
                organized_data = {'female': female, 'male': male}
                return JsonResponse({'results': organized_data})
            else:
                # Devolver los datos únicos como JSON si no hay categorización por género
                return JsonResponse({'results': unique_users[:limit]})
        else:
            return JsonResponse({'error': 'Error al obtener usuarios aleatorios'}, status=500)

