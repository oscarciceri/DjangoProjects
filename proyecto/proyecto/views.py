from datetime import datetime
from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request): # primera vista

    nombre = "******* Juan **************"
    apellido = " ---------- apellido --------------"

    doc_externo  = open("C:/Users/oscar/Documents/Git/DjangoProjects/proyecto/proyecto/plantillas/plantilla.html")
    
    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona": nombre, "apellido_perosna" : apellido , "test" : "test"})

    mensaje =  plt.render(ctx)
    
    return HttpResponse(mensaje)


def despedida(request):

     return HttpResponse("---------- Hasta la vista Hello World, primera pagina -----------")


def prueba(request):
    fecha_actual=datetime.datetime.now()
    mensaje="""
    <html>
        <body>
            <h2>
                Fecha y Hora actuales %s
            </h2>
       </body>
    </html>
    """ % fecha_actual

    return HttpResponse(mensaje)



def calcularEdad(request, edad, agno):

   
    
    edadFutura = int(agno) + int(edad)

    mensaje="""
    <html>
        <body>
            <h2>
                Tu edad furura es %s
            </h2>
       </body>
    </html>
    """ % edadFutura

    return HttpResponse(mensaje)