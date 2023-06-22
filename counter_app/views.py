from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return render(request, "index.html")

def destroy_session(request):
    del request.session['count']
    if 'custom' in request.session:
        del request.session['custom']
    return redirect("/")

def up_two(request):
    request.session['count'] += 1
    return redirect("/")

def custom(request):
    num_from_form = request.POST['custom_num']
    request.session['custom'] = num_from_form
    print(num_from_form)
    return redirect("/")

def up_custom_num(request):
    user_custom_num = request.session['custom']
    request.session['count'] += int(user_custom_num)-1
    return redirect("/")