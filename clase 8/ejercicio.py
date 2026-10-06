def calcular_imc(peso: float, altura: float) -> float:

    '''
    Calcula el IMC.
    Recibe dos flotantes que representan peso y altura.
    Retorna el IMC como flotante.
    '''

    return peso / (altura ** 2) 
    

def analizar_imc(imc: float) -> str:

    '''

    '''

    analisis = "El índice de masa corporal es de : " + str(imc)

    if imc < 18.5:
        analisis += ". Es necesario aumentar ingesta calórica."
    elif imc < 25:
        analisis += ". Peso equilibrado."
    else:
        analisis += ". Es necesario reducir ingesta calórica."

    return analisis

def analizar_temperatura(temperatura: float) -> str:

    '''
    '''

    diagnostico = str(temperatura) + "° de temperatura corporal."
    
    if temperatura > 41:
        diagnostico += " Fiebre muy alta."
    elif temperatura > 39:
        diagnostico += " Fiebre alta."
    elif temperatura >= 38:
        diagnostico += " Fiebre moderada."
    elif temperatura > 37.3:
        diagnostico += " Febrícula."
    else:
        diagnostico += " Temperatura normal."

    return diagnostico


def mostrar_consulta(nombre_paciente: str, peso: float,
                    altura: float, temperatura: float,
                    sistolica: float, diastolica: float) -> None:

    '''
    Carga la información de una consulta médica. Incluyendo IMC, presión y fiebre.
    Recibe 6 parametros.
    No retorna nada.
    '''

    imc = calcular_imc(peso, altura)

    diagnostico_imc = analizar_imc(imc)

    diagnostico_fiebre = analizar_temperatura(temperatura)

    diagnostico_presion = analizar_presion(sistolica, diastolica)

    info = f"""
    Diagnostico del paciente {nombre_paciente} \n
    Peso: {diagnostico_imc}. \n
    Fiebre: {diagnostico_fiebre}\n
    Presión: {diagnostico_presion}
    """

    print(info)

def analizar_presion(presion_sistolica: float,
                     presion_diastolica: float) -> str:

    '''
    '''

    if presion_sistolica < 90 or presion_diastolica < 60:
        diagnostico = "presión baja."
    elif presion_sistolica > 140 or presion_diastolica > 90:
        diagnostico = "Presión alta."
    else:
        diagnostico = "Presión normal."
    
    return diagnostico

mostrar_consulta("Pedro Perez", 
                 78.5, 1.75, 
                 38, 70, 60)