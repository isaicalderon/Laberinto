
import re
import math
import Nodo 
import Arco
import Grafo

archivo = open("entrada4.txt")
costo   = "X"
g       = Grafo.Grafo()
linea   = archivo.readline()
linea   = linea.rstrip()
linea   = linea.strip()
tmp     = re.findall("^costo\s*=\s*(\S+)",linea)

if len(tmp) > 0:
    costo = tmp[0]
# end if

if(costo == "no"):
    for linea in archivo.readlines():
        linea = linea.rstrip()
        linea = linea.strip()
        tmp = re.findall("\S+",linea)
        if len(tmp) > 0:
            origen = g.addNodo(tmp[0])
            for i in range(1, len(tmp)):
                destino = g.addNodo(tmp[i])
                origen.addAdyacente(destino)
                arco = Arco.Arco(1, origen, destino)
                g.addArco(arco)
            # end for
        # end if
    # end for
elif costo == "si":
    for linea in archivo.readlines():
        linea = linea.rstrip()
        linea = linea.strip()
        tmp = re.findall("\S+", linea)
        # print (costo)
    # end for
        if len(tmp) > 0:
            origen = g.addNodo(tmp[0])
            for i in range(1, len(tmp)):
                name = re.findall("(\S+)\s*:", tmp[i]);
                costo = re.findall(":\s*(\S+)", tmp[i])
                name = name[0]
                costo = float(costo[0])
                destino = g.addNodo(name)
                origen.addAdyacente(destino)
                arco = Arco.Arco(costo, origen, destino)
                g.addArco(arco)
            # end for
        # end if
    # end for
# end elif

print("G:")
g.DFS()
# g.sortByFDesc()
g.show2()


# print("\nGT: ")
# gt = g.getTrans()
# lista = gt.SCC()
# i = 0
# for u in lista:
#     print ("SCC[",i,"]",end="")
#     i = i+1
#     for v in u:
#         print(v.getNombre(), end=", ")
#     print("")
#     # end for v
# # end for u
# archivo.close()