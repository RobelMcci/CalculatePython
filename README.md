# Calculette du second degré (PyScript + Python + Bootstrap)

Une petite application web permettant de résoudre les équations du second degré de la forme :

ax2+bx+c=0

en utilisant Python directement dans le navigateur grâce à PyScript.

# Fonctionnalités

Interface simple et responsive grâce à Bootstrap 5.

Résolution automatique après saisie de a, b, c.

## Affichage de :
    Le discriminant (Δ)
    Les racines x1 et x2
	​

## Gestion des cas particuliers :
    a=0 → équation du premier degré
    Δ=0 → racine double
    Δ<0 → racines complexes

# Technologies utilisées
    HTML5 / Bootstrap 5.3 pour le front-end
    PyScript 2025.11.1 pour exécuter le code Python côté navigateur
    Pyodide (interne à PyScript) pour le lien entre Python et JavaScript

# Explication du fichier main.py
    Le fichier main.py contient toute la logique de calcul et d’interaction avec le DOM (le HTML).

## Étapes principales :
    Importation des modules :
        from js import document
        from pyodide.ffi import create_proxy
        import math
    
    document permet d’accéder aux éléments HTML depuis Python.
    create_proxy sert à connecter proprement une fonction Python à un événement JavaScript.
    math est utilisé pour les racines carrées et calculs.
    
    Définition de la fonction principale :
        def calculer_equation(event):
            a = float(document.getElementById("valeur-a").value or 0)
            b = float(document.getElementById("valeur-b").value or 0)
            c = float(document.getElementById("valeur-c").value or 0)

            delta = b**2 - 4*a*c
    
    Affichage dans les champs de sortie :
        document.getElementById("outputDelta").value = round(delta, 4)
        
        Les résultats sont directement injectés dans les champs HTML (outputDelta, output-x1, output-x2).
    
    Connexion de l’événement :
        proxy = create_proxy(calculer_equation)
        btn = document.getElementById("btn-valider")
        btn.addEventListener("click", proxy)
        
        Cette partie est essentielle : elle empêche Pyodide de “détruire” la fonction Python après le premier clic