from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q

def equijoins(request):
    EMPO=Emp.objects.select_related('deptno').all()
    EMPO=Emp.objects.select_related('deptno').filter(hiredate__day=11)
    EMPO=Emp.objects.select_related('deptno').filter(deptno__dloc='DALLAS')
    EMPO=Emp.objects.select_related('deptno').filter(deptno=10)
    EMPO=Emp.objects.select_related('deptno').filter(deptno=20)
    EMPO=Emp.objects.select_related('deptno').all()[3:5]
    EMPO=Emp.objects.select_related('deptno').all()[:7]
    EMPO=Emp.objects.select_related('deptno').filter(deptno__dloc='DALLAS')
    EMPO=Emp.objects.select_related('mgr').filter(deptno__dloc='NEW YORK')
    EMPO=Emp.objects.select_related('mgr').filter(deptno__dname='SALES')
    EMPO=Emp.objects.select_related('mgr').filter(hiredate__day=12)
    EMPO=Emp.objects.select_related('mgr').filter(hiredate__year=2024)
    EMPO=Emp.objects.select_related('mgr').filter(ename='KING')
    EMPO=Emp.objects.select_related('mgr').filter(mgr__deptno=30)
    EMPO=Emp.objects.select_related('mgr').filter(deptno__dloc='DALLAS')
    EMPO=Emp.objects.select_related('mgr').filter(deptno__dname='RESEARCH')
    
    d={'EMPO':EMPO}
    return render(request,'equijoins.html',d)


def selfjoins(request):
    EMO=Emp.objects.select_related('mgr').all()
    EMO=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE')
    EMO=Emp.objects.select_related('mgr').filter(sal__lte=2500)
    EMO=Emp.objects.select_related('mgr').filter(ename='SMITH')
    EMO=Emp.objects.select_related('mgr').filter(deptno=20)
    EMO=Emp.objects.select_related('mgr').filter(deptno__dloc='NEW YORK')
    EMO=Emp.objects.select_related('mgr').filter(deptno__dname='SALES')
    EMO=Emp.objects.select_related('mgr').filter(hiredate__day=12)
    EMO=Emp.objects.select_related('mgr').filter(hiredate__year=2024)
    EMO=Emp.objects.select_related('mgr').filter(ename='KING')
    EMO=Emp.objects.select_related('mgr').filter(mgr__deptno=30)
    EMO=Emp.objects.select_related('mgr').filter(deptno__dloc='DALLAS')
    EMO=Emp.objects.select_related('mgr').filter(deptno__dname='RESEARCH')
    d={'EMO':EMO}
    return render(request,'selfjoins.html',d)

def emp_mgr_dept(request):
    emdo=Emp.objects.select_related('deptno','mgr').all()
    emdo=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH')
    emdo=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    emdo=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='NEW YORK')
    emdo=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='S')
    emdo=Emp.objects.select_related('deptno','mgr').filter(ename__endswith='N')
    emdo=Emp.objects.select_related('deptno','mgr').filter(sal__gte=2500)
    emdo=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH',sal__lte=1000)
    emdo=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year=2024)|Q(ename__startswith='A'))
    emdo=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2024,ename__startswith='A')
    emdo=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year=2024)|Q(sal__gte=2000))
    emdo=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    emdo=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year=2024)|Q(ename='SMITH'))
    emdo=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emdo=Emp.objects.select_related('deptno','mgr').filter(deptno=10)
    emdo=Emp.objects.select_related('deptno').all()
    emdo=Emp.objects.select_related('deptno').filter(hiredate__day=11)
    emdo=Emp.objects.select_related('deptno').filter(deptno__dloc='DALLAS')
    emdo=Emp.objects.select_related('deptno').filter(deptno=10)
    emdo=Emp.objects.select_related('deptno').filter(deptno=20)
    emdo=Emp.objects.select_related('deptno').all()[3:5]
    emdo=Emp.objects.select_related('deptno').all()[:7]
    emdo=Emp.objects.select_related('deptno').filter(deptno__dloc='DALLAS')
    emdo=Emp.objects.select_related('mgr').filter(deptno__dloc='NEW YORK')
    emdo=Emp.objects.select_related('mgr').filter(deptno__dname='SALES')
    emdo=Emp.objects.select_related('mgr').filter(hiredate__day=12)
    emdo=Emp.objects.select_related('mgr').filter(hiredate__year=2024)
    emdo=Emp.objects.select_related('mgr').filter(ename='KING')
    emdo=Emp.objects.select_related('mgr').filter(mgr__deptno=30)
    emdo=Emp.objects.select_related('mgr').filter(deptno__dloc='DALLAS')
    emdo=Emp.objects.select_related('mgr').filter(deptno__dname='RESEARCH')
    emdo=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH',sal__lte=1000)
    emdo=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year=2024)|Q(ename__startswith='A'))
    emdo=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2024,ename__startswith='A')
    emdo=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year=2024)|Q(sal__gte=2000))
    emdo=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    emdo=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year=2024)|Q(ename='SMITH'))
    emdo=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emdo=Emp.objects.select_related('deptno','mgr').filter(deptno=10)
    d={'emdo':emdo}
    return render(request,'emp_mgr_dept.html',d)


def emp_salgrade(request):
    #EO=Emp.objects.all()
    #SO=SalGrade.objects.all()
    # Retrieving the data of employess who belongs to grade 4
    #SO=SalGrade.objects.filter(grade=4)#[grade4 SalgradeObjects]

    #EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    # Retrieving the data of employess who belongs to grade 3,4
    SO=SalGrade.objects.filter(grade__in=(3,4))

    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))
        d={'EO':EO,'SO':SO}
        return render(request,'emp_salgrade.html',d)