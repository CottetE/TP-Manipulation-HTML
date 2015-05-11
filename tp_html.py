#Travail pratique : Manipulation d'arbres HTML
#Réalisation du fichier : Emerald

# Importations : 

# pour utiliser le module de génération de html
from csudoci.html.htmltree import *
from csudoci.html.template import FileTemplate

# pour utiliser le parseur HTML qui construit un arbre
from csudoci.html.parser import HTMLTreeParser

# pour charger les structures de données
from csudoci.ds.stack import Stack


# Exercice 1 : 

def get_elements(tree, selectors):
    """get_elements(tree, selector) ==> list qui construit une liste des 
    sous-arbres de tree possédant pour racine une balise figurant dans la liste 
    selector. EX : header_list = get_elements(tree, ['h1', 'h2'])"""
    
    elements = []
    
    if tree.tag in selectors:
        elements += [tree]
    else:
        for child in tree.children:
            elements += get_elements(child, selectors)
    
    return elements

# Exercice 2 :

def table_matieres(tree, level):
    """prend un arbre HTML et construit un arbre HTML (sous forme de liste chez moi)
    représentant une table des matières sur la base des balises <h1>, <h2>, etc ...
    """
    
    balises_base = ['h1','h2','h3','h4','h5','h6']
    
    balises_h = []
    
    for i in range(level):
        balises_h += [balises_base[i]]
        
    
    elements = []
    
    if tree.tag in balises_h:
        elements += [tree]
        
    else:
        for child in tree.children:
            elements += table_matieres(child, level)
    
    return elements

#Exercice 3 
from csudoci.html.parser import html_to_tree

def remove_links(tree):
    """ prend un arbre HTML tree comme paramètre et enlève de cet arbre 
    tous les liens, tout en conservant leur texte. Retourne un arbre html sous
    forme de liste chez moi.
    """
    
    # il s'agit de parcourir l'arbre html pour identifier s'il y a des balises
    # <a ...> <a> pour ensuite les supprimer. Mais il ne faut pas supprimer les 
    # données child de la balise <a>. Autrement dit if <a> "has_a_child", alors 
    # child devient "is_a_child" de la balise parente de <a> et ainsi on supprime
    # cette balise <a> ... 
   
    # on part du principe qu'on ne met jamais de balises <a> dans une autre 
    # balise <a>, le contraire me semble étrange en tout cas...
            
    if tree.tag == 'a':
        kind = tree.children
        tree.parent.children = kind
        # en faisant ainsi je modifie directement l'arbre, par contre en l'affichant
        # j'ai le droit à des variantes d'espace qui apparaissent sans pour autant
        # que cela interfère avec le résultat cherché...

    else:
        for child in tree.children:
            remove_links(child)
       
    return tree
        
    