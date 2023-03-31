from django.shortcuts import render, redirect
from django.views import View
from .models import Institution, Donation, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):
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


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        elif User.objects.filter(username=username):
            return redirect('/login')
        else:
            return redirect('/register')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=email,
            password=password,
            first_name=name,
            last_name=surname,
            email=email
        )
        return redirect('/login')


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'institutions': institutions})

    def post(self, request):
        donate = Donation.objects.create(
            quantity=request.POST['bags'],
            categories=request.POST['categories'],
            institution=request.POST['organization'],
            address=request.POST['address'],
            phone_number=request.POST['phone'],
            city=request.POST['city'],
            zip_code=request.POST['postcode'],
            pick_up_date=request.POST['data'],
            pick_up_time=request.POST['time'],
            pick_up_comment=request.POST['more_info'],
            user_id=request.user.id
        )
        donate.save()
        return redirect('/confirmation/')


class UserView(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'user.html', {'user': user})


class ConfirmationView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')

