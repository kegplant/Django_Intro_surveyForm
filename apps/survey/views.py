from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    context={
        'email': 'blog@gmail.com',
        'name': 'mike'
    }
    #return HttpResponse(response)
    return render(request,'survey/index.html',context)
def process(request):
    if request.method=='POST':
        request.session['form1']=request.POST
        return redirect('/result')
def result(request):
    try:
        request.session['submits']
    except:
        request.session['submits']=0
    request.session['submits']+=1
    context=request.session['form1']
    return render(request,'survey/result.html',context)