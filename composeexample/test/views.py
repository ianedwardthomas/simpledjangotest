
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required
def page(request):
    return render(request, 'test/page.html')
