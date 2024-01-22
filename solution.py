def calcular_promedios(verbales: str, numericas: str) -> int:
    pass
#Funcion que calcula el promedio de los puntajes verbales y numericos

def calcular_promedios(numerical_skills, verbal_skills):
    numerical_skills = list(map(int, numerical_skills.split()))
    verbal_skills = list(map(int, verbal_skills.split()))

    averages = [(n + v) / 2 for n, v in zip(numerical_skills, verbal_skills)]
    general_average = sum(averages) / len(averages)

    return sum(1 for avg in averages if avg < general_average)