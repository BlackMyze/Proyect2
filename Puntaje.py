from Siguiente_Movimiento import main, chars
from Class.tree import Tree
import numpy as np

# Funciones determinantes de triki

def on_row(row, depth):
  """ Retorna False si char se encuentra en la lista(columna) es decir, si el jugador no ha hecho triki en la columna """
  return False if ( chars[depth%2] in row or ' ' in row) else True
  



def score(tree, depth=0):
    '''
    Funcion principal del codigo
    '''

    result = 0

    # -------- Comprobando triki -------------
    for num_row,row in enumerate(tree.label):
        
        # ~~~~ Analizando por fila ~~~~
        if ( on_row(row, depth+1) ): result = (-1)**(depth)
        # ~~~~ Analizando por columna ~~~~
        elif ( on_row(np.matrix(tree.label).transpose().tolist()[num_row], depth) ): 
            result = (-1)**(depth)

        # ~~~~ hacer los otros casos ~~~~



    # --------- Buscar cada <Siguiente_Movimiento> a el nodo --------

    for i in main(tree, depth):         # Recorrer cada 'Siguiente_Movimiento' de tree
        tree.branches.append(Tree(i))   # Agregar como hijo a cada 'Siguiente_Movimiento'
    
    # -------- Recursion --------
    for branch in tree.branches:        # Aplicar score a cada hijo de tree (recursion)
        if (depth%2==0):
            result = max(result,score(branch, depth+1))
        else: 
            result = min(result,score(branch, depth+1))

    return result




# Aca inicia la prueba (Codigo principal)


def prueba():
       
    t = Tree([["X","O","X"],
              ["O","X","O"],
              ["X"," "," "]])

    x = score(t)
    print(x)
    print(t)

prueba()


