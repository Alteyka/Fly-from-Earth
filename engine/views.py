from django.shortcuts import redirect

def redirect_planet(request):
    return redirect('cards_list_url', permanent=True)
