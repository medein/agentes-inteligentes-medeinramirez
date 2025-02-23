import random

def recomendar_pelicula():
    peliculas = {
        "acción": ["Mad Max: Fury Road", "John Wick", "Gladiador"],
        "comedia": ["Superbad", "La Máscara", "Dumb and Dumber"],
        "drama": ["Forrest Gump", "El Padrino", "Sueños de Libertad"],
        "ciencia ficción": ["Interestelar", "Blade Runner 2049", "The Matrix"],
        "terror": ["El Conjuro", "IT", "Halloween"]
    }
    
    print("Géneros disponibles: acción, comedia, drama, ciencia ficción, terror")
    genero = input("Ingrese su género favorito: ").strip().lower()
    
    if genero in peliculas:
        pelicula_recomendada = random.choice(peliculas[genero])
        print(f"Te recomendamos ver: {pelicula_recomendada}")
    else:
        print("Género no reconocido. Intente nuevamente.")

if __name__ == "__main__":
    recomendar_pelicula()