from django.http import HttpResponse
from django.views import View
import string
import random
    
class MiVista2(View):
    def get(self, request):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = "".join(random.choice(caracteres) for number in range(16))
        return HttpResponse (contraseña)

class MiVista(View):
    def get(self, request):
        caracteres = string.ascii_letters + string.digits
        return HttpResponse("".join([caracteres[i] for i in range(0, 10)]))