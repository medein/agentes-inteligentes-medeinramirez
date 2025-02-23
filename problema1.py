import time
import random

def agente_semaforo():
    estados = ["Verde", "Amarillo", "Rojo"]
    while True:
        cantidad_vehiculos = random.randint(0, 20)  # Simulación de detección de vehículos
        print(f"Vehículos detectados: {cantidad_vehiculos}")
        
        if cantidad_vehiculos > 10:
            tiempo_verde = 10  # Más autos, más tiempo en verde
        elif 5 <= cantidad_vehiculos <= 10:
            tiempo_verde = 7
        else:
            tiempo_verde = 4  # Pocos autos, menos tiempo en verde
        
        print(f"Estado: {estados[0]} (Duración: {tiempo_verde} seg)")
        time.sleep(tiempo_verde)
        
        print(f"Estado: {estados[1]} (Duración: 3 seg)")  # Amarillo fijo en 3 seg
        time.sleep(3)
        
        print(f"Estado: {estados[2]} (Duración: 5 seg)")  # Rojo fijo en 5 seg
        time.sleep(5)
        print("---------------------------")

if __name__ == "__main__":
    agente_semaforo()
    