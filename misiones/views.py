from django.shortcuts import render
from django.http import Http404

# Create your views here.
misiones_resistencia = [
    {"id": 1, "nombre": "Rescate en Robotropolis", "ubicacion": "Robotropolis",
     "nivel_dificultad": 8.5, "estado": "completada", "responsable": "Sally Acorn",
     "descripcion": "Infiltracion para liberar prisioneros capturados por Robotnik."},

    {"id": 2, "nombre": "Sabotaje a la fabrica de SWATbots", "ubicacion": "Fabrica Robotnik",
     "nivel_dificultad": 7.2, "estado": "completada", "responsable": "Sonic",
     "descripcion": "Destruccion de la linea de produccion de robots enemigos."},

    {"id": 3, "nombre": "Recuperacion de anillos de poder", "ubicacion": "Bosque de Knothole",
     "nivel_dificultad": 4.0, "estado": "en curso", "responsable": "Tails",
     "descripcion": "Busqueda de anillos dorados escondidos en la zona boscosa."},

    {"id": 4, "nombre": "Vigilancia en la frontera", "ubicacion": "Frontera de Mobius",
     "nivel_dificultad": 3.5, "estado": "en curso", "responsable": "Antoine",
     "descripcion": "Patrullaje constante para detectar movimientos de la Legion."},

    {"id": 5, "nombre": "Reparacion del escudo de Knothole", "ubicacion": "Knothole",
     "nivel_dificultad": 5.8, "estado": "pendiente", "responsable": "Rotor",
     "descripcion": "Arreglar el sistema de defensa daniado tras el ultimo ataque."},

    {"id": 6, "nombre": "Extraccion de Bunnie herida", "ubicacion": "Zona de guerra",
     "nivel_dificultad": 9.1, "estado": "completada", "responsable": "Sally Acorn",
     "descripcion": "Mision de alto riesgo para evacuar a un miembro del equipo."},
]

def inicio(request):
    contexto = {"misiones": misiones_resistencia, "total": len(misiones_resistencia)}
    return render(request, "misiones/inicio.html", contexto)

def detalle(request, id):
    mision = next((m for m in misiones_resistencia if m["id"] == id), None)
    if mision is None:
        raise Http404("Misión no encontrada")
    return render(request, "misiones/detalle.html", {"mision": mision})