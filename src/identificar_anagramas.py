first_word = input("Ingrese la primera palabra: ")
second_word = input("Ingrese la segunda palabra: ")
print("Son anagramas." if first_word == second_word[::-1] else "No son anagramas.")

