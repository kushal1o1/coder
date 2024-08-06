from django.shortcuts import render ,redirect
from django.http import HttpResponseForbidden
from .models import Code
PASSWORD = "STH"
def home(request):
    if request.method == 'POST':
        
        password = request.POST.get('password', '')
        if password == PASSWORD:
           
            name = request.POST.get('name', '')
            if name=='':
             name="Unknown"
            text = request.POST.get('inputText', '')
            if text:
              Code.objects.create(code=text, name=name)

        
            if Code.objects.count() > 10:
                # Delete the oldest object (the first created)
                oldest_code = Code.objects.first()
                oldest_code.delete()

            return redirect('home')

        
        else:
           return render(request, 'app1/access_denied.html')

    codes = Code.objects.all().order_by('-created_at')
    parms = {'codes': codes}
    return render(request, 'app1/index.html', parms)
