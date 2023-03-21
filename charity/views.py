from django.shortcuts import render, redirect
from django.views import View
from .models import Institution, Donation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class indexView(View):
    def get(self, request):
        institutions_count = 0
        bags_count = 0
        institutions = Institution.objects.all()
        for institution in institutions:
            institutions_count += 1
        bags = Donation.objects.all()
        for bag in bags:
            bags_count += bag.quantity
        inst_type_1 = Institution.objects.filter(type=1)
        inst_type_2 = Institution.objects.filter(type=2)
        inst_type_3 = Institution.objects.filter(type=3)
        return render(request, 'index.html', {
            'institutions': institutions_count,
            'bags': bags_count,
            'inst_type_1': inst_type_1,
            'inst_type_2': inst_type_2,
            'inst_type_3': inst_type_3
        })


class loginView(View):
    def get(self, request):
        return render(request, 'login.html')


class registerView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            raise ValidationError("Podane hasła nie są identyczne")

        User.objects.create_user(
            username=email,
            password=password,
            first_name=name,
            last_name=surname,
            email=email
        )
        return redirect('/login')

class addDonationView(View):
    def get(self, request):
        return render(request, 'form.html')
