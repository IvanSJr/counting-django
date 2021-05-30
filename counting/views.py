from django.shortcuts import render


def counter_view(request):
    if request.method == "POST" and 'count' in request.POST:
        try:
            request.session['count'] +=1
        except:
            request.session['count'] = 0
    elif request.method == 'POST' and 'reset' in request.POST:
        request.session['count'] = 0
    return render(request,'counter.html')
