from django.shortcuts import render


# Create your views here.
def vPagPrincipal(Request):

    return render(Request, 'PagPrincipal.html')