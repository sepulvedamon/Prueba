from django.http import HttpResponse
from django.template import loader
from encuestas.models import Pregunta

def index(request):
    listado = Pregunta.objects.order_by('-fecha_pub')[:10]
    template = loader.get_template('encuestas/index.html')
    context = {'listado': listado,}
    return HttpResponse(template.render(context, request))


def detalle(request, pregunta_id):    
    pregunta = Pregunta.objects.get(id=pregunta_id)
    template = loader.get_template('encuestas/detalle.html')
    context = {'pregunta':pregunta}
    return HttpResponse(template.render(context, request))



def resultados(request, total):
	preguntas = Pregunta.objects.order_by('-fecha_pub')[:total]
	output = ', '.join([p.texto for p in preguntas])
	return HttpResponse(output)

"""
	Construir una vista que despliegue todas las opciones
	relacionadas a una pregunta.
	La pregunta debe buscarse por su ID
"""