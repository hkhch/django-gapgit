from django.shortcuts import render
from django.http import JsonResponse
from .models import Tweet
from django.views import View
from django.views.generic.edit import BaseDeleteView
import json

# Create your views here.
class Tweets(View):
    def post(self, request):

        data = json.loads(request.body)

        db = Tweet(user_name = data['user_id'], contents = data['contents'])
        
        db.save()
                  
        return JsonResponse({"message":"SUCCESS"}, status = 201)

    def get(self, request):
        data = list(Tweet.objects.values())
        return JsonResponse(data, safe = False, status = 200)
            
    '''class Tweet_del(BaseDeleteView):
        
        model = Tweet
        
        def delete(self, request, *args, **kwargs):

            pk = data['index']

            self.object = self.get_object()
            self.object.delete()

            try:
                return JsonResponse({"message":"SUCCESS"}, status = 200)
            except:
                return JsonResponse({"messafe":"SUCCESS"}, status = 400)
'''

        

