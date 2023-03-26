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
            if ( on_row(row, depth+1) ): result = (-1)**(depth); return result
            # ~~~~ Analizando por columna ~~~~
            elif ( on_row(np.matrix(tree.label).transpose().tolist()[num_row], depth) ):
                return (-1)**(depth); break

            # ~~~~ diagonal principal ~~~~
            if ( row[num_row] == chars[depth%2] ): diag_p += ( 1/(len_row_tree+1) )

            # ~~~~ diagonal secundaria ~~~~
            if (row[len_row_tree - num_row] == chars[depth%2] and result ==0): diag_s += ( 1/(len_row_tree+1) )


    if ( diag_p == 1.0 and result == 0 ): result = (-1)**(depth)
    elif ( diag_s == 1.0 and result == 0): result = (-1)**(depth)

    # --------- Buscar cada <Siguiente_Movimiento> a el nodo --------

    for i in main(tree, depth):         # Recorrer cada 'Siguiente_Movimiento' de tree
        tree.branches.append(Tree(i))   # Agregar como hijo a cada 'Siguiente_Movimiento'

    # -------- Recursion --------
    for branch in tree.branches:        # Aplicar score a cada hijo de tree (recursion)
        if (depth%2==0):
            #result = max(result,score(branch, depth+1))
            print(result,score(branch, depth+1),depth)

        else:
            #result = min(result,score(branch, depth+1))
            print(result,score(branch, depth+1),depth)


    return result




# Aca inicia la prueba (Codigo principal)


def prueba():

    t = Tree([["O"," "," "],
              ["O"," "," "],
              ["O"," "," "]])

    print(score(t))

prueba()
