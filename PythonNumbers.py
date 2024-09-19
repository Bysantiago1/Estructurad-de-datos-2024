# Para verificar el tipo de objeto usamos type(objeto)
x = 100
y = 0.5
z = 1j
print (type(x))
print (type(y))
print (type(z))

# int se usa para un número entero de -infinito a infinito 
x = 10
y = 678594000837573833
z = -775899974

# Float es un número posito o negativo que contiene decimales
xF = 9.10
yF = 4.0
zF = -40.99
# Float tambien expresa numeros cientificos con "e"
x = 10e5
y = 40e-3
z = -35.6e100

# Los numeros comploejos se escriben con j como un imaginario
x = 30+22j
y = 7j
z = -8j

# Conversiones 
x = 15    # int
y = 2.2  # float
z = 10j   # complex

a = float(x)
b = int (y)
c = complex(x)

# Numero Random
import random
print (random.randrange(1, 100))
