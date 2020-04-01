Animales = [
    "Murcielago", "Leon","Pangolin",
    "Wombat","Axolote","Pingüino",
    "Panda","Tortuga","Ballena","Jaguar"
]

Muchos = Animales * 3

def unicos(L,C = False):
    if not L:
        return[]
    if not C:
        C = []
    P = L[0]
    if not P in C:
        C = C +[P]
    if len(L) == 1:
        return C
    return unicos(L[1:],C)

R = unicos(Muchos)
print(R)