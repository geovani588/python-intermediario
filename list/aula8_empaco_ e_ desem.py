"""
Introdução ao sesempacotamento + tuples (tuplas) 
"""

#nome1, nome2, nome3 = ['Maria', ' Helena', 'Luiz']
#print (nome2)
#nome1, *resto = ['Maria', ' Helena', 'Luiz', 'João'] # resto recebe o que sobra
#print(nome1, resto) 
_, nome2, *_= ['Maria', ' Helena', 'Luiz', 'João'] # resto recebe o que sobra
print(nome2, _) 
