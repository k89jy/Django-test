import json
from django.views import View
from django.http import JsonResponse
from .models import user
from django.shortcuts import render
# Create your views here.

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        user(
            username    = data['username'],
            phonenum    = data['phonenum'],
            email    = data['email'],
            password = data['password']
        )
        
        return JsonResponse({'message' : '회원가입 완료'} , status = 200)