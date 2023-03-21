from Class.queue import LinkedQueue

auxqueue = LinkedQueue()
chars = ['X','O'] # Opciones de marcado en el tablero, para el jugador A y B respectivamente

def Siguiente_Movimiento(tree, depth):
  """ Calcula uno de los mejores movimientos siguientes
  >>> t = Tree([["X","O","X"],["O","X","O"],[" "," "," "]])
  >>> Siguiente_Movimiento(t)
  Tree([["X","O","X"],["O","X","O"],["O"," "," "]])
  """
  MainIndex = 0 # Recorre cada lista(fila) dentro de <tree.label>
  label_copy = [tree.label[i].copy() for i in range(len(tree.label))]   # Copia de lo que almacena el arbol

  for MainIndex in range(len(tree.label)):  # Recorrer cada fila del tablero de triki

    if (' ' in tree.label[MainIndex]): # Condicion donde ' ' esta dentro de la lista(fila) con indice 'MainIndex'

      for SegIndex in range(len(tree.label)):   # Solo un for anidado

        if (tree.label[MainIndex][SegIndex]== ' '): # Verificar si la posicion del tablero esta vacia
          label_copy[MainIndex][SegIndex] = chars[depth%2] # Cambiar la posicion vacia por la jugada correspondiente segun la profundidad
          auxqueue.enqueue([i.copy() for i in label_copy]) # Agregar a la cola una copia del arbol siguiente
          label_copy[MainIndex][SegIndex] = ' ' # Dejar como estaba la posicion original

def main(t, depth):
    Siguiente_Movimiento(t, depth)
    if (__name__ == '__main__'): return auxqueue.first()
    else:
      while not auxqueue.is_empty():
        yield auxqueue.dequeue()
