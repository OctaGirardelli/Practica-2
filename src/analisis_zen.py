# from this import s,d

# zen_de_python = ("".join([d.get(c, c) for c in s])).lower().split("\n")

#Copio el zen de python en una variable, porque si hago from this import s,d lo imprime en consola
zen_de_python = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

#Almaceno las lineas que tengan al menos dos palabras y la segunda empiece por vocal
lineas_con_vocal = [linea for linea in zen_de_python if len(linea.split()) >= 2 and linea.split()[1].startswith(("a","e","i","o","u"))]

print("Lineas que su segunda palabra empieza por vocal:")
for linea in lineas_con_vocal:
    print(linea)
