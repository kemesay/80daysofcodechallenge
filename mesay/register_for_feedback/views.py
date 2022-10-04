from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method =="post":
        Fname = request.POST["Fname"]
        Lname = request.POST["Lname"]
        Phoneno = request.POST["Phoneno"]
        Address = request.POST["Address"]
        Email = request.POST["Email"]
        Feedback = request.POST["Feedback"]
    else:
       return render(request, 'register.html')