import numpy as np
import fractions

def Triangular_matriz(matriz):
    pivote = 0
    columna_pivote = 0
    while pivote < len(matriz):
        piv = matriz [pivote][columna_pivote]
        for i in range (pivote + 1, len(matriz) ):
            if piv == 0:
                contadorceros = 0
                for j in range(pivote + 1, len(matriz)) :
                    if matriz[j][columna_pivote] != 0:
                        matriz[pivote], matriz[j] = matriz[j], matriz[pivote]
                        piv = matriz [pivote][columna_pivote]
                        break
                    if j == len(matriz) - 1 and columna_pivote < len(matriz[0])-1:
                        columna_pivote += 1
                        piv = matriz [pivote][columna_pivote]

            sig = -matriz[i][columna_pivote] if i < len(matriz) else -matriz[i - 1][columna_pivote]
            if sig == 0:
                continue
            multiplicador = fractions.Fraction(sig , piv)
            for j in range(len(matriz[0])):
                matriz[i][j] += multiplicador * matriz[pivote][j]

        pivote += 1
        if columna_pivote < len(matriz[0])-1:
            columna_pivote += 1
        else:
            break
    return matriz
def Calcular_variables(matriz_triangulada):
    #elimino filas nulas
    matriz_sin_nulos = []
    for i in range(len(matriz_triangulada)):
        for j in range(len(matriz_triangulada[i])):
            if matriz_triangulada[i][j] != 0:
                matriz_sin_nulos.append(matriz_triangulada[i])
                break
    #rouche-frobenius
    rgM = len(matriz_sin_nulos)
    matrizA = np.array(matriz_sin_nulos)
    matrizA = matrizA[:, 0: len(matrizA[0])-1]
    matrizA_sin_nulos = []
    for i in range(len(matrizA)):
        for j in range(len(matrizA[i])):
            if matrizA[i][j] != 0:
                matrizA_sin_nulos.append(matrizA[i])
                break
    rgA = len(matrizA_sin_nulos)
    n = len(matriz_triangulada[0]) -1
    if rgA != rgM:
        return "SI"
    else:
        if rgA != n:
            return "SCI"
        else:
            A = np.array(matriz_sin_nulos)[:, 0: len(matriz_sin_nulos[0])-1]
            B = np.array(matriz_sin_nulos)[:, len(matriz_sin_nulos)]
            soluciones = [1 for i in range(n)]

            for i in range(len(matriz_sin_nulos)-1, -1, -1):
                if i+1 < len(A[i]):
                    sumaDeCoeficientes = 0
                    for j in range(i + 1, len(A[i])):
                        sumaDeCoeficientes += (A[i][j] * soluciones[j])
                    soluciones[i] = fractions.Fraction(B[i] - sumaDeCoeficientes, A[i][i])


                else:#ultima fila
                    soluciones[i] = fractions.Fraction(B[i], A[i][i])
            return list(map(lambda x: str(x),soluciones))
                
continuar = "y"
while continuar not in ("n", "N", "NO", "no"):
    filas = int(input("ingrese cantidad de filas: "))
    columnas = int(input("ingrese cantiad de columnas: "))

    matrizz = [[] for i in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            matrizz[i].append(int(input("ingrese el elemento de la fila {} y columna {}: ".format(i +1,j + 1))))

    matriz = Triangular_matriz(matrizz)
    sol = Calcular_variables(matriz)
    for j in range(len(matriz)):
        for a in range(len(matriz[j])):
            if type(matriz[j][a]) == fractions.Fraction:
                matriz[j][a] = str(matriz[j][a])
    print("\nMatriz triangulada")
    print(np.array(matriz), "\n")
    print("Soluciones:")
    if sol not in ("SI", "SCI"):
        for i in range(len(sol)):
            print("x{}= {}".format(i+1, sol[i]))
    else:
        print("El sistema es {}".format(sol))
    continuar = input("continuar con otra operacion?(Y/n)")
    if continuar == "":
        continuar="y"
    else:
        input("pulsa enter para salir")
    
