from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm
def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        try: 
            if form.is_valid():
                form.save()
                un = form.cleaned_data.get('username')
                messages.success(request,
                    'Account has been successfully created for {}!'.format(un))
                return redirect('sign_in')
        except Exception as e:
            messages.error(request, f"An error occurred during signup: {str(e)}")
            print("Error occurred during signup:", str(e))
    elif request.method == "GET":
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})