from django.shortcuts import redirect

def redirect_planet(request):
    return redirect('start_page_url', permanent=True)
