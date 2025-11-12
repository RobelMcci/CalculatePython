            from js import document
from pyodide.ffi import create_proxy
import math

def calculer_equation(event):
    try:
        a = float(document.getElementById("valeur-a").value or 0)
        b = float(document.getElementById("valeur-b").value or 0)
        c = float(document.getElementById("valeur-c").value or 0)

        delta = b*b - 4*a*c
        document.getElementById("output-delta").value = round(delta, 4)

        if a == 0:
            if b != 0:
                x = -c / b
                document.getElementById("output-x1").value = round(x, 4)
                document.getElementById("output-x2").value = "—"
            else:
                document.getElementById("output-x1").value = "Aucune solution"
                document.getElementById("output-x2").value = "—"
        else:
            if delta > 0:
                x1 = (-b - math.sqrt(delta)) / (2 * a)
                x2 = (-b + math.sqrt(delta)) / (2 * a)
                document.getElementById("output-x1").value = round(x1, 4)
                document.getElementById("output-x2").value = round(x2, 4)
                resultatdelta = "Deux solutions réelles distinctes"
                document.innertext.getElementById("valeurdelta").value = resultatdelta
            elif delta == 0:
                x = -b / (2 * a)
                document.getElementById("output-x1").value = round(x, 4)
                document.getElementById("output-x2").value = round(x, 4)
                resultatdelta = "Une seule solution réelle"
                document.innertext.getElementById("valeurdelta").value = resultatdelta
            else:
                real = -b / (2 * a)
                imag = math.sqrt(-delta) / (2 * a)
                document.getElementById("output-x1").value = f"{round(real, 4)} - {round(imag, 4)}i"
                document.getElementById("output-x2").value = f"{round(real, 4)} + {round(imag, 4)}i"
                resultatdelta = "Aucune solution réelle"
                document.innertext.getElementById("valeurdelta").value = resultatdelta
    except Exception as e:
        print("Erreur :", e)


proxy = create_proxy(calculer_equation)

btn = document.getElementById("btn-valider")
btn.addEventListener("click", proxy)
