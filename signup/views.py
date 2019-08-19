from django.shortcuts import render
from django.http import JsonResponse
from .models import Account
from django.views import View
import json
import bcrypt

# Create your views here.

class Signup(View):
    def post(self, request):

        data = json.loads(request.body)
        
        bytes_password = bytes(data['password'], "UTF-8")

        hash_password = bcrypt.hashpw(
                bytes_password,
                bcrypt.gensalt()
                ) 

        db = Account(
                user_id = data['user_id'], 
                user_name = data['user_name'],
                password = hash_password.decode("UTF-8"),
                profile = data['profile'],
            )
        
        try:
            db.save()
            return JsonResponse({"message":"SUCCESS"}, status = 200)
        except:
            return JsonResponse({"message":"ID already exists"}, status = 400)


    #if Account.objects.filter(user_id=data['user_id']).exists():
    #return JsonResponse({"message":"ID_USER_OVER"}, status = 400)
    #else:
    #db.save()
    #return JsonResponse({"message":"SUCCESS"}, status = 201

    def get(self, request):
        data = Account.objects.order_by('id')
        data = list(data.values())
        return JsonResponse(data, safe = False, status = 200)
