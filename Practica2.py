
import requests #paqueteria de requisitos 
import matplotlib.pyplot as plt #importas la paqueteria matplotlib 
import matplotlib.image as img

pokemon = input ("introduce el nombre de un pokemon: ") #ingresas una cadena de caracteres y los guardas en una variable 
url="https://pokeapi.co/api/v2/pokemon/" + pokemon #buscas en la api con el url el nombre del poquemon que ingresaste en la variable
res= requests.get(url) #obtienes el resultado de la busqueda y lo amnacenas en una variable

if res.status_code != 200: #con este if le decimos que si el estado es diferente de 200 es decir de exito nos diga que no encontramos en pokemon
    print("pokemon no encontrado") 
    exit()

imagen= img.imread(res.json()['sprites']['front_default']) #mandamos a traer la imagen frontal del pokemon y lo almacenamos en una variable
plt.title(res.json()['name'])#mostramos en un json el resultado obtenido a partir del nombre del poquemon
imgplot = plt.imshow(imagen)# mostramos la imagen que obtubimos 
plt.show()
