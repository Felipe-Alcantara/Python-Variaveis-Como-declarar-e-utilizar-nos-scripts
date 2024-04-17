# Tipos primitivos de dados em python
# Int = Inteiro
# Float = Real / Float Points
# Bool = Boolean (True or False / 0 or 1)
# Complex = Tipo complexo
# String = Alfanuméricos

# Variáveis de texto
# Declaração de diferentes tipos de dados em Python
texto = "Curso de Python Trovato" # Declaração de uma string
print(texto) # Imprime a string
print("Tipo: ", type(texto)) # Imprime o tipo de dado da variável 'texto'
print()

varNumero1 = 100 # Declaração de um inteiro
print(varNumero1) # Imprime o inteiro
print(type(varNumero1)) # Imprime o tipo de dado da variável 'varNumero1'
print()

# Declaração de diferentes tipos de variáveis
varA = 99 # Inteiro
varB = 4.99 # Float
varC = False # Booleano
varD = 2+9j # Complexo
varE = "Python" # String
print()

# Imprime o tipo de cada variável
print(type(varA), type(varB), type(varC), type(varD), type(varE))

# Conversão de tipos de variáveis
varF = float(varA) # Converte o inteiro 'varA' para float
print(varF) # Imprime o valor convertido
print(type(varF)) # Imprime o tipo de dado da variável 'varF'

varG = input("Digite um número: ") # Solicita ao usuário para digitar um número

varH = int(varG) # Converte a entrada do usuário para inteiro
print(varH) # Imprime o valor convertido
print(type(varH)) # Imprime o tipo de dado da variável 'varH'

# Variáveis Booleanas
varH = False # Declaração de um booleano
varE = True # Declaração de um booleano
varJ = not(False) # Inversor antes do False (0 = 1)
varK = not(True) # Inversor antes do True (1 = 0)

# Imprime os valores booleanos
print(varH, varE, varJ, varK)