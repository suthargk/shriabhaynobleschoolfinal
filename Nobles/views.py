from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
                                            PageNotAnInteger
from django.views.generic import ListView

# Create your views here.
from Nobles.models import Gallery, Faculty, Notice, Infrastructure_and_Facilities, Achievements, Download, Toppers
from Elearning.models import Classroom
def index(request):
    notices = Notice.published.all()
    infra = Infrastructure_and_Facilities.objects.all()
    achievements = Achievements.objects.all()
    class_8_top = Toppers.objects.filter(student__classroom="Class 8")
    class_10_top = Toppers.objects.filter(student__classroom="Class 10")
    class_12science_top = Toppers.objects.filter(student__classroom="Class 12 (Science)")
    return render(request,'Nobles/html/index.html', { 'notices' : notices, 'infrastructures' : infra, 'achievements' : achievements,'class_8_top' : class_8_top, 'class_10_top' : class_10_top, 'class_12science_top' : class_12science_top})

def about(request):
    return render(request,'Nobles/html/about.html')

def bus_route_plan(request):
    return render(request,'Nobles/html/bus_route_plan.html')

def gallery(request):
	gallery = Gallery.objects.all()
	return render(request,'Nobles/html/gallery.html', {'gallery' : gallery,}) # first' : first, 'latest_album' : latest_album 

def gallery_ahead(request,num):
	gallery = Gallery.objects.get(pk=num)
	
	return render(request,'Nobles/html/gallery_ahead.html',{'gallery' : gallery })

def principal_message(request):
    return render(request,'Nobles/html/principal_message.html')

def facilities(request):
    return render(request,'Nobles/html/facilities.html')

def route_plan(request):
    return render(request,'Nobles/html/route_plan.html')

def achievements(request):
    achievements = Achievements.objects.all()
    return render(request,'Nobles/html/achievements.html', {'achievements' : achievements})

def achievement_details(request,num):
    details = Achievements.objects.get(pk=num)
    achievements = Achievements.objects.all()
    return render(request,'Nobles/html/achievement_details.html', {'details' : details, 'achievements' : achievements})

def academic_achievements(request):
    return render(request,'Nobles/html/academic_achievements.html')

def faculty(request):
    faculty = Faculty.objects.order_by('name')
    return render(request,'Nobles/html/faculty.html',{'faculty' : faculty})

def contact(request):
    return render(request,'Nobles/html/contact.html')

# def all_notices(request):
#     notices = Notice.objects.all()
#     return render(request,'Nobles/html/all_notices.html', {'notices' : notices})

class NoticeListView(ListView):
    queryset = Notice.published.all()
    context_object_name = 'notices'
    #paginate_by = 3
    template_name = 'Nobles/html/all_notices.html'

def notice_detail(request, year, month, day, notice):
    notice = get_object_or_404(Notice, slug=notice,
                            status='published',
                            publish__year = year,
                            publish__month = month,
                            publish__day = day)

    return render(request,'Nobles/html/notice_detail.html', {'notice' : notice})

def infrastructure_facilities(request):
    infra = Infrastructure_and_Facilities.objects.all()
    return render(request, 'Nobles/html/infrastructure_facilities.html', {'infrastructures' : infra})

def admission(request):
    return render(request,'Nobles/html/admission_and_fees.html')

def download(request):
    files = Download.objects.order_by('-created_date')
    return render(request, 'Nobles/html/download.html', {'files' : files})

def homework(request):
    classes = Classroom.objects.all()
    return render(request, 'Nobles/html/homework.html', {'classes' : classes})

def toppers(request):
    class_1_top = Toppers.objects.filter(student__classroom="Class 1").order_by('-percentage')
    class_2_top = Toppers.objects.filter(student__classroom="Class 2").order_by('-percentage')
    class_3_top = Toppers.objects.filter(student__classroom="Class 3").order_by('-percentage')
    class_4_top = Toppers.objects.filter(student__classroom="Class 4").order_by('-percentage')
    class_5_top = Toppers.objects.filter(student__classroom="Class 5").order_by('-percentage')
    class_6_top = Toppers.objects.filter(student__classroom="Class 6").order_by('-percentage')
    class_7_top = Toppers.objects.filter(student__classroom="Class 7").order_by('-percentage')
    class_8_top = Toppers.objects.filter(student__classroom="Class 8").order_by('-percentage')
    class_9_top = Toppers.objects.filter(student__classroom="Class 9").order_by('-percentage')
    class_10_top = Toppers.objects.filter(student__classroom="Class 10").order_by('-percentage')
    class_11science_top = Toppers.objects.filter(student__classroom="Class 11(Science)").order_by('-percentage')
    class_12science_top = Toppers.objects.filter(student__classroom="Class 12 (Science)").order_by('-percentage')
    class_11commerce_top = Toppers.objects.filter(student__classroom="Class 11(Commerce)").order_by('-percentage')
    class_12commerce_top = Toppers.objects.filter(student__classroom="Class 12(Commerce)").order_by('-percentage')
    class_11arts_top = Toppers.objects.filter(student__classroom="Class 11(Arts)").order_by('-percentage')
    class_11agr_top = Toppers.objects.filter(student__classroom="Class 11 Agr.(Science)").order_by('-percentage')
    return render(request, 'Nobles/html/toppers.html', {'class_1_top' : class_1_top,'class_2_top' : class_2_top,'class_3_top' : class_3_top,'class_4_top' : class_4_top,'class_5_top' : class_5_top,'class_6_top' : class_6_top,'class_7_top' : class_7_top,'class_8_top' : class_8_top,'class_9_top' : class_9_top, 'class_10_top' : class_10_top, 'class_11science_top' : class_11science_top,'class_12science_top' : class_12science_top,'class_11commerce_top' : class_11commerce_top,'class_12commerce_top' : class_12commerce_top,'class_11arts_top' : class_11arts_top,'class_11agr_top' : class_11agr_top,})
