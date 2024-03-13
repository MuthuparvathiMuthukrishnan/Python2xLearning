x = 10
a , b = 10, 20
m,n,o = (1,2,3)

#NEsted tuples - as the name suggests - it is one tuples inside the another tuple
Marvel = ("Thor","Captain America")
Dc = ("Batman","Superman")
Team = (Marvel + Dc) #when given like this we can get the index of each inputs
#Team = Marvel, Dc #this just gives the index of each inputs togther and not separately by elements
print(Team)
print(Team[2][1])

#searchin tuples
cities = ("Paris","London","New York","Coimbatore")
print("Coimbatore" in cities)#retruns boolena values (True or False)




