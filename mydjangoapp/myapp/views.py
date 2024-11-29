from django.shortcuts import render

# Create your views here.
def myview(request):
    name = ""
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        print(name)
    return render(request, 'myapp/myapp.html', {'name': name})