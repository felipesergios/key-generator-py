Lista=[]
def Q1():
    n=int(input('Tamanho da Lista:\n'))
    i=0
    while i<n:
        Lista.append(int(input('Valro para POS {} '.format(i))))
        i+=1
        
    Busca=int(input('VAlor para Buscar:'))    
    return Lista.count(Busca)
print(Q1())
