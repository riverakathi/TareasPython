import random

def my_shuffle(lst):
    shuffled_lst = lst[:]  # Hacemos una copia de la lista
    for i in range(len(shuffled_lst)):
        j = random.randint(0, i)  # Generamos un índice aleatorio entre 0 e i (inclusive)
        shuffled_lst[i], shuffled_lst[j] = shuffled_lst[j], shuffled_lst[i]  # Intercambiamos los elementos en las posiciones i y j
    return shuffled_lst

# Ejemplo de uso:
letters = ['a', 'b', 'c']
print(f"Original: {letters}")

shuffled_letters = my_shuffle(letters)
print(f"Shuffle: {shuffled_letters}")