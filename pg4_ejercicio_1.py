#ejercicio 1
def ingresar_notas():
    notas = []
    for i in range(3):
        print("Ingrese las notas para el Curso", i+1, ": ")
        curso = []
        for estudiante in range(5):
            nota = input(f"Ingrese la nota del estudiante {estudiante+1} del Curso {i+1}: ")
            nota = float(nota)
            curso.append(nota)
        notas.append(curso)
    return notas


def cal_prom_curso(curso):
    suma_notas = 0
    total_estudiantes = len(curso)
    for nota in curso:
        suma_notas += nota
    return suma_notas / total_estudiantes
  
def calcular_prom_todos(notas):
    total_notas = 0
    total_estu = 0
    for curso in notas:
        for nota in curso:
            total_notas = total_notas + nota
            total_estu = total_estu + 1
    promedio_total = total_notas / total_estu
    return promedio_total


def calcular_porcentaje_aprobados(notas):
    num = 0
    for curso in notas:
        aprobados = 0
        for nota in curso:
            if nota >= 70:
                aprobados += 1
        porcentaje_aprobados = 100 * (aprobados / len(curso))
        print("\nEl porcentaje de aprobados del curso", num + 1, "es:", porcentaje_aprobados, "%")
        num += 1

def obtener_may_men(notas):
    for curso in notas:
        mayor = max(curso)
        menor = min(curso)
        print("Curso", notas.index(curso) + 1, ": Nota mayor:", mayor, "Nota menor:", menor)



notas = ingresar_notas()

print("\nMatriz para los tres cursos:")
for i in range(len(notas)):
    print("\nMatriz para el Curso", i+1, ":")
    for fila in notas[i]:
        print(fila)


promedio_total = calcular_prom_todos(notas)
print("\nPromedio total de los tres cursos:", promedio_total)


for i in range(len(notas)):
    promedio_curso = cal_prom_curso(notas[i])
    print("\nPromedio del curso", i+1, ":", promedio_curso)

calcular_porcentaje_aprobados(notas)

obtener_may_men(notas)

