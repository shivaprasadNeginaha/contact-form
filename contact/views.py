from django.shortcuts import render
from datetime import datetime
from contact.models import Contact

# Create your views here.
def index(request):
  if (request.method == 'POST'):
    name = request.POST.get('name')
    email = request.POST.get('email')
    desc = request.POST.get('desc')
    contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
    contact.save()
    return render(request,'base.html')
  return render(request, 'index.html')