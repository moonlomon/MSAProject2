from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from security.users.services import UserService

@api_view(['GET'])
@parser_classes([JSONParser])
def users(request):
    result = UserService().show_users()
    return JsonResponse({'result': result})