# 1) Variables 

# "Pablo" es igual a 'Pablo'  
x = str("Pablo")  
y = int(3)     
z = float(3)  

print (x); # Al imprimir Pablo
print (y); # Al imprimir (3)
print (z); # AL imprimir (3.0)

# 2) Variables globales (Permite crear variables afuera de la función)
x = "Increible"

def myfunc():
  print("Python es "+ x)

myfunc()

# 3) La llave global 

def myfunc():
  global x
  x = "fantastico"

myfunc()

print("Python es " + x)