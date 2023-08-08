Parámetros definidos por el usuario:

Max_corrida : Número de veces que se ejecutará el algoritmo
MaxIt:        Criterio de parada (máximo número de iteraciones)
Np:           Tamaño de la población o número de partículas 
Xmin:         Limite inferior del espacio de búsqueda
Xmax:         Limite superior del espacio de búsqueda

Parámetro definido por el problema
Car:          Número de características de la partícula (incógnitas del problema)


Los resultados de la optimización se almacenan en la Matriz 'Table_opt'
Donde: 
La primera columna es la corrida
Las n columnas siguientes son la ubicación de las partículas (solución al problema)
La última columna es el costo de la función

| corrida | x1 | x2 | ... | x Car | mínimo |

 
La curva de convergencia se almacena en el arreglo 'Table_Convergence_curve'.
Cada columna es la curva de convergencia de cada corrida

| corrida 1 | corrida 2 | ... | corrida Max_Corrida |

Nota: Este programa sólo optimiza para un espacio de búsqueda cuadrado entre Xmin y Xmax 
Estoy trabajando para hacerlo rectangular
