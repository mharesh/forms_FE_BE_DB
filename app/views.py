from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_school(request):
    if request.method=='POST':
        # request.POST={SCN:SV,SCP:SV,SCl:SV}
        SCN = request.POST['SCN']
        SCP = request.POST['SCP']
        SCL = request.POST['SCL']

        SO = School.objects.get_or_create(ScName=SCN,ScPrincipal=SCP,ScLocation=SCL)[0]
        SO.save()

        QSSO = School.objects.all()
        d={'QSSO':QSSO}
        return render(request,'display_school.html',d)

    return render(request,'insert_school.html')


def insert_student(request):
    if request.method=='POST':
        SID = request.POST['SID']
        SN = request.POST['SN']
        SCN = request.POST['SCN']

        SO = School.objects.get(ScName=SCN)
        STO = Student.objects.get_or_create(ScName=SO,Sname=SN,Sid=SID)[0]
        STO.save()

        QSTO = Student.objects.all()
        d={'QSTO':QSTO}
        return render(request,'display_student.html',d)

    return render(request,'insert_student.html')