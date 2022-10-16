import random

def approx(ptns):
    somme_de_points_dans_cercle = 0
    pi = 0

    for coordonnees in ptns:
        if (coordonnees[0]**2 + coordonnees[1]**2) <= 1:
            somme_de_points_dans_cercle += 1

    pi = 4 * (somme_de_points_dans_cercle / len(ptns))
    print(pi)



ptns = []
nombre_de_points = 10000 #10^x étant la précision de pi (digit)
for i in range(nombre_de_points):
    x = random.random()
    y = random.random()
    ptns.append([x, y])
approx(ptns)


