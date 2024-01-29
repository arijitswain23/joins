from django.shortcuts import render

# Create your views here.
from app.models import *

def equijoins(request):
    EMPO=Emp.objects.select_related('deptno').all()
    d={'EMPO':EMPO}
    return render(request,'equijoins.html',d)