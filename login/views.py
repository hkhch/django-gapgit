from django.shortcuts import render
from django.http import JsonResponse
from signup.models import Account 
from django.views import View
import json
import jwt
import datetime
import bcrypt

# Create your views here.

class login_post(View):
    def post(self, request):

        data = json.loads(request.body)
        
        user_id = data['user_id']
        password = data['password']

        if Account.objects.filter(user_id = data['user_id']).exists():
            account_get_id = Account.objects.filter(user_id = data['user_id']).get()
        else:
            return JsonResponse({"message":"id does not exists"}, status = 401)
        
        if bcrypt.checkpw(password.encode("UTF-8"), account_get_id.password.encode("UTF-8")):
            user_id = account_get_id.user_id
            payload = {
                'user_id': user_id,
                }
            token = jwt.encode(payload, 'SECRET_KEY')

            return JsonResponse({"access_token" : token.decode('UTF-8')}, status = 200)
        
        else:
            return JsonResponse({"message" : "password is invalid"}, status = 401)

        '''if len(Account.objects.all()) == 0:
                return JsonResponse({"message":"No account created"}, status = 400)

        if Account.objects.filter(user_id = data['user_id']).exists():
            if Account.objects.filter(password = data['password']).exists():
                return JsonResponse({"message":"SUCCESS"}, status = 200)
            else:
                return JsonResponse({"message":"Password is invalid."}, status = 400)
        else:
            return JsonResponse({"message":"ID does not exist"}, status = 400)
        '''     
