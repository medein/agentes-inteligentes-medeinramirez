import random
import time

def mostrar_cuadricula(cuadricula, agente_pos):
    for i in range(5):
        for j in range(5):
            if (i, j) == agente_pos:
                print("A", end=" ")  # Representa el agente
            elif cuadricula[i][j] == "O":
                print("O", end=" ")  # Representa el objeto
            else:
                print(".", end=" ")  # Espacio vacío
        print()
    print("--------------------")

def agente_buscador():
    cuadricula = [["." for _ in range(5)] for _ in range(5)]
    objeto_pos = (random.randint(0, 4), random.randint(0, 4))
    cuadricula[objeto_pos[0]][objeto_pos[1]] = "O"
    agente_pos = (0, 0)
    
    while agente_pos != objeto_pos:
        mostrar_cuadricula(cuadricula, agente_pos)
        time.sleep(1)
        
        # Movimiento del agente hacia el objeto
        x, y = agente_pos
        obj_x, obj_y = objeto_pos
        
        if x < obj_x:
            x += 1
        elif x > obj_x:
            x -= 1
        elif y < obj_y:
            y += 1
        elif y > obj_y:
            y -= 1
        
        agente_pos = (x, y)
    
    mostrar_cuadricula(cuadricula, agente_pos)
    print("¡Objeto encontrado!")

if __name__ == "__main__":
    agente_buscador()