from Siguiente_Movimiento import main, chars
from Class.tree import Tree
import numpy as np

# Funciones determinantes de triki

def on_row(row, depth):
  """ Retorna False si char se encuentra en la lista(fila) es decir, si el jugador no ha hecho triki en la fila """
  return False if ( chars[depth%2] in row or ' ' in row) else True




def score(tree, depth=0):
    '''
    Funcion principal del codigo
    '''
    
     

    result = 0

    # Implementacion para las diagonales
    diag_p = 0
    diag_s = 0

    # Longitud de la matrix
    len_row_tree = len(tree.label) -1

    # -------- Comprobando triki -------------
    for num_row,row in enumerate(tree.label):

        if not(result):
            # ~~~~ Analizando por fila ~~~~
            if ( on_row(row, depth+1) ): return (-1)**(depth)
            # ~~~~ Analizando por columna ~~~~
            elif ( on_row(np.matrix(tree.label).transpose().tolist()[num_row], depth+1) ):
                return (-1)**(depth)

            # ~~~~ diagonal principal ~~~~
            if ( row[num_row] == chars[depth%2] ): diag_p += ( 1/(len_row_tree+1) )

            # ~~~~ diagonal secundaria ~~~~
            if (row[len_row_tree - num_row] == chars[depth%2]): diag_s += ( 1/(len_row_tree+1) )


    if ( diag_p == 1.0 and result == 0 ): return (-1)**(depth)
    elif ( diag_s == 1.0 and result == 0): return (-1)**(depth)

    # --------- Buscar cada <Siguiente_Movimiento> a el nodo --------
    for i in main(tree, depth):         # Recorrer cada 'Siguiente_Movimiento' de tree
        tree.branches.append(Tree(i))   # Agregar como hijo a cada 'Siguiente_Movimiento'

   # -------- Recursion 1 --------
#    for branch in tree.branches:        # Aplicar score a cada hijo de tree (recursion)

#        if (depth%2==0):

            #result = max(result,)
#            print(score(branch, depth+1),depth)

#        else:
#            #result = min(result,score(branch, depth+1))
#            print(score(branch, depth+1),depth)

   # -------- Recursion 2 --------
#    temp = []
#    if (depth%2==0):
#        for branch in tree.branches:
#            temp.append(score(branch, depth+1))
            #if (branch.is_leaf()): return result
            #else: print(depth, "max", temp) #print(temp, depth, "maximo")
#            print(depth, temp, "maximo"); return max(temp)
            
#       return max(temp)

#    else:
#        for branch in tree.branches:
#            temp.append(score(branch, depth+1))
#            #if (branch.is_leaf()): return result
#            #else: print(depth, "min", temp) #print(temp, depth, "maximo")
#            print(depth, temp, "minimo")
        #result = min(temp)


   # -------- Recursion 3 --------
    temp = []
    for branch in tree.branches:
        temp.append(score(branch, depth+1))
        print(depth,temp)
            
    if(len(temp)): 
        if(depth%2==0): return max(temp)
        return min(temp)

    else: return result


# Aca inicia la prueba (Codigo principal)


def prueba():
    
    t = Tree([[" "," "," "],
              [" "," "," "],
              [" "," "," "]])

    points = {"X":0, "O":0}
    for i in range(len(t.label)):
        for j in range(len(t.label)):
            if t.label[i][j] == "X": points["X"] += 1
            elif t.label[i][j] == "O": points["O"] += 1
    
    if points["X"] < points["O"]: 
        print(score(t,1))
    else: 
        print(score(t))
    #print(t)
    #print(t, score(t))

prueba()
