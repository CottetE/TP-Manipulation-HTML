# Exercice 4 
# génération des tests pour le fichier tp_html.py

# Le choix d'afficher certains test à l'intérieur d'une balise <div> est purement
# arbitraire mais met bien en évidence l'essentiel...

# L'utilisation de vérifications visuelles n'est clairment pas optimal mais je ne veux 
# pas non plus prendre du temps à créer un canon pour tuer une mouche...

from tp_html import *

def get_links(tree):
    links = []
    root = tree
    
    if root.tag == 'a':
        links.append(tree)
    else:
        for c in tree.children:
            links += get_links(c)

    return links


def test_get_elements(tree):

    #si cela marche le test retournera True car c'est sensé faire la même chose:
    if get_links(tree) == get_elements(tree, ['a']):
        print('True\n')
    
    #test sur plusieurs éléments / vérification visuelle avec la réponse :
    
    reponse = """<div>
                   <li><a href="...">
                         ...
                      </a></li>
                   <li><em><a href="...">
                            ...
                         </a></em></li>
                   <li><a href="...">
                         ...
                      </a></li>
                   <p>
                      <li><strong>blabla</strong></li>
                   </p>
                   <p>
                      <h2>La page du collège du Sud se trouve sur</h2>
                      <a href="http://www.collegedusud.ch">
                          http://www.collegedusud.ch 
                      </a>
                   </p>
                   <li> truc </li>
                   <li> c'est pas beau <h6> mais un idiot pourrait faire </h6> ce genre de chose </li>
                </div>"""
    
    elem = get_elements(tree, ['a','li','p'])
    elem_in_div = Div() > elem
    print(elem_in_div.html()+'\n')
    
    #test si pas d'élément valide :
    if get_elements(tree, ['div']) == []:
        print('True')
    
    # Question en suspens : si le selector cherché se trouve dans un selector qui
    # a déjà été cherché, celui-ci ne s'affichera pas en "solitaire" mais est-ce gênant ?
    
def test_table_matieres(tree):
    """Pour être sur que ce soit fonctionnel il faut tester sur tous les
    niveaux possibles"""
    
    # test sur tous les levels donc nécessairement tous fonctionnent / vérification 
    # viuelle avec la réponse :
    
    reponse = """<div>
                   <h1> un h1 super tordu       <ul>
                         <li><a href="...">
                               ...
                            </a></li>
                         <li><em><a href="...">
                                  ...
                               </a></em></li>
                         <li><a href="...">
                               ...
                            </a></li>
                      </ul>      est moche en plus !      </h1>
                   <h1> Juste un vrai titre </h1>
                   <h2>La page du collège du Sud se trouve sur</h2>
                   <h3> C'est juste pour le test </h3>
                   <h4> ça dérange si je mets du : <h5> dedans </h5> , ou pas ? </h4>
                   <h5> du h5 pour voir </h5>
                   <h5> pareil qu'en dessus...</h5>
                   <h6> mais un idiot pourrait faire </h6>
                   <h2> comme ça finalement </h2>
                </div>"""

    
    tdm = table_matieres(tree, level = 6)
    tdm_in_div = Div() > tdm
    print(tdm_in_div.html()+'\n')
    
def test_remove_links(tree):
    
    # vérification visuelle avec la réponse :
    
    reponse = """<html>
                   <head>
                      ...
                   </head>
                   <body>
                      <h1> un h1 super tordu       <ul>
                            <li>               ...</li>
                            <li><em>                  ...</em></li>
                            <li>               ...</li>
                         </ul>      est moche en plus !      </h1>
                      <h1> Juste un vrai titre </h1>
                      <p>
                         <li><strong>blabla</strong></li>
                      </p>
                      <p>
                          http://www.collegedusud.ch 
                      </p>
                      <h3> C'est juste pour le test </h3>
                      <h4> ça dérange si je mets du : <h5> dedans </h5> , ou pas ? </h4>
                      <ol>
                         <h5> du h5 pour voir </h5>
                         <h5> pareil qu'en dessus...</h5>
                         <li> truc </li>
                         <li> c'est pas beau             <h6> mais un idiot pourrait faire </h6> ce genre de chose </li>
                      </ol>
                      <h2> comme ça finalement </h2>
                   </body>
                </html>"""
    
    rml = remove_links(tree)
    rml_in_div = Div() > rml
    print(rml_in_div.html()+'\n')
    
# Corps du programme de test :   

test_html = '''
<html>
  <head>...</head>
  <body>
     <h1> un h1 super tordu 
     <ul>
        <li><a href="...">...</a></li>
        <li><em><a href="...">...</a></em></li>
        <li><a href="...">...</a></li>
     </ul>
     est moche en plus !
     </h1>
     <h1> Juste un vrai titre </h1>
     <p><li><strong>blabla</strong></li></p>
     <p>
        <h2>La page du collège du Sud se trouve sur</h2>
        <a href="http://www.collegedusud.ch"> http://www.collegedusud.ch </a>
     </p>
     <h3> C'est juste pour le test </h3>
     <h4> ça dérange si je mets du : <h5> dedans </h5> , ou pas ? </h4>
     <ol>
        <h5> du h5 pour voir </h5>
        <h5> pareil qu'en dessus...</h5>
        <li> truc </li>
        <li> c'est pas beau <h6> mais un idiot pourrait faire </h6> ce genre de chose </li>
     </ol>
     <h2> comme ça finalement </h2>
  </body>
</html>
'''
tree = HTMLTreeParser(test_html).get_tree()

print('Tests pour la fonction get_elements :\n')
test_get_elements(tree)
print('\n\n')

print('Tests pour la fonction test_table_matieres :\n')
test_table_matieres(tree)
print('\n\n')

print('Tests pour la fonction remove_links :\n')
test_remove_links(tree)
print('\n\n')


# P.S. j'ai le mérite au moins de ne pas avoir regardé d'autres codes pour réaliser
# ce tp et je me suis éfforcé d'être le plus autonome possible :)