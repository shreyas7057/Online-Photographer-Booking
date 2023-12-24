# here the views are of localhost:8000 ie searching for the photographers according to the city.
# Also, other view is of the showing portoflio website of searched photographer


from django.shortcuts import render,redirect
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail

from .models import Photographer,Category,Team,Gallery,Stat,Booking,Package,Service
from .forms import BookingForm


# this view is created for searching the photographers, this is first page when website is opened.
def index(request):
    query = request.GET.get('q','')
    if query:
        queryset = (Q(location__icontains=query))
        results = Photographer.objects.filter(queryset).distinct()
    else:
       results = Photographer.objects.all()
    context = {
        'results':results,
        'query':query,
    }
    return render(request,'index.html',context)

# this view is to see the portfolio of selected photographer
def visit_photography_site(request,id):
    photographer = Photographer.objects.get(id=id)

    gallery = Gallery.objects.filter(photographer=photographer.id)
    team = Team.objects.filter(photographer=photographer.id)
    stat = Stat.objects.get(photographer=photographer.id)
    package = Package.objects.filter(photographer=photographer.id)
    service = Service.objects.filter(photographer=photographer.id)

    # booking form
    
    if request.method == "POST":

        form = BookingForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.photographer = photographer
            book.save()

            # send mail
            subject = "Booking Done!"
            content = "Name: "+book.name+" Shoot Start Date: "+str(book.start_date)+" till "+str(book.end_date)+" Number Of Days: "+str(book.no_of_days)
            tomail = book.email
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject,content,email_from,[tomail,email_from,photographer.user.email],fail_silently=False,)
            return redirect('visit_photography_site',id=id)

    else:
        form = BookingForm()

    context = {
        'photographer':photographer,
        'gallery':gallery,
        'team':team,
        'stat':stat,
        'package':package,
        'service':service,
        'form':form,
    }
    return render(request,'photoapp/home.html',context)