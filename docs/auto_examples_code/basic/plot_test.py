"""
Comment écrire un notebook ?
============================

Déjà, on import les librairies python kivonbien®.

"""

import matplotlib.pyplot as plt


######################################################################
# Et ensuite, on trace ce que l’on veut. Par exemple on peut même écrire
# des maths :
# 
# .. math::
# 
# 
#    E = mc^2
# 
# 

plt.plot([1,2],[2,1], marker="*")


######################################################################
# Et on ajoute une cellule de code:
# 

plt.bar([1,2], [1,2])

plt.show()
