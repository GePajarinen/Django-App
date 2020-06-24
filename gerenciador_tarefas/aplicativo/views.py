from django.shortcuts import render

# Create your views here.
def listar_tarefas(request):
    return render(request, 'tarefas/listar_tarefas.html')