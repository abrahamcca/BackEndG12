nombre = 'Jimena'
apellido = 'Rodriguez'
if nombre == 'Jimena' and apellido == 'Rodriguez':
    print('hola amiga, cómo estás?')
else:
    print('quien eres tú?')
nombre_completo = nombre +' '+ apellido
print(nombre_completo)

# recibir informacion por el teclado desde la terminal
ingreso = input()
print(ingreso)

dia = input('Ingrese el dia de la semana:')
# Si el dia es SABADO indicar que es fin de semana caso contrario indicar que ese dia se trabaja PERO si es DOMINGO indicar que es fin de semana y hay que lavar la ropa
dia = dia.upper()

if dia == 'SABADO':
    print('Es fin de semana')
elif dia == 'DOMINGO':
    print('Es fin de semana y hay que lavar la ropa')
else:
    print('Ese dia se trabaja')