# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 15:39:19 2023

@author: luis_
"""
import os
import numpy as np
import matplotlib.pyplot as plt

os.system('cls')

def Eggholder(x):
    return (-(x[1]+47)*(np.sin(np.sqrt(np.abs((x[0]/2)+(x[1]+47)))))) - (x[0]*np.sin(np.sqrt(np.abs(x[0]-(x[1]+47)))))

Max_corrida = 5

 # Parametros iniciales
Car = 2 # son las características de la partícula
Xmin = -520 #0.2 # Limite inferior
Xmax = 520 #2.8 # Limite superior
MaxIt = 200 # Generaciones (Iteraciones) máximas
Np = 50 # Tamaño de la población o número de partículas
 
# Parámetros de la ecuación PSO
w = 1 # Parametro de Inercia
#wdamp = 0.9  # Diezmado del parametro de Inercia
c1 = 1.95 # Coeficiente Personal
c2 = 1.95 #  Coeficiente Global
 
Table_Convergence_curve = np.zeros((MaxIt,Max_corrida))
Table_opt = np.zeros((Max_corrida,Car + 2))
w_history = np.zeros((MaxIt,Max_corrida))

corrida = 0
while (corrida < Max_corrida): # for corrida in range (1,Max_corrida,1):
    
    w = 1 # Parametro de Inercia
    
    #============================= Initalización =================================#
    # Empty particle
    Sparticula = {'Position': None, 'Velocity': None, 'Cost': None, 
                       'BestPosition': None, 'BestCost': None}

    # Initialize Best Solution Ever Found
    BestGlobal = {'Position': None, 'Cost': np.inf, 'Iter': 0} #np.inf para darle el valor más grande
    
    # Create Initial Population
    particula = []
    
    k = 0
    while (k < Np):
        
        particula.append(Sparticula.copy()) #.append es para agregar un elemento más al final de la lista
        particula[k]['Position'] = np.random.uniform(Xmin, Xmax, Car) #random entre Xmin y Xmax con 10 características
        particula[k]['Velocity'] = np.zeros(Car)
        particula[k]['Cost'] = Eggholder( particula[k]['Position'] ) # Objective Value
        
        particula[k]['BestPosition'] = particula[k]['Position']
        particula[k]['BestCost'] = particula[k]['Cost']

        
        
        if (particula[k]['Cost'] <= particula[k]['BestCost']):
            particula[k]['BestPosition'] = particula[k]['Position']
            particula[k]['BestCost'] = particula[k]['Cost']
        
        
        if (particula[k]['BestCost'] <= BestGlobal['Cost']):
            BestGlobal ['Position'] =  particula[k]['BestPosition']
            BestGlobal ['Cost'] =  particula[k]['BestCost']
        k = k + 1
        

    iniciales = BestGlobal ['Position']
    
    # Vector con todos los mejores Globales de cada iteración
    BestCosto = []
    
    ## Ciclo principal del algoritmo PSO
    g = 0 # Contador de generaciones (iteraciones)
    
    while ( g < MaxIt ):
        a = 0
        while (a < Np):
            # Actualizar Velocidad
            r1 = np.random.rand(Car)
            r2 = np.random.rand(Car)
            particula[a]["Velocity"] = w*particula[a]["Velocity"] + (c1*r1*(particula[a]['BestPosition'] - particula[a]['Position'])) + (c2*r2*(BestGlobal ['Position'] - particula[a]['Position']))
            
            # Actualizar Posición
            particula[a]['Position'] = particula[a]['Position'] + particula[a]["Velocity"]
            
            # Aplicar Límites
            particula[a]['Position'] = np.maximum(particula[a]['Position'], Xmin)
            particula[a]['Position'] = np.minimum(particula[a]['Position'], Xmax)
            
            # Evaluación de la nueva posición
            particula[a]['Cost'] = Eggholder( particula[a]['Position'] ) # Objective Value
            
            # Recordar el mejor personal
            if (particula[a]['Cost'] <= particula[a]['BestCost']):
                particula[a]['BestPosition'] = particula[a]['Position']
                particula[a]['BestCost'] = particula[a]['Cost']
            
            # Actualizar el mejor Global
            if (particula[a]['BestCost'] <= BestGlobal['Cost']):
                BestGlobal ['Position'] =  particula[a]['BestPosition']
                BestGlobal ['Cost'] =  particula[a]['BestCost']
                BestGlobal ['Iter'] = g
                
            a = a + 1
        
        BestCosto.append(BestGlobal['Cost'])
        # disp(['Iteration ' num2str(g) ': Mejor Costo = ' num2str(BestCosto(g))]);
        
        # Almacenando el mejor global para conocer el historial de la convergencia
        temp = BestGlobal['Cost'] 
        Table_Convergence_curve[g,corrida] = BestGlobal['Cost']
        
        w_history[g,corrida] = w
        
        # Se actualiza el coeficiente de Inercia
        g = g + 1
        w = (MaxIt-g)/MaxIt;
        
        
        temp = BestGlobal ['Position']
        Table_opt[corrida] = (corrida+1, temp[0], temp[1], BestGlobal['Cost'])
        # temp2 = Table_opt[:,0]: # asigna sólo la primera columna de la tabla
        
        # fin Np
    #fin MaxIt
    corrida = corrida + 1
    
iteracion = np.arange(0, MaxIt, 1)
fig, f1 = plt.subplots()
f1.plot(iteracion, Table_Convergence_curve)
plt.title('Convergence Curve')
plt.xlabel('Iteration')
plt.ylabel('Cost')
#plt.show()


