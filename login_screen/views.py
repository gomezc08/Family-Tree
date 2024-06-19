from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        
        # Check if the code matches
        if code == '1129460':  # Replace with your correct login code
            return redirect('index')  # Redirect to the 'members' page
        else:
            messages.error(request, 'Invalid login code.')
    
    return render(request, 'login_screen/login.html')
