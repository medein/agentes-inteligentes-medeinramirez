def diagnostico():
    print("Sistema Experto de Diagnóstico Médico")
    print("Ingrese 'sí' o 'no' para los siguientes síntomas:")
    
    fiebre = input("¿Tiene fiebre? ").strip().lower() == "sí"
    tos = input("¿Tiene tos? ").strip().lower() == "sí"
    dolor_garganta = input("¿Tiene dolor de garganta? ").strip().lower() == "sí"
    congestion = input("¿Tiene congestión nasal? ").strip().lower() == "sí"
    fatiga = input("¿Siente fatiga? ").strip().lower() == "sí"
    
    if fiebre and tos and fatiga:
        print("Posible diagnóstico: Gripe.")
    elif fiebre and dolor_garganta and congestion:
        print("Posible diagnóstico: Infección respiratoria.")
    elif tos and congestion and not fiebre:
        print("Posible diagnóstico: Resfriado común.")
    elif fiebre and tos and dolor_garganta:
        print("Posible diagnóstico: Faringitis viral.")
    elif fiebre and fatiga and not tos:
        print("Posible diagnóstico: Infección bacteriana.")
    elif fiebre and tos and not congestion and fatiga:
        print("Posible diagnóstico: Neumonía.")
    elif fiebre and fatiga:
        print("Posible diagnóstico: Mononucleosis.")
    else:
        print("Los síntomas ingresados pueden no coincidir con una enfermedad específica. Se recomienda consultar a un médico.")
    
if __name__ == "__main__":
    diagnostico()