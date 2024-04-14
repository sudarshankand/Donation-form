from django.shortcuts import render, redirect
from .forms import PersonDonationForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def donation_form(request):
    if request.method == 'POST':
        form = PersonDonationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('donation_form')  # Redirect to success page
    else:
        form = PersonDonationForm()

    context = {'form': form}
    return render(request, 'donate/donation_form.html', context)
