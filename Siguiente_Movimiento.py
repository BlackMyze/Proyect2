from Class.queue import LinkedQueue

auxqueue = LinkedQueue()

def Siguiente_Movimiento(tree, depth):
  """ Calcula uno de los mejores movimientos siguientes
  >>> t = Tree([["X","O","X"],["O","X","O"],[" "," "," "]])
  >>> Siguiente_Movimiento(t)
  Tree([["X","O","X"],["O","X","O"],["O"," "," "]])
  """
  chars = ['X','O']
  MainIndex = 0 # Recorre cada lista(fila) dentro de <tree.label>
  label_copy = [tree.label[i].copy() for i in range(len(tree.label))]

  for MainIndex in range(len(tree.label)):

    if (' ' in tree.label[MainIndex]): # Condicion donde ' ' esta dentro de la lista(fila) con indice 'MainIndex'

      for SegIndex in range(len(tree.label)):

        if (tree.label[MainIndex][SegIndex]== ' '):
          label_copy[MainIndex][SegIndex] = chars[depth%2]
          auxqueue.enqueue([i.copy() for i in label_copy])
          label_copy[MainIndex][SegIndex] = ' '

def main(t, depth):
    Siguiente_Movimiento(t, depth)
    if (__name__ == '__main__'): return auxqueue.first()
    else:
      while not auxqueue.is_empty():
        yield auxqueue.dequeue()
