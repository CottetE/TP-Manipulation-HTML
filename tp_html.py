#Travail pratique Manipulation d'arbres HTML
#Réalisation du fichier : Emerald

# Importations : 

# pour utiliser le module de génération de html
from csudoci.html.htmltree import *
from csudoci.html.template import FileTemplate

# pour utiliser le parseur HTML qui construit un arbre
from csudoci.html.parser import HTMLTreeParser

# pour charger les structures de données
from csudoci.ds.stack import Stack

from csudoci.html.manip import *

#Exercice 1 : 
#def get_links(tree):
#    links = []    
#    root = tree
#    
#    if root.tag == 'a':
#        links.append(tree)
#    else:
#        for c in tree.children:
#            links += get_links(c)
def get_elements(tree, selectors):
    """get_elements(tree, selector) ==> list qui construit une liste des 
    sous-arbres de tree possédant pour racine une balise figurant dans la liste 
    selector. EX : header_list = get_elements(tree, ['h1', 'h2'])"""
    
    links = []
    
    if tree.tag in selectors:
        links.append(tree)
    else:
        for child in tree.children:
            links += get_elements(child, selectors)

test()          
get_links(tree) == get_elements(tree, ['a'])