# E5
import imdb
ia = imdb.IMDb()
input = input("Escribe el nombre de una película:\n")
name = input
print("Peliculas relacionadas:\n")
search = ia.search_movie(name)
for i in range(len(search)):
      
    # getting the id
    id = search[i].movieID
      
    # printing it
    
    print(search[i]['title'] + " : " + id )