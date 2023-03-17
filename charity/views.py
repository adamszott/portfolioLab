from django.shortcuts import render
from django.views import View
from .models import Institution, Donation


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
        return render(request,'index.html', {'institutions':institutions_count, 'bags':bags_count})


class loginView(View):
    def get(self, request):
        return render(request,'login.html')


class registerView(View):
    def get(self, request):
        return render(request, 'register.html')


class addDonationView(View):
    def get(self, request):
        return render(request, 'form.html')