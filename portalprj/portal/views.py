from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *
# Create your views here.

@login_required
def index_view(request):
    level = request.GET.get('level')
    sem = request.GET.get('sem')
    
    student = Student.objects.filter(user=request.user)

    results_all = Result.objects.filter(student__in=student)

    if level and sem:
        results = Result.objects.filter(student__in=student).filter(course__year=level).filter(course__semester=sem)
    elif level:
        results = Result.objects.filter(student__in=student).filter(course__year=level)
    else:
        results = results_all

    CCR = 0
    CGV = 0
    TCR = 0
    TGP = 0

    for result in results_all:
        CCR += result.course.credit
        CGV += float(result.grade) * (result.course.credit) 
    
    for result in results:
        TCR += result.course.credit
        TGP += float(result.grade) * (result.course.credit) 

    
    
    try:
        CGPA = CGV / CCR
    except ZeroDivisionError:
        CGPA = 0

    try:
        SGPA = TGP / TCR
    except ZeroDivisionError:
        SGPA = 0
    
    class_designation = get_class(CGPA)

    # if SGPA != 0 and CGPA != 0:
    #     SGPA = list(str(SGPA))
    #     SGPA[4] = 0
    #     SGPA = "".join(map(str, SGPA))
    #     CGPA = list(str(CGPA))
    #     CGPA[4] = 0
    #     CGPA = "".join(map(str, CGPA))

    context = {
        'results': results,
        'student': student,
        'TCR': TCR,
        'TGP': TGP,
        'SGPA': float(SGPA),
        'CCR': CCR,
        'CGV': CGV,
        'CGPA': float(CGPA),
        'class_designation': class_designation,
    }

    return render(request, 'portal/index.html', context)

def get_class(cgpa:float):
    if cgpa >= 3.5 and cgpa <= 4.0:
        return "First Class"
    elif cgpa > 3.0 and cgpa <= 3.49:
        return "Second Class (Upper Division)"
    elif cgpa > 2.5 and cgpa <= 2.99:
        return "Second Class (Lower Division)"
    elif cgpa > 2.0 and cgpa <= 2.49:
        return "Third Class"
    elif cgpa > 1.0 and cgpa <= 1.99:
        return "Pass"
    