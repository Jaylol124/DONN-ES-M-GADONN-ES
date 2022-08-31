# Documentation
# ----------------------------------------------------------------------------
# Python documentation : 
#   - Documentation officielle : https://www.python.org/doc/
#   - RealPython : https://realpython.com/
#   - ...
#   - StackOverflow


# Version installée à l'école
# ----------------------------------------------------------------------------
import sys
import copy
print('Version : ', sys.version)


# Bonnes pratiques
# ----------------------------------------------------------------------------
# CALTAL 
#   - Code A Little, Test A Little
#   - Codez et testez une petite quantité de développement à la fois.
# DRY 
#   - Don't Repeat Yourself
#   - Ne vous répété pas, c'est le signe d'une faible qualité de développement logiciel (pas toujours).
# UMUD 
#   - yoU Must Use the Debugger _when available_
#   - Lorsqu'un débogueur est disponible, il est impératif de l'utiliser et de ne pas polluer son code avec des impressions inutiles.
# OFOT 
#   - One Fonction, One Task
#   - Chaque fonction doit avoir un rôle unique.
# MAP 
#   - Modularity Above Performance 
#   - La modularité doit avoir préscéance sur la performance (sauf lorsque la performance est réellement requise).
# WORO
#   - Write Once, Read Often
#   - Vous allez écrire le code une fois. Il sera lu certainement très souvent, par beaucoup et pendant longtemps. Autant prendre le temps de bien l'écrire.
# DARAD
#   - Don't Assume, Read Attentively the Documentation
#   - Il est important de lire la documentation afin de bien comprendre les outils utilisés, leurs limites et les nuances existantes.
# SOCBUD
#   - Separation Of Concerne Between User and Developer
#   - Lorsque vous développé des outils réutilisables, faire un effort d'abstraction afin d'offrir la meilleure interface de programmation possible.


# Norme de codage
# ----------------------------------------------------------------------------
# Une norme de codage présente :
# • un ensemble de plusieurs règles déterminant la pratique de rédaction du code;
# • des lignes directrices;
# • une convention;
# • ce qui est considéré comme une bonne pratique.
# Elle permet d'assurer une certaine qualité logicielle et une uniformisation de la pratique à travers :
# • les divers intervenants d’un projet;
# • le temps;
# • les technologies employées.
# Cette pratique du génie aide un logiciel à être davantage :
# • maintenable : peut évoluer plus facilement;
# • portable : il fonctionne similairement dans différents environnements;
# • testable : il peut être tester par des procédures standardisées à l'interne;
# • fiable : il fonctionne tel qu'attendu;
# • sûre et sécuritaire : ne peut causer de dommage et plus difficilement piratable;
# en offrant un code :
# • uniforme;
# • plus facile à lire;
# • plus facile à écrire;
# • respectant des guides établis par des développeurs expérimentés;
# • apportant les compromis nécessaires à une pratique de qualité.
# Sachez que dans l'industrie, une norme de codage peut être stricte, contraignante et détaillée ou
# complètement l'inverse. De plus, aucune norme est la meilleure. Les normes varient selon les entreprises,
# les projets, les développeurs, les langages de programmation, l’époque, les outils disponibles, ….

# Avec Python, sauf avis contraire (employeur, enseignant, ...), utilisez la norme de codage PEP8 : https://www.python.org/dev/peps/pep-0008/.
# C'est la règle d'usage dans le cours... et ça compte (sans être strict)!
#  -> PEP : Python Enhancement Proposals <- il y en a plusieurs, allez les consulter progressivement pendant votre formation et votre vie professionnelle.

# Résumé des éléments importants :
#   - disposition
#       - utilisation des espaces (pas de tab)
#       - indentation de 4 espaces
#       - lignes de 79 caractères (*)
#       - lignes vides (au minimum) :
#           - 2 avant la déclaration d'une fonction ou d'une classe
#           - 1 avant la déclaration d'une méthode
#       - 'import' au début du fichier dans l'ordre suivant : 
#           - librairies standards
#           - librairies externes
#           - librairies internes
#   - nommage
#       - types : PascalCase
#       - variables, fonctions, méthodes : snake_case
#       - constantes : CAPITAL_SNAKE_CASE --- les constantes n'existent pas en Python
#       - nom auto descriptif (auto documentation)
#       
#   - on reviendra sur la notion de masquage en Python!!!
#
#   - commentaires 
#       - JAMAIS DE COMMENTAIRES TRADUISANT EXPLICITEMET LE CODE
#       - JAMAIS DE COMMENTAIRES CREUX
#       - les commentaires doivent ajouter des informations
#       - le docstring devrait prendre la plus grande partie des commentaires - et de loin!
#
#   - ...
#   - ...
#   - ...



# fonctions utilitaires
# ----------------------------------------------------------------------------
def print_title(title, space=80):
    title = title[0:space-4]
    print('\n'*2 + title + ' ' + '-' * max(space - len(title),0))
    
    
# Types fondamentaux
# ----------------------------------------------------------------------------
print_title('Types fondamentaux')
a = 1 # integer
b = 3.141592654 # floating point
c = 1+2j # complex
d = 'C52' # string - il n'y a pas de type caractère
e = True # boolean
# ILS SONT TOUS IMMUABLES

print('a', type(a), a, type(a).__name__)
print('b', type(b), b, type(b).__name__)
print('c', type(c), c, type(c).__name__)
print('d', type(d), d, type(d).__name__)
print('e', type(e), e, type(e).__name__)


# Conditionnel ternaire et opérateur ternaire
# ----------------------------------------------------------------------------
print_title('Conditionnel ternaire et opérateur ternaire')
value = -5
print(0 <= value < 10) # condition ternaire
print('positif' if value >= 0 else 'négatif') # opérateur ternaire (équivalent C/C++ de : value >= 0 ? "Positif" : "Négatif")



# Structures de données
# ----------------------------------------------------------------------------

# fonctions utilitaires
# ----------------------------------------------------------------------------
def print_ds(title, space=80):
    print_title(title, space)
    print('string : ', my_str__)
    print('list   : ', my_list_)
    print('tuple  : ', my_tuple)
    print('set    : ', my_set__)
    print('dict   : ', my_dict_)


# basic data structure              |   subscriptable[read/write]   |   mutable     |   iterable    |   duplicate   |
# structures de données de base     |   indexable[lecture/écriture] |   modifiable  |   itérable    |   doublon     |
# immutable => sécurité et performance
my_str__ = 'Hello world'        #   |   1/0                         |   0           |   1           |   1           | fixed size array
my_list_ = [0, 1, 2, 3, 4]      #   |   1/1                         |   1           |   1           |   1           | variable size array
my_tuple = (0, 1, 2, 3, 4)      #   |   1/0                         |   0           |   1           |   1           | array
my_set__ = {0, 1, 2, 3, 4}      #   |   0/0                         |   1           |   1           |   0           | hash table
my_dict_ = {                    #   |   1/1                         |   1           |   1           |   0:1         | hash table
                0:'zéro', 
                1:'un', 
                2:'deux', 
                3:'trois', 
                4:'quatre'
            }


print_ds('Data structure')

# subscriptable
print_title('subscriptable')
print(my_str__[1])
print(my_list_[1])
print(my_tuple[1])
#print(my_set__[1])
print(my_dict_[1])


#mutable
# my_str__[1] = 'z'
my_list_[1] = 5
my_list_.append(5)
# my_tuple[1] = 5
my_set__.update({5}) # non subscriptable
my_dict_[5] = 'cinq'

print_ds('Mutable')


# duplicate
my_str__ = '012342'    
my_list_ = [0, 1, 2, 3, 4, 2]  
my_tuple = (0, 1, 2, 3, 4, 2)  
my_set__ = {0, 1, 2, 3, 4, 2}  
my_dict_ = {0:'zéro', 1:'un', 2:'deux', 3:'trois', 4:'quatre', 2:'-deux-(duplicate-key)', 33:'trois'} # 33 => (duplicate-value)

print_ds('duplicate')


# slicing -> indexation++
# only for iterable
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print_title('slicing')
print(my_list)
# single index
print(my_list[0]) # positif, à partir du premier à gauche de 0 à n-1
print(my_list[3]) 
print(my_list[9]) 
print(my_list[-1]) # négatif, à partir du dernier à droite de -1 à -n
print(my_list[-3])
print(my_list[-10])
# slicing => from : to (exluded)
print(my_list[3:6]) # 6 est exclu (souvent appelé : end ou post last)
print(my_list[3:])
print(my_list[:-3])
print(my_list[-4:-2])
print(my_list[-4:])
# slicing => from : to (exluded) : stride (step)
print(my_list[0:-1:2])
print(my_list[::3])
print(my_list[::-1])
print(my_list[-2:-6:-2])



# iterator - conceptuellement
# i = my_list.iterator()
# while i != my_list.last_iterator():
#     print(i) # do something
#     i += 1
print_title('iterator')
for i in my_list:
    print(i, end=' ')
print('')
for i in range(10):
    print(i, end=' ')
print('')
for key in my_dict_:  # my_dict_.keys()
    print(key, end=' ')
print('')
for value in my_dict_.values():
    print(value, end=' ')
print('')
for key, value in my_dict_.items():
    print(key, ' => ', value)
    
for items in my_dict_.items():
    print(items, end=' ')


list_1 = ['a', 'l', 'l', 'o']
list_2 = [5, 12, 45, 7]
list_3 = [[1, 3], [2, 4], [5, 6]]
print()
for a, b in list_3:
    print('(', a, ' : ', b, ')')

my_str__ = 'Hello world!'
for c in my_str__:
    print(f'>{c}< ', end=' ')

print()
for i, value in enumerate(my_str__):
    print('position ', i, ' => ', value, ' ', ord(value))
    
for v1, v2 in zip(list_1, list_2):
    print(v1, ' <=> ', v2, )    
    
    
    
    
# basic empty list construction
my_list = [] # 1
my_list = list() # 2
    
# basic list construction
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 1
my_list = list(range(10)) # 2
my_list = [] # 3 --------------v
for i in range(10):         #  |
    if i % 2:               #  |
        my_list.append(i)   # <-
my_list = [None] * 10 # 4

# comprehension list
# my_list = [ _expression_ for _member_ in _iterable_ (if _condition_) ] # () optional
# équivalent à 
# my_list = []
# for _member_ in _iterable_:
#   if _condition_:
#       my_list.append(_expression_)

print_title('comprehension list')
my_list = []
for i in range(10):
  if i % 2:
      my_list.append(i**2)
print(my_list)

my_list = [i**2 for i in range(10) if i % 2]
print(my_list)

print_title('autres exemples')
my_list = [i for i in range(10)]
print('1 -> ', my_list)
print('2 -> ', [0 for i in range(10)])
print('3 -> ', [i**2 for i in range(10)])
print('4 -> ', [i if i % 2 else 0 for i in range(10)])
print('5 -> ', [i for i in range(10) if i % 2])
print('6 -> ', [i for i in my_str__ if i != 'l'])
print('7 -> ', [[0, 0, 0, 0, 0] for _ in range(4)])
print('8 -> ', [[0 for _ in range(6)] for _ in range(4)])
print('9 -> ', [[y * 10 + x for x in range(6)] for y in range(4)])





# Notion de référence (pointeur), garbage collecteur, immuable et diverses considérations
print_title('Référence et concepts reliés')
# Concepts de :
#   - référence vers (pointeur)
#   - garbage collector
# types fondamentaux => IMMUABLE (IMMUTABLE)
a = 5
b = 5
print(id(a), id(b), f'Same : {id(a) == id(b)}')

a = 10
b = a
print(id(a), id(b), f'Same : {id(a) == id(b)}')

a = 5
print(id(a), id(b), f'Same : {id(a) == id(b)}')

a = 'Allo'
print(hex(id(a)))
a = a + ' monde'
print(hex(id(a)))


a = [1, 2, 3, 4]
b = a
print(id(a), id(b), f'Same : {id(a) == id(b)}')
print(a, b)
a[0] = 10
b[2] = 30
print(id(a), id(b), f'Same : {id(a) == id(b)}')
print(a, b)



a = (1, 2, 3, 4)
b = a
print(hex(id(a)), hex(id(b)), f'Same : {id(a) == id(b)}')
print(a, b)
# a[0] = 10 => impossible
# b[2] = 30 => impossible
a = (10, 2, 3, 4)
print(hex(id(a)), hex(id(b)), f'Same : {id(a) == id(b)}')
print(a, b)




# considération de copie
a = [1, 2, 3, 4]
b = copy.deepcopy(a)
print(hex(id(a)), hex(id(b)), f'Same : {id(a) == id(b)}')
print(a, b)